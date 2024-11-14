from User import User
from Object import Object

from enum import Enum
from random import randint
from typing import List, Dict

class Action(Enum):
    READ = 1
    WRITE = 2
    TRANSFER = 3

class Matrix:
    def __init__(self, users: List['User']):
        # Создаем матрицу, где каждому пользователю соответствует словарь доступов к объектам
        self.matrix: Dict['User', Dict['Object', List['Action']]] = {
            user: {} for user in users
        }

    def has_access(self, user: 'User', obj: 'Object', action: 'Action') -> bool:
        # Проверяем, есть ли у пользователя доступ к конкретному объекту и действию
        return action in self.matrix.get(user, {}).get(obj, [])

    def grant_access(self, user: 'User', obj: 'Object', action: 'Action'):
        # Назначаем доступ пользователю к объекту для указанного действия
        if obj not in self.matrix[user]:
            self.matrix[user][obj] = []
        if action not in self.matrix[user][obj]:
            self.matrix[user][obj].append(action)

    def transfer_access(self, user_from: 'User', user_to: 'User', obj: 'Object', action: 'Action'):
        # Передача только одного указанного права доступа от одного пользователя к другому
        if self.has_access(user_from, obj, action) and self.has_access(user_from, obj, Action.TRANSFER):
            if obj not in self.matrix[user_to]:
                self.matrix[user_to][obj] = []
            if action not in self.matrix[user_to][obj]:
                self.matrix[user_to][obj].append(action)
            return True
        return False

    def __str__(self):
        # Преобразование матрицы доступа в строку для наглядного отображения
        matrix_str = ""
        for user, access in self.matrix.items():
            matrix_str += f"{user.name} ({user.type.name}):\n"
            for obj, actions in access.items():
                actions_str = ', '.join([action.name for action in actions])
                matrix_str += f"  {obj.name}: [{actions_str}]\n"
        return matrix_str