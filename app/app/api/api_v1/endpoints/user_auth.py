from fastapi import APIRouter, Depends
from app.api.deps import commit_and_close_session, get_current_user_auth
from dependency_injector.wiring import inject, Provide
from app.core.containers import Container
from app.schemas.auth import AuthOut, MyProfileOut

router = APIRouter()


@router.get('/login', response_model=AuthOut)
@inject
async def login(
        user: str = Depends(get_current_user_auth),
        rep_user=Depends(Provide[Container.repository_user])
):
    return rep_user.get(login=user)


@router.post('/registration')
@inject
@commit_and_close_session
async def registration():
    pass


@router.post('/profile', response_model=MyProfileOut)
@inject
async def my_profile(
    #! Сюда нужно вставить функцию получения айди по тому какой пользователь обращается
        # user_id: str = Depends(get_current_user_auth),
        registration_service=Depends(Provide[Container.registration_service])):
    """Личный кабинет."""
    return registration_service.my_profile(user_id="ID") 

