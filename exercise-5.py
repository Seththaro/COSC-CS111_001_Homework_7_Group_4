# In a given string you should reverse every word, but the words should stay in their places.

def backward_string_by_word(text):        
    return ' '.join(word[::-1] for word in text.split(' '))

def init():
    print(backward_string_by_word(''))
    print(backward_string_by_word('world'))
    print(backward_string_by_word('hello world'))
    print(backward_string_by_word('hello world'))

if __name__ == '__main__':
  init()
