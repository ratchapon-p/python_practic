import random


stages = ['a','b','c','d','e','f']

wordlist = ['keyboard']

choosen_word = random.choice(wordlist)

lives = 6

# print(f'Word is {choosen_word}')

display = []
word_length = len(choosen_word)
for word in range (word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input('I guess : ').lower()


    for position in range (word_length):
        word = choosen_word[position]
        # print(f'current position : {position} \n Current word : {word} \nI think next letter is : {guess}')
        if word == guess:
            display[position] = word

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('Game over')

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print('Victory')
    
    print(stages[lives - 1])
    
