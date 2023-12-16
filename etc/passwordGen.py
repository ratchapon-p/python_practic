import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['1', '2','3', '4','5', '6','7', '8','9', '0']
symbol = ['!', '@','#', '$','%', '^','&', '*','+', '?']

print('welcome to password generator')
letter_num = int(input('How many letters would you like in your password : \n'))
symbol_num = int(input('How many symbol would you like in your password : \n'))
number_num = int(input('How many number would you like in your password : \n'))

password_list = []

for char in range(1, letter_num + 1):
    password_list.append(random.choice(letter))
    

for char in range(1, symbol_num + 1):
    password_list.append(random.choice(symbol))
    

for char in range(1, number_num + 1):
    password_list.append(random.choice(number))

print(password_list)

password = random.shuffle(password_list)
    
password = ''

for char in password_list:
    password += char

print(f'your password is {password}')