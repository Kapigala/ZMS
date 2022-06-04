class Figura:
    def __init__(self,lengths):
        self.dlugosci=lengths

    def powierzchnia(self):
        print('figura nie jest okreslona: nieznany {}-bok'.format(len(self.dlugosci)))

    def obwod(self):
        print(sum(self.dlugosci))
        return sum(self.dlugosci)

class Prostokat(Figura):
    def powierzchnia(self):
        a=self.dlugosci.copy()
        a=list(set(a))
        if len(a)<3:
            return a[0]*a[1]
        else:
            print('To nie jest prostokąt')

class Kwadrat(Prostokat):
    def powierzchnia(self):
        if len(set(self.dlugosci))==1:
            return self.dlugosci[0]**2
        else:
            print('To nie jest kwadrat')

x=Kwadrat([2,2,2,2])
x.powierzchnia()
x.obwod()

