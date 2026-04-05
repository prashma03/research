import socket

TARGET_IP = '127.0.0.1'
TARGET_PORT = 65432

def execute_remote_termination():
    """Simulates a guardian agent sending a validated termination signal."""
    print("--- Guardian Agent Interface ---")
    input("Press Enter to broadcast 'SIG_TERMINATE' to the Target Node...")
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender:
            sender.connect((TARGET_IP, TARGET_PORT))
            # Sending the standard control signal
            sender.sendall(b"SIG_TERMINATE")
            print("[+] Signal successfully transmitted to Target Node.")
    except ConnectionRefusedError:
        print("[X] ERROR: Communication failed. Target Node is offline.")

if __name__ == "__main__":
    execute_remote_termination()
    