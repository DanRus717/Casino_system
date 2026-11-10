from src.CasinoSystem.repositories import bank_accounts_repository
from src.CasinoSystem.repositories import user_repository
from random import randint


def game(bet:int, user_id:int):
    user = user_repository.get_by_id(user_id)
    bank = bank_accounts_repository.get_by_id(user.bank_id)
    if bet == 0:
        return None

    if user.user_role == 3:
        return None

    if randint(1,100)>70:
        bank_accounts_repository.update(bank.account_id, bank.money+2*bet, bank.profit-2*bet)
        return "Win."
    else:
        bank_accounts_repository.update(bank.account_id, bank.money-bet, bank.profit+bet)
        return "Lose. Try again!"