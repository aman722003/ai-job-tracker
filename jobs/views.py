from django.shortcuts import (render,redirect,get_object_or_404)
from django.contrib.auth.decorators import login_required
from .models import JobApplication
from .forms import JobApplicationForm
from .utils import (extract_text_from_pdf,extract_skills)


@login_required
def dashboard_view(request):

    jobs = JobApplication.objects.filter(
        user=request.user
    )

    # Search functionality

    search_query = request.GET.get(
        'search'
    )

    if search_query:

        jobs = jobs.filter(

            company_name__icontains=search_query

        ) | jobs.filter(

            role__icontains=search_query
        )

    # Status filter

    status_filter = request.GET.get(
        'status'
    )

    if status_filter:

        jobs = jobs.filter(
            status=status_filter
        )

    # Analytics

    total_jobs = jobs.count()

    applied_count = jobs.filter(
        status='Applied'
    ).count()

    interview_count = jobs.filter(
        status='Interview'
    ).count()

    rejected_count = jobs.filter(
        status='Rejected'
    ).count()

    offer_count = jobs.filter(
        status='Offer'
    ).count()

    context = {

        'jobs': jobs,

        'total_jobs': total_jobs,

        'applied_count': applied_count,

        'interview_count': interview_count,

        'rejected_count': rejected_count,

        'offer_count': offer_count,
    }

    return render(

        request,

        'jobs/dashboard.html',

        context
    )


@login_required
def create_job_view(request):

    if request.method == 'POST':

        form = JobApplicationForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            # Resume AI Analyzer
            if job.resume:
                pdf_path = job.resume.path
                text = extract_text_from_pdf(pdf_path)
                skills = extract_skills(text)
                job.extracted_skills = ", ".join(skills)
                job.save()
            return redirect('dashboard')
    else:
        form = JobApplicationForm()
    return render(request,'jobs/create_job.html',{'form': form})
@login_required
def update_job_view(request, pk):
    job = get_object_or_404(JobApplication,pk=pk,user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST,request.FILES,instance=job)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobApplicationForm(instance=job)
    return render(request,'jobs/update_job.html',{'form': form})

@login_required
def delete_job_view(request, pk):
    job = get_object_or_404(JobApplication,pk=pk,user=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('dashboard')
    return render(request,'jobs/delete_job.html',{'job': job})