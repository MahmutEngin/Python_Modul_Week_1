"""Question 1: Write a Python code that prints numbers from 1 to 10 on the screen."""
for x in range(1,11):
    print(x)

    """Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.""",
x =[x for x in range(1,11)]
print(x)

"""Question 1: Write a Python code that prints numbers from 1 to 10 on the screen."""
x =1
while x <11:
    print(x)
    x += 1

    """Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops."""
sayi= int(input("Lütfden bir sayi giriniz: "))
cift = []
for x in  range(sayi):
       if x % 2==0:
           cift.append(x)
       else:
            None
print(cift)

"""Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops."""
sayi= int(input("Lütfden bir sayi giriniz: "))
for x in  range(sayi):
       if x % 2==0:
           print(x)

           """Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops."""
sayi= int(input("Lütfden bir sayi giriniz: "))
x=0
while x<sayi:
        if x % 2==0:
           print(x)
        x +=1


        """Question 3: Write a Python code that receives a start and end value from the user and prints all the numbers between these values
 ​​(including the end value) on the screen."""
x = int(input("Lütfen başlangıç sayısını giriniz: "))
y = int(input("Lütfen bitiş sayısını giriniz: "))
z = [z for z in range(x,y+1)]
print(z)



"""Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even."""
x = int(input("Lütfen bir sayı giriniz: "))
if x%2==0:
    print("Girilen sayı çifttir")
else:
    print("Girilen sayı tektir")


    """Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial. 
Factorial is the product of all positive integers between a number itself and 1. For example: if the user entered 5, 
the program should give the following output: Enter a number from the user: 5 Factorial: 120 """

x = int(input("Lütfen pozitif bir sayı giriniz: "))
f = 1
i=1
if x<0:
    print("Girdiğiniz sayı pzitif değil lütfen pozitif bir sayı girin: ")
if x>=0:
    while i<=x:
        f *=i
        i +=1
if x ==0 or x== 1:
    f =1
print("Girilen sayı :",x)
print("Girdiğinişz sayının faktöriyeli ", f)
    

    """Question 6: Write a Python code that receives a number from the user and checks whether this number is prime."""
sayi= int(input("Lütfden bir sayi giriniz: "))
asal =True
for x in range(2,int(sayi**0.5)+1):
    if sayi % x ==0:
        asal = False
        break
if sayi <2:
    print("Sayı Asal değildir. ")
elif asal:
    print("Sayı Asaldır")
else:
    print("Sayı Asal değildir")

    """Question 7: How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?"""
def fibonacci(x):
    liste =[]
    a,b =0,1
    for _ in range(x):
        liste.append(a)
        a,b = b, a+b
    return liste
x = int(input("Fibonacci sayı adededini giriniz."))
print(fibonacci(x))


"""Question 7: How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?"""
def fibonacci_sequence(limit):
    fib_list = []
    a, b = 0, 1  # Starting values for Fibonacci sequence
    
    while a <= limit:
        fib_list.append(a)
        a, b = b, a + b  # Update to the next Fibonacci numbers
    
    return fib_list

# Example usage
limit = int(input("Enter the limit for the Fibonacci sequence: "))
result = fibonacci_sequence(limit)
print(result)

"""Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen."""
kelime = input("Lütfen bir kelime giriniz: ")
ters = kelime[::-1]
print(ters)

"""Question 9: How to create a combination of loop and conditional statement that takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?"""

kelime = input("Lütfen bir kelime giriniz: ")
ters = kelime[::-1]
if kelime==ters:
    print(f"Girdiğiniz {kelime} palindrom kelimedir. ")
else:
    print(f"Girdiğiniz {kelime} palindrom değildir. ")

    """Question 10: Write the code that calculates the person's weight index and returns the result as underweight, overweight or overweight according to the index value. 
(You can look on the internet for the weight index calculation) To do this, ask the user for their weight and height measurements. weight index If it is below 25, 
it is weak, Between 25-30 is normal, If you are over 30-40, you are overweight. If you are over 40, you are overweight."""
boy = float(input("Lütfen boy uzunluğunu giriniz: "))
birim =input("Lütfen uzunluk birimini giriniz cm veya m: ")
kilo = int(input("Lütfen kilonuzu giriniz: "))
if birim=="m":
    endex = (kilo/(boy**2))
else:
    endex= (kilo/((boy/100)**2))
if endex < 18.5:
    print("Zayıfsınız")
elif endex < 24.9:
    print("Sğlıklı")
elif endex < 29.9:
    print("Şişman")
elif endex < 39.9:
    print("Obez")
else: 
    print("Aşırı obez")


"""Question 11: How to write a Python program that finds the largest of three numbers entered by a user?"""
x = int(input("Lütfen birinci sayıyı giriniz: "))
y = int(input("Lütfen ikinci sayıyı giriniz: "))
z = int(input("Lütfen üçüncğ sayıyı giriniz: "))
maximum = max(x,y,z)
print(maximum)

"""Question 12: Get Midterm and Final grades from a student for any course. The sum of 40% of the midterm exam grade and 60% of the final grade will give the year-end average. 
If the average is below 50, "FAILED" will appear on the screen, and if it is 50 or above, "SUCCESSFUL" will be displayed on the screen. This printing process is 4 lessons. 
and the lessons will be written one after the other."""
dersler=[]
sayac=0

while sayac<4:
    ders=input("Dersin adini yaziniz. Cikmak icin q yaziniz")
    sayac+=1
    if ders=="q":
        print("Programdan cikiliyor")
        break    
    if ders not in dersler:
        
        dersler.append(ders)
        x = int(input("Lütfen Vize Notunuzu Giriniz: "))
        y = int(input("Lütfen Final Notunuzu Giriniz: "))
        ortalama = x*0.4 + y*0.6
        if ortalama<50:
            print(f"{ders} dersinden BASARIZSIZ oldunuz")
        else:
            print(f"{ders} dersinden BASARILI oldunuz")
    else:
        print(f'{ders} dersinin notunu zaten girdiniz')