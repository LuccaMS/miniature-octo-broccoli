import os
import csv

class Communication():
    def __init__(self):
        #Creating the emissor and recebedor lists
        self.emissores = []
        self.recebedores = []
        self.list_of_who_has_the_token = []
        self.messages_list = []
        self.emissor_recieved_list = []
    
    def rotate_token(self):
        if self.list_of_who_has_the_token == [0 for i in range(len(self.emissores))]:
            self.list_of_who_has_the_token[0] = 1
        else:
            current_index = self.list_of_who_has_the_token.index(1)
            next_index = (current_index + 1) % len(self.list_of_who_has_the_token)
            self.list_of_who_has_the_token[current_index] = 0
            self.list_of_who_has_the_token[next_index] = 1

class Emissor():
    def __init__(self,id,token=None,list_recebedores=[],com=None):
        self.id = id
        self.token = token
        self.list_recebedores = list_recebedores
        self.communication = com

    def send_message(self,message,token,reciever_id):

        recebedor = self.list_recebedores[reciever_id]

        if token == None:
            print("token is none")
            pass
        else:
            confirm = recebedor.recieve_message(message,token,self.id)
            if confirm == True:
                #then it recieved the message
                
                string = f'Emissor {self.id} recebeu a resposta do recebedor {reciever_id}'
                self.communication.emissor_recieved_list.append(string)

                return True
            else:
                #Se o recebedor não confirmar o recebimento da mensagem, então, o emissor não pode enviar a mensagem
                #para o próximo recebedor
                return False

class Recebedor():
    def __init__(self,id,com):
        self.id = id
        self.communication = com

    def recieve_message(self,message,token,emissor_id):
        if token is not None:
            string = f'Recebedor {self.id} recebeu msg de Emissor {emissor_id}'
            self.communication.messages_list.append(string)

            return True
        else:
            return False
            #message is discarded as the emissor did not have the right to send the message
