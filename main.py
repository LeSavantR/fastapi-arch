from fastapi import FastAPI
from uvicorn import run

from routes.users import router as user_router
from routes.sections import router as section_router
from routes.courses import router as courses_router

meta_tags = [
    {
        'name': 'Courses',
        'description': 'Operations with courses.',
        'externalDocs': {
            'description': 'Courses External Docs',
            'url': 'http://www.example.com'
        }
    },
    {
        'name': 'Sections',
        'description': 'Operations with sections.'
    },
    {
        'name': 'Users',
        'description': 'Operations with users. The **Login** logic is also here.'
    },
]

app = FastAPI(
    title='API-Users',
    description='Users API Interface.',
    version='0.0.1',
    terms_of_service='http://www.example.com',
    contact={
        'name': 'LeSavantR',
        'url': 'http://www.example.com',
        'email': 'uniruben22@gmail.com'
    },
    license_info={
        'name': 'MIT License',
    },
    openapi_tags=meta_tags,
    debug=True
)

app.include_router(router=courses_router)
app.include_router(router=section_router)
app.include_router(router=user_router)


if __name__ == '__main__':
    run(
        app='main:app', host='0.0.0.0', port=8000,
        log_level='info', reload=True,
        # workers=2
    )
