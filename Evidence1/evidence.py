def rot13_decoder(text):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char) - ord('A') if is_upper else ord(char) - ord('a')
            decoded_char = (char_code + 13) % 26
            decoded_char += ord('A') if is_upper else ord('a')
            result += chr(decoded_char)
        else:
            result += char
    return result

#Simple substitution on this one
def the_numbers():
    number_to_letter = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
        6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
        16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
        21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
    }

    leading = [16, 9, 3, 15, 3, 20, 6]
    flag = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

    leading_decrypted = ""
    for number in leading:
        leading_decrypted += number_to_letter[number]
    flag_decrypted = ""
    for number in flag:
        flag_decrypted += number_to_letter[number]
    print(leading_decrypted + '{' + flag_decrypted + '}')


def shift_cipher_encrypt(plaintext, shift):
    """
    The function will always make the string into uppercase for ease of demonstration in this example
    """

    ciphertext = ""
    for letter in plaintext:
        ciphertext += chr(65 + (ord(letter) + shift - 65) % 26)
    print('Plaintext: "{}"\nShift: "{}"\nCiphertext: "{}"\n'.format(plaintext, shift, ciphertext))


def vigenere_decrypt(ciphertext, key):
    key = key.upper()

    decrypted_text = ""

    for i in range(len(ciphertext)):
        char = ciphertext[i]

        if char.isalpha() and char.isupper():
            key_char = key[i % len(key)]

            decrypted_char = chr(((ord(char) - ord(key_char)) % 26) + ord('A'))

            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text


if __name__ == '__main__':
    ##MOD 26
    encoded_text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
    decoded_text = rot13_decoder(encoded_text)
    print(decoded_text)
    the_numbers()

    ##13
    encoded_text = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
    decoded_text = rot13_decoder(encoded_text)
    print(decoded_text)

    ##caesar - bruteforced, picked 16 because it wasn't gibberish
    cipher = "gvswwmrkxlivyfmgsrhnrisegl"
    for i in range(26):
        shift_cipher_encrypt(cipher, i)

    ##Easy1 - I did this by hand on the table but a classmate convinced me to do a code solution
    ciphertext = "UFJKXQZQUNB"
    key = "SOLVECRYPTO"

    decrypted_text = vigenere_decrypt(ciphertext, key)
    print("Ciphertext:", ciphertext)
    print("Decrypted Text:", decrypted_text)