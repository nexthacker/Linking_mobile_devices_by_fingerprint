from processing import text_formating as tf 
from processing import processamento as pro
from db import db_helper as dbh
from equations import rarity, modify_adamic, idf, idf_similarity, adamic, jaccard_similarity
from processing.link_analisis import define_links

num_colestas = 18
if __name__ == "__main__":
    print('Iniciando tabelas...')
    dbh.init(drop_tables=False)
    print('Pronto!')
    print("processando coletas...")
    # tf.text_processing(num_colestas)
    # pro.process_entry(num_colestas)
    print("Analizando dados...")
    define_links()

