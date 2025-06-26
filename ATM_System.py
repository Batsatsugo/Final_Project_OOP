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

    def build_login_screen(self):
        self.frame = Frame(self.window, background="#ff69b4")
        self.frame.pack()

        Label(self.frame, text="Welcome to Banko De Cora's ATM System", font=("Arial", 17, "bold"),
              background="#ff69b4").pack(pady=20)
        Label(self.frame, text="Enter PIN", font=("Arial", 14, "bold"), background="#ff69b4").pack()

        self.pin_entry = Entry(self.frame, font=("Arial", 17), show="*", width=6)
        self.pin_entry.pack()

        self.error_label = Label(self.frame, text="", font=("Arial", 12), background="#ff69b4")
        self.error_label.pack()

        Button(self.window, text="Confirm", command=self.login).pack()

    def login(self):
        input_pin = self.pin_entry.get()
        for acc in self.accounts:
            if acc.check_pin(input_pin):
                self.current_account = acc
                self.window.destroy()
                self.show_menu()
                return
        self.error_label.config(text="Invalid PIN. Try again.", fg="red")

    def show_menu(self):
        self.menu_window = Tk()
        self.menu_window.geometry("500x500")
        self.menu_window.title("ATM Menu")
        self.menu_window.config(background="#ff69b4")

        Label(self.menu_window, text=f"Welcome {self.current_account.name}", font=("Arial", 17, "bold"),
              background="#ff69b4").pack(pady=20)

        self.balance_label = Label(self.menu_window, text=f"Balance: ₱{self.current_account.balance:.2f}",
                                   font=("Arial", 14), background="#ff69b4")
        self.balance_label.pack()

        Button(self.menu_window, text="Withdraw", font=("Arial", 14), command=self.withdraw_window).pack(pady=5)
        Button(self.menu_window, text="Deposit", font=("Arial", 14), command=self.deposit_window).pack(pady=5)
        Button(self.menu_window, text="Change PIN", font=("Arial", 14), command=self.change_pin_window).pack(pady=5)
        Button(self.menu_window, text="Logout", font=("Arial", 14), command=self.logout).pack(pady=5)

    def logout(self):