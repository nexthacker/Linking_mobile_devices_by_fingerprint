from processing import text_formating as tf 
from processing import processamento as pro
from db import db_helper as dbh
from equations import rarity, modify_adamic, idf, idf_similarity, adamic, jaccard_similarity

num_colestas = 1
if __name__ == "__main__":
    print('Iniciando tabelas...')
    dbh.init(drop_tables=False)
    print('Pronto!')
    print("processando coletas...")
    # tf.text_processing(num_colestas)
    # pro.process_entry(num_colestas)
    print("Analizando dados...")
    print("[RESULT] rarity: {}".format(rarity("dc:35:f1:4f:72:c0", "00:25:86:bc:da:76")))
    print("[RESULT] adamic: {}".format(adamic("dc:35:f1:4f:72:c0", "00:25:86:bc:da:76")))
    print("[RESULT] modified adamic: {}".format(modify_adamic("dc:35:f1:4f:72:c0", "00:25:86:bc:da:76")))
    print("[RESULT] idf: {}".format(idf("dc:35:f1:4f:72:c0", "00:25:86:bc:da:76")))
    print("[RESULT] jaccard: {}".format(jaccard_similarity("dc:35:f1:4f:72:c0", "00:25:86:bc:da:76")))
    print("[RESULT] idf_similarity: {}".format(idf_similarity("dc:35:f1:4f:72:c0", "00:25:86:bc:da:76")))
