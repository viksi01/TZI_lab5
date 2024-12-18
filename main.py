from functions import feistel_decrypt, feistel_encrypt

text = "This is a text for lab using the Feistel network"
cipher_text = feistel_encrypt(text)
decrypted_text = feistel_decrypt(cipher_text)

print("Text:", text)
print("Cipher:", cipher_text)
print("Decrypted text:", decrypted_text)
print("Сomparison:", decrypted_text == text)