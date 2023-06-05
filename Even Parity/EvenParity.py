def getParityBit(dataword):
    return dataword.count('1') % 2

def isCorrupt(codeword):
    return codeword.count('1') % 2    