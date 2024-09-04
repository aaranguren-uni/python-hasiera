def amaieraAmankomuna(bat, bi):
    gehienezkoa=0
    if len(bat) > len(bi):
        gehienezkoa=len(bi)
    else:
        gehienezkoa=len(bat)
    erantzuna=""
    for x in range(gehienezkoa):
        if bi[len(bi)-x:len(bi)]==bat[len(bat)-x:len(bat)]:
            erantzuna=bi[len(bi)-x:len(bi)]
        else:
            break
    return erantzuna

print("Bi hitzen arteko amaiera amankomuna hurrengoa da: "+amaieraAmankomuna('Kauro','Aguro'))
