from fastapi import APIRouter


router = APIRouter(
    prefix='/sections',
    tags=['Sections']
)

sections = []


@router.get('/{id}')
async def get_section(id: int):
    return { 'sections': sections }


@router.get('/{id}/content-blocks')
async def get_section_content(id: int):
    return { 'sections': sections }


@router.get('/content-blocks/{id}')
async def get_content_block(id: int):
    return { 'sections': sections }