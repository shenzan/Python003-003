
def checkNum(answer, guess):
    for g in guess:
        a = b = 0
        for i in range(len(answer)):
            if answer[i] == g[0][i]:
                a += 1
            elif g[0].find(answer[i]) != -1:
                b += 1
        if a != g[1] or b != g[2]:
            return False
    return True


# [2324 3A0B] [6809 0A0B]
example = [['2324', 3, 0], ['6809', 0, 0]]


def findAnswer():
    for i in range(1000, 10000):
        if checkNum(str(i), example):
            return i
    return "NA"


print(findAnswer())
