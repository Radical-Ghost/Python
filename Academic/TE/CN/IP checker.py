def ip_verify(ip): 
    if ip.count('.') != 3:
        return "Invalid IP"

    ip_octate = ip.split('.')

    for octate in ip_octate:
         if int(octate) == 0 or int(octate == 255):
             pass
         if int(octate) < 0 or int(octate) > 255:
            return "Invalid IP"    

    return "Valid IP"

print(ip_verify(input("Enter IP address: ")))