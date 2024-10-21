def stuffing(bit_sequence):
    stuffed_sequence = []
    consecutive_ones = 0
    
    for bit in bit_sequence:
        stuffed_sequence.append(bit)
        if bit == 1:
            consecutive_ones += 1
            if consecutive_ones == 5:
                stuffed_sequence.append(0)
                consecutive_ones = 0
        else:
            consecutive_ones = 0
    
    return stuffed_sequence

def unstuffing(bit_sequence):
    unstuffed_sequence = []
    consecutive_ones = 0
    
    i = 0
    while i < len(bit_sequence):
        unstuffed_sequence.append(bit_sequence[i])
        if bit_sequence[i] == 1:
            consecutive_ones += 1
            if consecutive_ones == 5 and i + 1 < len(bit_sequence) and bit_sequence[i + 1] == 0:
                i += 1  # Skip the stuffed 0
                consecutive_ones = 0
        else:
            consecutive_ones = 0
        i += 1
    
    return unstuffed_sequence

def get_user_input():
    num_bits = int(input("Enter length of bits: "))
    bit_sequence = [int(input(f"Enter bit {i + 1}: ")) for i in range(num_bits)]
    return bit_sequence

def main():
    bit_sequence = get_user_input()
    
    print("Sender: \n", bit_sequence)
    stuffed_sequence = stuffing(bit_sequence)
    print("After stuffing: \n", stuffed_sequence)
    
    unstuffed_sequence = unstuffing(stuffed_sequence)
    print("At receiver after destuffing:", unstuffed_sequence)

main()