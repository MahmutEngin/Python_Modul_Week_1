#Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops.
sayi=int(input("Bir sayı giriniz: "))
#for i in range(1,sayi+1):
#    if i % 2 == 0:
#        print(i, end=", ")
i=0
while i<= sayi:
    if i % 2 == 0:
        print(i)
    i+=1