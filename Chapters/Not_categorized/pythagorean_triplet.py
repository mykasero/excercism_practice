def triplets_with_sum(number):
    final = []

    for a in range(1, number // 3 + 1):
        for b in range(a, (number - a)//2 +1):
            c = number - a - b

            if (a * a) + (b * b) == c * c:
                final.append([a,b,c])

    return final