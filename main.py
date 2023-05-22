#Importing from classes.py
from classes import *

#checking if tis the main file
if __name__ == "__main__":
    qtd_emissor = 3
    qtd_recebedor = 3
    com = Communication()

    for i in range(qtd_recebedor):
        com.recebedores.append(Recebedor(i))

    for i in range(qtd_emissor):
        com.emissores.append(Emissor(i,token=None,list_recebedores=com.recebedores))
        com.list_of_who_has_the_token.append(0)


    #Now we will create the main loop for testing for 10 times
    for i in range(qtd_emissor):
        com.rotate_token()
        print("list of who has the token: ",com.list_of_who_has_the_token)
        current_emissor_index = com.list_of_who_has_the_token.index(1)

        print("current emissor index: ",current_emissor_index)

        emissor_now = com.emissores[current_emissor_index]

        #now we have to in fact give the token to the emissor that is right on the list_of_who_has_the_token

        if(emissor_now.id == current_emissor_index):
            emissor_now.token = 1

        for i in range(qtd_recebedor):
            emissor_now.send_message("Hello",emissor_now.token,i)
        
        #and after sending all messages, we have to remove the token from the emissor
        emissor_now.token = None
