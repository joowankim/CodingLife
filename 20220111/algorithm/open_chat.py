# 프로그래머스 - 오픈채팅방
#
# 유저가 출입할 때 메시지가 생긴다.
from collections import namedtuple
from typing import Dict

User = namedtuple('User', ['operation', 'uid', 'name'], defaults=("", ) * 3)


class UserManager:
    def __init__(self, users: Dict):
        self.users = users

    def register(self, uid, name):
        self.users[uid] = name
        return self.users


def transform_records(record):
    return [User(*msg.split()) for msg in record]


def solution(record):
    records = transform_records(record)
    user_manager = UserManager({})
    messages = []
    for transformed in records:
        if transformed.operation == "Enter":
            user_manager.register(transformed.uid, transformed.name)
            messages += [(transformed.uid, "님이 들어왔습니다.")]
        elif transformed.operation == "Leave":
            messages += [(transformed.uid, "님이 나갔습니다.")]
        elif transformed.operation == "Change":
            user_manager.register(transformed.uid, transformed.name)

    stacked_messages = []
    for message in messages:
        stacked_messages += [user_manager.users[message[0]] + message[1]]
    return stacked_messages


assert solution(
    [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    ]
) == [
    "Prodo님이 들어왔습니다.",
    "Ryan님이 들어왔습니다.",
    "Prodo님이 나갔습니다.",
    "Prodo님이 들어왔습니다."
]


assert UserManager({}).register("uid1234", "Muzi") == {"uid1234": "Muzi"}
assert UserManager({"uid1234": "Muzi"}).register("uid1234", "Prodo") == {"uid1234": "Prodo"}

assert transform_records(
    [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    ]
) == [
    User("Enter", "uid1234", "Muzi"),
    User("Enter", "uid4567", "Prodo"),
    User("Leave", "uid1234", ""),
    User("Enter", "uid1234", "Prodo"),
    User("Change", "uid4567", "Ryan"),
]
