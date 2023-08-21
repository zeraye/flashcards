from fastapi import FastAPI, HTTPException

from database import get_user_by_username, get_set_by_set_id

app = FastAPI()


@app.get("/users/{username}")
def get_user(username: str):
    try:
        return get_user_by_username(username)
    except KeyError as e:
        return HTTPException(status_code=404, detail=str(e))
    except:
        return HTTPException(status_code=404, detail="Exception not handeled!")


@app.get("/sets/{set_id}")
def get_set(set_id: str):
    try:
        return get_set_by_set_id(set_id)
    except KeyError as e:
        return HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=404, detail="Exception not handeled!")
