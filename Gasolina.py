try:
    print("Sartu zure motorrarekin egin duzun distantzia")
    distantzia=int(input())
    
    print("Sartu motorrak kontsumitu duen gasolina litro kopurua")
    gasolina=int(input())


    kontsumoa=gasolina/distantzia
    print("Zure motorrak "+kontsumoa+" litro/km gastatu ditu.")
except ValueError:
    print("Sartutako horrek ez dauka zenbaki itxurarik...");