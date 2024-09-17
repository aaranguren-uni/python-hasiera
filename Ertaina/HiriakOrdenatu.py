def hiriakOrdenatu(hizt):
    zerrenda=[]
    hiztegiOrdenatua=dict(sorted(hizt.items(), key=lambda item: item[1], reverse=True))
    for key in hiztegiOrdenatua:
        if(hiztegiOrdenatua.get(key) > 200000):
            zerrenda.append(key)

    return zerrenda
def main():
    hiztegia=dict(Bilbo=250000,
              Roma=50000000,
              Avila=60000,
              Bartzelona=1000000)
    hiriHandiak=hiriakOrdenatu(hiztegia)
    print(" ".join(hiriHandiak))

main()