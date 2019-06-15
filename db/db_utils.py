from db.db_helper import get_session, MacAdress, SsidObj, Link, Mac_ssid
from processing.application_objects import *


def add_mac(mac_entry):
    session = get_session()
    session = session()
    new_mac = MacAdress()
    new_mac.mac = mac_entry
    session.add(new_mac)
    session.commit()
    session.refresh(new_mac)
    mac_id = new_mac.id
    session.close()
    return mac_id


def add_ssid(ssid_entry):
    session =  get_session()
    session = session()
    new_ssid = SsidObj()
    new_ssid.ssid = ssid_entry
    session.add(new_ssid)
    session.commit()
    session.refresh(new_ssid)
    ssid_id =  new_ssid.id
    session.close()
    return ssid_id


def search_mac_by_adress(adress):
    session = get_session()
    session = session()
    mac_query = session.query(MacAdress).filter(MacAdress.mac == adress)
    if mac_query:
        mac_query = mac_query[0]
        ssids_list = search_ssid_by_mac(mac_query.mac)
        if ssids_list:
            mac_obj = Mac()
            mac_obj.set_adress(adress)
            for ssid in ssids_list:
                mac_obj.add_ssid(ssid)
            return mac_obj
        else:
            print("[Warning]: There is no SSid for mac adress {}".format(adress))
            return None
    else:
        print("[Warning]: Mac adress {} doesn't exists".format(adress))
        return None


def search_all_ssid_macs(ssid):
    session = get_session()
    session = session()
    list_macs = []
    query = session.query(Mac_ssid).filter(Mac_ssid.ssid == ssid)
    if query:
        for element in query:
            list_macs.append(element.ssid)
        return list_macs
    else:
        return None



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


def search_mac_by_ssid(ssid):
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