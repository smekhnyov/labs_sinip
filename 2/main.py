alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ''

    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char in alphabet:
            char_index = alphabet.index(char)
            key_char = key[key_index % key_length]
            key_char_index = alphabet.index(key_char)

            encrypted_char = alphabet[(char_index + key_char_index) % len(alphabet)]
            ciphertext += encrypted_char

            key_index += 1
        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    decrypted_text = ''

    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char in alphabet:
            char_index = alphabet.index(char)
            key_char = key[key_index % key_length]
            key_char_index = alphabet.index(key_char)

            decrypted_char = alphabet[(char_index - key_char_index) % len(alphabet)]
            decrypted_text += decrypted_char

            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text


plaintext = "SHIFROVANIE"
key = "FIORD"
ciphertext = encrypt_vigenere(plaintext, key)
decrypted_text = decrypt_vigenere(ciphertext, key)

print(f"Исходный текст: {plaintext}")
print(f"Зашифрованный текст: {ciphertext}")
print(f"Расшифрованный текст: {decrypted_text}")
