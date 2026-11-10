from src.CasinoSystem.database.database import get_connection
from src.CasinoSystem.models.operations import Operations


def _map(row) -> Operations:
    return Operations(*row)


def create(operation_type: bool, user_operator: int, amount: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO operations(
            operation_type,
            user_operator,
            amount
        )
        VALUES (?, ?, ?)
    """, (operation_type, user_operator, amount))

    conn.commit()
    conn.close()


def get_by_operator(user_operator: int) -> Operations | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT operation_id, operation_type, user_operator, amount
                FROM operations
                WHERE user_operator = ?
                """, (user_operator,))

    row = cur.fetchone()
    conn.close()

    return _map(row) if row else None


def get_all() -> list[Operations]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT operation_id, operation_type, user_operator, amount
                FROM operations
                """)

    rows = cur.fetchall()
    conn.close()

    return [_map(r) for r in rows]


def delete_operations(user_operator:int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                DELETE from operations
                WHERE user_operator = ?
                """, (user_operator))

    conn.commit()
    conn.close()