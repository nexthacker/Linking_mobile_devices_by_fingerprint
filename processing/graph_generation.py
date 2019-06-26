import matplotlib.pyplot as plt
from db import db_utils as dbu
from pylab import *

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