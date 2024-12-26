import random

def initialize_memory(size):
    """Create a block of memory filled with zeros."""
    return [0] * size

def initialize_registers(register_names=None):
    """Set up registers with default names and initialize them to zero."""
    if register_names is None:
        register_names = ["R0", "R1", "R2", "R3", "IR", "AR"]
    return {reg: 0 for reg in register_names}

def preload_ram(size=16):
    """Fill RAM with random 8-bit values."""
    return [random.randint(0, 255) for _ in range(size)]

def display_ram(ram):
    """Show the RAM contents as binary values."""
    print("RAM Contents (16 bytes, 8 bits each):")
    for i, byte in enumerate(ram):
        print(f"Address {i:04b}: {format(byte, '08b')}")
