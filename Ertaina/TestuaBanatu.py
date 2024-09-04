print("Sartu espazioz berezitako hitz zerrenda bat")
hitzak=input()

zerrenda=hitzak.split(" ")
amaierakoZerrenda=[]
[amaierakoZerrenda.append(hitza) for hitza in zerrenda if hitza not in amaierakoZerrenda]
amaierakoZerrenda.sort()
for x in range (len(amaierakoZerrenda)):
    amaierakoZerrenda[x]=amaierakoZerrenda[x].upper()
print(" ".join(amaierakoZerrenda))