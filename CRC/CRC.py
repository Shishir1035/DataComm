def getCRC(dataword, divisor):
    crc = 0
    divisorlen = len(divisor)
    augdataWord = dataword+ '0' * (divisorlen - 1)

    for i in range(len(augdataWord)-divisorlen+1):
        if augdataWord[i] == '1':
            xor_result = ''
            for j in range(divisorlen):
                xor_bit = int(augdataWord[i + j]) ^ int(divisor[j])
                xor_result += str(xor_bit)      
                # print(f'i = {i}, j = {j}, xor_bit = {xor_bit}, xor_res = {xor_result}')  
            
            # 0 to i , i to i+divisor, i+divisor to last
            augdataWord = augdataWord[:i] + xor_result + augdataWord[i + divisorlen:]

    rem = int(augdataWord[-divisorlen + 1:], 2)
    crc = augdataWord[-divisorlen+1:]
    return rem,crc

