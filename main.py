# this is the Pig Latin translator
# pass any string and have it translated to Pig Latin

print('\nWelcome to the Pig Latin translator. \n'
      'Simply provide any amount of text and have it translated from english to Pig Latin.'
      '\nHit the "Enter" Key once you have inserted your sample of text')

# collecting user input from the CLI
user_input = str(input('\nEnter text sample here: '))


# This function will translate any text the user inputs
def piglator(para):
    # split the string into words and push into list
    new_para = ''
    word_list = para.split()
    print('\nOriginal sample:', para, '\n')

    # grab each word in the word list
    for word in word_list:
        # grab first letter of each word in the paragraph

        first_letter = word[0]

        # check if word begin with a vowel
        if first_letter in 'aeiou':
            pig_word = word + 'ay'

        else:
            pig_word = word[1:] + first_letter + 'ay'

        new_para += pig_word + ' '
        para = new_para
        continue

    print('Here is your translated text:\n')
    return print(para)


# calling the function
piglator(user_input)
print('\n\nThank you for using the Pig Latin Translator. Good Bye.')
