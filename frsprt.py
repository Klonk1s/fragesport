from pathlib import Path

def läs_in_frågesport(filväg):
    frågor = []
    svar = []

    try:
        with open(filväg, 'r', encoding='utf-8') as fil:
            rader = fil.readlines()
            i = 0
            while i < len(rader):
                fråga = rader[i].strip()
                i += 1
                svar_alternativ = []
                while i < len(rader) and rader[i].strip() and not rader[i].strip().startswith('Rätt svar:'):
                    svar_alternativ.append(rader[i].strip())
                    i += 1
                rätt_svar = rader[i].replace('Rätt svar:', '').strip()
                frågor.append(fråga)
                svar.append((svar_alternativ, rätt_svar))
                i += 1
    except FileNotFoundError:
        print("Kunde inte hitta filen:", filväg)

    return frågor, svar

def visa_frågesport(frågor, svar):
    for i in range(len(frågor)):
        print("Fråga", i+1, ":", frågor[i])
        print("Svarsalternativ:")
        for j, alternativ in enumerate(svar[i][0]):
            print(f"{chr(65+j)}. {alternativ}")
        användarens_svar = input("Ange ditt svar (A, B, C, D): ").upper()
        if användarens_svar == svar[i][1]:
            print("Rätt svar!\n")
        else:
            print(f"Fel svar. Rätt svar är: {svar[i][1]}\n")

#En loop för att låta användaren spela olika quizer
while True:
    #Ange sökvägar för frågesporter
    filväg_frågesport_1 = Path('C:/Users/edvin.bromarkpestan/Hemmissida/pyupgftfrsprt/frsprt.txt')
    filväg_frågesport_2 = Path('C:/Users/edvin.bromarkpestan/Hemmissida/pyupgftfrsprt/frsport2.txt')

    #Läs in frågesporter från textfiler
    frågesport_1_frågor, frågesport_1_svar = läs_in_frågesport(filväg_frågesport_1)
    frågesport_2_frågor, frågesport_2_svar = läs_in_frågesport(filväg_frågesport_2)

    #Visa tillgängliga frågesporter
    print("Välj en frågesport:")
    print("1. Frågesport 1")
    print("2. Frågesport 2")

    val = input("Ange ditt val (1 eller 2), eller 'q' för att avsluta: ")

    if val.lower() == 'q':
        #Om användaren vill avsluta programmet så skriver hen "q"
        break
    elif val == '1':
        #Spela quiz 1
        visa_frågesport(frågesport_1_frågor, frågesport_1_svar)
    elif val == '2':
        #Spela quiz 2
        visa_frågesport(frågesport_2_frågor, frågesport_2_svar)
    else:
        print("Ogiltigt val. Vänligen välj antingen 1, 2 eller 'q' för att avsluta.")

    play_again = input("Vill du spela en annan frågesport? (ja/nej): ").lower()
    if play_again != 'ja':
        #Om användern inte vill spela igen så kan de avsluta programmet genom att skriva något annat än ja
        break

print("Tack för att du spelade! Hej då!")
