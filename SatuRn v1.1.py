#V1.1 add :
#Handling Invalid Input
#IP address classes, membership in private or public networks, types of subnets
#Adding input validation
#by Despait

import ipaddress

print("\n-----------------------------------------------")
print("Welcome on SatuRn, a Subnet Mask Calculator \n")
print("""                                _.oo.       
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
 ^^""")
print("By Crucif3ry, V 1.1")

def main():
    while True:
        number = input("-----------------------------------------------\n1 - IPv4 Subnet Mask Calculator \n2 - IPv6 Subnet Mask Calculator \n-----------------------------------------------\n\nPlease Enter a Number: ")

        if number == '1':
            ipv4()
            break

        if number == '2':
            ipv6()
            break

        print("Invalid input. Please enter a valid number.")

def ipv4():
    print("\n-----------------------------------------------")
    print("----------IPv4 Subnet Mask Calculator---------- ")
    print("-----------------------------------------------\n")

    while True:
        network_address_ipv4 = input("Enter IPv4 address: ")
        subnet_mask_bits = input("Enter Subnet Mask in classic or CIDR format: ")

        try:
            network_address_ipv4 = ipaddress.IPv4Address(network_address_ipv4)
            network = ipaddress.IPv4Network((network_address_ipv4, subnet_mask_bits), strict=False)
            broadcast = network.broadcast_address

            first_ip = network.network_address + 1
            last_ip = broadcast - 1

            ipint = int(network_address_ipv4)
            ipv4inbinary = bin(ipint)[2:].zfill(32)

            smint = int(network.netmask)
            subnetmaskinbinary = bin(smint)[2:].zfill(32)

            netaddr = int(network.network_address)
            netaddrbinary = bin(netaddr)[2:].zfill(32)

            brd = int(broadcast)
            brdbinary = bin(brd)[2:].zfill(32)

            print("\n==========IP ADDRESS===========")
            print("IP Address: ", network_address_ipv4)
            print("Binary IP Address: ", ipv4inbinary)
            print("Integer IP Address: ", ipint)

            print("\n==========SUBNET MASK==========")
            print("Subnet Mask: ", network.netmask)
            print("Subnet Mask in CIDR notation: /", network.prefixlen)
            print("Binary Subnet Mask: ", subnetmaskinbinary)

            print("\n==========NETWORK ADDRESS==========")
            print("Network IP Address: ", network.network_address)
            print("Binary Network IP Address: ", netaddrbinary)

            print("\n==========BROADCAST==========")
            print("Broadcast IP Address: ", broadcast)
            print("Binary Broadcast IP Address: ", brdbinary)

            print("\n==========AVAILABLE IP==========")
            print("Number of available IP Addresses: ", network.num_addresses)
            print("Network Range: ", network.network_address, "-", broadcast)

            print("\n==========USABLE IP==========")
            print("Number of usable IP Addresses: ", len(list(network.hosts())))
            print("First usable IP Address: ", first_ip)
            print("Last usable IP Address: ", last_ip)

            print("\n==========IP TYPE==========")
            if network.is_private:
                print("Private IP Address")
                if network.is_loopback:
                    print("Loopback Address")
                elif network.is_link_local:
                    print("Link-local Address")
                elif network.is_multicast:
                    print("Multicast Address")
                else:
                    print("Global Unicast Address")
            else:
                print("Public IP Address")

            print("\n==========NETWORK CLASS==========")
            if network.is_private:
                print("Private Network (RFC 1918)")
            elif network.is_reserved:
                print("Reserved Network")
            elif network.is_multicast:
                print("Multicast Network")
            elif network.is_loopback:
                print("Loopback Network")
            elif network.is_link_local:
                print("Link-local Network")
            else:
                print("Public Network")

            break

        except ipaddress.AddressValueError:
            print("Invalid IPv4 address or subnet mask.")

def ipv6():
    print("\n-----------------------------------------------")
    print("----------IPv6 Subnet Mask Calculator---------- ")
    print("-----------------------------------------------\n")

    while True:
        ipv6_network_str = input("Enter IPv6 address: ")

        try:
            network = ipaddress.IPv6Network(ipv6_network_str, strict=False)
            broadcast = network.broadcast_address

            print("\n==========IP ADDRESS===========")
            print("IP Address: ", ipv6_network_str)

            print("\n==========NETWORK ADDRESS==========")
            print("Network IP Address: ", network.network_address)
            print("Full Network IP Address: ", network.exploded)

            print("\n==========BROADCAST==========")
            print("Broadcast IP Address: ", broadcast)

            print("\n==========AVAILABLE IP==========")
            print("Number of available IP Addresses: ", network.num_addresses)
            print("Network Range: ", network.network_address, "-", broadcast)

            print("\n==========IP TYPE==========")
            if network.is_private:
                print("Private IP Address")
            else:
                print("Public IP Address")

            print("\n==========NETWORK CLASS==========")
            if network.is_private:
                print("Private Network (ULA)")
            elif network.is_link_local:
                print("Link-local Network")
            elif network.is_multicast:
                print("Multicast Network")
            elif network.is_loopback:
                print("Loopback Network")
            elif network.is_reserved:
                print("Reserved Network")
            else:
                print("Global Unicast Network")

            break

        except ipaddress.AddressValueError:
            print("Invalid IPv6 address.")

if __name__ == '__main__':
    main()
