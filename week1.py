# Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.
for i in range(1,11):
    print(i,sep=" ",end=" ")
print()
# - Question 2: Take a number input from the user and write a Python program 
# that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops.
kullanici_veri = int(input("bir numara girin: "))
# --------for--------------------
for i in range(0,kullanici_veri):
    print(i,sep=" ",end=" ")

print() # --------while-----------
count= 0
while True:
    print(count,sep=" ",end=" ")
    count += 1
    if count ==kullanici_veri:
        break


# - Question 3: Write a Python code that receives a start and end value from the user and 
# prints all the numbers between these values ​​(including the end value) on the screen.
start = int(input("start number: "))
end = int(input("end number: "))

for i in range(start,end+1):
    print(i,sep=" ",end=" ")


# - Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.
user_veri = int(input("bir numara girin: "))
if user_veri%2 == 0:
    print("even")
else:
    print("odd")

# - Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial. 
# Factorial is the product of all positive integers between a number itself and 1.
#  For example: if the user entered 5, the program should give the following output:
#  Enter a number from the user: 5
#  Factorial: 120

user_data = int(input("bir numara girin: "))
faktoriyel= 1 
if user_data< 0: 
    print("Negatif sayi")
else:
    for i in range(1,user_data+1):
        faktoriyel *= i
    print(f"{user_data}! = {faktoriyel}")

# - Question 6: Write a Python code that receives a number from the user and checks whether this number is prime.

# Kullanıcıdan bir sayı alınır
sayi = int(input("Bir sayi girin: "))

if sayi <= 1:
    print(f"{sayi} asal bir sayi değildir.")
else:
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            print(f"{sayi} asal bir sayi değildir.")
            break
    else:
        print(f"{sayi} asal bir sayidir.")

# - Question 7: How to create a loop that calculates the Fibonacci sequence and 
# returns the result as a list containing numbers up to a certain limit?

def fibonacci_up_to(limit):
    fibonacci_list = [0, 1]
    
    while True:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        if next_number > limit:
            break
        fibonacci_list.append(next_number)
    
    return fibonacci_list

limit = int(input("Fibonacci sayıları için bir üst limit girin: "))
print(f"Fibonacci dizisi (limite kadar): {fibonacci_up_to(limit)}")


# - Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.

kelime = input("Bir kelime girin: ")
ters_kelime = kelime[::-1]
print(f"Girdiğiniz kelimenin tersi: {ters_kelime}")

# - Question 9: How to create a combination of loop and conditional statement that takes a word input from the user and 
# checks whether that word is a palindrome (the same when read backwards)?
# Kullanıcıdan bir kelime alınır
kelime = input("Bir kelime girin: ")

# Harfleri küçük harfe çevirerek karşılaştırma yapılır (büyük/küçük harf duyarlılığını önlemek için)
kelime = kelime.lower()
is_palindrome = True
for i in range(len(kelime) // 2):
    if kelime[i] != kelime[-(i + 1)]:
        is_palindrome = False
        break
if is_palindrome:
    print(f"'{kelime}' bir palindromdur.")
else:
    print(f"'{kelime}' bir palindrom değildir.")
# - Question 10: Write the code that calculates the person's weight index and returns the result as underweight, 
# overweight or overweight according to the index value. (You can look on the internet for the weight index calculation)
# To do this, ask the user for their weight and height measurements. weight index
# If it is below 25, it is weak,
# Between 25-30 is normal,
# If you are over 30-40, you are overweight.
# If you are over 40, you are overweight.

# Vücut kitle indeksi hesaplama fonksiyonu
def vki_hesapla(kilo, boy):
    return kilo / (boy ** 2)

def durum_belirle(vki):
    if vki < 18.5:
        return "Zayıf"
    elif 18.5 <= vki < 25:
        return "Normal"
    elif 25 <= vki < 30:
        return "Kilolu"
    elif 30 <= vki < 35:
        return "Obez"
    elif 35 <= vki < 40:
        return "Ciddi obez"
    else:
        return "Aşırı obez"

def main():
    try:
        # Kullanıcıdan kilo ve boy bilgisi al
        kilo = float(input("Kilonuzu kilogram olarak girin: "))
        boy = float(input("Boyunuzu metre olarak girin (örneğin 1.75): "))

        # Girilen değerlerin geçerli olup olmadığını kontrol et
        if kilo <= 0 or boy <= 0:
            print("Kilo ve boy pozitif sayı olmalıdır.")
        else:
            # VKİ hesapla
            vki = vki_hesapla(kilo, boy)
            # Durumu belirle
            durum = durum_belirle(vki)
            # Sonucu yazdır
            print(f"Vücut Kitle İndeksiniz: {vki:.2f} ({durum})")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")


main()

# - Question 11: How to write a Python program that finds the largest of three numbers entered by a user?
# Kullanıcıdan üç sayı alınır
sayi1 = float(input("1. sayiyi girin: "))
sayi2 = float(input("2. sayiyi girin: "))
sayi3 = float(input("3. sayiyi girin: "))

# En büyük sayıyı bulmak için karşılaştırma yapılır
if sayi1 >= sayi2 and sayi1 >= sayi3:
    en_buyuk = sayi1
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    en_buyuk = sayi2
else:
    en_buyuk = sayi3

# Sonuç ekrana yazdırılır
print(f"En büyük sayi: {en_buyuk}")


# - Question 12: Get Midterm and Final grades from a student for any course. The sum of 40% of the midterm exam grade 
# and 60% of the final grade will give the year-end average. If the average is below 50, 
# "FAILED" will appear on the screen, and if it is 50 or above, "SUCCESSFUL" will be displayed on the screen. 
# This printing process is 4 lessons. and the lessons will be written one after the other.
# 4 ders için notları al ve başarı durumunu hesapla

for i in range(1, 5):  # 1'den 4'e kadar olan dersler için döngü başlatıyoruz
    print(f"\n{i}. Dersin Notlarını Giriniz")  # Her ders için açıklama yazdırıyoruz
    
    # Kullanıcıdan vize ve final notlarını alıyoruz
    vize = float(input("Vize notu: "))  # Vize notu alınır
    final = float(input("Final notu: "))  # Final notu alınır

    # Yıl sonu not ortalamasını hesaplıyoruz
    ortalama = (vize * 0.4) + (final * 0.6)  # Vizenin %40'ı ve finalin %60'ı alınarak ortalama hesaplanır

    # Ortalama 50 ve üzeri ise "BAŞARILI", 50'nin altı ise "BAŞARISIZ" olarak belirlenir
    if ortalama >= 50:
        durum = "BAŞARILI"
    else:
        durum = "BAŞARISIZ"

    # Her dersin yıl sonu ortalamasını ve durumunu ekrana yazdırıyoruz
    print(f"{i}. Dersin yıl sonu not ortalaması: {ortalama:.2f} → {durum}")
    
# ## Hackerrank assignments
# 1.  https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# 2.  https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# 3.  https://www.hackerrank.com/challenges/python-print/problem
# 4.  https://www.hackerrank.com/challenges/finding-the-percentage/problem
