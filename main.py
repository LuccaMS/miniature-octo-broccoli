#Importing from classes.py
from classes import *

#checking if tis the main file
if __name__ == "__main__":
    com = Communication(qtd_emissor=3,qtd_recebedor=3)
    com.teste()