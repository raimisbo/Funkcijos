import random

print("FUNKCIJOS")
print("=======================UZDAVINIAI==========================")

print("================uzd.1=================")

# Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina.


def skaiciai():
    a = random.randint(0, 3)
    b = random.randint(0, 7)
    result = a + b
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
    return sum(generuoti_mas)

suma = suma_mas(masyvas)
print(f'Masyvo nariu skaitiniu reiksmiu suma: {suma}')

print('=============Uzd.8===============')

# Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double). Kas tas (double?)

def vidurkis(masyvas):
    return sum(masyvas) / len(masyvas)

print(f'Vidurkis: {vidurkis(masyvas)}')

print('================Uzd.9====================')

# Sukurkite Funkciją kuri priimtų du int skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas int - išoriniam ciklui, antras vidiniam.

def staciak(aukstis: int, plotis: int):
    for i in range(aukstis):
        print('*' * plotis)


staciak(5,10)

print('==================Uzd.10==================')

# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)

def skaiciuoti_simbolius_ir_tarpus(sakinys: str):
    simboliu_kiekis = len(sakinys)
    tarpu_kiekis = sakinys.count(' ')

    print(f'Simboliu yr: {simboliu_kiekis}, tarpu yra: {tarpu_kiekis}')

skaiciuoti_simbolius_ir_tarpus("Sunkiausia yra pagauti uzdavinio logika")

print('====================Uzd.11=================')

# Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės.
# Pvz “Naglis” turi gautis “silgaN”.

def uzkoduoti(sakinys: str):
    return sakinys[::-1]

uzkoduotas = uzkoduoti("Naglis")
print(uzkoduotas)

print('========================SUNKUS UZDAVINIAI============================')

print('==========================Uzd.1======================================')

# Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale. PVZ (---labas---)

def priedai_tekste(tekstas: str):
    print(f'---{tekstas}---')

priedai_tekste(' SOS ')

print('==========================Uzd.2=================================')

# Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu. Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75]. (apačioje yra funkcija, ją nusikopijuokite ir paleiskite, ji sugeneruos stringą, su kuriuo dirbsite)

def generateRndStr(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

rnd_str = (generateRndStr(10))
print(rnd_str)

def kita_funkcija(txt):
    nums = ""
    for symbol in txt:
        if symbol.isdigit():
            nums += symbol
        else:                       # else:# jeigu turiu prikaupes skaiciu, atspausdinu ir isvalau kintamaji [54]
            if nums:
                print(f'[{nums}]')
                nums = ""
            print(symbol)

kita_funkcija(rnd_str)











