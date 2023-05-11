import socket
import threading
import ipaddress

def port_scan(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
    except socket.error as e:
        print(f"An error occurred while scanning port {port}: {e}")

def main():
    while True:
        target = input("Enter target IP address: ")
        try:
            ipaddress.ip_address(target)
            break
        except ValueError:
            print("Invalid IP address. Please try again.")

    threads = []
    for port in range(1, 1025):  # Scanning well-known ports (1-1024)
        t = threading.Thread(target=port_scan, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
