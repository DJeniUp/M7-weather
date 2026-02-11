from __future__ import annotations
import time
from dataclasses import dataclass
import re

def add(a: int, b: int) -> int:
    return a + b

def normalize_name(name: str) -> str:
    name = name.strip()
    name = re.sub(r"\s+", " ", name)
    return name.lower()

def is_even(n: int) -> bool:
    return n % 2 == 0

@dataclass
class BankAccount:
    owner: str
    balance: int = 0

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

def parse_port(value: str) -> int:
    port = int(value)
    if not (1 <= port <= 65535):
        raise ValueError("port out of range")
    return port

def fetch_user(user_id: int, gateway) -> dict:
    return gateway.get_user(user_id)

def greet_user(user_id: int, gateway) -> str:
    user = fetch_user(user_id, gateway)
    return f"Hello, {normalize_name(user['name'])}!"

def get_current_timestamp() -> float:
    return time.time()
