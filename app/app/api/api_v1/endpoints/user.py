from pathlib import Path

from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import commit_and_close_session, get_current_user
from dependency_injector.wiring import inject, Provide
from app.core.containers import Container
from app.schemas.auth import Token, RegUserIn, MyProfileOut
from app.models.user import User
from loguru import logger

router = APIRouter()


@router.get('/my_profile')
async def get_user(
        current_user=Depends(get_current_user)):
    logger.error(current_user.status.user)
    logger.error(type(current_user.status))
    representation_of_profile = {
        "status": current_user.status,
        "login": current_user.login,
        "email": current_user.email,
        "balance": current_user.balance
    }
    return representation_of_profile


@router.post('/update_image')
@inject
def update_image(
        image: UploadFile = File(...),
        current_user=Depends(get_current_user)):
    """Обновляет аватарку пользователя."""
    current_file = Path(__file__)
    current_file_dir = current_file.parent
    project_root = current_file_dir.parent.parent.parent.parent / "image/user"
    project_root_absolute = project_root.resolve()
    static_root_absolute = project_root_absolute / f"{current_user.login}.png"
    file_location = static_root_absolute
    with open(file_location, "wb+") as file_object:
        image.filename = f"{current_user.id}.png"
        file_object.write(image.file.read())
    return {"info": f"file '{image.filename}' saved at '{file_location}'"}

