from processing import text_formating as tf 
from processing import processamento as pro
from db import db_helper as dbh
from equations import rarity, modify_adamic, idf, idf_similarity, adamic, jaccard_similarity

num_colestas = 18
if __name__ == "__main__":
    print('Iniciando tabelas...')
    dbh.init(drop_tables=False)
    print('Pronto!')
    print("processando coletas...")
    tf.text_processing(num_colestas)
    pro.process_entry(num_colestas)
    print("Analizando dados...")
    print("[RESULT] rarity: {}".format(rarity("fc:64:3a:03:82:cc", "18:89:5b:09:d8:08")))
    print("[RESULT] adamic: {}".format(adamic("fc:64:3a:03:82:cc", "18:89:5b:09:d8:08")))
    print("[RESULT] modified adamic: {}".format(modify_adamic("fc:64:3a:03:82:cc", "18:89:5b:09:d8:08")))
    print("[RESULT] idf: {}".format(idf("fc:64:3a:03:82:cc", "18:89:5b:09:d8:08")))
    print("[RESULT] jaccard: {}".format(jaccard_similarity("fc:64:3a:03:82:cc", "18:89:5b:09:d8:08")))
    print("[RESULT] idf_similarity: {}".format(idf_similarity("fc:64:3a:03:82:cc", "18:89:5b:09:d8:08")))
