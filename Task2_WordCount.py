def get_user_input():
    #Take the user input 
    user_input = input("Enter a sentence or paragraph: ")
    #Check if the input is empty after removing leading and trailing whitespaces
    if not user_input.strip():
        raise ValueError("Input cannot be empty")
    #Return the user entered sentence
    return user_input

def count_words(input_text):
    #Split the input text into words and then return the words count
    words = input_text.split()
    return len(words)

def display_output(word_count):
    #Display the word count to the user
    print("Word count: ",word_count)

while True:
    try:
        #Get the user input using function
        user_input = get_user_input()
        #Check it user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        #Check for the word count
        word_count = count_words(user_input)
        #Display the output
        display_output(word_count)

    except ValueError as ve:
        #It handles other potential errors
        print("Error: ",ve)
    except Exception as e:
        print("Error: ",e)