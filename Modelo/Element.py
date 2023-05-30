import uuid
from typing import Optional
from datetime import datetime


class Element:
    UUID: uuid.UUID
    UUID_list_type: uuid.UUID
    element_type: Optional[str]
    title: Optional[str]
    details: Optional[str]
    est_low: Optional[int]
    est_mid: Optional[int]
    est_high: Optional[int]
    creation_time: Optional[datetime]
    real_value: Optional[int]
    UUID_list_type: Optional[uuid.UUID]
    completion_time: Optional[datetime]

    # element_type debe ser o time o money

    def __init__(self, uuidv4: Optional[uuid.UUID] = None, uuid_list_type: Optional[uuid.UUID] = None,
                 element_type: Optional[str] = None,
                 title: Optional[str] = None,
                 details: Optional[str] = None, est_low: Optional[int] = None, est_mid: Optional[int] = None,
                 est_high: Optional[int] = None, creation_time: Optional[datetime] = None,
                 real_value: Optional[int] = None, completion_time: Optional[datetime] = None,
                 UUID_list_type: Optional[uuid.UUID] = None):
        """

        :param uuidv4:
        :param element_type:
        :param title:
        :param details:
        :param est_low:
        :param est_mid:
        :param est_high:
        :param creation_time:
        :param real_value:
        """
        self.UUID = uuidv4 or uuid.uuid4()
        self.UUID_list_type = uuid_list_type

        if Element.__check_element_type(element_type):
            self.element_type = element_type
        else:
            self.element_type = 'default'

        self.title = title
        self.details = details
        self.est_low = est_low
        self.est_mid = est_mid
        self.est_high = est_high
        self.creation_time = creation_time or datetime.now()
        self.real_value = real_value
        self.completion_time = completion_time
        self.UUID_list_type = UUID_list_type

    @staticmethod
    def __check_element_type(element_type: str) -> bool:
        if (element_type == "time") or (element_type == "budget"):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.UUID}, {self.title}, {self.details}: {self.est_low} | {self.est_mid} | {self.est_high}"

    # atención, estos dos métodos son necesarios para poder indexar en un set
    def __eq__(self, other):
        return self.UUID == other.UUID

    def __hash__(self):
        return hash(self.UUID)

    def __lt__(self, other):
        return self.UUID_list_type < other.UUID_list_type
