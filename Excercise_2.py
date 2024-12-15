# Zadania na GitHub: https://github.com/KunegundaKosek/python-task_1-7

# 1. Napisz program w Python, który sprawdzi, czy podana liczba jest parzysta.

get_even_numer = int(input("Podaj liczbę: "))

is_even_number = "parzysta" if get_even_numer % 2 == 0  else "nieparzysta"
print(f"Liczba jest {is_even_number}")

# 2. Napisz program w Python, który sprawdzi czy podana liczba jest dodatnia,
# ujemna czy równa zero. Wykorzystaj instrukcję warunkową IF.

if get_even_numer > 0:
      print("Liczba jest dodatnia")
elif get_even_numer < 0:
      print("Liczba jest ujemna")
else:
      print("Liczba jest równa 0")


# 3. Napisz program w Python, który sprawdzi czy podany rok jest rokiem
# przestępnym. Rok przestępny jest wtedy, gdy jest podzielny przez 4, ale nie jest
# podzielny przez 100, chyba że jest podzielny przez 400. Wykorzystaj instrukcję
# warunkową IF... ELSE...


# 4. Napisz program w Python, który sprawdzi czy podana liczba jest parzysta czy
# nieparzysta. Wykorzystaj instrukcję warunkową IF... ELSE...

if get_even_numer % 2 == 0 and get_even_numer != 0:
      print("Liczba jest parzysta.")
elif get_even_numer % 2 != 0:
      print("Liczba jest nieparzysta.")
else:
      print("Liczba jest równa 0.")

# 5. Napisz program w Python, który przyjmie od użytkownika wiek i sprawdzi czy
# osoba jest pełnoletnia czy niepełnoletnia. Wykorzystaj instrukcję warunkową IF...
# ELSE...

get_age = int(input("Podaj swój wiek: "))

if get_age >= 18:
      print("Jesteś pełnoletni.")
elif get_age >= 1 and get_age < 18:
      print("Jesteś niepełnoletni.")
else: 
      print("Podałeś niepoprawny wiek.")

# 6. Napisz program w Python, który przyjmie od użytkownika ocenę z przedmiotu
# i wyświetli odpowiedni komunikat na podstawie skali ocen (np. 5 - bardzo dobry,
# 4 - dobry, 3 - dostateczny, 2 - dopuszczający, 1 - niedostateczny). Wykorzystaj
# instrukcję warunkową ELIF.

# a)
get_grade = int(input("Podaj ocenę w skali od 1 do 6: "))

if get_grade == 1:
      print("Niedostateczny.")
elif get_grade == 2:
      print("Dopuszczający.")
elif get_grade == 3:
      print("Dostateczny")
elif get_grade == 4:
      print("Dobry.")
elif get_grade == 5:
      print("Bardzo dobry.")
elif get_grade == 6:
      print("Celujący.")
else:
      print("Podałeś niepoprawną ocenę.")

# b) 

get_grade_2 = int(input("Podaj poprawną ocenę w skali od 1 do 6: "))
      
match get_grade_2:
      case 1:
            print("Niedostateczny.")
      case 2:
            print("Dopuszczający.")       
      case 3:
            print("Dostateczny")      
      case 4:
            print("Dobry.")     
      case 5:
            print("Bardzo dobry.")      
      case 6:
            print("Celujący.")     
      case _:
            print("Podałeś niepoprawną ocenę.")
                  

# 7. Napisz program w Python, który sprawdzi, czy podana liczba jest liczbą
# pierwszą.

# Pobranie liczby od użytkownika
number = int(input("Podaj liczbę: "))


if number < 2:
    print(f"{number} nie jest liczbą pierwszą, ponieważ jest mniejsza niż 2.")
else:
    is_prime = True  
    for i in range(2, int(number**0.5) + 1):  
        if number % i == 0:
            is_prime = False  
            break

    if is_prime:
        print(f"{number} jest liczbą pierwszą.")
    else:
        print(f"{number} nie jest liczbą pierwszą.")

