from db.db_utils import get_all_macs, add_link, search_ssid_by_mac
from equations import jaccard_similarity, adamic, modify_adamic, idf, idf_similarity


def define_links():
    mac_list = get_all_macs()
    for mac in mac_list:
        for new_mac in mac_list:
            if new_mac == mac:
                pass
            else:
                if not search_ssid_by_mac(mac) or not search_ssid_by_mac(new_mac):
                    pass
                else:
                    jaccard = jaccard_similarity(mac, new_mac)
                    print("[RESULT] JACCARD: {}".format(jaccard))
                    adamic = adamic(mac, new_mac)
                    print("[RESULT] ADAMIC: {}".format(adamic))
                    m_adamic = modify_adamic(mac, new_mac)
                    print("[RESULT] M_ADAMIC: {}".format(m_adamic))
                    idf = idf(mac, new_mac)
                    print("[RESULT] IDF: {}".format(idf))
                    idf_similarity = idf_similarity(mac, new_mac)
                    print("[RESULT] IDF SIMILARITY: {}".format(idf_similarity))

                    add_link(mac, new_mac, jaccard, adamic, m_adamic, idf, idf_similarity)


