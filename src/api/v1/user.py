from fastapi import APIRouter

from src.core.schemas import User

router = APIRouter()


@router.post()
def create_user(user: User): ...
