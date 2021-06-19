def solution(number):
    multiples = []
    for n in range(2, number):
        if n % 3 == 0:
            multiples.append(n)
        elif n % 5 == 0:
            multiples.append(n)
    return sum(multiples)
