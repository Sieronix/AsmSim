import tkinter as tk
from asm_sim_gui.gui.components.console import Console
from asm_sim_gui.gui.components.left_panel import LeftPanel
from asm_sim_gui.gui.components.center_panel import CenterPanel
from asm_sim_gui.gui.components.right_panel import RightPanel
from asm_sim_gui.gui.components.controls import Controls

class AssemblySimulatorGUI:
    def __init__(self, registers, memory):
        """Initialize the GUI with components and layout."""
        self.root = tk.Tk()
        self.registers = registers
        self.memory = memory

        self._setup_main_window()

        # Initialize components
        self.console = Console(self.root)
        self.left_panel = LeftPanel(self.root)
        self.center_panel = CenterPanel(self.root)
        self.right_panel = RightPanel(self.root, self.registers, self.memory)
        self.controls = Controls(self.root, self.run_command, self.reset_command)

        # Log startup message
        self.console.write_to_console("Program Start.")

    def _setup_main_window(self):
        """Configure the main window layout."""
        self.root.title("Assembly Language Simulator")
        self.root.geometry("1200x960")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)

        # Grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=2)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=0)

    def run_command(self):
        """Handle the Run button action."""
        self.console.write_to_console("Run command executed.")
        self.left_panel.clear_input_box()

    def reset_command(self):
        """Handle the Reset button action."""
        self.console.clear_console()
        self.console.write_to_console("Program Start.")
        self.left_panel.clear_input_box()
        self.center_panel.reset_canvas()

    def run(self):
        """Start the main application loop."""
        self.root.mainloop()


if __name__ == "__main__":
    registers = {"AR": 0, "BR": 255, "CR": 128}
    memory = [0] * 16
    app = AssemblySimulatorGUI(registers, memory)
    app.run()
