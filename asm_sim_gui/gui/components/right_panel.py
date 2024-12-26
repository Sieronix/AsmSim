import tkinter as tk

class RightPanel:
    def __init__(self, root, registers, memory):
        """Set up the right panel with registers and memory sections."""
        right_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10, width=300)
        right_frame.grid(row=0, column=2, sticky="nsew")
        right_frame.grid_propagate(False)

        self.register_labels = {}
        self.memory_labels = {}

        self._setup_registers_section(right_frame, registers)
        self._setup_memory_section(right_frame, memory)

    def _setup_registers_section(self, parent, registers):
        """Create a section to display registers."""
        registers_frame = tk.LabelFrame(
            parent, text="Registers", font=("Arial", 12), padx=5, pady=5, bg="#eaeaea"
        )
        registers_frame.pack(fill=tk.X, padx=5, pady=5)

        for i, (reg, value) in enumerate(registers.items()):
            tk.Label(registers_frame, text=f"{reg}:", font=("Arial", 10), bg="#eaeaea").grid(
                row=i, column=0, sticky=tk.W, padx=5, pady=2
            )
            value_label = tk.Label(
                registers_frame, text=f"{value:08b}" if reg != "AR" else f"{value:04b}",
                font=("Arial", 10), width=10, anchor="center", bg="#ffffff"
            )
            value_label.grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)
            self.register_labels[reg] = value_label

    def _setup_memory_section(self, parent, memory):
        """Create a section to display memory values."""
        memory_frame = tk.LabelFrame(
            parent, text="Memory", font=("Arial", 12), padx=5, pady=5, bg="#eaeaea"
        )
        memory_frame.pack(fill=tk.BOTH, padx=5, pady=5)

        for i, value in enumerate(memory):
            tk.Label(memory_frame, text=f"{i:04b}:", font=("Arial", 10), bg="#eaeaea").grid(
                row=i, column=0, sticky=tk.W, padx=5, pady=2
            )
            value_label = tk.Label(
                memory_frame, text=f"{value:08b}", font=("Arial", 10), width=10, anchor="center", bg="#ffffff"
            )
            value_label.grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)
            self.memory_labels[f"{i:04b}"] = value_label
