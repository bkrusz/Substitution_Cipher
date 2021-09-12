alphabet_lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def cipher_array(array, key):
    cipher_array=[0]*len(array)
    key_count=0
    for i in range(len(array)):
        if key_count >= len(key):
            key_count=0
        cipher_array[i]=alphabet_upper.index(key[key_count].upper())
        key_count=key_count+1
    return cipher_array

def decipher(array, cipher_array):
    deciphered_array=['']*len(array)
    for i in range(len(array)):
        if array[i].isupper():
            deciphered_array[i]=alphabet_upper[(alphabet_upper.index(array[i])-cipher_array[i])%26]
        else:
            deciphered_array[i]=alphabet_lower[(alphabet_lower.index(array[i])-cipher_array[i])%26]
    return deciphered_array

def cipher(array, cipher_array):
    ciphered_array=['']*len(array)
    for i in range(len(array)):
        if array[i].isupper():
            ciphered_array[i]=alphabet_upper[(alphabet_upper.index(array[i])+cipher_array[i])%26]
        else:
            ciphered_array[i]=alphabet_lower[(alphabet_lower.index(array[i])+cipher_array[i])%26]
    return ciphered_array

def print_array(array):
    for i in range(len(array)):
        print(array[i],end="")
    print("")

option=input("To cipher, input 1. To decipher, input 0. To quit, input q: ")
while option!='q':
    if option=='1':
        text=input("Text to be ciphered: ")
        key=input("Key to cipher with: ")
        new_cipher_array=cipher_array(text, key)
        print_array(cipher(text, new_cipher_array))
        option=input("To cipher, input 1. To decipher, input 0. To quit, input q: ")
    elif option=='0':
        cipher=input("Text to be deciphered: ")
        key=input("Key to decipher with: ")
        new_cipher_array=cipher_array(cipher, key)
        print_array(decipher(cipher, new_cipher_array))
        option=input("To cipher, input 1. To decipher, input 0. To quit, input q: ")
    else:
        print("Unkown input. Try again.")
    text=""
    key=""
    cipher=""
