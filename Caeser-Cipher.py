
# Function to display Student's details
def display_details():
    print('File: Programming Assignment 2.py')
    print('Author: Taranjot Singh')
    print('Student id : Sinty019')
    print('Email id: sinty019@mymail.unisa.edu.au')
    print('Description : Programming Assignment 2 - Caesar Cipher')
    print('This is my own work as defined by the University\'s')
    print('Acedemic misconduct policy.')

# fuction to get offset value
def get_offset():
    offset_value = int(input('Please enter your offset value(1 to 94): '))
    # while loop to make sure the value is between 1 to 94
    while offset_value < 1 or offset_value > 94:
        offset_value = int(input('Value has to be between 1 to 94: '))
        
    return offset_value
            
# Function displaying the menu and prompt to enter  
def get_menu_choice():

    menu = True
    # Starting a while loop for menu choice
    while menu == True:
        user = int(input('What would you like to do [1,2,3,4]? ' ))
        print()
        # Giving While loop to make sure user input is right 
        while user < 1 or user > 4:
            user = int(input('It has to be 1,2,3 or 4: '))
            print()
        
        if user == 1:
            print('1. Encrypt String')
            
        elif user == 2:
            print('2. Decrypt String')
            
            
        elif user == 3:
            print('3. Brute Force Decryption')
            
        elif user == 4:
            print('4. Quite')
        menu = False 
    return user

    
# Calling the display_details
display_details()
print('\n')

# Menu Description
print('*** Menu ***')
string1 = '1. Encrypt string'
string2 = '2. Decrypt String'
string3 = '3. Brute force decryption'
string4 = '4. Quite'

# Printing menu items
    
print(string1)
print(string2)
print(string3)
print(string4)

# To start the while loop

menu = True

# To join  and print the list
list2 = ''

# To use in Brute Foece decryption
offset_value = 0


while menu == True:

    # For spacing
    print()

    # Calling the get_menu_choice 
    user = get_menu_choice()
    
    if user == 1:
        # To empty the list
        list2 = ''
        word = input('Please enter string to encrypt: ')

        # Calling get_offset function for offset value
        offset = get_offset()

        # Breaking the word
        for letter in word:

            # Giving ASCII number to I
            ascii_number = ord(letter)
            

            # Joing the Encryption
            encrypting = ascii_number + offset
            
            # Wrapping back the words to ASCII 32 to 126
            if encrypting > 126:
                encrypting = encrypting - 95
            
            

        

            # Giving the ASCII character to ASCII numbers
            encrypt = chr(encrypting)
            
            # List2 Joing to print
            list2 = list2 + encrypt
            
        print()
        print('Encrypted String is')    
        print(list2)
        print()


    
    
    elif user == 2:
        word = input('Please enter string to decrypt: ')
        
        # Emptying the to list 
        list2 = ' '

        # calling the get_offset
        offset = get_offset()
        
        for letter in word:

            # Breaking the words in ASCII numbers
            ascii_number = ord(letter)

            # To Decrypt pulling out the number
            decrypting = ascii_number - offset

            # Wrap up loop 
            if decrypting < 32:
                decrypting = decrypting + 95
                

            # Giving ASCII character to ASCII number
            decrypt = chr(decrypting)

            # Making list to print
            list2 = list2 + decrypt
            
        print()
        print('Decrypted String')
        print(list2)
        print()


    # IF user choose  to Brute force decryption
        
    elif user == 3:
        word = input('Please enter string to decrypt: ')
        # Giving the space as shown in form
        print()
        

        for numbers in range(94):
            offset_value = numbers + 1

            # empyting the list
            list2 =  ''
            for letter in word:
                

                # breaking the word in ASCII numbers
                ascii_number = ord(letter)

                # pulling out the number to decrypt in chr 
                decrypting = ascii_number - offset_value
                
                
                # Wrapping up the ASCII words to 32
   
                if decrypting < 32:
                    decrypting =  decrypting + 95
                


                # Giving character to decrypt
                decrypt = chr(decrypting)

                # Joining with the list to print the character
                list2 = list2 + decrypt
            

            
            print('offset',offset_value,'= Descrypted string:' ,list2)


            
            
  # If user choose to end 
    elif user == 4:
        print('Good bye')
        menu = False
            



           
                
                

        
