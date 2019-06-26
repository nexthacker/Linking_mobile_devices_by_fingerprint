import matplotlib.pyplot as plt
from db import db_utils as dbu
from pylab import *

from db.db_utils import get_links


def graph_rank_ssid():
    list_rank =  dbu.rank_ssid_by_apearences()
    list_result = []
    listX = []
    listY= []
    pos = arange(5) + .30

    cont = 0
    for i in list_rank[::-1]:
        list_result.append(i)
        cont+=1
        if cont==5:
           break
    print(list_result)

    for i in list_result:
        listX.append(i[0])
        listY.append(i[1])

    print(listX)
    print(listY)

    barh(pos, listY[::-1], align='center', color="#b8ff5c")
    yticks(pos, listX[::-1])
    xlabel('Frequência')
    ylabel('SSIDs')
    title('Frequência dos SSIDs')
    show()


def alg_comparison():
    links = get_links()
    # jaccard = []
    adamic = []
    # mod_adamic = []
    # idf = []
    # idf_similarity = []

    for element in links:
        # jaccard.append(element[0])
        adamic.append(element[1])
        # mod_adamic.append(element[2])
        # idf.append(element[3])
        # idf_similarity.append(element[4])

    s_list = list(range(len(adamic)))


    # jaccard.sort()
    adamic.sort()
    # mod_adamic.sort()
    # idf.sort()
    # idf_similarity.sort()

    fig, ax = plt.subplots()
    # ax.plot(s_list, jaccard, label="jaccard")
    ax.plot(s_list, adamic, label="adamic")
    # ax.plot(s_list, mod_adamic, label="mod_adamic")
    # ax.plot(s_list, idf, label="idf")
    # ax.plot(s_list, idf_similarity, label="idf_similarity")
    title('Comparação de Links')
    xlabel('Link')
    ylabel('Grau do Link')
    ax.legend()
    plt.show()
