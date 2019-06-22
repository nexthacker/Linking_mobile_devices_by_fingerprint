from db.db_utils import get_all_macs, add_link
from equations import jaccard_similarity, adamic, modify_adamic, idf, idf_similarity

mac_list = get_all_macs()

for mac in mac_list:
    for new_mac in mac_list:
        if new_mac == mac:
            pass
        else:
            jaccard = jaccard_similarity(mac, new_mac)
            adamic = adamic(mac, new_mac)
            m_adamic = modify_adamic(mac, new_mac)
            idf = idf(mac, new_mac)
            idf_similarity = idf_similarity(mac, new_mac)

            add_link(mac, new_mac, jaccard, adamic, m_adamic, idf, idf_similarity)

