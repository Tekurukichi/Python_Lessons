import ipaddress

def generate_network_commands(start_ip, end_ip, subnet_mask):
    network_address = ipaddress.ip_network((start_ip, end_ip), subnet_mask)
    for network in network_address.subnets():
        network_command = f"network {network.network_address} {network.netmask}"
        yield network_command

def main():
    start_ip = input("Введіть початкову IP-адресу: ")
    end_ip = input("Введіть кінцеву IP-адресу: ")
    subnet_mask = input("Введіть маску підмережі: ")

    for network_command in generate_network_commands(start_ip, end_ip, subnet_mask):
        print(network_command)

if __name__ == "__main__":
    main()
