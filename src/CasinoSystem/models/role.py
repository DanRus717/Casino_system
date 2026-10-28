from dataclasses import dataclass


@dataclass
class Role:
    user_role_id: int
    name: str