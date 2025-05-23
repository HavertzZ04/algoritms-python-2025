numeros = [3, -2, 5, -1, 6, -3, 2, 7, -5, 2]

def sublista_maxima(numeros):
    max_sum = current_sum = numeros[0]

    for num in numeros[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
print(sublista_maxima(numeros))