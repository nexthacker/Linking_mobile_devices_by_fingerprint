from db.db_utils import add_line, add_mac, add_ssid

def process_entry(num_coleta):
    lista_entradas = []
    arquivo = open("coletas/nova_coleta_{}.txt".format(num_coleta))
    dados_coleta = arquivo.readlines()
    for entrada in dados_coleta:
        entrada = entrada.split()
        if entrada[1] != "\x00":
            entrada[1] = entrada[1].replace("\x00", "")
            # print(entrada)
            if entrada not in lista_entradas:
                lista_entradas.append(entrada)
                # add_mac(entrada[0])
                # add_ssid(entrada[1])
                add_line(entrada[0], entrada[1])
        #TODO: solve this
