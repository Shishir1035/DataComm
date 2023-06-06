from CRC import getCRC,reshape

dataword = '1001'
divisor = '1011'
FLAG = ["correct","wrong"]

# CRC encoding
rem = getCRC(dataword, divisor)
crc = reshape(rem, len(divisor)-1)
encoded_dataword = dataword + crc
print(f"CRC = {crc} , Encoded Codeword = {encoded_dataword}")


received_dataword= '10101010100000'

# CRC checking
newrem = getCRC(received_dataword, divisor)
newcrc = reshape(newrem, len(divisor)-1)
decoded_dataword = dataword+ newcrc
print(f"CRC = {newcrc} , Decoded Codeword = {decoded_dataword}")
print(f"The received dataword is {FLAG[newrem!=0]}")
