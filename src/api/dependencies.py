from fastapi import Depends
from db.session import session_dep


session_dependency = Depends(session_dep)