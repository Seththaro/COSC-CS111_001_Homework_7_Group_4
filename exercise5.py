# In a given string you should reverse every word, but the words should stay in their places.

def backward_string_by_word(text):        
    return text[::-1]

def init():
    cont = True
    while cont == True:
        print("Welcome to the Text Reverser app!")
        text = input("Please enter your word: ")
        print(f'Your reversed text is "{backward_string_by_word(text)}"')
        # Condition to loop the program
        while True:
            ans = input("Do you want to restart the application?(Yes/No): ")
            if ans.lower() == 'yes':
                cont = True
                break
            elif ans.lower() == 'no':
                cont = False
                break
            else: 
                print("Invalid Input")
init()
