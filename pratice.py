# NUMBERS = [7, 11, 12, 0, 6]
# BIT = 4
# def wrap(summ,bit):
#     summ = bin(summ)[2:]
#     print(summ)
#     while len(summ) > bit:
#         num1 = summ[-bit:]
#         num2 = summ[:len(summ)-bit]
#         num1,num2 = int(num1,2), int(num2,2)
#         summ = bin(num1+num2)[2:]
#     return summ

# def check(wrappedsum,bit):
#     return wrappedsum ^ ((1<<bit) - 1)

# summ = sum(NUMBERS)
# wrappedsum = int(wrap(summ,BIT),2)
# checksum = check(wrappedsum,BIT)
# print(wrappedsum,checksum)

# NUMBERS.append(checksum)
# summ = sum(NUMBERS)
# wrappedsum = int(wrap(summ,BIT),2)
# checksum = check(wrappedsum,BIT)
# print(wrappedsum,checksum)



dataword = '1001'
divisor = '1011'
new_dataword = dataword + '0'*(len(divisor)-1) 
print(new_dataword)

def getcrc(dataword,divisor):
    for i in range(len(dataword) - len(divisor) + 1):
        if dataword[i] == '1':
            exorseq = ''
            for j in range(len(divisor)):
                exor = int(dataword[i+j],2) ^ int(divisor[j],2)
                exorseq = exorseq + str(exor)
            dataword = dataword[:i] + exorseq + dataword[i+len(divisor):]
    return dataword[-len(divisor)+1:]


crc = getcrc(new_dataword,divisor)
print(crc)
Codeword = dataword+crc
print(Codeword)


print(getcrc(Codeword,divisor))
















