
alphabet = "abcdefghijklmnopqrstuvwxyz"

done = False

def encrypt():    
    plaintext = input ('Enter Message for Encryption ')
    cipher = '' 
    key = input ('Enter Desired Key for Encryption: ')
    key = int (key)
    for c in plaintext:
        if c in alphabet:
            cipher += alphabet [(alphabet.index(c)-key)%(len(alphabet))]
    print ('Encryption Complete. Your Message is: ' + cipher)
   

def decrypt():
        plaintext = input ('Enter Message for Decryption ')
        key = 1
        decrypt = ''
        key = input ('Enter Desired Key for Decryption: ')
        key = int (key)        
        for c in plaintext:
            if c in alphabet:
                decrypt += alphabet [(alphabet.index(c)+key)%(len(alphabet))]
        print ('Decryption Complete. Your Message is: ' + decrypt)
        


while not done:
    print ("\nWelcome to the Encryption and Decryption Machine.\nPlease select an option from the list below.\nA. Encrypt.\nB. Decrypt.\nc. Quit.")
    choice = input(" ")
    
    if choice.lower() == "a":
        try: 
            encrypt()
        except:
            print ("Invalid Key")
            continue
        
    elif choice.lower() == "b":
        try: 
            decrypt()   
        except:
            print ("Invalid Key")
            continue
        
    elif choice.lower() == "c":
        print ("Bye Bye")
        done = True 