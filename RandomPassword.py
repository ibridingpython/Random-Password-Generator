from random import choice

# Made by Ibad 15/3/26 18:40
# Update at 15/03/26 20:00
# Updated to make sure that it always generates a strong password.

prompt = ("Welcome to password generator!")
prompt += ("\nEnter 0 to end the program.")
prompt += ("\nEnter the length of the password: ")

lowercase = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

uppercase = [
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = [
'0','1','2','3','4','5','6','7','8','9'
]

symbols = [
'!','@','#','$','%','^','&','*','(',')',
'-','_','=','+','?'
]

characters = lowercase + uppercase + numbers + symbols

while True:
    move = input(prompt)
    move = int(move)
    
    password = []
    
    password.append(choice(lowercase))
    password.append(choice(uppercase))
    password.append(choice(numbers))
    password.append(choice(symbols))
    
    if move != 0:
        for _ in range(move - 4):
            value = choice(characters)
            password.append(value)
            
        print(f"===Generating {move} Characters===")
        print(f"Generated password:", "".join(str(char) for char in password))
        print()
    else:
        print("Program terminated, thank you.")
        print()
        break
