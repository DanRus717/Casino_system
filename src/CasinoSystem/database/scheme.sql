DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS user_roles;
DROP TABLE IF EXISTS operations;
DROP TABLE IF EXISTS bank_accounts;

CREATE TABLE user_roles(
    user_role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE bank_accounts(
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    money INTEGER NOT NULL,
    profit INTEGER NOT NULL
);

CREATE TABLE users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (user_role) REFERENCES (user_role_id),
    FOREIGN KEY (bank_id) REFERENCES (account_id),
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    patronymic TEXT,
    login TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    date_of_reg DATE NOT NULL,
    date_last_enter DATE NOT NULL
);

CREATE TABLE operations(
    operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    operation_type BIT,
    FOREIGN KEY (user_operator) REFERENCES (user_id),
    amount INTEGER NOT NULL
);

INSERT INTO user_roles (name)
VALUES ('Admin'), ('Player'), ('Blocked');




