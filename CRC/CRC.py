def getCRC(dataword, divisor):
    crc = 0
    divisor_length = len(divisor)

    augdataWord = dataword+ '0' * (divisor_length - 1)
    for i in range(len(augdataWord)-divisor_length+1):
        if augdataWord[i] == '1':
            xor_result = ''
            for j in range(divisor_length):
                xor_bit = int(augdataWord[i + j]) ^ int(divisor[j])
                xor_result += str(xor_bit)        
            augdataWord = augdataWord[:i] + xor_result + augdataWord[i + divisor_length:]

        crc = int(augdataWord[-divisor_length + 1:], 2)
    return crc