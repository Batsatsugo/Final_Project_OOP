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
        if messagebox.askyesno("Logout", f"Are you sure you want to log out?\nTotal Requests: {self.request_counter}"):
            self.menu_window.destroy()
            main()

    def withdraw_window(self):
        self.request_counter += 1
        win = Toplevel(self.menu_window)
        win.geometry("200x200")
        win.title("Withdraw")
        win.config(background="#ffefa1")

        Label(win, text="Enter amount:", background="#ffefa1").pack()
        entry = Entry(win)
        entry.pack()

        def confirm():
            try:
                amount = float(entry.get())
                result = self.current_account.withdraw(amount)
                if result == "Success":
                    self.update_balance()
                    self.generate_receipt("Withdrawal", amount)
                    win.destroy()
                else:
                    messagebox.showerror("Error", result)
            except:
                messagebox.showerror("Error", "Invalid input")

        Button(win, text="Confirm", command=confirm).pack(pady=5)
        Button(win, text="Cancel", command=win.destroy).pack(pady=5)

    def deposit_window(self):
        self.request_counter += 1
        win = Toplevel(self.menu_window)
        win.geometry("300x300")
        win.title("Deposit")
        win.config(background="#ff69b4")

        Label(win, text="Enter amount:", background="#ff69b4").pack()
        entry = Entry(win)
        entry.pack()

        def confirm():
            try:
                amount = float(entry.get())
                result = self.current_account.deposit(amount)
                if result == "Success":
                    self.update_balance()
                    self.generate_receipt("Deposit", amount)
                    win.destroy()
                else:
                    messagebox.showerror("Error", result)
            except:
                messagebox.showerror("Error", "Invalid input")

        Button(win, text="Confirm", command=confirm).pack(pady=5)
        Button(win, text="Cancel", command=win.destroy).pack(pady=5)

    def change_pin_window(self):
        self.request_counter += 1
        win = Toplevel(self.menu_window)
        win.geometry("200x200")
        win.title("Change PIN")
        win.config(background="#ffefa1")

        Label(win, text="Enter new PIN:", background="#ffefa1").pack()
        entry = Entry(win)
        entry.pack()

        def confirm():
            new_pin = entry.get()
            self.current_account.change_pin(new_pin)
            messagebox.showinfo("Success", "PIN changed successfully!")
            win.destroy()

        Button(win, text="Confirm", command=confirm).pack(pady=5)
        Button(win, text="Cancel", command=win.destroy).pack(pady=5)

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ₱{self.current_account.balance:.2f}")

    def generate_receipt(self, transaction_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        receipt_text = f"""
        ********** Banko De Cora Banking **********
        Transaction Type: {transaction_type}
        Amount: ₱{amount:.2f}
        Date & Time: {timestamp}
        ************************************
        """