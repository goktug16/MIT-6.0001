import string

def phrase_check(text,phrase):
    text = text.lower()
    number_of_founds = 0
    for ch in string.punctuation:
        text = text.replace(ch, ' ')
    words = text.split(" ")
    for i in words.copy():
        if i == '':
            words.remove(i)
    phrase_list = phrase.split()
    print(words,phrase_list)

    if len(words) < len(phrase_list):
        return False
    for i in range(abs(len(phrase_list) - len(words)) + 1):
        for j in range(len(phrase_list)):
            if words[i + j] == phrase_list[j]:
                number_of_founds += 1

        if number_of_founds == len(phrase_list):
            return True
        number_of_founds = 0
    return False

word = 'PURPLE COW'




word2 = 'purple cow'

print(phrase_check(word,word2))


