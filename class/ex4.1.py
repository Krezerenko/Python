#Сложить элементы списка s с четными индексами.
s = [3, 4, 5, 2, 3, 5, 4]

print([(s.__setitem__(i*2, s[i*2 - 2] + s[i*2]) is not None) + s[i*2] for i in range(1, len(s) // 2 + 1)][-1])