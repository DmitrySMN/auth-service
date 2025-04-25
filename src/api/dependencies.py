from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Path, status
from db.session import session_dep
from db.crud import user_crud
from db.models.user import Users


session_dependency = Depends(session_dep)


async def user_by_id_dep(
    user_id: Annotated[int, Path],
    session: AsyncSession = session_dependency,
) -> Users:
    user = await user_crud.get_user_by_id(session=session, user_id=user_id)
    if user is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
