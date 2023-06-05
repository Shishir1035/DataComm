def getWrappedSum(sum, bit):
    bin_form = bin(sum)[2:]
    wrappedsum = sum
    while len(bin_form) > bit:
        num1 = bin_form[-bit:]
        num2 = bin_form[:len(bin_form)-bit]

        # converting bin to dec
        num1 , num2 = int(num1, 2) , int(num2, 2)
        wrappedsum = num1 + num2
        bin_form = bin(wrappedsum)[2:]
    return wrappedsum

def getCheckSum(wrappedsum, bit):
    num = ( 1 << bit ) - 1
    return wrappedsum ^ num
