import socket

def scan_ports(target):
    print(f"Scanning ports on {target}...")
    for port in range(20, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":  # ✅ double underscores!
    target = input("Enter target IP: ")
    scan_ports(target)
