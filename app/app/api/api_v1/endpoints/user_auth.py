from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import commit_and_close_session, get_current_user
from dependency_injector.wiring import inject, Provide
from app.core.containers import Container
from app.schemas.auth import Token, RegUserIn

router = APIRouter()


@router.post('/login', response_model=Token)
@inject
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        auth_service=Depends(Provide[Container.auth_service])
):
    return await auth_service.login(form_data=form_data)


@router.post('/registration')
@inject
@commit_and_close_session
async def registration(
        user: RegUserIn,
        auth_service=Depends(Provide[Container.auth_service])
):
    return await auth_service.registration(user=user)


@router.get('/user')
async def get_user(current_user=Depends(get_current_user)):
    return current_user


@router.post('/test')
@inject
async def my_profile():
    pass

