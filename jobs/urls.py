from django.urls import path

from .views import (

    dashboard_view,

    create_job_view,

    update_job_view,

    delete_job_view
)

urlpatterns = [

    path(
        '',
        dashboard_view,
        name='dashboard'
    ),

    path(
        'create/',
        create_job_view,
        name='create_job'
    ),

    path(
        'edit/<int:pk>/',
        update_job_view,
        name='update_job'
    ),

    path(
        'delete/<int:pk>/',
        delete_job_view,
        name='delete_job'
    ),
    
]