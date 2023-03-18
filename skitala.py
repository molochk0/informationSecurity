#https://pro-prof.com/forums/topic/cipher-scytale-algorithm
#источник данных

# для расшифрования нужно указать зашифрованный текст и ключ Скиталла, равный количеству столбцов при шифровании

def skitala_encrypt(text, m):  # inp - исходное сообщение, m - количество строк
    symbolAmount = len(text)  # длина сообщения
    n = int(((symbolAmount-1)/m)+1)  # кол-во столбцов
    print(f"длина сообщения {symbolAmount}")
    print(f"кол-во столбцов {n}")
    print(f"кол-во строк (ключ Скиталла) {m}")

    cipherText = [None for _ in range(symbolAmount)]
    textArray = list(text)

    for i in range(symbolAmount):
        index = int(m * (i % n) + (i / n))
        cipherText[index] = textArray[i]

    return cipherText


def skitala_print(text, m):
    ans = skitala_encrypt(text, m)
    for i in range(len(ans)):
        print(ans[i],end='')
