def gehiengoAbsolutua(bozkak):
    alderdiak=set(bozkak)
    for alderdi in alderdiak:
        """
        kontaketa=dict()
        #kontaketa.update({alderdi: bozkak.count(alderdi)})
        #print(kontaketa)
        """
        if bozkak.count(alderdi) > len(bozkak)/2:
            return alderdi+" alderdiak dauka gehiengo absolutua"
    return "Inork ez dauka gehiengo absoluturik"

x=['EAJ', 'Bildu', 'EAJ','EAJ', 'Bildu', 'PSE', 'PP']
print(gehiengoAbsolutua(x))