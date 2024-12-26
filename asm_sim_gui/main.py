from asm_sim_gui.gui.main import AssemblySimulatorGUI
from memory import initialize_registers, preload_ram

def main():
    """Set up the registers, load the RAM, and launch the app."""
    registers = initialize_registers(["R0", "R1", "R2", "R3", "IR", "AR"])
    memory = preload_ram()
    app = AssemblySimulatorGUI(registers, memory)
    app.run()

if __name__ == "__main__":
    main()