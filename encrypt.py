'''
Func to create rand key
    take random seed and create a key using it.

Func to encrypt
    take string or text file. check if key exists if yes enc aes using said key. save to new file hash is stored next to 

Func to decrypt
    take enc file and key. hash file and output to allow user to check. then use key to decrypt and save to new file


'''

import os
import hashlib
from cryptography.fernet import Fernet
import base64

def Main():

    startinput = None
    while startinput not in ["1", "2"]:
        startinput = input("1)Encrypting or 2)Decrypting?: ")
    KeyGen() if startinput == "1" else Decrypt()

def KeyGen():
    random_key = Fernet.generate_key()
    Keyvalue = Fernet(random_key)
   
    with open("key.txt", 'wb') as f:
        f.write(random_key)
    
    print("Key saved to 'key.txt'.")
    Encrypt(Keyvalue)

def Decrypt():
    with open("key.txt", 'rb') as f:
        saved_key = f.read()
    with open("cyphertext.txt", 'rb') as g:
              Ciphertext = g.read()
    Check = CheckHash()    
    if Check != 0:
         print("Hash not the same")
         return
    else:
          key = Fernet(saved_key)
          PlainTextENC = key.decrypt(Ciphertext)
          with open("plaintext.txt", 'wb') as f:
            f.write(PlainTextENC)
          print("Plaintext saved to plaintext.txt")

         
   
   
    
def Encrypt(Keyvalue):
    

    Text2Encrypt = None
    while Text2Encrypt == None:
        Text2Encrypt = input("Enter the text you want encrypted: ")
    print(Text2Encrypt)
    BytesText2Encrypt = Text2Encrypt.encode()
    ciphertext = Keyvalue.encrypt(BytesText2Encrypt)
    stringCipherText = ciphertext.decode()
    f = open("cyphertext.txt", 'w') ##CHANGE TO WHILE OPEN FOR CONSISTENCY ACROSS CODE
    f.write(stringCipherText)
    f.close()

    global CyphertextHash 
    CyphertextHash = calcHash()
    print("calchash return", CyphertextHash)
    with open("hash.txt", 'w') as file:
         file.write(CyphertextHash)

    with open("hash.txt", 'r') as f:
        hashout = f.read()

    print("hash", hashout)

    CheckHash()
    print("String Encrypted!")

def CheckHash():
      with open("hash.txt", 'r') as g:
              Hash = g.read()
      print("hash.txt: ", Hash)
      HashToCheck = calcHash()
      print("calcHash(): ",HashToCheck)
      if HashToCheck == Hash:
           return 0
      else:
           return 1
      
      
     
       

def calcHash():
        sha256 = hashlib.sha256()
        with open("cyphertext.txt", 'rb', buffering=0) as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()






Main()




