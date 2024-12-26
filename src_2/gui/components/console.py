import tkinter as tk

class Console:
    def __init__(self, root):
        """Set up the console for displaying output."""
        console_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=5)
        console_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

        console_label = tk.Label(
            console_frame, text="Console Output", font=("Arial", 12, "bold"), bg="#f0f0f0"
        )
        console_label.pack(anchor="w")

        self.console_output = tk.Text(
            console_frame,
            bg="#1e1e1e", fg="#00ff00", font=("Courier New", 10),
            state=tk.DISABLED, wrap=tk.WORD, relief=tk.SUNKEN, borderwidth=3
        )
        self.console_output.pack(fill=tk.BOTH, expand=True)

    def write_to_console(self, text):
        """Append text to the console."""
        self.console_output.config(state=tk.NORMAL)
        self.console_output.insert(tk.END, f"{text}\n")
        self.console_output.config(state=tk.DISABLED)
        self.console_output.see(tk.END)

    def clear_console(self):
        """Clear all text from the console."""
        self.console_output.config(state=tk.NORMAL)
        self.console_output.delete("1.0", tk.END)
        self.console_output.config(state=tk.DISABLED)
