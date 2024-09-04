try:
    print("Sartu ezazu zenbaki bat")
    zenbakia=int(input())
    zenbakia=zenbakia*85/100
    print("Zure zenbakia ehuneko 15eko deskontuarekin: "+str(zenbakia))
except ValueError:
    print("Sartutako horrek ez dauka zenbaki itxurarik...")