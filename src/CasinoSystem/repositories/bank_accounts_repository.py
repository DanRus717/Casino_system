from src.CasinoSystem.database.database import get_connection
from src.CasinoSystem.models.bank_accounts import Bank_accounts


def create(money, profit):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                INSERT INTO users(money, profit)
                VALUES (?, ?)
                """, (money, profit))

    conn.commit()
    conn.close()

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
    """, (date_last_enter, user_id))

    conn.commit()
    conn.close()