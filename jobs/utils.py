import fitz


SKILLS = [

    'python',

    'django',

    'flask',

    'postgresql',

    'mysql',

    'mongodb',

    'javascript',

    'react',

    'html',

    'css',

    'docker',

    'aws',

    'git',

    'github',

    'rest api',

    'machine learning',

    'pandas',

    'numpy'
]


def extract_text_from_pdf(pdf_path):

    text = ""

    pdf_document = fitz.open(pdf_path)

    for page in pdf_document:

        text += page.get_text()

    return text.lower()


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        if skill in text:

            found_skills.append(skill)

    return found_skills