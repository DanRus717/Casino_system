from src.CasinoSystem.database.database import get_connection
from src.CasinoSystem.models.role import Role


def get_all() -> list[Role]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT user_role_id, name
                FROM user_roles
                ORDER BY user_role_id
                """)

    rows = cur.fetchall()

    conn.close()

    return [
        Role(
            user_role_id=row[0],
            name=row[1]
        )
        for row in rows
    ]


def get_by_id(role_id: int) -> Role | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT user_role_id, name
                FROM user_roles
                WHERE user_role_id = ?
                """, (role_id,))

    row = cur.fetchone()

    conn.close()

    if not row:
        return None

    return Role(
        user_role_id=row[0],
        name=row[1]
    )