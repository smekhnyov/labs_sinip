from User import User, UserType
from Object import Object
from Matrix import Matrix, Action

from random import randint

# Параметры для варианта
count_user = 7
count_obj = 3

def generate_matrix() -> Matrix:
    users = [User(f'root', UserType.ADMIN)]
    for i in range(1, count_user):
        random_type = UserType(randint(1, 3))
        users.append(User(f'user{i}', random_type))

    objects = [Object(f'obj{i}') for i in range(count_obj)]

    matrix = Matrix(users)

    for user in users:
        if user.name == 'root':
            for obj in objects:
                for action in Action:
                    matrix.grant_access(user, obj, action)
        for obj in objects:
            for action in Action:
                if randint(0, 1) == 1:
                    matrix.grant_access(user, obj, action)
    return matrix, users, objects

def transfer_access(matrix: Matrix, user_from: User):
    while True:
        obj_name = input('Введите имя объекта для передачи прав (или = для выхода): ')
        if obj_name == '=':
            break

        obj = next((o for o in objects if o.name == obj_name), None)
        if obj is None:
            print('Такого объекта нет. Попробейте ещё раз.')
            continue

        while True:
            action_name = input(
                f'Введите имя действия, право которого на объект {obj} передается (или = для выхода): ').upper()

            if action_name == '=':
                break

            if action_name not in [action.name for action in Action]:
                print('Такого действия нет. Попробейте ещё раз.')
                continue

            action_to = Action[action_name]

            while True:
                user_to_name = input('Введите имя другого пользователя (или = для выхода): ')
                if user_to_name == '=':
                    break

                user_to = next((u for u in users if u.name == user_to_name), None)
                if user_to is None:
                    print('Такого пользователя нет. Попробейте ещё раз.')
                    continue

                result = matrix.transfer_access(user_from, user_to, obj, action_to)
                if result:
                    print('Право передано.')
                else:
                    print('Вы не имеете права на передачу этого действия.')
                print(matrix)
                return


if __name__ == '__main__':
    matrix, users, objects = generate_matrix()
    print(matrix)

    finish_flag = False
    while not finish_flag:
        user_name = input('Введите имя пользователя (или = для выхода): ')
        if user_name == '=':
            finish_flag = True
            continue

        user = next((u for u in users if u.name == user_name), None)
        if user is None:
            print('Такого пользователя нет. Попробуйте ещё раз.')
            continue

        while True:
            action_name = input('Введите имя действия (или = для выхода): ').upper()
            if action_name == '=':
                break

            if action_name not in [action.name for action in Action]:
                print('Такого действия нет. Попробейте ещё раз.')
                continue

            action = Action[action_name]

            if action == Action.TRANSFER:
                transfer_access(matrix, user)
            else:
                while True:
                    obj_name = input('Введите имя объекта (или = для выхода): ')
                    if obj_name == '=':
                        break

                    obj = next((o for o in objects if o.name == obj_name), None)
                    if obj is None:
                        print('Такого объекта нет. Попробуйте ещё раз.')
                        continue

                    result = matrix.has_access(user, obj, action)
                    if result:
                        print(f'Пользователь {user.name} имеет право на {obj.name} с действием {action.name}')
                    else:
                        print(f'Пользователь {user.name} не имеет права на {obj.name} с действием {action.name}')

    print('Программа завершена.')
