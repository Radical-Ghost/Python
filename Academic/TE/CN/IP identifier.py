def get_ids(ip_octate, default_mask):
    mask_octate = list(map(int, default_mask.split('.')))
    net_id = []
    brd_id = []

    for i in range(4):
        net_id.append(ip_octate[i] & mask_octate[i])
        brd_id.append(ip_octate[i] | (255 - mask_octate[i]))

    print(f"Network ID: {'.'.join(map(str, net_id))}")
    print(f"Broadcast ID: {'.'.join(map(str, brd_id))}")
    print(f"Limited Broadcast ID: 255.255.255.255")
    print(f"Directed Broadcast ID: {'.'.join(map(str, brd_id))}")


def get_mask(ip_class):
    if ip_class == 'A':
        return '255.0.0.0'
    elif ip_class == 'B':
        return '255.255.0.0'
    elif ip_class == 'C':
        return '255.255.255.0'
    return None

def class_checker(ip_octate):
    if  1 <= ip_octate[0] <= 126:
        return "A"
    if 128 <= ip_octate[0] <= 191:
        return "B"
    if 192 <= ip_octate[0] <= 223:
        return "C"
    if 224 <= ip_octate[0] <= 239:
        return "D"
    if 240 <= ip_octate[0] <= 255:
        return "E"

def identifier(ip_octate):
    ip_class = class_checker(ip_octate)
    print(f"\nIP Class: {ip_class}")

    default_mask = get_mask(ip_class)
    if default_mask:
        print(f"Default Subnet Mask: {default_mask}")
    else:
        print(f"No subnet mask for Class {ip_class} address.")
        return
    
    get_ids(ip_octate, default_mask)


def ip_verify(ip):
    if ip.count(".") != 3:
        return 1
    
    ip_octate = ip.split('.')

    for octate in ip_octate:
        if int(octate) == 0 or int(octate == 255):
            pass
        if int(octate) < 0 or int(octate) > 255:
            return 1    

    return 0

def main():
    ip = input("Enter the IP address: ")
    
    if ip_verify(ip) or ip == "0.0.0.0":
        print("Invalid IP")
        return
    
    identifier(list(map(int, ip.split('.'))))

main()