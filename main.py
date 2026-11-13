from pannello.py import PannelloFotovoltaico
from impianto.py import ImpiantoSolare

def registra_impianto(impianti: list[ImpiantoSolare], impianto: ImpiantoSolare) -> None:
    for myimpianto in impianti:
        if myimpianto.codice == impianto.codice:
            raise ValueError("Codice già presente")
        
    impianti.append(impianto)
    
def cerca_impianto(impianti: list[ImpiantoSolare], codice: str) -> ImpiantoSolare:
    for impianto in impianti:
        if impianto.codice == codice:
            return impianto
        
    return None

def riepilogo_impianti(nome_azienda: str, impianti: list[ImpiantoSolare]) -> None:
    for impianto in impianti:
        print(f"Codice: {impianto.codice}, Modello: {impianto.modello}, Potenza: {impianto.potenza_massima_kw}, Stato: {impianto.stato}")


