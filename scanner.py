import socket
import sys

def port_scanner(target, start_port, end_port):
    
    print(f"Scanning {target} for open ports...")

    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) #   Timeout for connection attempt


        result = sock.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()

    print("Scan complete.")

if __name__ == '__main__':
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter start port: "))
    end_port =  int(input("Enter end port: "))

    port_scanner(target_ip,start_port,end_port)