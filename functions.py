# Функція для зсуву вліво
def feistel_function(data, shift):
    return ''.join(chr((ord(char) << shift) % 256) for char in data)

def feistel_encrypt(input_text, rounds=10, shift=3):
    # Розділення тексту на дві частини
    left = input_text[:len(input_text) // 2]
    right = input_text[len(input_text) // 2:]
    
    # Процес шифрування
    for _ in range(rounds):
        new_left = right
        new_right = ''.join(chr(ord(l) ^ ord(feistel_function(right, shift)[i])) 
                            for i, l in enumerate(left))
        left, right = new_left, new_right

    # З'єднання двох частин
    cipher_text = right + left
    return cipher_text

def feistel_decrypt(cipher_text, rounds=10, shift=3):
    # Розділення шифрованого тексту
    right = cipher_text[:len(cipher_text) // 2]
    left = cipher_text[len(cipher_text) // 2:]
    
    # Процес дешифрування
    for _ in range(rounds):
        new_right = left
        new_left = ''.join(chr(ord(r) ^ ord(feistel_function(left, shift)[i])) 
                           for i, r in enumerate(right))
        left, right = new_left, new_right

    # З'єднання двох частин
    decrypted_text = left + right
    return decrypted_text

