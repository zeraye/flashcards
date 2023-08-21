from typing import List, Any
from pydantic import BaseModel


class User(BaseModel):
    username: str
    sets: Any = None


users: List[User] = [
    User(
        username="zeraye",
        sets=[
            {
                "id": "469145123",
                "title": "Countries",
                "description": "learn countries in korean",
                "term_locale_code": "ko_KR",
                "definition_locale_code": "pl_PL",
                "flashcards": [
                    {
                        "id": 0,
                        "streak": 0,
                        "term": "한국",
                        "definition": "Korea Południowa",
                    },
                    {"id": 1, "streak": 0, "term": "미국", "definition": "USA"},
                    {"id": 2, "streak": 0, "term": "중국", "definition": "Chiny"},
                    {
                        "id": 3,
                        "streak": 0,
                        "term": "영국",
                        "definition": "Wielka Brytania",
                    },
                    {"id": 4, "streak": 0, "term": "일본", "definition": "Japonia"},
                    {"id": 5, "streak": 0, "term": "독일", "definition": "Niemcy"},
                    {"id": 6, "streak": 0, "term": "호주", "definition": "Australia"},
                    {"id": 7, "streak": 0, "term": "프랑스", "definition": "Francja"},
                    {"id": 8, "streak": 0, "term": "캐나다", "definition": "Kanada"},
                ],
            }
        ],
    ),
    User(username="test"),
]


def get_user_by_username(username: str):
    for user in users:
        if user.username == username:
            return user

    raise KeyError(f"User {username} not found in database!")


def get_set_by_set_id(set_id: str):
    for user in users:
        for _set in user.sets:
            if _set["id"] == set_id:
                return _set

    raise KeyError(f"Set {set_id} not found in database!")
