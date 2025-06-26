import datetime
from tkinter import *
from tkinter import messagebox

class BankAccounts:
    def __init__(self, pin, balance, name):
        self.pin = pin
        self.balance = balance
        self.name = name

    def check_pin(self, input_pin):
        return self.pin == input_pin

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return "Success"

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount."
        self.balance += amount
        return "Success"

    def change_pin(self, new_pin):
        self.pin = new_pin

class ATMApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("500x500")
        self.window.title("Banko De Cora")
        self.window.config(background="#ff6ec7")

        self.accounts = [
            BankAccounts("1234", 10000.0, "Patricia Gwyneth"),
            BankAccounts("0309", 10000.0, "Jian Christian")
        ]

        self.current_account = None
        self.request_counter = 0

        self.build_login_screen()