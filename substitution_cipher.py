alphabet = "aAbBcCdDeEfFgGh HiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ123456789!@#$%^&*()_+-=,./<>?;:'\"[]{}\\|~`" 
key = " plmkoijnbhuygvcftrdxsezawqQAZXWSEDCRFVG_BTNYJHUMKILOP*&^%$#()-+1236,./<>?;:'\"[]{}\\|~`54789@!="

def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    result = ""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result


unencrypted_message = "Apples can taste sour \ sweet, but Timmy says that some apples are both sour and sweet! What do you think?"
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)

