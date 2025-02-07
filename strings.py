name = "John" #string
print(len(name)) #len() shows the lenght of string
print(name[0]) #number in quare bracket gets the letter, it means index

x = "Hello I am learning python"
if "Hello" in x:
    print("word 'hello' is in a text") # 'in' function check if the something is in argument

if "burger" not in x:
    print("word 'burger' is not in text")

print(x[2:10]) #from index 2 to index 9
print("Life is", x[:4]) #TRY IT ^-^ (joke)

a = "Hello, World"
print(a.upper()) # upper function = uppercase letters
print(a.lower()) # lower function = lowercase letters
print(a.replace("H", "J")) #replaces H with J
b = a.split(",") #splits the sentence and makes list of words
print(b)
