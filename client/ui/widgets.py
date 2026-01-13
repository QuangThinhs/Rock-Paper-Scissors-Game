import tkinter as tk

COLORS = {
    'bg': '#1a1a2e',
    'accent': '#e94560',
    'success': '#2ecc71',
    'warning': '#f39c12'
}

def modern_button(parent, text, command, color):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=color,
        fg="white",
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        padx=25,
        pady=10,
        cursor="hand2"
    )

def modern_entry(parent, placeholder, show=None):
    e = tk.Entry(parent, font=("Segoe UI", 12), show=show)
    e.insert(0, placeholder)
    return e
