import socket
import sys
import os

def check_port(port=5000):
    """Check if port is open on all interfaces"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Try to bind to all interfaces on the given port
        s.bind(('0.0.0.0', port))
        print(f"Port {port} is NOT being used")
        return False
    except socket.error:
        print(f"Port {port} IS being used")
        return True
    finally:
        s.close()

def get_ip_addresses():
    """Get all IP addresses of this machine"""
    hostname = socket.gethostname()
    print(f"Hostname: {hostname}")
    
    try:
        # Get all addresses this machine has
        addresses = socket.getaddrinfo(hostname, None)
        
        for addr in addresses:
            # Filter only IPv4 addresses
            if addr[0] == socket.AF_INET:
                ip = addr[4][0]
                print(f"IP Address: {ip}")
                
                # Try to connect to our own server on port 5000
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
                    s.connect((ip, 5000))
                    s.close()
                    print(f"  → Successfully connected to {ip}:5000")
                except Exception as e:
                    print(f"  → Failed to connect to {ip}:5000 - {str(e)}")
        
    except Exception as e:
        print(f"Error getting IP addresses: {str(e)}")

if __name__ == "__main__":
    print("\n=== NETWORK CONNECTIVITY TEST ===\n")
    print("This script will check if your Flask app is accessible.\n")
    
    # Check if port is being used
    check_port()
    
    # Get IP addresses
    print("\nChecking IP addresses:")
    get_ip_addresses()
    
    print("\n=== TEST COMPLETE ===")
    print("\nIMPORTANT: If your server is running but you cannot connect from mobile:")
    print("1. Check if your home router blocks device-to-device connections")
    print("2. Try turning off Windows firewall temporarily")
    print("3. Make sure your Flask app is running with host='0.0.0.0'")
    print("4. Try connecting using the actual IP address (not localhost)")
    
    input("\nPress Enter to exit...")
