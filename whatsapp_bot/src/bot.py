from io import IncrementalNewlineDecoder
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import find_customer 
import find_Agency 
app = Flask(__name__)

@app.route('/mybot', methods=['POST'])
def mybot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    block_check = False
    def menu():
        msg.body("Olá, bem-vindo(a) ao atendimento automático Sicredi! Para iniciar os nossos serviços, por favor escolha uma das opções a seguir:")
        msg.body("1 - Localizar Agência mais próxima 2- Consulta de cartão 3- Pix 4-Perguntas frequentes")
    
    def menu_freq_quest():
        msg.body("Escolha uma das perguntas: ")
        msg.body("a - Quais as diferenças entre cooperativa e banco? b-O que é capital social? c- O que é distribuição de resultados? d- Como posso solicitar minha abertura de conta?")
    
    if 'hi' in incoming_msg: # qualquer msg
        menu()
        responded = True
    if '1' or '2' or '3' or '4' in incoming_msg:
        block_check = True
        if incoming_msg == '1':
                msg.body('Digite a sua rua: (Ex: Rua + seu local)')
                responded = True
        if 'rua' in incoming_msg and block_check:
            address = incoming_msg
            msg.body(find_Agency.get_place(address))
            responded = True
        if incoming_msg == '2':
                msg.body('Digite o seu numero do cartão: ')
                responded = True
        if '1110' in incoming_msg:
            card_number = incoming_msg
            msg.body('Boa tarde ' + find_customer.get_customer(card_number))
            responded = True
        if incoming_msg == '3':
                msg.body('Como usar o Pix no Sicredi: '+
                            ' Acesse o aplicativo Sicredi no seu celular e clique em Menu > Pix para aproveitar todas as vantagens de transferir, pagar e receber pelo Pix.' +
                            ' Se você ainda não fez o cadastro para usar o Pix no Sicredi, faça agora em Menu > Pix > Cadastro e defina as suas chaves.' +
                            ' Já tem o cadastro? Então é só começar a usar!' 
                        )
                responded = True
        if incoming_msg == '4':
            block_check = True
            menu_freq_quest()
            responded = True

        if incoming_msg == 'a' and block_check:
                msg.body('São muitas as vantagens de ser um associado. Enquanto que em um banco tradicional você é só mais um cliente, aqui você é dono do negócio, tendo direito ao voto nas tomadas de decisões da nossa cooperativa, e participação nos resultados ao final de cada ano, além de um atendimento muito mais próximo e personalizado. Em um banco tradicional, o objetivo maior é o lucro, já o cooperativismo tem como princípios a intercooperação e o interesse pela comunidade. Além disso, possuímos taxas e tarifas menores do que em bancos tradicionais.')
                responded = True
        if incoming_msg == 'b' and block_check:
                msg.body('Capital social é a participação que cada associado possui no patrimônio da cooperativa. No momento da abertura de conta, o associado faz um aporte de valor que será sua cota capital, ou seja, sua parte na cooperativa, tornando-se dono do negócio e ajudando a constituir o capital da Sicredi Mil.')
                responded = True
        if incoming_msg == 'c' and block_check:
                msg.body('Ao abrir uma conta na Sicredi Mil, o associado se torna dono do negócio, tendo direito a sua parte no resultado anual da cooperativa. A distribuição varia de acordo com os produtos e serviços utilizados pelo associado no ano anterior.')
                responded = True
        if incoming_msg == 'd' and block_check:
                msg.body('Para solicitar sua abertura de conta, você precisa do seu comprovante de residência, comprovante de renda e documento de identidade. Compareça em uma de nossas agências ou escritórios, ou acesse https://www.surveymonkey.com/r/5PKJ9TT.')
                responded = True
        if incoming_msg == 'voltar':
            menu()
            responded = True
        if not responded:
            msg.body("Por favor escolha uma opção válida!")
    return str(resp)


if __name__ == "__main__":
    app.run()
