from db.db_utils import add_line, add_mac, add_ssid, get_mac, get_ssid, get_line


def process_entry(num_coleta):
    for num in range(1, num_coleta):
        arquivo = open("coletas/nova_coleta_{}.txt".format(num))
        dados_coleta = arquivo.readlines()
        for entrada in dados_coleta:
            entrada = entrada.split()
            if entrada[1] != "\x00":
                entrada[1] = entrada[1].replace("\x00", "")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {} {}".format(entrada[0], entrada[1]))
                if not entrada[1] == "SSID:":
                    if not get_mac(entrada[0]):
                        add_mac(entrada[0])
                    if not get_ssid(entrada[1]):
                        add_ssid(entrada[1])
                    if not get_line((entrada[0], entrada[1])):
                        print("[LINHA ADICIONADA]")
                        print((entrada[0], entrada[1]))
                        add_line(entrada[0], entrada[1])
                else:
                    if not get_mac(entrada[0]):
                        add_mac(entrada[0])

