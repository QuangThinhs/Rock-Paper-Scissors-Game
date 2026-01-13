import tkinter as tk
from ui.widgets import modern_button, modern_entry, COLORS

class LoginScreen(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root, bg=COLORS['bg'])
        self.app = app
        self.pack(expand=True, fill="both")

        tk.Label(self, text="ĐĂNG NHẬP", fg="white", bg=COLORS['bg'],
                 font=("Segoe UI", 26, "bold")).pack(pady=40)

        self.username = modern_entry(self, "Tên đăng nhập")
        self.username.pack(pady=10)

        self.password = modern_entry(self, "Mật khẩu", show="*")
        self.password.pack(pady=10)

        modern_button(
            self, "ĐĂNG NHẬP", self.login, COLORS['success']
        ).pack(pady=20)

    def login(self):
        self.app.connect()
        self.app.send({
            "action": "login",
            "username": self.username.get(),
            "password": self.password.get()
        })

    def handle_server_message(self, msg):
        if msg['action'] == 'login_response':
            if msg['success']:
                self.app.user = msg['user']
                # chuyển menu
