from random import choice

prompt = ("Welcome to password generator!")
prompt += ("\nEnter 0 to end the program.")
prompt += ("\nEnter the length of the password: ")

characters = [1,2,3,4,5,6,7,8,9,0,
              'a','b','c','d','e','f','g',
              'h','i','j','k','l','m','n','o',
              'p','q','r','s','t','u','v','w','x','y','z',
              '!','@','#','$','%','^','&','*','(',')',
              '-','_','=','+','?']

while True:
    move = input(prompt)
    move = int(move)
    
    password = []
    
    if move != 0:
        for _ in range(move):
            value = choice(characters)
            password.append(value)
            
        print(f"===Generating {move} Characters===")
        print(f"Generated password:", "".join(str(char) for char in password))
        print()
    else:
        print("Program terminated, thank you.")
        print()
        break
