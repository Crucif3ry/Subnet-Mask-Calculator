# SatuRn by Crucif3ry Version 1.0 #

import ipaddress

print("\n-----------------------------------------------")
print("Welcome on SatuRn, is a Subnet Mask Calculator \n")
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
print("By Crucif3ry V 1.0")

def main() : 
    number = input("-----------------------------------------------\n1 - IPv4 Subnet Mask Calculator \n2 - IPv6 Subnet Mask Calculator \n-----------------------------------------------\n\n Please Enter a Number :")
    
    if number == '1' :
        ipv4()

    if number == '2' :
        ipv6()
     

def ipv4() :
    print("\n-----------------------------------------------")
    print("----------IPv4 Subnet Mask Calculator---------- ")
    print("-----------------------------------------------\n")

    network_address_ipv4 = input("Enter IPv4 address :")
    subnet_mask_bits = input ("Enter Subnet Mask in classic or cidr format :")

    network_address_ipv4 = ipaddress.IPv4Address(network_address_ipv4)

    network = ipaddress.IPv4Network((network_address_ipv4, subnet_mask_bits), strict=False )
    broadcast = network.broadcast_address
    
    first_ip = network.network_address + 1
    last_ip = broadcast - 1

    ipint = int(network_address_ipv4)
    ipv4inbinary = bin(ipint)
    noprefixipv4 = str(ipv4inbinary)[2:]

    smint = int(network.netmask)
    subnetmaskinbinary = bin(smint)
    noprefixsmbinary = str(subnetmaskinbinary)[2:]

    netaddr = int(network.network_address)
    netaddrbinary = bin(netaddr)
    netaddrnoprefix = str(netaddrbinary)[2:]

    brd = int(broadcast)
    brdbinary = bin(brd)
    brdnoprefix = str(brdbinary)[2:]

    print("\n==========IP ADDRESS===========")
    print("Ip Address :", network_address_ipv4  )
    print("Binary Ip Adress :", noprefixipv4 )
    print("Integer Ip Address :", ipint)
    
    print("\n==========SUBNET MASK==========")
    print("Subnet Mask :", network.netmask )
    print("Subnet Mask in CIDR notation:", network.prefixlen )
    print("Binary Subnet Mask :", noprefixsmbinary )
    
    print("\n==========NETWORK ADDRESS==========")
    print("Network Ip Address :", network.network_address )
    print("Binary Network Ip Address :", netaddrnoprefix)
    
    print("\n==========BROADCAST==========")
    print("Broadcast Ip Address :", broadcast )
    print("Binary Broadcast Ip Address :", brdnoprefix )
    
    print("\n==========AVAILABLE IP==========")
    print("Number of available Ip Address:", network.num_addresses)
    print("Network Range :", network.network_address,"-",broadcast )
    
    print("\n==========USABLE IP==========")
    print("Number of usable Ip Address :", len(list(network.hosts())))
    print("First usable Ip Address :", first_ip )
    print("Last usable Ip Address :", last_ip )
    
    print("\n==========IP TYPE==========")
    if network.is_private :
        print("Private Ip Address")
    else :
        print("Public Ip Address ")
    


   

    



def ipv6() :
    print("\n-----------------------------------------------")
    print("----------IPv6 Subnet Mask Calculator---------- ")
    print("-----------------------------------------------\n")

    ipv6_network_str = input("Enter IPv6 address :")
    
    
    network = ipaddress.IPv6Network((ipv6_network_str), strict=False )
    broadcast = network.broadcast_address
    
    print("\n==========IP ADDRESS===========")
    print("Ip Address :", ipv6_network_str  )
     
    print("\n==========NETWORK ADDRESS==========")
    print("Network Ip Address :", network.network_address )
    print("Full Network Ip Address :", network.exploded )
     
    print("\n==========BROADCAST==========")
    print("Broadcast Ip Address :", broadcast )
    
    print("\n==========AVAILABLE IP==========")
    print("Number of available Ip Address:", network.num_addresses)
    print("Network Range :", network.network_address,"-",broadcast )
    
    print("\n==========IP TYPE==========")
    if network.is_private :
        print("Private Ip Address")
    else :
        print("Public Ip Address ")




if __name__ == '__main__':
    main()