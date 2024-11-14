import math

def RSA(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Найдем e (взаимно простое с phi)
    e = 2
    while (e < phi):
        if (math.gcd(e, phi) == 1):
            break
        else:
            e += 1

    # Найдем d — мультипликативную обратную к e по модулю phi
    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# Шифрование
def encrypt(message, public_key):
    e, n = public_key
    # Преобразуем строку в числовый формат
    message = [ord(char) for char in message]
    print(message)
    # Зашифровываем каждое число
    encrypted_message = [(char ** e) % n for char in message]
    return encrypted_message

# Расшифровка
def decrypt(encrypted_message, private_key):
    d, n = private_key
    # Расшифровываем каждое число
    decrypted_message = [chr((char ** d) % n) for char in encrypted_message]
    return ''.join(decrypted_message)

# Пример
p = 61  # Первое простое число
q = 53  # Второе простое число

message = "BASIS"
print("Исходный текст:", message)

# Генерация ключей
public_key, private_key = RSA(p, q)
print("Открытый ключ:", public_key)
print("Закрытый ключ:", private_key)

# Шифрование
encrypted_message = encrypt(message, public_key)
print("Зашифрованный текст:", encrypted_message)

# Расшифровка
decrypted_message = decrypt(encrypted_message, private_key)
print("Расшифрованный текст:", decrypted_message)
