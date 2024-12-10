inv = [
    (1, "Lauad",),
    (2, "Toolid"),
    (3, "Kapid"),
    (4, "Uksed"),
    (5, "Potid"),
    (6, "Telliskivid"),
    (7, "Mutrid"),
    (8, "Riiulid")
]
alg = ""
inv_kogus = [1, 1, 2, 3, 1, 6, 8, 1, 5, 3, 5, 7, 8, 3, 8, 1, 1, 1, 1, 2, 3, 6, 6, 6, 1]

#Lisame otsingu toote numbri järgi
def Otsi_nr(number):
    for num, text in inv:
        if num == number:
            return f"Nr.{num}, Toode: {text}"
    return "Toodet selle numbriga ei leitud"

#Tavaline bubble sort algoritm

def sort(inv_kogus):
  for i in range(len(inv_kogus)):
    for j in range(0, len(inv_kogus) - i - 1):
      if inv_kogus[j] > inv_kogus[j + 1]:
        temp = inv_kogus[j]
        inv_kogus[j] = inv_kogus[j+1]
        inv_kogus[j+1] = temp


#Lugemis algoritm, mis vaatab palju on kindlat toodet laos
def count(ladu, y):
    count = 0
    for toode in ladu:
        if toode == y:
            count += 1
    return count





while alg != "stop":
    alg = str(input("\n\n\nMida soovite teha? \n1. Otsida toodet toote numbri järgi. \n2. Näha toodete nimekirja \n3. Sorteeri tooted laos \n\n4. Lisage toode \n5. Eemaldage toode \nSisestage valiku number: "))
    
    if alg == "1":
        Otsitav_nr = int(input("\nPalun sisestage toote number, mida otsite: "))
        vastnr = Otsi_nr(Otsitav_nr)
        print(vastnr)
        kogus = count(inv_kogus, Otsitav_nr)
        print(f"Laos on seda toodet {kogus}")
        
    
    elif alg == "2":
        print(f"\n{inv}")
    
    elif alg == "3":
        inv = sort(inv_kogus)
        print(f"\n{inv_kogus}")
        
    elif alg == "4":
        print(f"\n {inv}")
        sisestus = int(input("Palun valige toode, mida tuuakse lattu: "))
        if sisestus >= 1 and sisestus <= 8:
            koguslisa = int(input("Palun sisestage toote kogus: "))
            for i in range(koguslisa):
                inv_kogus.append(sisestus)
        else:
            print("Sellist toodet pole valikus")
    
    elif alg == "5":
        print(f"\n {inv}")
        sisestus2 = int(input("Palun valige toode, mida laost ära viiakse: "))
        if sisestus2 >= 1 and sisestus2 <= 8:
            kadu = int(input("Palun sisestage toote kogus: "))
            for i in range(kadu):
                inv_kogus.remove(sisestus2)
        else:
            print("Sellist toodet pole valikus")
    else :
        print("Pole võimalik valik")