from pannello.py import PannelloFotovoltaico

class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.localita = localita
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli = list[PannelloFotovoltaico]
        
    def aggiungi_pannello(self, pannello: PannelloFotovoltaico) -> None:
        for mypannello in self.pannelli:
            if mypannello.codice == pannello.codice:
                raise ValueError("Pannello già presente")
        
        if pannello.potenza_kw > self.potenza_massima_kw:
            raise ValueError("Potenza troppo alta")
        
        self.pannelli.append(pannello)
        
    def potenza_pannelli(self) -> float:
        float result = 0
        for pannello in self.pannelli:
            result += pannello.potenza_kw
        
        return result
    
    
    def cerca_pannello(self, codice: str) -> PannelloFotovoltaico:
        for pannello in self.pannelli:
            if pannello.codice == codice:
                return pannello
            
        return None
    
    def rimuovi_pannello(self, codice: str) -> PannelloFotovoltaico:
        result = None
        for pannello in self.pannelli:
            if pannello.codice == codice:
                result = pannello
                self.pannelli.remove(pannello)
                return result
            
        return result
    
    def pannelli_sotto_potenza(self, potenza_massima: float) -> list[PannelloFotovoltaico]:
        result = [pannello in self.pannelli if pannello.potenza_kw <= potenza_massima]
        return result
    
    
        
        
        
        
        
        
        
        
        
        
        