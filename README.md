#Personal Finance Tracker

A simple command-line Python application to help you track your income and expenses. You can add, remove, summarize, and export your transactions to Excel or CSV. Built as a final project for CS50P (CS50’s Introduction to Programming with Python).

##Features

• Add Transactions (income or expense)
• Remove Transactions by category
• View Summary of your finances (total income, expenses, and balance)
• Export to Excel (.xlsx) and CSV (.csv)
• Data is stored in a persistent JSON file
• Fully testable with simple unit tests

##Requirements
• Python 3.7+
###Modules used:
• json
• csv
• datetime
• openpyxl
• tabulate

##How to Run
###Run the script:
python project.py
###Follow the on-screen menu to:
• Add or remove a transaction
• View summary
• Export to Excel/CSV

##Running Tests
###Tests are written using pytest. To run:
• pip install pytest
• pytest test_project.py

##License
This project is for learning purposes. Feel free to use or modify it as needed!

