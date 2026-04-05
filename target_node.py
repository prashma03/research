import socket
import sys

# Network Configuration
LISTEN_IP = '127.0.0.1'
LISTEN_PORT = 65432

def start_target_node():
    """Initializes the managed node and waits for control signals."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.bind((LISTEN_IP, LISTEN_PORT))
        listener.listen()
        print(f"[*] Target Node initialized. Monitoring Port: {LISTEN_PORT}")
        print("[*] Status: Operational / Listening for Consensus Signals...")
        
        while True:
            connection, address = listener.accept()
            with connection:
                instruction = connection.recv(1024).decode('utf-8')
                
                # Consensus-driven termination logic
                if instruction == "SIG_TERMINATE":
                    print(f"\n[!] ALERT: Termination signal received from {address}")
                    print("[!] ACTION: Executing Autonomous Process Termination...")
                    print("[!] Logic: Flushing volatile buffers and exiting.")
                    sys.exit(0) # Standard exit code for successful termination
                else:
                    print(f"[*] Logic: Ignored unauthorized or unknown signal: {instruction}")

if __name__ == "__main__":
    start_target_node()