import pytest
import app

@pytest.fixture
def account() -> app.BankAccount:
    return app.BankAccount(owner="alice", balance=100)

def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150

def test_withdraw_decreases_balance(account):
    account.withdraw(30)
    assert account.balance == 70

def test_withdraw_too_much_raises(account):
    with pytest.raises(ValueError, match="insufficient funds"):
        account.withdraw(999)

@pytest.fixture
def accounts():
    return [
        app.BankAccount("alice", 100),
        app.BankAccount("bob", 0),
    ]

def test_total_balance(accounts):
    total = sum(a.balance for a in accounts)
    assert total == 100

def test_write_receipt(tmp_path, account):
    p = tmp_path / "receipt.txt"
    account.withdraw(10)
    p.write_text(f"{account.owner}:{account.balance}")
    assert p.read_text() == "alice:90"
