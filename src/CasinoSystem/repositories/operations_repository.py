from src.CasinoSystem.database.database import get_connection
from src.CasinoSystem.models.operations import Operations


def _map(row) -> Operations:
    return Operations(*row)


def create(operation_type: bool, user_operator: int, amount: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO reservations(
            operation_type,
            user_operator,
            amount
        )
        VALUES (?, ?, ?)
    """, (operation_type, user_operator, amount))

    conn.commit()
    conn.close()