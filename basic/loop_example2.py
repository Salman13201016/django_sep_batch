









name = "Emad"
list_binary = []
list_binary_sum = []

for i in name:
    binary = (bin(ord(i)))
    # print(binary)
    binary = binary[2:]
    print(binary)
    sum = 0
    for j in binary:
        print(j)
        sum = sum + int(j)
    
    
    list_binary_sum.append(sum)
    list_binary.append(binary)

print(list_binary,list_binary_sum)