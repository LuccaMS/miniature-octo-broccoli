class Communication():
    def __init__(self):
        #Creating the emissor and recebedor lists
        self.emissores = []
        self.recebedores = []
        self.list_of_who_has_the_token = []
    
    def rotate_token(self):
        #once we call this function, we have to circle the token around the emissors to give each one the chance to send a message
        
        #we are going to use a list of the size of the emissor list and the only one that has 1 is the one that has the token
        #respecting the index of the emissor list
        #first we have to verify if all the list is 0, if it is, then, we have to give the token to the first emissor
        if self.list_of_who_has_the_token == [0 for i in range(len(self.emissores))]:
            self.list_of_who_has_the_token[0] = 1
        else:
            current_index = self.list_of_who_has_the_token.index(1)
            next_index = (current_index + 1) % len(self.list_of_who_has_the_token)
            self.list_of_who_has_the_token[current_index] = 0
            self.list_of_who_has_the_token[next_index] = 1

class Emissor():
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
            print("token is none")
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

class Recebedor():
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
