from processing import text_formating as tf 
from processing import processamento as pro
from db import db_helper as dbh
from equations import rarity

num_colestas = 6
if __name__ == "__main__":
    print('Iniciando tabelas...')
    dbh.init()
    print('Pronto!')
    print("processando coletas...")
    tf.text_processing(num_colestas)
    pro.process_entry(num_colestas)
    print("Analizando dados...")
    print(rarity("fc:64:3a:03:82:cc", "18:89:5b:09:d8:08"))

    while True:
        pass
        # TODO: menu for aplication on consol
