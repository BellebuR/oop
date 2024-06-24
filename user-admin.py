class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    # Методы для получения значений атрибутов
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Методы для установки значений атрибутов
    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        self._access_level = access_level


class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name, 'admin')
        self._admin_level = admin_level

    def get_admin_level(self):
        return self._admin_level

    def set_admin_level(self, admin_level):
        self._admin_level = admin_level

    # Метод для добавления пользователя
    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
        else:
            raise ValueError("Invalid user object")

    # Метод для удаления пользователя
    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                return
        raise ValueError("User ID not found")


# Пример использования
if __name__ == "__main__":
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    admin1 = Admin(3, "Eve", "super")

    user_list = [user1, user2]

    # Добавление нового пользователя
    user3 = User(4, "Charlie")
    admin1.add_user(user_list, user3)

    # Попытка удалить пользователя
    try:
        admin1.remove_user(user_list, 2)  # Удалить пользователя с ID 2 (Bob)
    except ValueError as e:
        print(e)

    # Вывод списка пользователей
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")