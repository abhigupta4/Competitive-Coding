def is_even(numb):
    if numb % 2:
        return 0
    else:
        return 1
def even(numb):
    if is_even(numb):
        binary = bin(numb)
        m = 1
        new_num = 0
        for i in range(2,len(binary)):
            new_num += m * int(binary[i])
            m *= 2
        return new_num
    else:
        return numb

for _ in range(input()):
    print even(input())

#DONE