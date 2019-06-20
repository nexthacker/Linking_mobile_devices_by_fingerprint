from math import*
from db.db_utils import*

def frequency(fingerprints_z, all_fingerprints):   # recebe todos os SSIDs e todos os SSIDs de um MAC
    return len(fingerprints_z)/len(all_fingerprints)

def inter(list1, list2):  # recebe dois conjuntos de SSIDs para ver quais estão em comum
    inter =[]
    for value in list1:
        if value in list2:
            inter.append(value)
    if len(inter) > 0:
        return inter
    else:
        return 0


def rarity(mac1, mac2):  # recebe a lista da intersection retornada na funcao INTER
    intersect = inter(search_ssid_by_mac(mac1), search_ssid_by_mac(mac2))
    result = 0
    for item in intersect:
        result += (log(frequency(search_all_ssid_macs(item), get_all_ssids()), 10))*-1
    return result


def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)

def adamic(inter_list):
    result = 0
    for item in inter_list:
        result += 1/(log(frequency(get_all_ssids(), search_all_ssid_macs(item))))
    return result

def modify_adamic(inter_list):
    result = 0
    q = 3
    for item in inter_list:
        result += 1/(frequency(get_all_ssids(), search_all_ssid_macs(item))*q)
    return result