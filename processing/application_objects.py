class Mac:
    def __init__(self):
        self.ssid = []
        self.mac_adress = None

    def add_ssid(self, new_ssid):
        self.ssid.append(new_ssid)

    def set_adress(self, new_adress):
        self.mac_adress = new_adress

    def get_ssids(self):
        return self.ssid

    def get_adress(self):
        return self.mac_adress

class Ssid:
    def __init__(self):
        self.nome = None

    def set_ssid(self, new_ssid):
        self.nome = new_ssid

    def get_nome(self):
        return self.nome
