from dataclasses import dataclass


@dataclass
class Users:
    user_id: int
    user_role: int
    bank_id: int
    first_name: str
    second_name: str
    patronymic: str
    login: str
    password_hash: str
    date_of_reg: str
    date_last_enter: str