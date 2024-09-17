print("Sartu espazioz berezitako hitz zerrenda bat")
hitzak=input()

zerrenda=hitzak.upper().split(" ")
amaierakoZerrenda=[]
[amaierakoZerrenda.append(hitza) for hitza in zerrenda if hitza not in amaierakoZerrenda]
amaierakoZerrenda.sort()
print(" ".join(amaierakoZerrenda))