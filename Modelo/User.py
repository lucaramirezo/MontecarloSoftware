import uuid
import hashlib 
from typing import Optional
from datetime import datetime


class User:
    UUID: uuid.UUID
    login: str
    password: str
    name: Optional[str]
    surname: Optional[str]
    phone: Optional[str]
    address_1: Optional[str]
    address_2: Optional[str]
    city: Optional[str]
    province: Optional[str]
    postal_code: Optional[str]
    date_registration: Optional[datetime]
    boss_id: Optional[uuid.UUID]
    can_edit: Optional[bool]

    def __init__(self, login: str, password: str, uuidv4: Optional[uuid.UUID] = None, name: Optional[str] = None,
                 surname: Optional[str] = None,
                 phone: Optional[str] = None, address_1: Optional[str] = None, address_2: Optional[str] = None,
                 city: Optional[str] = None, province: Optional[str] = None, postal_code: Optional[str] = None,
                 date_registration: Optional[str] = None, boss_id: Optional[uuid.UUID] = None,
                 can_edit: Optional[bool] = None):
        """
        :param login:
        :param password:
        :param uuidv4: Por defecto genera un uuidv4 al crearse, a no ser que haya sido especificado
        :param name:
        :param surname:
        :param phone:
        :param address_1:
        :param address_2:
        :param city:
        :param province:
        :param postal_code:
        :param date_registration:
        :param boss_id:
        :param can_edit:
        """
        if boss_id is not None:
            self.UUID = uuidv4 or uuid.uuid4()
            self.password = password

            self.login = login
            self.name = name
            self.surname = surname
            self.phone = phone
            self.address_1 = address_1
            self.address_2 = address_2
            self.city = city
            self.province = province
            self.postal_code = postal_code
            # intenta crear un datetime con el formato especificado, si no funciona, devuelve None
            self.date_registration = date_registration

            self.boss_id = boss_id
            self.can_edit = can_edit

    def cipher_password(self) -> None:
        """

        :return:
        """
        hasher = hashlib.md5()
        hasher.update(self.password.encode())

        self.password = hasher.hexdigest()

    def str_to_datetime(self, date_format='%Y-%m-%d %H:%M:%S') -> None:
        """

        :param date_format:
        :return:
        """
        self.date_registration = datetime.strptime(self.date_registration, date_format)

    def __str__(self):
        return f"[UUID:{self.UUID}, name:{self.name}, login:{self.login}, password:{self.password}]"
