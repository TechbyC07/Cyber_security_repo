import socket 

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    result = scanner.connect_ex((ip,port))
    scanner.close()
    return result == 0

def main():
    target_ip = input("Enter IP to scan: ")
    for port in range(1, 1025):
        if scan_port(target_ip, port):
            print(f"Port {port} is open!")
        else:
            print(f"Port {port} is closed.")

if __name__ == "__main__":
    main()