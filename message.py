import time
from machine import Pin, UART

# Configure UART for USB communication
uart = UART(0, baudrate=9600)
uart.init(tx=Pin(0), rx=Pin(1))

# Wait for USB enumeration
time.sleep(2)

# Define your keyboard payload
keyboard_payload = [
    "DELAY 1000",              # Delay for 1 second
    "STRING notepad.exe",      # Open Notepad
    "ENTER",                   # Press Enter
    "DELAY 1000",              # Delay for 1 second
    "STRING Hello, World!",    # Type "Hello, World!"
    "ENTER",                   # Press Enter
]

# Execute the keyboard payload
for command in keyboard_payload:
    uart.write(command.encode())
    time.sleep(0.01)  # Delay between keypresses

# Close the connection
uart.deinit()
