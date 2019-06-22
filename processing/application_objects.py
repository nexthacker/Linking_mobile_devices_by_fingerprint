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


class LinkOBJ:
    def __init__(self, mac1, mac2, jaccard, adamic, m_adamic, idf, idf_similarity):
        self.mac1 = mac1
        self.mac2 = mac2
        self.jaccard = jaccard
        self.adamic = adamic
        self.m_adamic = m_adamic
        self.idf = idf
        self.idf_similarity = idf_similarity

    def get_mac1(self):
        return self.mac1

    def get_mac2(self):
        return self.mac2

    def get_jaccard_score(self):
        return self.jaccard

    def get_adamic_score(self):
        return self.adamic

    def get_m_adamic_score(self):
        return self.m_adamic

    def get_idf(self):
        return self.idf

    def get_idf_similarity_score(self):
        return self.idf_similarity
