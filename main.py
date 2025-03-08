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

skaiciai()

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
    print(f'Sandauga:', result)

sandauga()

print('===================Uzd.4=====================')

# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.

