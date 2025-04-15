import pytest
from unittest.mock import patch
from project import add_transaction, remove_transaction, summary

@pytest.fixture
def sample_transactions():
    return [
        {'date': '2025-04-15', 'category': 'Food', 'description': 'Lunch', 'type': 'expense', 'amount': 100},
        {'date': '2025-04-15', 'category': 'Salary', 'description': 'Monthly Pay', 'type': 'income', 'amount': 1000},
        {'date': '2025-04-15', 'category': 'Grocery', 'description': 'Veggies', 'type': 'expense', 'amount': 150},
    ]

def test_add_transaction(monkeypatch):
    inputs = iter(['income', 'Gift', '200', 'Birthday gift'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    transactions = []
    with patch('builtins.open'):
        add_transaction(transactions, 'transactions.json')

    assert len(transactions) == 1
    assert transactions[0]['category'] == 'Gift'
    assert transactions[0]['amount'] == 200

def test_remove_transaction(sample_transactions, capsys):
    remove_transaction(sample_transactions, "Food")
    captured = capsys.readouterr()

    categories = [t['category'] for t in sample_transactions]
    assert "Transaction Removed" in captured.out
    assert "Food" not in categories

def test_summary(sample_transactions, capsys):
    summary(sample_transactions)
    captured = capsys.readouterr()

    assert "Total income" in captured.out
    assert "Total Expense" in captured.out
    assert "Total Balance" in captured.out
