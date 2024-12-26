import tkinter as tk

class LeftPanel:
    def __init__(self, root):
        """Set up the left panel with an instruction input box."""
        input_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10, width=200)
        input_frame.grid(row=0, column=0, sticky="nsew")

        tk.Label(
            input_frame, text="Enter Instructions", font=("Arial", 14, "bold"), bg="#f0f0f0"
        ).pack(anchor="w", pady=(0, 5))

        self.input_box = tk.Text(input_frame, height=20, width=25, bg="#ffffff", font=("Courier New", 10))
        self.input_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.input_box.insert("1.0", ">>> ")
        self.input_box.bind("<Return>", self._add_prefix_to_new_line)

    def _add_prefix_to_new_line(self, event):
        """Add '>>>' to the start of each new line in the input box."""
        self.input_box.insert("insert", "\n>>> ")
        return "break"

    def clear_input_box(self):
        """Clear the input box and reset it to the initial state."""
        self.input_box.delete("1.0", tk.END)
        self.input_box.insert("1.0", ">>> ")