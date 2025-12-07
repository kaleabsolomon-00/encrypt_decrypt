
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def encrypt(val, shift):
    encrypted=[]
    for letter in val:
        index=alphabet.index(letter)
        goal=int(index)+int(shift)
        let=alphabet[goal]
        encrypted.append(let)
    word=""
    for i in encrypted:
        word+=i
    print(word)
def decrypt(val, shift):
    decrypted=[]
    for letter in val:
        index=alphabet.index(letter)
        goal=int(index)-int(shift)
        let=alphabet[goal]
        decrypted.append(let)
    word=""
    for char in decrypted:
        word+=char
    print(word)
while True:
    choice=input("a.encrypt\nb.decrypt\n")
    if choice == "a" or choice== "A":
        val=input(" enter the word:  ")
        shift=input(" enter the shifting position:  ")
        encrypt(val,shift)
    elif choice == "b" or choice== "B":
        val = input(" enter the :  ")
        shift = input(" enter the shifting position:  ")
        decrypt(val, shift)
    else:
        print("wrong choice please wnter a right choice")