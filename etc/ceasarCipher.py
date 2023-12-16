alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceasar(start_text, shift_anmount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_anmount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_anmount
        end_text += alphabet[new_position]
    print(f"Here's the{direction}d result : {end_text}")
    
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt and Type decode to decrypt : \n")
    text = input('Type Your message : \n')
    shift = int(input('Type shift number : \n'))

    shift = shift % 26
    ceasar(start_text=text, shift_anmount=shift, cipher_direction=direction)

    result = input("Do you want to continue 'yes' / 'no' : ")
    if result == 'no':
        should_continue = False
        print('goodbye')

# def encrypt(plain_text, shift_anmount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_anmount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f'The encode is {cipher_text}')

# def decrypt(cipher_text, shift_anmount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_anmount
#         plain_text += alphabet[new_position]
#     print(f'decode is {plain_text}')


# if direction == 'encode':
#     encrypt(plain_text=text, shift_anmount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_anmount=shift)
