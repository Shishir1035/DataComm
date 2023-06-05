def dist(code, code1):
    count = 0
    if len(code) != len(code1):
        print("They are not equal length")
        exit()
    
    for i in range(0,len(code)):
        if code[i] != code1[i]:
            count = count + 1
    return count