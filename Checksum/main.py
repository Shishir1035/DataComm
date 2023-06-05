from CheckSum import getWrappedSum, getCheckSum

# 8 bit numbers
NUMBERS = [7, 11, 12, 0, 6]
BIT = 4
FLAG = ["wrong","correct"]

def vals():
    summ = sum(NUMBERS)
    wrappedsum = getWrappedSum(summ,BIT)
    checksum = getCheckSum(wrappedsum,BIT)
    return summ,wrappedsum,checksum

# checksum generate
summ, wrappedsum, checksum = vals()
print(f"Sum = {summ}, Wrapped Sum = {wrappedsum}, CheckSum = {checksum}")

# checksum verify
NUMBERS.append(checksum)
summ, wrappedsum, checksum = vals()
print(f"Sum = {summ}, Wrapped Sum = {wrappedsum}, CheckSum = {checksum}")
print(f"Received CheckSum is {FLAG[checksum==0]}")


