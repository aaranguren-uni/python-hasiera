def bisitakZenbatu(ekintza):
    with open("C:\\Users\\aaranguren\\Documents\\Python\\python-hasiera\\Fitxategiak\\Bisitak.txt","a+") as fitxategia:
        testua=fitxategia.readline()
        if not testua:
            kontadorea=0
            fitxategia.write(str(kontadorea))
        else:
            kontadorea=int(testua)
        fitxategiaAldatu(fitxategia, kontadorea, ekintza)     
    return None
def fitxategiaAldatu(fitxategia, kontadorea, ekintza):
    if ekintza=='G':
        kontadoreBerria=kontadorea+1
        fitxategia.seek(0)
        fitxategia.truncate()
        fitxategia.write(str(kontadoreBerria))
    elif ekintza=='K':
        kontadoreBerria=kontadorea-1
        fitxategia.seek(0)
        fitxategia.truncate()
        fitxategia.writelines(str(kontadoreBerria))
    else:
        print(str(kontadorea))
    return None
bisitakZenbatu('W')
