from collections import Counter


def checkTheGuess(answer, guess):
    ans, gue = Counter(answer), Counter(guess.split(' ')[0])
    a = sum(i == j for i, j in zip(answer, guess))
    return guess.split(' ')[1] == '%sA%sB' % (a, sum((ans & gue).values()) - a)


def findAnswers(guesses):
    res = [i for i in range(1000, 10000) if all(
        checkTheGuess(str(i), guess) for guess in guesses)]
    return res if res else 'NA'


print(findAnswers(['2324 3A0B', '6809 0A0B']))
