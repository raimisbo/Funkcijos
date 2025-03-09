import random

print("FUNKCIJOS")
print("=======================UZDAVINIAI==========================")

print("================uzd.1=================")

# Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina.


def skaiciai():
    a = random.randint(0, 3)
    b = random.randint(0, 7)
    result = a + b
    print(f"Skaiciai : {a} ir {b}")
    print("Suma:", result)
    return result

print(f"Funkcijos grazinimas: {skaiciai()}")

print('==================Uzd.2======================')

# Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina float tipo reikšmę. Reikšmė yra : 9.8596;
# Gautą reikšmę atspausdinkite. (Klaida salygoj  turi buti 9,8696)

def PISq():
    return 9,8596

print(PISq())

print('==================Uzd.3====================')

# Sukurkite Funkciją kuri priima du int tipo kintamuosius. Funkcija gražina skaičių sandaugą.;
# Gautą reikšmę atspausdinkite.

def sandauga():
    a = random.randint(0, 3)
    b = random.randint(0, 7)
    result = a * b
    print(f'Skaiciai : {a} ir {b}')
    return result

print(f'Funkcijos grazinimas: {sandauga()}')

print('===================Uzd.4=====================')

# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.


mas = []
def masyvas_a(mas):

    for i in range(7):
        a = random.randint(0, 7)
        mas.append(a)
    return mas

print(masyvas_a(mas))


print("=============Uzd.5=================")

# Sukurkite Funkciją kuri priima du int tipo kintamuosius, min ir max reikšmėms nustatyti ir
# sugeneruoja random int skaičių ir jį gražintų.

def generuoti(min_value: int, max_value: int):
    return random.randint(min_value, max_value)

skaicius = generuoti(5, 34)
print(f'Sugeneruotas skaicius:', skaicius)

print("==================Uzd.6========================")

# Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą ir jį gražintų. Funkcija priima tris int tipo kintamuosius, min, max ir length reikšmėms nustatyti.

def generuoti_mas( min_value: int, max_value: int, length: int):
    return [random.randint(min_value, max_value) for _ in range(length)]

masyvas = generuoti_mas(1, 100, 10)
print(masyvas)

print('=============Uzs.7===============')

# Sukurkite Funkciją kuri panaudotų 6-toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir grąžintų reikšmę.

def suma_mas(generuoti_mas):
    return sum(masyvas)

suma = suma_mas(masyvas)
print(suma)

print('=============Uzd.8===============')





