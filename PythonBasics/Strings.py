# Substring

message = "Hello World"
print(message[3:7])  # lo W

newmessage = message[5:11]
print(newmessage)  # World

print(message[2:])  # llo World
print(message[:8])  # Hello Wo

# %% len Function
print(len(message))  # 11

newmessage2 = message[len(message)-1:len(message)]
print(newmessage2)  # d

#  %% Lower Upper
print(message.lower())
print(message.upper())

# %% Replace Function
print(message.replace("o", "ö"))
print(message.replace("e", "T"))

# %% Split Function
info = "Berkay Çiftçi 21 Aydın"
print(info.split())
info2 = "Berkay;Çiftçi;21;Aydın"
print(info2.split(";"))
print(info2.split(";")[3])
print("Name = "+info2.split(";")[0])

# %% Input
name = input("What is Your Name ?")
print("Your name is "+name)
age = input("How Old Are You ?")
print(age+" years old ")

number1 = input("Please Enter Number One = ")
number2 = input("Please Enter Number Two = ")

print(number1+number2)
print(int(number1)+int(number2))
