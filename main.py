from fastapi import FastAPI, Path, Query

meta_tags = [
    {
        'name': 'Users',
        'description': 'Operations with users. The **Login** logic is also here.'
    },
    {
        'name': 'Items',
        'description': 'Operations with users. The **Login** logic is also here.',
        'externalDocs': {
            'description': 'Items External Docs',
            'url': 'http://www.example.com'
        }
    },
]

app = FastAPI(
    title='Medical Soft',
    description='Inicio de Application Medical Soft',
    version='0.0.1',
    terms_of_service='http://www.example.com',
    contact={
        'name': 'LeSavantR',
        'url': 'https://www.lesavant.dev',
        'email': 'uniruben22@gmail.com'
    },
    license_info={
        'name': 'MIT License',
    },
    openapi_tags=meta_tags
)
