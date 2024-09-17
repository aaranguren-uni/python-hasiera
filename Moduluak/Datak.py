from datetime import date, datetime

format="%Y-%m-%d"
jaiotze=input("Sartu zure jaiotze data hurrengo formatuan [AAAA-MM-DD]: ")

try:
    emaitza=bool(datetime.strptime(jaiotze, format))
except ValueError:
    emaitza = False
if emaitza:
    jaiotze_data=date.fromisoformat(jaiotze)

    #Asteko eguna kalkulatu eta adierazi
    eguna=""
    match jaiotze_data.weekday():
        case 0:
            eguna="astelehena"
        case 1:
            eguna="asteartea"
        case 2:
            eguna="asteazkena"
        case 3:
            eguna="osteguna"
        case 4:
            eguna="ostirala"
        case 5:
            eguna="larunbata"
        case 6:
            eguna="igandea"
    print(f"Zure jaiotze eguna {eguna} izan zen")

    #Urtebetetzerako falta diren egunak kalkulatu
    aurtengo_urtebetetzea=jaiotze_data.replace(year=2024)
    if aurtengo_urtebetetzea == date.today():
        print("Zorionak!!!!")
    else:
        if aurtengo_urtebetetzea < date.today():
            aurtengo_urtebetetzea=jaiotze_data.replace(year=2025)
        faltan = aurtengo_urtebetetzea - date.today()
        print(f"Zure urtebetetzerako {faltan.days} egun falta dira.")
else:
    print("Sartutako horrek ez du formatua betetzen...")
