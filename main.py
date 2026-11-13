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


if __name__ == "__main__":
    impianti = list[ImpiantoSolare]
    registra_impianto(impianti, ImpiantoSolare("a", "bello", "Cesena", 10.0, "in installazione"))
    registra_impianto(impianti, ImpiantoSolare("b", "brutto", "Cesena", 20.0, "attivo"))
    registra_impianto(impianti, ImpiantoSolare("c", "cosicosi", "Cesenatico", 15.0, "in collaudo"))
    registra_impianto(impianti, ImpiantoSolare("d", "costoso", "Cervia", 100.0, "attivo"))
    impianti[1].aggiungi_pannello(Pa)