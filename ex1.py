def count_characters(word):
    i = 0
    for _ in word:
        i += 1
    return i


if __name__ == '__main__':
    word = raw_input('Write a word: ')
    number = count_characters(word)
    if number == 1:
        print('You wrote a word with {} character'.format(number))
    else:
        print('You wrote a word with {} characters'.format(number))
