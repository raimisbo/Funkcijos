import math
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

def symb_lett_digit(txt):
    nums = ""
    for symbol in txt:
        if symbol.isdigit():
            nums += symbol
        else:          # else:# jeigu turiu prikaupes skaiciu, atspausdinu ir isvalau kintamaji [54]
            if nums:
                print(f'[{nums}]')
                nums = ""
            print(symbol)
    if nums:
        print(f'[{nums}]')
symb_lett_digit(rnd_str)

print('=========================Uzd.3=========================')

# Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas dalijasi be liekanos (išskyrus vienetą ir patį save). Pvz padavus 10 turi grąžinti 2, o padavus 20 gražintų 3

def dividers(dig):
    skaicius = 0
    for i in range(2, math.ceil(math.sqrt(dig))):
        if dig % i == 0:
            skaicius += 1
    return skaicius

print(dividers(29))

print('==================Uzd.4===================')

# Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77. Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją.

mas_4 = [random.randint(33, 77) for _ in range(100)]

for i in range(len(mas_4)):
        for r in range(i + 1, len(mas_4)):
            if dividers(mas_4[i]) < dividers(mas_4[r]):
                print(f'{mas_4[i]} turi {dividers(mas_4[i])} daliklius < {mas_4[r]} turi {dividers(mas_4[r])} daliklius')
                mas_4[i], mas_4[r] = mas_4[r], mas_4[i]

print(mas_4)

print('============================Uzd.5==================================')

# Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 333 iki 777.
# Naudodami 3 uždavinio funkciją iš masyvo suskaičiuokite kiek yra pirminių skaičių.

mas_5 = [random.randint(333, 777) for _ in range(100)]
print(mas_5)

def prime_dig(skaicius):
    if skaicius <= 1:
        return False
    for i in range(2, int(skaicius / 2) + 1):
        if skaicius % i == 0:
            return False
    return True

def prime_from(mas_5):
    pirminiai_skaiciai = [skaicius for skaicius in mas_5 if prime_dig(skaicius)]
    return pirminiai_skaiciai

pirminiai_skaiciai = (prime_from(mas_5))
surusiuoti_pirminiai = pirminiai_skaiciai
surusiuoti_pirminiai.sort()
print(f'Pirminiai skaiciai is masyvo mas_5 ir surusiuoti yra: {surusiuoti_pirminiai}')

print('=====================Uzd. 6=========================')

# Sugeneruokite atsitiktinio (nuo 10 iki 20) ilgio masyvą, kurio visi, išskyrus paskutinį, elementai yra atsitiktiniai skaičiai nuo 0 iki 10, o paskutinis - masyvas, kuris generuojamas pagal tokią pat salygą kaip ir pirmasis masyvas. Viską pakartokite atsitiktinį nuo 10 iki 30  kiekį kartų. Paskutinio masyvo paskutinis elementas yra lygus 0;

def generate_masyv():
    length = random.randint(10, 20)
    mas_6s = [random.randint(0, 10) for _ in range(length - 1)]
    mas_6s. append(random.randint(0, 10))
    return mas_6s

kartai = random.randint(10, 30)
for _ in range(kartai):
    mas_6s = generate_masyv()
    mas_6s[-1] = 0
    last_mas_6s = generate_masyv()
    last_mas_6s[-1] = 0
    mas_6s.append(last_mas_6s)
    print(mas_6s)

# arr = [masyvas_s6_random]
# arr.append(masyvas_s6_random_last)
# kartai = random.randint(10, 30)
# for _ in range(kartai):
#     print(arr)


#     masyvas_s6_len = random.randint(10, 20)
# masyvas_s6_random = [random.randint(0, 10) for _ in range(masyvas_s6_len)]
# masyvas_s6_random_last = [random.randint(0,10) for _ in range(masyvas_s6_len)]
# masyvas_s6_random_last[-1] = 0
#
# print(masyvas_s6_random_last)
#

