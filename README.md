# Keylogger and Listener
This repository contains two Python scripts: `keylogger.py` and `listener.py`.
The `keylogger.py` script is designed to be run on the target system where you want to log keystrokes
The `listener.py` script is intended to be run on the system that needs to listen to the data sent by the target.

## Keylogger
The `keylogger.py` script is a simple keylogger implemented in Python. Once executed, it runs in the background on the target system and captures keystrokes made by the user. These keystrokes are sent to the listener automatically.

### Usage
To use the keylogger:
1. Clone or download this repository to the target system.
2. Run the `keylogger.py` script using Python:
3. Make sure to change the ip address in the code
4. The keylogger will start capturing keystrokes silently in the background.
**Note:** It's important to ensure that you have the necessary permissions to run the keylogger on the target system, and it should only be used for ethical purposes with the consent of the system owner.

## Listener
The `listener.py` script is responsible for listening to the data sent by the keylogger running on the target system. It receives the logged keystrokes and displays them to the user for real-time monitoring.

### Usage
To use the listener:
1. Clone or download this repository to the system where you want to monitor the keystrokes.
2. Run the `listener.py` script using Python:
3. Make sure to change the ip address in the code
4. The listener will connect to the keylogger running on the target system and display the captured keystrokes in real-time.

**Note:** Make sure that both the listener and the keylogger are configured to communicate with each other over a secure and trusted network connection.

## Disclaimer
This keylogger and listener are provided for educational only. Misuse of these scripts may violate privacy laws and regulations. The author of these scripts is not responsible for any illegal or unethical use of the software.

