from dataclasses import dataclass


@dataclass
class Operations:
    operation_id: int
    operation_type: bool
    operation_user: int
    amount: int