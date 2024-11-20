import random


class Kutya:
    def __init__(self,nev:str,nem:str,faj:str,marmagassag:float,suly:float):
        self.nev=nev
        self.nem=nem
        self.faj=faj
        self.marmagassag=marmagassag
        self.suly=suly
        self.tevekenysegSzam:int=0


    def __str__(self):
        return f"{self.nev} kiskutya {self.nem} és {self.faj}"
    
    def tevekenyseg(self):
        self.tevekenysegSzam=random.randint(1,3)
        if self.tevekenysegSzam == 1:
            print(f"A {self.nev} éppen ugat")
        elif self.tevekenysegSzam == 2:
            print(f"A {self.nev} éppen alszik")
        else:
            print(f"A {self.nev} éppen játszik")
    
    def harap(self):
        if self.tevekenysegSzam==1:
            print(f"A {self.nev} nem harap")
        else:
            print(f"A {self.nev} harap")
    
    