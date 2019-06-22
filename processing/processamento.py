from db.db_utils import add_line, add_mac, add_ssid, get_mac, get_ssid, get_line


def process_entry(num_coleta):
    arquivo = open("coletas/nova_coleta_{}.txt".format(num_coleta))
    dados_coleta = arquivo.readlines()
    for entrada in dados_coleta:
        entrada = entrada.split()
        if entrada[1] != "\x00":
            entrada[1] = entrada[1].replace("\x00", "")
            # print(entrada)
            if not get_mac(entrada[0]):
                add_mac(entrada[0])
            if not get_ssid(entrada[1]):
                add_ssid(entrada[1])
            if not get_line((entrada[0], entrada[1])):
                add_line(entrada[0], entrada[1])

