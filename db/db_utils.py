from db.db_helper import get_session, MacAdress, SsidTable, Link, Mac_ssid
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

def get_mac(mac_entry):
    session = get_session()
    session = session()
    returning_mac = session.query(MacAdress).filter(MacAdress.mac == mac_entry).all()
    session.close()
    if returning_mac:
        return returning_mac[0].mac
    else:
        return None

def add_ssid(ssid_entry):
    session =  get_session()
    session = session()
    new_ssid = SsidTable()
    new_ssid.ssid = ssid_entry
    session.add(new_ssid)
    session.commit()
    session.refresh(new_ssid)
    ssid_id = new_ssid.id
    session.close()
    return ssid_id

def get_ssid(ssid_entry):
    session = get_session()
    session = session()
    returning_ssid = session.query(SsidTable).filter(SsidTable.ssid == ssid_entry).all()
    session.close()
    if returning_ssid:
        return returning_ssid[0].ssid
    else:
        return None


def get_line(line_entry):
    session = get_session()
    session = session()
    returning_line = session.query(Mac_ssid).filter(Mac_ssid.mac_adress == line_entry[0] and Mac_ssid.ssid == line_entry[1]).all()
    session.close()
    if returning_line:
        return returning_line[0].mac_adress, returning_line[0].ssid
    else:
        return None


def search_mac_by_adress(adress):
    session = get_session()
    session = session()
    mac_query = session.query(MacAdress).filter(MacAdress.mac == adress).all()
    if mac_query:
        mac_query = mac_query[0]
        ssids_list = search_ssid_by_mac(mac_query.mac)
        if ssids_list:
            mac_obj = Mac()
            mac_obj.set_adress(adress)
            for ssid in ssids_list:
                mac_obj.add_ssid(ssid)
            session.close()
            return mac_obj
        else:
            print("[Warning]: There is no SSid for mac adress {}".format(adress))
            session.close()
            return None
    else:
        print("[Warning]: Mac adress {} doesn't exists".format(adress))
        session.close()
        return None


def search_all_ssid_macs(ssid):
    session = get_session()
    session = session()
    list_macs = []
    query = session.query(Mac_ssid).filter(Mac_ssid.ssid == ssid).all()
    if query:
        for element in query:
            list_macs.append(element.ssid)
        session.close()
        return list_macs
    else:
        session.close()
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
    query = session.query(SsidTable).all()
    session.close()
    for returning_ssid in query:
        list_of_ssids.append(returning_ssid.ssid)
    return list_of_ssids


def search_ssid_by_mac(mac):
    list_ssid = []
    session = get_session()
    session = session()
    ssid_query = session.query(Mac_ssid).filter(Mac_ssid.mac_adress == mac).all()
    print(ssid_query)
    if ssid_query:
        for returned_ssids in ssid_query:
            list_ssid.append(returned_ssids.ssid)
    print(list_ssid)
    session.close()
    return list_ssid


def search_mac_by_ssid(ssid):
    list_macs = []
    session = get_session()
    session = session()
    mac_query = session.query(Mac_ssid).filter(Mac_ssid.ssid == ssid).all()
    if mac_query:
        for returned_macs in mac_query:
            list_macs.append(returned_macs.ssid)
    session.close()
    return list_macs


def rank_ssid_by_apearences():
    list_of_ssids = get_all_ssids()
    output = []
    session = get_session()
    session = session()
    for ssid_uniq in list_of_ssids:
        ssid_query = session.query(Mac_ssid).filter(Mac_ssid.ssid == ssid_uniq).all()
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
    session.close()
    return retuning_id