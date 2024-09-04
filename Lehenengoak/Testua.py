
print("Sartu ezazu testu bat")
testua=input()
print("Zure testua hurrengo hizkiarekin hasten da: "+testua[:1])

print("Sartu "+ str(len(testua))+" baino txikiagoa den zenbaki positibo bat:")
try:
    zenbaki=int(input())
    if zenbaki >= len(testua) or zenbaki <= 0:
        print("Zenbakia txikiagoa eta positiboa izan behar da")
    else:
        print("Posizio horretan dagoen hizkia hurrengoa da: "+testua[zenbaki-1:zenbaki])
except ValueError:
        print("Sartutako horrek ez dauka zenbaki itxurarik...")