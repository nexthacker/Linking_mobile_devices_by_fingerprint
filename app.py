from processing import text_formating as tf 
from processing import processamento as pro
from db import db_helper as dbh

num_colestas = 4
if __name__ == "__main__":
    print('Iniciando tabelas...')
    dbh.init()
    print('Pronto!')
    print("processando coletas...")
    tf.text_processing(num_colestas)
    pro.process_entry(num_colestas)
    print("Analizando dados...")
    


    while True:
        pass
        # TODO: menu for aplication on consol
