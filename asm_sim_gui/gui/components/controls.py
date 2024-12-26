import tkinter as tk

class Controls:
    def __init__(self, root, run_callback, reset_callback):
        """Set up Run and Reset buttons in the control panel."""
        control_frame = tk.Frame(root, bg="#f0f0f0")
        control_frame.grid(row=2, column=0, columnspan=3, pady=10)

        buttons = [
            ("Run", "#4caf50", run_callback),
            ("Reset", "#f44336", reset_callback)
        ]

        for text, color, callback in buttons:
            tk.Button(
                control_frame,
                text=text,
                font=("Arial", 12),
                bg=color,
                fg="white",
                command=callback,
            ).pack(side=tk.LEFT, padx=10)
