class ContaCorrente:
    def __init__(self):
        self.ag = 0
        self.conta = 0
        self.saldo = 0
        self.titular = ""
    
    def saldo(self, valor):
        self.saldo = valor
        print("seu saldo é de, {}".format(self.saldo))
        
    def saque(self, valor):
            self.saldo -= valor
    
    def deposito(self, valor):
        self.saldo += valor
    
    def transferir(self, valor, contaDestino):
        if self.saldo < valor: 
            print("saldo insuficiente")
        else:
            self.saldo = self.saldo - valor
            contaDestino.saldo += valor  

def verificaSaque():
        cc = ContaCorrente()
        cc.saldo = 100
        cc.saque(50)
        return cc.saldo
        
print (verificaSaldo())


        
        
