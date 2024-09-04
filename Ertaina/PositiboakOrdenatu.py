def positiboak(zenbaki):
    return zenbaki > 0

def ordenatuPositiboak(zerrenda):
    negatiborikGabe=list(filter(positiboak, zerrenda))
    negatiborikGabe.sort()
    aldatuta=0
    for x in range(len(zerrenda)):
        if zerrenda[x]>0:
            zerrenda[x]=negatiborikGabe[aldatuta]
            aldatuta=aldatuta+1
    return zerrenda

x=[6, 3, -2, 5, -8, 2, -2]
print(ordenatuPositiboak(x))