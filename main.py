from random import randint as random

def load_alphabets():                        # Extracts all the information from the alphabets.json file
    return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "", ";", ":", "'", ",", ".", "/", "<", ">", "?", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
def password_randomiser(alphabets, total_length):
    number_of_alphabets = len(alphabets)
    string = alphabets[random(0, number_of_alphabets)]
    for x in range(total_length - 1):
        try:
            string += alphabets[random(0, number_of_alphabets)]
        except IndexError:
            pass
    
    return string

alphabets = load_alphabets()
length = input("Enter the length of the password you want: ")
length = int(length)

print(password_randomiser(alphabets, length))