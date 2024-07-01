from fastapi import APIRouter, HTTPException, status, Response, Depends
from sqlalchemy.testing.pickleable import User
from app.users.dependencies import get_current_user
from app.users.schemas import SUserAuth
from app.users.dao import UsersDAO
from app.users.auth import get_password_hash, authenticate_user, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["auth & пользоватли"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Некорректный логин и/или пароль")
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token


@router.post("/logout")
async def logout(response: Response) -> dict:
    response.delete_cookie("booking_access_token")
    return {"message": "Пользователь вышел из системы"}


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user