from db.db_utils import get_all_macs, add_link, search_ssid_by_mac
from equations import jaccard_similarity, adamic, modify_adamic, idf, idf_similarity


def define_links():
    mac_list = get_all_macs()
    count = 0
    for mac in mac_list:
        count +=1
        print(count)
        for new_mac in mac_list:
            print("[Warning] current macs for evaluation {} <<<>>>> {}".format(mac, new_mac))
            if new_mac == mac:
                pass
            else:
                if len(search_ssid_by_mac(mac)) == 0:
                    print("[WARNING] Jumping to the next mac adress, current one is invalid")
                    break
                elif len(search_ssid_by_mac(new_mac)) == 0:
                    print("[WARNING] Jumping to the next secondary mac adress, current one is invalid")
                else:
                    jaccard = jaccard_similarity(mac, new_mac)
                    print("[RESULT] JACCARD: {}".format(jaccard))
                    adamic_score = adamic(mac, new_mac)
                    print("[RESULT] ADAMIC: {}".format(adamic_score))
                    m_adamic = modify_adamic(mac, new_mac)
                    print("[RESULT] M_ADAMIC: {}".format(m_adamic))
                    idf_score = idf(mac, new_mac)
                    print("[RESULT] IDF: {}".format(idf_score))
                    idf_similarity_score = idf_similarity(mac, new_mac)
                    print("[RESULT] IDF SIMILARITY: {}".format(idf_similarity_score))

                    add_link(mac, new_mac, jaccard, adamic_score, m_adamic, idf_score, idf_similarity_score)


