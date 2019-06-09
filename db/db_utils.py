from db.db_helper import get_session, Mac, Ssid, Link, Mac_ssid
from processing.application_objects import *


def add_mac(mac):
    session = get_session()
    session = session()
    new_mac = Mac()
    new_mac.mac = mac
    session.add(mac)
    session.commit()
    session.refresh(new_mac)
    mac_id = new_mac.id
    session.close()
    return mac_id

def add_ssid(ssid):
    session =  get_session()
    session = session()
    new_ssid = Ssid()
    new_ssid.ssid = ssid
    session.add(new_ssid)
    session.commit()
    session.refresh(new_ssid)
    ssid_id =  new_ssid.id
    session.close()
    return ssid_id

def get_all_macs():
    session = get_session()
    session = session()
    list_of_macs = [] 
    query = session.query(Mac).all()
    session.close()
    for mac in query:
        list_of_macs.append(mac.mac)
    return list_of_macs

def get_all_ssids():
    session = get_session()
    session = session()
    list_of_ssids = []
    query = session.query(Ssid).all()
    session.close()
    for returning_ssid in query:
        list_of_ssids.append(returning_ssid.ssid)
    return list_of_ssids

def search_ssid_by_mac(mac):
    list_ssid = []
    session = get_session()
    session = session()
    ssid_query = session.query(Mac_ssid).filter(Mac_ssid.mac_adress == mac)
    if ssid_query:
        for returned_ssids in ssid_query:
            list_ssid.append(returned_ssids.ssid)
    return list_ssid

def search_mac_by_ssid(siid):
    list_macs = []
    session = get_session()
    session = session()
    mac_query = session.query(Mac_ssid).filter(Mac_ssid.ssid == ssid)
    if mac_query:
        for returned_macs in mac_query:
            list_macs.append(returned_macs.ssid)
    return list_macs

        

def rank_ssid_by_apearences():
    list_of_ssids = get_all_ssids()
    output = []
    session = get_session()
    session = session()
    for ssid_uniq in list_of_ssids:
        ssid_query = session.query(Mac_ssid).filter(Mac_ssid.ssid == ssid_uniq)
        number_appearences = len(ssid_query)
        output.append((ssid_uniq, number_appearences))
    output.sort(key=lambda tup: tup[1])
    session.close()
    return output


def add_line(mac, new_ssid):
    session = get_session()
    session = session()
    line = Mac_ssid()
    line.mac_adress = mac
    line.ssid = new_ssid
    session.add(line)
    session.commit()
    session.refresh(line)
    retuning_id = line.id
    return retuning_id