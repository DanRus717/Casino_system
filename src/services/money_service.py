# Пополнение, списание. Взаимодействует с банк. счетом и операциями.
from src.CasinoSystem.repositories import bank_accounts_repository
from src.CasinoSystem.repositories import operations_repository
from src.CasinoSystem.repositories import user_repository

TYPE_DEPOSIT = True
TYPE_WITHDRAW = False

def deposit_money(amount:int, user_operator:int):
    user = user_repository.get_by_id(user_operator)
    bank = bank_accounts_repository.get_by_id(user.bank_id)
    if amount == 0:
        return None

    if user.user_role == 3:
        return None

    operations_repository.create(TYPE_DEPOSIT,user_operator, amount)
    bank_accounts_repository.update(bank.account_id, bank.money+amount, bank.profit)
    return

def withdraw_money(amount:int, user_operator:int):
    user = user_repository.get_by_id(user_operator)
    bank = bank_accounts_repository.get_by_id(user.bank_id)
    if amount == 0:
        return None

    if user.user_role == 3:
        return None

    if bank.money-amount<0:
        return None

    operations_repository.create(TYPE_WITHDRAW,user_operator, amount)
    bank_accounts_repository.update(bank.account_id, bank.money-amount, bank.profit)
    return