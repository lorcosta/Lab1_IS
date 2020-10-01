def count_occurrences(word, character):
    i = 0
    for _ in word:
        if _ == character:
            i += 1
    return i


if __name__ == '__main__':
    word = raw_input('Write a word: ')
    character = raw_input('Type a character to look for: ')
    while len(character) != 1:
        print('Just one character!')
        character = raw_input('Type a character to look for: ')

    number = count_occurrences(word, character)
    if number == 1:
        print('You wrote a word with {} occurrence of the character {}'.format(number, character))
    else:
        print('You wrote a word with {} occurrences of the character {}'.format(number, character))
