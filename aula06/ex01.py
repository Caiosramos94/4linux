# orientado a objeto - classe
class pai:
    def __init__(self):
        self.nome = "joao"
        self.nac = "bra"
        
     def falarbra(self):
         print("Feijoada")
         
class mae:
    def __init__(self):
        self.nome = "maria"
        self.nac = "ale"
    
    def falarale(self):
        return("chucrute")


class filha (pai,mae):
    def __init_(self):
        self.nome = "Pamêla"
        self.nac = "Brasileira"

def main():
    pam = filha #criei um objeto da classe
    
    print(pam.falarbra)
    print(pam.falarale)
    
    exit()
    
          
                    
        
        
    
