from ex02 import ContaCorrente
import unittest

class TestaConta(unittest.TestCase):
    
    def verificaSaldo(self):
        cc = ContaCorrente()
        cc.saldo = 100
        cc.saque(50)
        self.assertEqual(50, cc.saldo)

unittest.main()
