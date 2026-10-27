from dataclasses import dataclass


@dataclass
class Role:
    usr_role_id: int
    name: str