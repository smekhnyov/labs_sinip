def EnterMatrix(text, rows, cols):
    index = 0
    matrix = [[None for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if index < len(text):
                matrix[row][col] = text[index]
            else:
                matrix[row][col] = "_"
            index += 1
    return matrix

def PrintMatrix(matrix, rows, cols):
    message = ""
    for j in range(cols):
        for i in range(rows):
            message += matrix[i][j]
    return message

def Encrypt(message, key1, key2, rows, cols):
    matrix = EnterMatrix(message, rows, cols)

    ct_matrix = [[None for _ in range(cols)] for _ in range(rows)]
    for j in range(cols):
        col = key1[j] - 1
        for i in range(rows):
            ct_matrix[i][j] = matrix[i][col]

    rt_matrix = [[None for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        row = key2[i] - 1
        for j in range(cols):
            rt_matrix[i][j] = ct_matrix[row][j]

    return PrintMatrix(rt_matrix, rows, cols)

def Decrypt(message, key1, key2, rows, cols):
    matrix = EnterMatrix(message, rows, cols)

    ct_matrix = [[None for _ in range(cols)] for _ in range(rows)]
    for j in range(cols):
        col = key2[j] - 1
        for i in range(rows):
            ct_matrix[i][col] = matrix[i][j]

    rt_matrix = [[None for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        row = key1[i] - 1
        for j in range(cols):
            rt_matrix[row][j] = ct_matrix[i][j]

    return PrintMatrix(rt_matrix, rows, cols)


message = "шифрование_перестановкой_"
key1 = [1, 2, 5, 4, 3]
key2 = [4, 2, 1, 5, 3]
rows = 5
cols = 5

print("Начальное сообщение: " + message)

encrypt_messsage = Encrypt(message, key1, key2, rows, cols)
print("Зашифрованное сообщение: " + encrypt_messsage)

decrypt_messsage = Decrypt(encrypt_messsage, key1, key2, rows, cols)
print("Расшифрованное сообщение: " + decrypt_messsage)
