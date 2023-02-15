from uuid import UUID
from fastapi import APIRouter

router = APIRouter(
    prefix='/courses',
    tags=['Courses']
)

courses = []


@router.get('')
async def get_all_courses():
    return { 'courses': courses }


@router.post('')
async def create_course():
    return { 'courses': courses }


@router.get('/{id}')
async def get_course(id: UUID):
    return { 'courses': courses }


@router.patch('/{id}')
async def update_course(id: UUID):
    return { 'courses': courses }


@router.delete('/{id}')
async def delete_course(id: UUID):
    return { 'courses': courses }


@router.get('/{id}/sections')
async def get_course_section(id: UUID):
    return { 'courses': courses }
