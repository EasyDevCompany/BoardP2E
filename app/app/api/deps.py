from fastapi import Header, Depends, Response, HTTPException
from dependency_injector.wiring import inject, Provide
from app.core.containers import Container
from functools import wraps
from app.db.session import scope
from uuid import uuid4, UUID


def get_current_user():
    pass


@inject
async def create_session():
    scope.set(str(uuid4()))


@inject
def commit_and_close_session(func):

    @wraps(func)
    @inject
    async def wrapper(db=Depends(Provide[Container.db]), *args, **kwargs,):
        scope.set(str(uuid4()))
        try:
            result =  await func(*args, **kwargs)
            db.session.commit()
            return result
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            # db.session.expunge_all()
            db.scoped_session.remove()

    return wrapper
