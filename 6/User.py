from enum import Enum

class UserType(Enum):
    ADMIN = 1
    USER = 2
    GUEST = 3

class User:
    def __init__(self, name: str, type: UserType) -> None:
        self.name = name
        self.type = type

    def __str__(self) -> str:
        return f'{self.name} ({self.type.name})'