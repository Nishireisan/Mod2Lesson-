def reshenie(*args):
    i = 1
    spisok = []
    while i < ch1:
        for j in range(i, ch1 + 1):
            if ch1 % (i + j) == 0:
                spisok.append(i)
                spisok.append(j)
        i += 1
    spisok = str(spisok)
    return spisok.replace(', ', '')


ch1 = int(input('Первое число в вставке '))
print(reshenie(ch1), '- нужный пароль')
