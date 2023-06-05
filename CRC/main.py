from CRC import getCRC

dataword = '1001'
divisor = '1011'
FLAG = ["correct","wrong"]

# CRC encoding
crc = getCRC(dataword, divisor)
encoded_dataword= dataword+ format(crc, '0' + str(len(divisor) - 1) + 'b')
print(f"CRC = {crc} , Encoded Codeword = {encoded_dataword}")

# CRC checking
received_dataword= '1001110'
newcrc = getCRC(received_dataword, divisor)
decoded_dataword= dataword+ format(newcrc, '0' + str(len(divisor) - 1) + 'b')

print(f"CRC = {newcrc} , Decoded Codeword = {decoded_dataword}")
print(f"The received dataword is {FLAG[newcrc!=0]}")
