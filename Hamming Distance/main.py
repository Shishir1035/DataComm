import HammingDistance as hd

def MinimumHammingDist(codewords):
    init_dist = 100000000000000000
    for code in codewords:
        for code1 in codewords:
            if code == code1:
                pass
            else:
                init_dist = min(init_dist, hd.dist(code,code1))
    return init_dist


# ------------------- codewords input ---------------------------
codewords = ['10110', '01011', '11100', '00101']
min_ham = MinimumHammingDist(codewords)
print("Minimum Hamming Distance is: 1100" + '\033[4m' + str(min_ham) + '\033[0m')
