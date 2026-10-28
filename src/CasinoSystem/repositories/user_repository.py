from src.CasinoSystem.database.database import get_connection
from src.CasinoSystem.models.users import Users


def _map(row) -> Users:
    return Users(*row)


def create(user_role, bank_id, name, surname, patronymic, login, password_hash):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                INSERT INTO users(user_role, bank_id, name, surname, patronymic, login, password_hash, date_of_reg, date_last_enter)
                VALUES (?, ?, ?, ?, ?, ?, ?, date('now'), date('now'))
                """, (user_role, bank_id, name, surname, patronymic, login, password_hash, date_of_reg, date_last_enter))

    conn.commit()
    conn.close()


def get_by_login(login: str) -> Users | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT user_id, user_role, bank_id, name, surname, patronymic, login, password_hash, date_of_reg, date_last_enter
                FROM users
                WHERE login = ?
                """, (login,))

    row = cur.fetchone()
    conn.close()

    return _map(row) if row else None


def get_by_id(user_id: int) -> Users | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT user_id, user_role, bank_id, name, surname, patronymic, login, password_hash, date_of_reg, date_last_enter
                FROM users
                WHERE user_id = ?
                """, (user_id,))

    row = cur.fetchone()
    conn.close()

    return _map(row) if row else None


def get_all() -> list[Users]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT user_id, user_role, bank_id, name, surname, patronymic, login, password_hash, date_of_reg, date_last_enter
                FROM users
                ORDER BY surname, name
                """)

    rows = cur.fetchall()
    conn.close()

    return [_map(r) for r in rows]

def update_date(
    user_id: int,
    date_last_enter: str
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET date_last_enter = date('now')
        WHERE user_id = ?
    """, (date_last_enter, user_id))

    conn.commit()
    conn.close()

def block(user_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET user_role = 3
        WHERE user_id = ?
    """, (user_id,))

    conn.commit()
    conn.close()
