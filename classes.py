class Communication():
    def __init__(self, qtd_emissor=3, qtd_recebedor=3):
        #Creating the emissor and recebedor lists
        self.emissor = []
        self.recebedor = []

        #Creating the emissor and recebedor objects

        for i in range(qtd_recebedor):
            self.recebedor.append(Recebedor(i))

        for i in range(qtd_emissor):
            self.emissor.append(Emissor(i,token=None,list_recebedores=self.recebedor))

    def teste(self):
        self.emissor[0].token = True
        self.emissor[0].send_message("Hello World",self.emissor[0].token,2)

        self.emissor[1].send_message("Hello World",self.emissor[1].token,2)

class Emissor(Communication):
    def __init__(self,id,token=None,list_recebedores=[]):
        self.id = id
        self.token = token
        self.list_recebedores = list_recebedores

    def send_message(self,message,token,reciever_id):
        #precisamos que a aplicação nos passe o reciever_id para que possamos enviar a mensagem para o recebedor correto
        #a classe mãe tem uma lista chamada recebedor que contém todos os recebedores, então, podemos acessar o recebedor
        #correto através do id passado pela aplicação

        recebedor = self.list_recebedores[reciever_id]

        #Agora precisamos verificar se o emissor tem direito de enviar a mensagem para o recebedor
        #Para isso, precisamos verificar se o token é nulo ou não
        if token == None:
            pass
        else:
            #Se o token não for nulo, então, o emissor tem direito de enviar a mensagem para o recebedor
            #Então, vamos enviar a mensagem para o recebedor e esperar a confirmação
            confirm = recebedor.recieve_message(message,token,self.id)
            if confirm == True:
                #Se o recebedor confirmar o recebimento da mensagem, então, o emissor pode enviar a mensagem
                #para o próximo recebedor
                return True
            else:
                #Se o recebedor não confirmar o recebimento da mensagem, então, o emissor não pode enviar a mensagem
                #para o próximo recebedor
                return False

class Recebedor(Communication):
    def __init__(self,id):
        self.id = id
        pass

    def recieve_message(self,message,token,emissor_id):
        #Neste caso vamos apenas verificar se o token não é nulo, então, receberemos a mensagem e confirmamos para o emissor
        if token != None:
            print(f"Recebedor {self.id} recebeu a mensagem {message} do emissor {emissor_id}")
            return True
        else:
            print(f"Recebedor {self.id} não recebeu a mensagem {message} do emissor {emissor_id} pois o mesmo não tem o token")
            return False
