import datetime
from tkinter import *
from tkinter import messagebox

class BankAccounts:
    def __init__(self, pin, balance, name):
        self.pin = pin
        self.balance = balance
        self.name = name