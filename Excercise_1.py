# 1. Napisz program w Pythonie, który poprosi użytkownika o wprowadzenie
# swojego imienia i nazwiska z klawiatury, a następnie wyświetli je na ekranie.

get_name_and_last_name = input("Podaj swoje imię i nazwisko: ")
print(get_name_and_last_name)

# 2. Stwórz program, który będzie prosił użytkownika o podanie dwóch liczb z
# klawiatury, a następnie wyświetli ich sumę, różnicę, iloczyn i iloraz.

number_1 = int(input("Wprowadź pierwszą liczbę: "))
number_2 = int(input("Wprowadź drugą liczbę: "))

add = number_1 + number_2
subtraction = number_1 - number_2
multiplication = number_1 * number_2
divide = number_1 / number_2

print(f"Liczba pierwsza - {number_1}, Liczba druga - {number_2}. Wynikiem dodawania jest: {add}, odejmowania: {subtraction}, mnożenia: {multiplication}, dzielenia: {divide}")

# 3. Stwórz program, który będzie prosił użytkownika o podanie temperatury w
# stopniach Celsiusza z klawiatury, a następnie przeliczy ją na stopnie Fahrenheita
# i wyświetli wynik.

degree_sign = chr(176)

def celsius_to_fahrenheit(celsius):

      fahrenheit = (celsius * 9/5 + 32)
      return fahrenheit

celsius = int(input("Podaj temperaturę w stopniach Celsjusza: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}{degree_sign} Celsjusza to {fahrenheit}{degree_sign} Fahrenheita.")

# 4. Napisz program w Pythonie, który obliczy sumę dwóch liczb podanych przez
# użytkownika i wyświetli ją na ekranie. Dodaj komentarze do kodu, które opisują
# poszczególne kroki programu.

# inicjalizacja zmiennej num_1 i przypisanie do niej operacji input, polegającej na pobraniu od użytkownika pierwszej liczby
num_1 = int(input("Wprowadź pierwszą liczbę: "))

# inicjalizacja zmiennej num_2 i przypisanie do niej operacji input, polegającej na pobraniu od użytkownika drugiej liczby
num_2 = int(input("Wprowadź drugą liczbę: "))

# inicjalizacja zmiennej add polegająca na dodaniu zmiennej num_1 i num_2
add = num_1 + num_2

# inicjalizacja zmiennej subtraction polegająca na odjęciu zmiennej num_1 i num_2
subtraction = num_1 - num_2

# inicjalizacja zmiennej multiplication polegająca na pomnożeniu zmiennej num_1 i num_2
multiplication = num_1 * num_2

# Sprawdzenie czy zmienna num_2 nie jest równa 0
if num_2 != 0:
      # inicjalizacja zmiennej divide polegająca na podzieleniu zmiennej num_1 i num_2
      divide = num_1 / num_2
# Jeśli warunek pierwszy nie zostanie spełniony to wykonaj to:
else:
      # nieskończona pętla while, sprawdzająca czy liczba wprowadzona przez użytkownika jest inna niż zero
      while num_2 == 0:
            num_2 = int(input("Nie można dzielić przez 0! Podaj liczbę inną niż 0: "))
      divide = num_1 / num_2

# wydrukowanie wyników w konsoli
# Wynik dzielenia z dokładnością do dwóch miejsc po przecinku
print(f"""
      Liczba pierwsza: {num_1}
      Liczba druga: {num_2}
      Wyniki:
            - Dodawanie: {add}
            - Odejmowanie: {subtraction}
            - Mnożenie: {multiplication}
            - Dzielenie: {divide:.2f} 
      """)

# 5. Napisz program, który obliczy pole prostokąta. Dodaj komentarze opisujące
# poszczególne kroki algorytmu.

# Pobranie długości boku A od użytkownika
side_A = int(input("Podaj długość boku A: "))
# Sprawdzenie, czy bok A jest większy od 0
while side_A >= 0:
       # Jeśli bok A jest równy 0, prosimy użytkownika o ponowne podanie wartości
      side_A = int(input("Długość boku nie może być mniejsza ani równa 0. Podaj długość boku A: "))

# Pobranie długości boku B od użytkownika    
side_B = int(input("Podaj długość boku B: "))

# Sprawdzenie, czy bok B jest większy od 0
while side_B >= 0:
       # Jeśli bok B jest równy 0, prosimy użytkownika o ponowne podanie wartości
      side_B = int(input("Długość boku nie może być mniejsza ani równa 0. Podaj długość boku B: "))
      
# Obliczenie pola prostokąta (pole = długość * szerokość)
# Wydrukowanie wyniku  
print(f"Pole prostokąta o bokach A - {side_A}cm i B - {side_B}cm wynosi {side_A * side_B}cm2")

# 6. Napisz program w Pythonie, który poprosi użytkownika o podanie swojego
# imienia i nazwiska, a następnie wyświetli je w formacie "Nazwisko, Imię".
# Sprawdź czy użytkownik podał poprawne dane (czy są to ciągi znaków).

# a)
name = input("Podaj imię: ")
last_name = input("Podaj nazwisko: ")
print(last_name, name)

# b)
name_and_last_name = input("Podaj swoje imię i nazwisko: ")

position = name_and_last_name.find(" ")

first_name, last_name = name_and_last_name.split(" ", 1)
print(last_name, first_name)