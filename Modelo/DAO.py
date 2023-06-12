import hashlib
import uuid
from datetime import datetime

import mariadb
import mysql.connector
from typing import Optional

from Modelo.ListType import ListType
from Modelo.Element import Element
from Modelo.User import User


def CachedFunction(func):
    cache = {}

    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key in cache:
            print(f"----Inside {func.__name__} cache ")
            return cache[args]
        else:
            result = func(*args, **kwargs)

            if len(cache.items()) >= 5:
                cache.popitem()

            cache[cache_key] = result
            return result

    return wrapper


class DAO:
    __instance = None
    con: mysql.connector.connect()

    def __init__(self, host: str, user: str, password: str, database: str):
        try:
            self.con = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        except mysql.connector.Error as e:
            print("Error de conexión: " + str(e))

    @staticmethod
    def get_instance(host: str = '195.235.211.197', user: str = 'psi_grupo6', password: str = '50K2f#k!wg^M',
                     database: str = 'psi_grupo6'):  
        if DAO.__instance is None:
            DAO.__instance = DAO(host, user, password, database)
        return DAO.__instance

    def __del__(self):
        if self.con:
            self.con.close()


    def sql_query(self, sql):
        cursor = self.con.cursor()

        cursor.execute(sql)

        datos = cursor.fetchall()
        if datos:
            return datos
        else:
            return None

    def close_connection(self):
        self.__del__()

    def check_user_exists(self, login: str) -> bool:
        sql = f"SELECT * FROM User WHERE login='{login}'"
        try:
            cursor = self.con.cursor()
            cursor.execute(sql)

            if cursor.fetchone() is not None:
                return True
            return False
        except mariadb.Error as e:
            print("Error: " + str(e))
            return False

    def create_user(self, user: User):
        if DAO.__instance is not None:
            sql = "INSERT INTO User(UUID, login, password, name, surname, phone, address_1, address_2, city, " \
                  "province, postal_code, date_registration, boss_id, can_edit) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                 str(user.UUID), user.login, user.password, user.name, user.surname,
                 user.phone, user.address_1,
                 user.address_2, user.city, user.province, user.postal_code,
                 str(user.date_registration),
                 str(user.boss_id), user.can_edit)
        # Evita inyecciones al preparar los valores y definirlos como tal, por eso los interrogantes
        # values = (
        #     str(user.UUID), user.login, user.password, user.name, user.surname,
        #     user.phone, user.address_1,
        #     user.address_2, user.city, user.province, user.postal_code,
        #     str(user.date_registration),
        #     str(user.boss_id), user.can_edit)

        try:
            cursor = self.con.cursor()
            cursor.execute(sql, values)
            self.con.commit()
            print(f"User {user.login} with UUID {str(user.UUID)} created")
        except mysql.connector.Error as e:
            self.con.rollback()
            print(f"ERROR User {user.login} with UUID {str(user.UUID)} not created: {str(e)}")

    def update_user(self, user: User):
        if DAO.__instance is not None:
            cursor = self.con.cursor()
            sql = f"update User set login='{user.login}', password='{user.password}', name='{user.name}', " \
                  f"surname='{user.surname}', phone = '{user.phone}', address_1='{user.address_1}', " \
                  f"address_2='{user.address_2}', city='{user.city}', province='{user.province}'," \
                  f" postal_code='{user.postal_code}', date_registration='{str(user.date_registration)}', " \
                  f"boss_id ='{str(user.boss_id)}', can_edit='{int(user.can_edit)}' where UUID = '{str(user.UUID)}' "
            try:
                cursor.execute(sql)
                self.con.commit()
                print(f"User {user.login} with UUID {str(user.UUID)} edited")
            except mysql.connector.Error as e:
                self.con.rollback()
                print(f"ERROR User {user.login} with UUID {str(user.UUID)} not edited: {str(e)}")

    def delete_user(self, user: User = None) -> bool:
        if DAO.__instance is not None and user is not None:
            # verificar si el usuario no es jefe de más de una persona (sí misma)
            sql_count = f"select count(boss_id) from User where boss_id = '{str(user.UUID)}'"

            try:
                cursor = self.con.cursor()
                cursor.execute(sql_count)
            except mysql.connector.Error as e:
                print("ERROR counting " + str(e))

            no_referencias = cursor.fetchall()
        else:
            raise Exception("Method requires DAO.__instance, user or uuid")

        if str(user.boss_id).__eq__(str(user.UUID)):
            # si es su propio jefe
            if no_referencias[0][0] == 1:
                # secuencia de borrado
                sql_drop_constrain = "alter table User drop constraint User_ibfk_1"
                sql_delete = f"delete from MSS.User where UUID like '{str(user.UUID)}'"
                sql_add_constrain = "alter table MSS.User add constraint foreign key (boss_id) references User (UUID)"

                try:
                    cursor.execute(sql_drop_constrain)
                    # Atención, no se podrá borrar un usuario hasta que haya eliminado todas las referencias de otras
                    # tablas como Assigned_Elements
                    cursor.execute(sql_delete)
                    cursor.execute(sql_add_constrain)

                    self.con.commit()
                    print(f"Privileged user {user.login} - {str(user.UUID)} - deleted successfully")
                    return True
                except mysql.connector.Error as e:
                    self.con.rollback()
                    print(f"ERROR deleting privileged user {str(user.UUID)}, {str(e)}")

            else:
                print(f"ERROR This privileged user still has references: {no_referencias[0][0]} references detected")
                return False

        elif user.boss_id != user.UUID:
            # si no es su propio jefe, y no es jefe de nadie
            if no_referencias[0][0] == 0:
                sql_delete = f"delete from MSS.User where UUID like '{str(user.UUID)}'"
                try:
                    cursor.execute(sql_delete)
                    self.con.commit()
                    print(f"User {user.login} - {str(user.UUID)} deleted")
                except mysql.connector.Error as e:
                    self.con.rollback()
                    print(f"ERROR deleting user {str(user.UUID)}: {str(e)}")

            else:
                print(f"ERROR This user still has references: {no_referencias[0][0]} references detected")

    @CachedFunction
    def login_user(self, login: str, password: str) -> Optional[User]:
        if (DAO.__instance is not None) and (login is not None) and (password is not None):
            sql = f"select password from MSS.User where login = '{login}'"

            try:
                cursor = self.con.cursor()
                cursor.execute(sql)
                # user_raw es una variable que mantiene la información para crear un usuario, sacada de la base,
                # de datos, para poder manipularlo, primero construimos el dato
                password_raw = cursor.fetchall()
            except mysql.connector.Error as e:
                print(f"ERROR getting user: {str(e)}")

            if len(password_raw) != 0:
                if str(hashlib.md5(password.encode()).hexdigest()) == password_raw[0][0]:
                    sql = f"select * from User where login = '{login}'"

                    try:
                        cursor.execute(sql)
                        # user_raw es una variable que mantiene la información para crear un usuario, sacada de la base,
                        # de datos, para poder manipularlo, primero construimos el dato
                        user_raw = cursor.fetchall()
                    except mysql.connector.Error as e:
                        print(f"ERROR getting user: {str(e)}")

                    if len(user_raw) != 0:
                        print("Login successful")
                        return User(uuidv4=user_raw[0][0], password=user_raw[0][1], login=user_raw[0][2],
                                    name=user_raw[0][3], surname=user_raw[0][4], phone=user_raw[0][5],
                                    address_1=user_raw[0][6], address_2=user_raw[0][7], city=user_raw[0][8],
                                    province=user_raw[0][9], postal_code=user_raw[0][10],
                                    date_registration=user_raw[0][11],
                                    boss_id=user_raw[0][12], can_edit=user_raw[0][13])
                    else:
                        print(f"User by login: {login} does not exist")
                        return None
                else:
                    print("Password incorrect!")
                    return None
            else:
                print(f"Password length cannot be 0")

    @CachedFunction
    def get_users_UUID_under_boss(self, boss: User):
        if DAO.__instance is not None:
            try:
                cursor = self.con.cursor()
                sql_get_users_under = f"select UUID from User where boss_id='{boss.UUID}'"
                cursor.execute(sql_get_users_under)
                return cursor.fetchall()

            except mysql.connector.Error as e:
                print(f"ERROR trying to fetch users under boss: {boss.UUID}, {str(e)}")

    def create_assigned_elements(self, user: User, element: Element, blanket_assign_mode: bool = True):
        # Atención por defecto se asigna a todos los usuarios directamente por debajo del usuario
        if DAO.__instance is not None:
            # si es un administrador con permisos de edición y es su propio jefe la edición afecta a todos sus empleados
            if blanket_assign_mode:
                # conseguir todos los usuarios que tienen de jefe a este usuario
                users_UUID = self.get_users_UUID_under_boss(user)
                # asignar los elementos
                if user.UUID != user.boss_id:
                    self.__insert_into_assigned_elements_routine(str(user.UUID), str(element.UUID))
                for row_UUIDs in users_UUID:
                    for user_UUID in row_UUIDs:
                        self.__insert_into_assigned_elements_routine(user_UUID, str(element.UUID))

            elif not blanket_assign_mode:
                self.__insert_into_assigned_elements_routine(str(user.UUID), str(element.UUID))

    def __insert_into_assigned_elements_routine(self, user_UUID: str, element_UUID: str):
        cursor = self.con.cursor()
        sql = f"INSERT INTO Assigned_Elements (user_UUID, element_UUID) VALUES ('{user_UUID}', '{element_UUID}')"
        try:
            cursor.execute(sql)
            self.con.commit()
            print(f"Success! Created entry in Assigned_Elements: ({user_UUID}, {element_UUID})")
        except mysql.connector.Error as e:
            self.con.rollback()
            print(f"ERROR, NOT assigned ({user_UUID}, to {element_UUID}), error: {str(e)}")

    def delete_from_assigned_elements(self, user: User, element: Element, blanket_mode: bool = True):
        if DAO.__instance is not None and user is not None and element is not None:
            # blanket_assign_mode: bool = True afecta a todos los usuarios directamente por debajo
            if blanket_mode:
                # conseguir todos los usuarios que tienen de jefe a este usuario
                if user.UUID != user.boss_id:
                    self.__delete_assigned_elements_routine(user.UUID, element.UUID)
                users_UUID = self.get_users_UUID_under_boss(user)
                for row_UUIDs in users_UUID:
                    for user_UUID in row_UUIDs:
                        self.__delete_assigned_elements_routine(user_UUID, element.UUID)

            # si es un admin con edición, pero no es su propio jefe, la edición solo afecta a este usuario
            elif not blanket_mode:
                self.__delete_assigned_elements_routine(user.UUID, element.UUID)

    def delete_all_assigned_elements(self, user: User, blanket_mode: bool = True):
        if DAO.__instance is not None and user is not None:
            if blanket_mode:
                employee_UUIDs = self.get_users_UUID_under_boss(user)
                for employee_UUID in employee_UUIDs:
                    sql_delete_assignment = f"delete from Assigned_Elements where user_UUID like '{employee_UUID[0]}'"
                    try:
                        cursor = self.con.cursor()
                        cursor.execute(sql_delete_assignment)
                        self.con.commit()
                    except mysql.connector.Error as e:
                        self.con.rollback()
                        print(f"ERROR deleting all assigned elements on user {user.UUID}")

            sql_delete_assignment = f"delete from Assigned_Elements where user_UUID like '{user.UUID}'"

            try:
                cursor = self.con.cursor()
                cursor.execute(sql_delete_assignment)
                self.con.commit()
            except mysql.connector.Error as e:
                self.con.rollback()
                print(f"ERROR deleting all assigned elements on user {user.UUID}")

    def __delete_assigned_elements_routine(self, user_UUID: str, element_UUID: str):
        cursor = self.con.cursor()
        sql_delete = f"delete from Assigned_Elements where user_UUID ='{user_UUID}' and element_UUID='{element_UUID}'"
        try:
            cursor.execute(sql_delete)
            self.con.commit()
            print(f"Success! Deleted entry in Assigned_Elements: ({user_UUID}, {element_UUID})")
        except mysql.connector.Error as e:
            self.con.rollback()
            print(f"ERROR, NOT deleted ({user_UUID}, {element_UUID}), error: {str(e)}")

    @CachedFunction
    def get_assigned_elements(self, user: User) -> [Element]:
        if DAO.__instance is not None and user is not None:
            sql = f"select element_UUID from Assigned_Elements where user_UUID like '{str(user.UUID)}'"

            try:
                cursor = self.con.cursor()
                cursor.execute(sql)
                elements_UUID = cursor.fetchall()
                elements = []
                for element_UUID in elements_UUID:
                    elements.append(self.__get_element_routine(element_UUID[0]))
                print(f"Retrieved elements assigned for user {user.UUID}, totaled {str(len(elements))}")

                return elements
            except mysql.connector.Error as e:
                print(f"ERROR getting assigned elements on user {user.UUID}: {str(e)} ")

    def __get_element_routine(self, element_UUID: str):
        if DAO.__instance is not None and element_UUID is not None:
            sql = f"select * from Element where UUID like '{element_UUID}'"

            try:
                cursor = self.con.cursor()
                cursor.execute(sql)

                element_raw = cursor.fetchall()

                return Element(uuidv4=element_raw[0][0], element_type=element_raw[0][1], title=element_raw[0][2],
                               details=element_raw[0][3], real_value=element_raw[0][4], est_low=element_raw[0][5],
                               est_mid=element_raw[0][6], est_high=element_raw[0][7], creation_time=element_raw[0][8],
                               UUID_list_type=element_raw[0][9], completion_time=element_raw[0][10])

            except mysql.connector.Error as e:
                print(f"ERROR constructing element by UUID {element_UUID}: {str(e)}")

    def update_assigned_elements(self, user: User, elements: [Element], is_blanket: bool = True):
        if DAO.__instance is not None and user is not None and elements is not None:
            # Realiza una intersección con todos los elementos asignados del usuario
            assigned_elements = self.get_assigned_elements(user)
            # Utiliza implementación propia de __eq__() y de __hash__() en Element
            intersect_elements = list(set(assigned_elements).intersection(elements))
            # Proceder a eliminar los elementos asignados y reemplazarlos por los nuevos
            for element in assigned_elements:
                self.delete_from_assigned_elements(user=user, element=element, blanket_mode=is_blanket)
            for element in intersect_elements:
                self.create_assigned_elements(user=user, element=element, blanket_assign_mode=is_blanket)

    def create_list_type(self, list_type: ListType):
        if DAO.__instance is not None:
            cursor = self.con.cursor()
            sql = f"INSERT INTO List_Type (UUID, title, details) VALUES ('{str(list_type.UUID)}',' {list_type.title}','{list_type.details}')"
            try:
                cursor.execute(sql)
                self.con.commit()
                print(f"Created List_type {str(list_type.UUID)}, title {list_type.title}")
            except mysql.connector.Error as e:
                self.con.rollback()
                print(
                    f"ERROR creating element {str(list_type.UUID)}, titled {list_type.title}:  {str(e)}")
        else:
            print("DAO instance not created")

    def delete_list_type(self, list_type: ListType):
        if DAO.__instance is not None and list_type is not None:
            cursor = self.con.cursor()
            sql = f"delete from MSS.List_Type where UUID like '{str(list_type.UUID)}'"

            try:
                cursor.execute(sql)
                self.con.commit()
                print(f"Deletion successful for list_type {list_type.UUID}")
            except mysql.connector.Error as e:
                self.con.rollback()
                print(f"ERROR deleting category, error: {str(e)}")
        else:
            print("DAO instance not instantiated")

    def update_list_type(self, list_type: ListType):
        if DAO.__instance is not None and list_type is not None:
            cursor = self.con.cursor()
            sql = f"update List_Type set title = '{list_type.title}', details = '{list_type.details}'"

            try:
                cursor.execute(sql)
                self.con.commit()
                print(f"Update successful for list_type {list_type.UUID}")
            except mysql.connector.Error as e:
                self.con.rollback()
                print(f"ERROR updating list_type, error: {str(e)}")
        else:
            print("DAO instance not instantiated")

    def get_list_type_from_UUID(self, list_type_UUID: uuid.UUID):
        sql = f"select * from List_Type where UUID like '{list_type_UUID}'"
        try:
            cursor = self.con.cursor()
            cursor.execute(sql)
            list_type_raw = cursor.fetchall()
            return ListType(uuidv4=list_type_raw[0][0], title=list_type_raw[0][1], details=list_type_raw[0][2])
        except mysql.connector.Error as e:
            print(f"ERROR getting list type from UUID {list_type_UUID}: {str(e)} ")

    def get_list_type_from_element(self, element: Element = None, element_UUID: uuid.UUID = None) -> ListType:
        if DAO.__instance is not None and (element is not None or element_UUID is not None):
            sql = "None"
            if element is not None:
                sql = f"select UUID_list_type from Element where UUID like '{element.UUID}'"
            elif element_UUID is not None:
                sql = f"select UUID_list_type from Element where UUID like '{element_UUID}'"

            try:
                cursor = self.con.cursor()
                cursor.execute(sql)
                list_type_UUID = cursor.fetchall()
                return self.get_list_type_from_UUID(list_type_UUID[0][0])

            except mysql.connector.Error as e:
                if element is not None:
                    uuid_ = element.UUID
                elif element_UUID is not None:
                    uuid_ = element_UUID
                else:
                    uuid_ = "--UNDEFINED--"
                print(f"ERROR getting list type from element {uuid_}: {str(e)}")

    @CachedFunction
    def get_list_type_from_user(self, user: User) -> set([ListType]):
        if DAO.__instance is not None and user is not None:
            sql = f"select element_UUID from Assigned_Elements where user_UUID='{user.UUID}'"
            try:
                list_types = []

                cursor = self.con.cursor()
                cursor.execute(sql)

                element_UUIDs = cursor.fetchall()

                for element_UUID in element_UUIDs:
                    list_types.append(self.get_list_type_from_element(element_UUID=element_UUID[0]))

                return set(list_types)
            except mysql.connector.Error as e:
                print(f"ERROR getting categories from user {user.UUID}: {str(e)}")

    def create_element(self, element: Element, list_type: ListType, user: User = None, is_blanket: bool = True):
        if DAO.__instance is not None and element is not None and list_type is not None:
            sql = "INSERT INTO Element (UUID, UUID_list_type, title, element_type, details, est_low, est_mid, " \
                  "est_high, creation_time, real_value, completion_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                str(element.UUID), str(list_type.UUID), element.title, element.element_type,
                element.details, element.est_low, element.est_mid, element.est_high, str(element.creation_time),
                element.real_value, str(element.completion_time)
                )
            try:
                cursor = self.con.cursor()
                cursor.execute(sql)
                self.con.commit()
                element.UUID_list_type = list_type.UUID
                print(f"Created element: {str(element.UUID)} and assigned to list: {str(element.UUID)}")
            except mysql.connector.Error as e:
                self.con.rollback()
                print(f"ERROR creating element:  {str(element.UUID)}: {str(e)}")

        if user is not None:
            self.create_assigned_elements(user=user, element=element, blanket_assign_mode=is_blanket)

    def delete_element(self, element: Element, user: User = None, is_blanket: bool = True):
        if DAO.__instance is not None and element is not None:
            sql_delete = f"delete from Element where UUID like '{element.UUID}'"

            try:
                cursor = self.con.cursor()
                cursor.execute(sql_delete)
                self.con.commit()
                print(f"Deleted element: {str(element.UUID)}")
            except mysql.connector.Error as e:
                self.con.rollback()
                print(f"ERROR Deleting element {element.UUID}: {str(e)}")

        if user is not None:
            self.delete_from_assigned_elements(user=user, element=element, blanket_mode=is_blanket)

    def finish_element(self, user: User, element: Element, completion_time: datetime,
                       real_value: int):
        if DAO.__instance is not None and element is not None:
            element.completion_time = completion_time or datetime.now()
            element.real_value = real_value

            self.update_element(element)
            self.delete_from_assigned_elements(user=user, element=element)
            print("----Updated finished status")
            print(
                f"Completed element {element.UUID}, {element.title} at {element.completion_time} for {element.real_value} ")

    def update_element(self, element: Element):
        if DAO.__instance is not None and element is not None:
            if element.real_value is not None:
                real_value = f"'{element.real_value}'"
            else:
                real_value = "Null"

            if element.completion_time is not None:
                completion_time = f"'{element.completion_time}'"
            else:
                completion_time = "Null"

            sql = f"Update Element set element_type='{element.element_type}', title='{element.title}', " \
                  f"details='{element.details}', real_value = {real_value}, est_low = '{element.est_low}', " \
                  f"est_mid='{element.est_mid}', est_high= '{element.est_high}', " \
                  f"creation_time='{element.creation_time}', UUID_list_type = '{element.UUID_list_type}', " \
                  f"completion_time={completion_time} where UUID like '{element.UUID}'"

            try:
                cursor = self.con.cursor()
                cursor.execute(sql)
                self.con.commit()
                print(f"Updated element: {str(element.UUID)}")
            except mysql.connector.Error as e:
                self.con.rollback()
                print(f"ERROR Updating element {element.UUID}: {str(e)}")
