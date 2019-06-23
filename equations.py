from math import*
from db.db_utils import*
import math

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


def union(list1, list2):
    return list1 + list2


def rarity(mac1, mac2):  # recebe a lista da intersection retornada na funcao INTER
    intersect = inter(search_ssid_by_mac(mac1), search_ssid_by_mac(mac2))
    print(intersect)
    result = 0
    if intersect:
        for item in intersect:
            result += (log(frequency(search_all_ssid_macs(item), get_all_ssids()), 10))*-1
    return result


def jaccard_similarity(mac1, mac2):
    intersection_cardinality = len(inter(search_ssid_by_mac(mac1), search_ssid_by_mac(mac2)))
    union_cardinality = len(union(search_ssid_by_mac(mac1), search_ssid_by_mac(mac2)))
    return intersection_cardinality/float(union_cardinality)


def adamic(mac1, mac2):
    intersect = inter(search_ssid_by_mac(mac1), search_ssid_by_mac(mac2))
    result = 0
    if intersect:
        for item in intersect:
            result += 1/(log(frequency(get_all_ssids(), search_all_ssid_macs(item)), 10))
    return result


def modify_adamic(mac1, mac2):      # calcula a similaridade usando a constante q
    intersect = inter(search_ssid_by_mac(mac1), search_ssid_by_mac(mac2))
    result = 0
    q = 3
    if intersect:
        for item in intersect:
            result += 1/(frequency(get_all_ssids(), search_all_ssid_macs(item))*q)
    return result


def idf(ssd, all_macs):         # calcula o IDF do SSID x
    return log(1/(frequency(ssd, all_macs)), 10)


def idf_similarity(mac1, mac2):     # calcula a similaridade baseada do IDF
    intersect = inter(search_ssid_by_mac(mac1), search_ssid_by_mac(mac2))
    union_macs = union(search_ssid_by_mac(mac1), search_ssid_by_mac(mac2))
    top = 0
    bottom1 = 0
    bottom2 = 0
    for x in union_macs:
        if x in intersect:
            top += idf(x, get_all_ssids())**2
        if x in search_ssid_by_mac(mac1):
            bottom1 += math.sqrt(idf(x, get_all_ssids())**2)
        if x in search_ssid_by_mac(mac2):
            bottom2 += math.sqrt(idf(x, get_all_ssids())**2)

    if bottom1 == 0 or bottom2 == 0:
        return 0
    else:
        return top/(bottom1*bottom2)
