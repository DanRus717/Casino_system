from src.CasinoSystem.database.database import get_connection
from src.CasinoSystem.models.bank_accounts import Bank_accounts


def _map(row) -> Bank_accounts:
    return Bank_accounts(*row)


def create(money, profit):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                INSERT INTO bank_accounts(money, profit)
                VALUES (?, ?)
                """, (money, profit))

    conn.commit()
    conn.close()


def get_by_id(account_id: int) -> Bank_accounts | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT account_id, money, profit
                FROM bank_accounts
                WHERE account_id = ?
                """, (account_id,))

    row = cur.fetchone()
    conn.close()

    return _map(row) if row else None


def get_all() -> list[Bank_accounts]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT account_id, money, profit
                FROM bank_accounts
                """)

    rows = cur.fetchall()
    conn.close()

    return [_map(r) for r in rows]

def update(
    account_id: int,
    money: int,
    profit: int
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE bank_accounts
        SET money = ?,
            profit = ?
        WHERE account_id = ?
    """, (money, profit, account_id))

    conn.commit()
    conn.close()

def delete_account(account_id:int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
            DELETE from bank_accounts
            WHERE account_id = ?
            """, (account_id))

    conn.commit()
    conn.close()