import math

# 1. Napisz program w Pythonie, który za pomocą pętli for wyświetli liczby od 1 do
# 10.

for i in range(1, 11):
      print(i)

# 2. Napisz program w Pythonie, który za pomocą pętli while obliczy sumę liczb od
# 1 do 100.

# a)
sum_1 = 0
i = 1
while i <= 100:
      sum_1 += i
      i += 1

print(sum_1)

# b)
sum_2 = sum(range(1, 101))
print(sum_2)

# 3. Napisz program w Pythonie, który za pomocą pętli for wyświetli wszystkie
# liczby parzyste od 1 do 50.

print("Liczby parzyste: ")
for i in range(1, 51):
      if i % 2 == 0:
            print(i)


# 4. Napisz program w Pythonie, który za pomocą pętli while będzie obliczał silnię
# podanej przez użytkownika liczby.

# a)
n = int(input("Podaj liczbę, żeby obliczyć silnię: "))

def factorial(n):
      if n == 0 or n == 1:
            return 1
      else:
            return n * factorial(n - 1)

print(f"Silnia liczby {n} wynosi {factorial(n)}")

# b) 

print(f"Silnia liczby {n} wynosi {math.factorial(n)}")

# c)
if n < 0:
      print("Silnia jest zdefiniowana tylko dla liczb nieujemnych.")
else:
      factorial = 1
      i = 1
      
      while i <= n:
            factorial *= i
            i += 1
      print(f"Silnia liczby {n} wynosi {factorial}")

# 5. Napisz program w Pythonie, który za pomocą pętli for będzie sprawdzał, czy
# podane przez użytkownika słowo jest palindromem.

word = input("Podaj słowo: ")

word = word.replace(" ", " ").lower()

is_palindrome = True

for i in range (len(word) // 2):
      if word[i] != word[-(i + 1)]:
            is_palindrome = False
            break

if is_palindrome:
      print("Palindrom")
else:
      print("To nie jest palindrom")

# 6. Napisz program w Pythonie, który za pomocą pętli for będzie wyświetlał
# kolejne liczby Fibonacciego do podanej przez użytkownika liczby.

def fibonacci_iterative(n):
      a, b = 0, 1
      for _ in range(n):
            a, b = b, a + b
      return a

n = int(input("Podaj liczbę: "))
print(f"Element {n}-ty ciągu Fibonacciego to: {fibonacci_iterative(n)}")

# 7. Napisz program w Pythonie, który za pomocą pętli while będzie obliczał
# średnią arytmetyczną z podanych przez użytkownika liczb.

sum_of_numbers = 0
count = 0

while True:
      user_input = input("Podaj liczbę (lub wpisz 'koniec' aby zakończyć): ")
      
      if user_input.lower() == "koniec":
            break
      
      try:
            number = float(user_input)
            
            sum_of_numbers += number
            count += 1
      
      except ValueError:
            print("Nieprawidłowa liczba. Spróbuj ponownie.")
            
if count > 0:
      average = sum_of_numbers / count
      average_rounded = round(average, 2)
      print(f"Średnia arytmetyczna wprowadzonych liczb to: {average}")
else:
      print("Nie wprowadzono żadnych liczb.")