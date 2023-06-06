from CRC import getCRC
dataword = '1001'
divisor = '1011'
FLAG = ["correct","wrong"]

# CRC encoding
rem,crc = getCRC(dataword, divisor)
encoded_dataword = dataword + crc
print(f"CRC = {crc} , Encoded Codeword = {encoded_dataword}")


received_dataword= '10101010100000'
# CRC checking
newrem,newcrc = getCRC(received_dataword, divisor)
print(f"Received_CRC for {received_dataword} = {newcrc}")
print(f"The received dataword is {FLAG[newrem!=0]}")
