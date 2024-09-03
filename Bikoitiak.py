try:
    print("Sartu ezazu zenbaki bat")
    zenbakia=int(input())
    bikoitia=zenbakia % 2 == 0
    print("Zure zenbakia bikoitia da: "+str(bikoitia))
except ValueError:
    print("Sartutako horrek ez dauka zenbaki itxurarik...")