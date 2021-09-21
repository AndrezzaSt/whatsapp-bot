import unittest
import find_Agency
import find_customer

class TestBot(unittest.TestCase):
    def test_find_agency(self):
        ## qualquer nome de rua -> se possui uma agencia perto desta rua
        self.assertEqual(find_Agency.get_place('rua fernando osorio'), 'Agência mais próxima localizada em: Av.Protasio Alves N 795')
        self.assertEqual(find_Agency.get_place('rua apamecor'), 'Agência mais próxima localizada em: Av.Protasio Alves N 795')
        self.assertEqual(find_Agency.get_place('avenida assis brasil'), 'Agência mais próxima localizada em: Av.Assis Brasil N 3940')
        self.assertEqual(find_Agency.get_place('Berlim'), 'Desculpe, não há agencias perto deste endereço')
        self.assertEqual(find_Agency.get_place(1), 'Input Invalido!')

    def test_find_customer(self): 
        self.assertEqual(find_customer.get_customer('11106'), 'ANDREZZA  Número do cartão: 11106 Tipo: C')
        self.assertEqual(find_customer.get_customer('10000'), 'Cartao não encontrado!')
        self.assertEqual(find_customer.get_customer('numero'), 'Cartao não encontrado!')

if __name__ == '__name__':
    unittest.main()