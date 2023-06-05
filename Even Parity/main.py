from EvenParity import getParityBit, isCorrupt

# ------------------- get parity bit --------------------
dataword = "10011"
parbit = getParityBit(dataword)
codeword = dataword + '\033[4m' + str(parbit) + '\033[0m'
print(f"Codeword for the given {dataword} is {codeword}")

# ---------- check codeword is correct or not -----------
codeword = "110011"
flag = ["Correct","Corrupted"]
print(f"The codeword {codeword} is {flag[isCorrupt(codeword)]}")
