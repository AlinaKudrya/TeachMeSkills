words = ['комок', 'собака', 'заказ']

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

for i in range(3):
    print(f'The word: "{words[i]}" is palindrome: {palindrome(words[i])}')
