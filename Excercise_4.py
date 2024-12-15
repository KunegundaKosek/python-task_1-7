# Zadania na GitHub: https://github.com/KunegundaKosek/python-task_1-7

import random

# 1. Napisz program w języku Python, który przyjmie od użytkownika liczbę
# całkowitą i sprawdzi, czy jest ona parzysta czy nieparzysta. Wykorzystaj
# instrukcję warunkową if-else.

number = int(input("Podaj liczbę: "))

if number % 2 == 0 and number != 0:
      print("Parzysta")
elif number % 2 != 0:
      print("Nieparzysta")
else: 
      print("Podałeś zero!")


# 2. Stwórz program, który będzie generował losowe liczby z zakresu od 1 do 10 i
# wyświetlał je na ekranie. Program powinien kontynuować generowanie liczb
# dopóki nie zostanie wylosowana liczba większa niż 5. Wykorzystaj instrukcję
# warunkową oraz pętlę while.


while True:
      random_number = random.randint(1, 10)
      print(random_number)
      if random_number > 5:
            break

# 3. Napisz program, który będzie obliczał sumę liczb naturalnych od 1 do n, gdzie
# n jest podane przez użytkownika. Program powinien wykorzystać pętlę for oraz
# instrukcję warunkową.

n = int(input("Podaj liczbę: "))

if n <= 0:
      print("Podaj liczbę więszką niż 0.")
else:
      sum_1 = 0
      
      for i in range(1, n + 1):
            sum_1 += i
      
      print(f"Suma liczb od 1 do {n} wynosi: {sum_1}")

# 4. Stwórz program, który będzie pobierał od użytkownika kolejne liczby
# całkowite i dodawał je do listy. Program powinien przerywać pobieranie liczb,
# gdy użytkownik wpisze wartość równą zero. Następnie program powinien
# wyświetlić sumę wszystkich liczb z listy. Wykorzystaj instrukcję warunkową oraz
# instrukcję break.

numbers_list = []

while True:
      get_number = int(input("Podaj liczbę (napisz '0', żeby zakończyć): "))
      
      if get_number == 0:
            break
      
      numbers_list.append(get_number)

sum_of_numbers = sum(numbers_list)

print(f"Suma liczb: {sum_of_numbers}")


# 5. Napisz program, który będzie generował liczby z zakresu od 1 do 100 i
# wyświetlał tylko te, które są podzielne przez 3. Program powinien wykorzystać
# pętlę for oraz instrukcję continue.

for i in range(1, 101):
      if i % 3 != 0:
            continue
      
      print(i)

# 6. Napisz program w języku Python, który będzie wyświetlał wszystkie liczby od 1
# do 100, pomijając liczby podzielne przez 3.

for i in range (1, 101):
      if i % 3 == 0:
            continue
      print(i)


# 7. Stwórz program, który będzie pobierał od użytkownika listę liczb całkowitych i
# wyświetlał tylko te liczby, które są podzielne przez 3. Jeśli liczba jest równa 0,
# program powinien pominąć ją i kontynuować działanie. Wykorzystaj instrukcję
# warunkową if oraz wyrażenie continue.

numbers_list_2 = []

while True:
      get_number = int(input("Podaj liczbę: "))
      
      if get_number == 0:
            continue
      
      if get_number % 3 != 0:
            continue
      
      print(get_number)
      
      