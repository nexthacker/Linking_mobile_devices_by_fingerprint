from math import*
from db.db_utils import*

def frequency(all_fingerprints, fingerprints_z):   # recebe todos os SSIDs e todos os SSIDs de um MAC
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


def rarity(inter_list):  # recebe a lista da intersection retornada na funcao INTER
    result = 0
    for item in inter_list:
        result += (log(frequency(get_all_ssids(), get_all_ssids(item)), 10))*-1
    return result


def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)


