import math
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def standard_deviation(listofnumbers):
    mean = sum(listofnumbers) / len(listofnumbers)

    minus_mean = []

    for number in listofnumbers:
        minus_mean.append((number - mean) ** 2)

    meany_mean = sum(minus_mean) / len(minus_mean)

    answer = math.sqrt(meany_mean)

    return answer


print(standard_deviation(list))
