fitxategi=open("C:\\Users\\aaranguren\\Documents\\Python\\python-hasiera\\Fitxategiak\\Jendea.txt")
hiztegienZerrenda=[]
errenkadak=fitxategi.readlines()
for x in range(len(errenkadak)):
    zerrenda=errenkadak[x].split(";")
    hiztegia={'id': zerrenda[0], 'izena': zerrenda[1], 'abizena': zerrenda[2], 'jaiotze': zerrenda[3][:10]}
    hiztegienZerrenda.append(hiztegia)
print(hiztegienZerrenda)
fitxategi.close()