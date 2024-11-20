from kutya import Kutya


def kutyak_letrehozasa() -> list[Kutya]:
    kutya_1:Kutya=Kutya("Maja","nosteny","husky",40,3500)
    kutya_2:Kutya=Kutya("Milo","hím","Golden Retriever",65,5420)
    kutya_3:Kutya=Kutya("Max","hím","Labrador",85,9780)
    kutya_lista:list[Kutya]=[]
    kutya_lista.append(kutya_1)
    kutya_lista.append(kutya_2)
    kutya_lista.append(kutya_3)
    return kutya_lista

def kutyak_kiirasa(kutya_lista:list[Kutya]):
    for kutya in kutya_lista:
        print(kutya)
        kutya.tevekenyseg()
        kutya.harap()
