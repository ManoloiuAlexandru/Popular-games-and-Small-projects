# import sys
# import os
#
# old_path = sys.path[:]
# sys.path.append(os.sep.join([os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', '..']))
# from python.connectors.parsers.firewalls.stonegate.xml_utils import XmlUtils
# from python.connectors.parsers.firewalls.stonegate.models import ServiceObject
# from python.intermediate.intermediate import Intermediate
#
# # ==============================================================================
# sys.path = old_path
#
#
# # ==============================================================================
#
#
# class ParserServiceObjects(XmlUtils):
#     def __init__(self, file_name: str, param_interm: Intermediate, param_dict_iml_hosts: dict):
#         self.interm = param_interm
#         self.dict_iml_hosts = param_dict_iml_hosts
#         self.file_name = file_name
#         self.dict_service_objects = {}
#
#     def get_service_udp(self):
#         list_nodes = self.get_list_of_first_degree_nodes_by_tag(self.file_name, 'service_udp')
#         count = 1
#         for nod in list_nodes:
#             # create object of type ServiceObject
#             # add created object to list_of_service_objects
#             service_object = ServiceObject()
#             dict_result = self.get_all_attributes_of_node(nod)
#             max_port = ""
#             min_port = ""
#             for key in dict_result:
#                 print(key, ":", dict_result[key], " count este", count)
#                 if key == "name":
#                     count += 1
#                     service_object.name = dict_result[key]
#                 elif key == "min_dst_port":
#                     min_port = dict_result[key]
#                 elif key == "max_dst_port":
#                     max_port = dict_result[key]
#             if max_port == "":
#                 max_port = min_port
#             service_object.min_port = min_port
#             service_object.max_port = max_port
#             if service_object.is_valid() is True:
#                 service_object.fw_services = "1-65535/" + min_port + "-" + max_port + "/UDP"
#                 self.dict_service_objects[service_object.name] = service_object
#
#     def get_service_tcp(self):
#         list_nodes = self.get_list_of_first_degree_nodes_by_tag(self.file_name, 'service_tcp')
#         for nod in list_nodes:
#             # create object of type ServiceObject
#             # add created object to list_of_service_objects
#             service_object = ServiceObject()
#             dict_result = self.get_all_attributes_of_node(nod)
#             max_port = ""
#             min_port = ""
#             for key in dict_result:
#                 print(key, ":", dict_result[key])
#                 if key == "name":
#                     service_object.name = dict_result[key]
#                 elif key == "min_dst_port":
#                     min_port = dict_result[key]
#                 elif key == "max_dst_port":
#                     max_port = dict_result[key]
#             if max_port == "":
#                 max_port = min_port
#             service_object.min_port = min_port
#             service_object.max_port = max_port
#             if service_object.is_valid() is True:
#                 service_object.fw_services = "1-65535/" + min_port + "-" + max_port + "/TCP"
#                 self.dict_service_objects[service_object.name] = service_object
#
#     def get_service_ip(self):
#         list_nodes = self.get_list_of_first_degree_nodes_by_tag(self.file_name, 'service_ip')
#         for nod in list_nodes:
#             service_object = ServiceObject()
#             dict_result = self.get_all_attributes_of_node(nod)
#             for key in dict_result:
#                 print(key, ":", dict_result[key])
#                 if key == "name":
#                     service_object.name = dict_result[key]
#                 if key == "protocol_number" and dict_result[key] != "":
#                     service_object.fw_services = dict_result[key] + "-" + dict_result[key] + "/" + dict_result[
#                         key] + "-" + dict_result[key] + "/IP"
#             self.dict_service_objects[service_object.name] = service_object
#
#     def get_service_icmp(self):
#         list_nodes = self.get_list_of_first_degree_nodes_by_tag(self.file_name, 'service_icmp')
#         for nod in list_nodes:
#             service_object = ServiceObject()
#             dict_result = self.get_all_attributes_of_node(nod)
#             service_type = ""
#             service_code = ""
#             count = 0
#             for key in dict_result:
#                 print(key, ":", dict_result[key], " count este", count)
#                 count += 1
#                 if key == "name":
#                     service_object.name = dict_result[key]
#                 if key == "icmp_type":
#                     service_type = dict_result[key]
#                 if key == "icmp_code":
#                     service_code = dict_result[key]
#             if service_code == "":
#                 service_code = service_type
#             service_object.fw_services = service_type + "/" + service_code + "/ICMP"
#             self.dict_service_objects[service_object.name] = service_object
#
#     def get_host_firewall(self):
#         list_nodes = self.get_list_of_first_degree_nodes_by_tag(self.file_name, 'host')
#         for nod in list_nodes:
#             dict_result = self.get_all_attributes_of_node(nod)
#             for key in dict_result:
#                 print(key, ":", dict_result[key])
#
#     def add_list_service_objects_to_one_host(self, iml_one_host):
#         for (service_name, service_object) in self.dict_service_objects:
#             self.interm.new_service_object(host=iml_one_host, name=service_object.name,
#                                            fw_services=service_object.fw_services)
#
#     def create_well_known_services(self):
#         self.dict_service_objects["HTTP"] = "1-65535/80-80/TCP"
#         self.dict_service_objects["HTTP (with URL Logging)"] = "1-65535/80-80/TCP"
#         self.dict_service_objects["HTTPS"] = "1-65535/443-443/TCP"
#         self.dict_service_objects["DNS (UDP)"] = "1-65535/53-53/UDP"
#         self.dict_service_objects["DNS (TCP)"] = "1-65535/53-53/TCP"
#         self.dict_service_objects["FTP"] = "1-65535/21-21/TCP"
#         self.dict_service_objects["SSH"] = "1-65535/22-22/TCP"
#         self.dict_service_objects["HTTP proxy"] = "1-65535/8080-8080/TCP"
#         self.dict_service_objects["SNMP (UDP)"] = "1-65535/161-161/UDP"
#         self.dict_service_objects["SNMP (TCP)"] = "1-65535/161-161/TCP"
#         self.dict_service_objects["SNMP"] = "1-65535/161-161/TCP"
#         self.dict_service_objects["LDAP (TCP)"] = "1-65535/389-389/TCP"
#         self.dict_service_objects["LDAP (UDP)"] = "1-65535/389-389/UDP"
#         self.dict_service_objects["RADIUS (Authentication)"] = "1-65535/1812-1812/TCP"
#         self.dict_service_objects["Remote Desktop"] = "1-65535/3389-3389/TCP"
#         self.dict_service_objects["Echo Request (Any Code)"] = "8-8/8-8/icmp"
#         self.dict_service_objects["Echo Reply (Any Code)"] = "0-0/0-0/icmp"
#         self.dict_service_objects["SMTP"] = "1-65535/25-25/TCP"
#         self.dict_service_objects["NTP (TCP)"] = "1-65535/123-123/UDP"
#         self.dict_service_objects["FTP (Data)"] = "1-65535/20-20/TCP"
#         self.dict_service_objects["HTTPS (with decryption)"] = "1-65535/443-443/TCP"
#         self.dict_service_objects["SIP (TCP)"] = "1-65535/5060-5061/TCP"
#         self.dict_service_objects["SIP Control (TCP)"] = "1-65535/0-0/TCP"
#         self.dict_service_objects["Telnet"] = "1-65535/23-23/TCP"
#         self.dict_service_objects["ANY service"] = '0-65535/0-65535/IP'
#         self.dict_service_objects["Any UDP Service"] = '0-65535/0-65535/UDP'
#
#     def run(self, dict_iml_hosts: dict):
#         self.get_service_ip()
#         self.get_service_tcp()
#         self.get_service_udp()
#         self.get_service_icmp()
#         self.create_well_known_services()
#         for (hostname, iml_one_host) in dict_iml_hosts:
#             self.add_list_service_objects_to_one_host(iml_one_host)
#
#
# if __name__ == "__main__":
#     parser = ParserServiceObjects('C:\\Users\\amanoloiu\\Downloads\\exported_data.xml', None, None)
#     # parser.get_service_udp()
#     parser.get_service_icmp()
#     # parser.get_service_udp()
#     # parser.get_service_tcp()
#     # print('num udp services: ' + str(len(parser.dict_service_objects)))
#     # parser.get_service_ip()
#     # parser.get_service_icmp()
#     # parser.create_well_known_services()
#     # parser.run(parser.dict_service_objects)
#     parser.get_host_firewall()
#
import random


class card:
    def __init__(self, number, card_type):
        self.number = number
        self.card_type = card_type

    def __eq__(self, other):
        if not isinstance(other, card):
            return NotImplemented

        return self.number == other.number and self.card_type == other.card_type


class player:
    def __init__(self, name, nr_cards):
        self.name = name
        self.nr_cards = nr_cards
        self.cards = []
        self.points = 0


numbers = [7, 8, 9, 10, 12, 13, 14, 15]
type_cards = ['diamond', 'clover', 'hearts', 'spades']
out_cards = []
deck_size = 32
player1 = player("player 1", 0)
card_picked = card(random.choice(numbers), random.choice(type_cards))
player1.cards.append(card_picked)
while (player1.nr_cards < 3):
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in player1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    if card_is_in_hand == 0:
        player1.cards.append(card_picked)
        player1.nr_cards += 1

player2 = player("player 2", 0)
card_is_in_hand = 1
while card_is_in_hand == 1:
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in player1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
                break

player2.cards.append(card_picked)
card_picked = card(random.choice(numbers), random.choice(type_cards))
player2.cards.append(card_picked)
while (player2.nr_cards < 2):
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in player1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    for card_in_hand in player2.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    if card_is_in_hand == 0:
        player2.cards.append(card_picked)
        player2.nr_cards += 1

deck_size -= 8
for card_in_hand in player1.cards:
    print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
print()
player1.nr_cards = 4
for card_in_hand in player2.cards:
    print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
print()
player2.nr_cards = 4
card_down2 = None
card_down1 = None
in_progress = 0
while deck_size > 0 and player1.nr_cards>0 and player2.nr_cards>0:
    max_nr_of_card = 0
    if (in_progress == 0):
        card_to_play = card(None, None)
        for card_in_hand in player1.cards:
            nr_of_card = player1.cards.count(card_in_hand)
            if nr_of_card == 4 and card_in_hand.number == 7:
                print("Player 1 won because he has only 7's in his hand")
                deck_size = 0
            elif (card_in_hand.number == 7 and nr_of_card > 1) or (card_in_hand.number == 7 and player1.nr_cards == 1):
                max_nr_of_card = nr_of_card
                card_to_play = card_in_hand
            elif max_nr_of_card < nr_of_card and card_in_hand.number != 7 and player1.nr_cards > 1:
                max_nr_of_card = nr_of_card
                card_to_play = card_in_hand
        print("Player 1 should play this card", card_to_play.card_type, card_to_play.number)
        card_down1 = card_to_play
        player1.nr_cards -= 1
        player1.cards.remove(card_down1)
        out_cards.append(card_down1)
    else:
        card_to_play = card_down1
        print("Player 1 should play this card", card_to_play.card_type, card_to_play.number)
    for card_in_hand in player1.cards:
        print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print()
    for card_in_hand in player2.cards:
        print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print("There are ", deck_size, " cards left")
    print()

    max_nr_of_card = 0
    if (in_progress == 0):
        card_to_play = card(None, None)
        for card_in_hand in player2.cards:
            nr_of_card = player2.cards.count(card_in_hand)
            if nr_of_card == 4 and card_in_hand.number == 7:
                print("Player 2 won because he has only 7's in his hand")
                deck_size = 0
            elif (card_in_hand.number == 7 and nr_of_card > 1) or (card_in_hand.number == 7 and player2.nr_cards == 1):
                max_nr_of_card = nr_of_card
                card_to_play = card_in_hand
            elif max_nr_of_card < nr_of_card and card_in_hand.number != 7 and player2.nr_cards > 1:
                max_nr_of_card = nr_of_card
                card_to_play = card_in_hand
        print("Player 2 should play this card", card_to_play.card_type, card_to_play.number)
        card_down2 = card_to_play
        player2.nr_cards -= 1
        player2.cards.remove(card_down2)
        out_cards.append(card_down2)
    else:
        card_to_play = card_down2
        print("Player 2 should play this card", card_to_play.card_type, card_to_play.number)
    for card_in_hand in player1.cards:
        print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print()
    for card_in_hand in player2.cards:
        print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print("There are ", deck_size, " cards left")
    print()

    if card_down1.number != card_down2.number and card_down2.number != 7:
        in_progress = 0
        print("Player 1 gets the cards")
        if card_down1.number == 10 or card_down1.number == 15:
            player1.points += 1
        for card_in_hand in player1.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print()
        for card_in_hand in player2.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print("There are ", deck_size, " cards left")
        print()

        while player1.nr_cards < 4 and deck_size > 0:
            card_picked = card(random.choice(numbers), random.choice(type_cards))
            card_is_in_hand = 0
            for card_in_hand in player1.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in out_cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in player2.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1

            if card_is_in_hand == 0:
                player1.cards.append(card_picked)
                player1.nr_cards += 1
                deck_size -= 1
        while player2.nr_cards < 4 and deck_size > 0:
            card_picked = card(random.choice(numbers), random.choice(type_cards))
            card_is_in_hand = 0
            for card_in_hand in player1.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in player2.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in out_cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            if card_is_in_hand == 0:
                player2.cards.append(card_picked)
                player2.nr_cards += 1
                deck_size -= 1
        for card_in_hand in player1.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print()
        for card_in_hand in player2.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print()

    elif card_down1.number == card_down2.number:
        in_progress = 1
        can_continue = 0
        for card_in_hand in player1.cards:
            if card_down1.number == card_in_hand.number:
                card_down1 = card_in_hand
                player1.nr_cards -= 1
                player1.cards.remove(card_down1)
                out_cards.append(card_down1)
                can_continue = 1
                break
        if can_continue == 0:
            for card_in_hand in player1.cards:
                if card_in_hand.number != 10 or card_in_hand.number != 15 or card_in_hand.number != 7:
                    card_down1 = card_in_hand
                    player1.nr_cards -= 1
                    player1.cards.remove(card_down1)
                    out_cards.append(card_down1)
                    break
        can_continue = 0
        for card_in_hand in player2.cards:
            if card_down2.number == card_in_hand.number:
                card_down2 = card_in_hand
                player2.nr_cards -= 1
                player2.cards.remove(card_down2)
                out_cards.append(card_down2)
                can_continue = 1
                break
        if can_continue == 0:
            for card_in_hand in player2.cards:
                if card_in_hand.number != 10 or card_in_hand.number != 15 or card_in_hand.number != 7:
                    card_down2 = card_in_hand
                    player2.nr_cards -= 1
                    player2.cards.remove(card_down2)
                    out_cards.append(card_down2)
                    break
    else:
        in_progress = 0
        print("Player 2 gets the cards")
        if card_down1.number == 10 or card_down1.number == 15:
            player2.points += 1
        for card_in_hand in player1.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print()
        for card_in_hand in player2.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print("There are ", deck_size, " cards left")
        print()

        while player1.nr_cards < 4 and deck_size > 0:
            deck_size -= 1
            card_picked = card(random.choice(numbers), random.choice(type_cards))
            card_is_in_hand = 0
            for card_in_hand in player1.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in out_cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            if card_is_in_hand == 0:
                player1.cards.append(card_picked)
                player1.nr_cards += 1
        while player2.nr_cards < 4 and deck_size > 0:
            deck_size -= 1
            card_picked = card(random.choice(numbers), random.choice(type_cards))
            card_is_in_hand = 0
            for card_in_hand in player1.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in player2.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in out_cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            if card_is_in_hand == 0:
                player2.cards.append(card_picked)
                player2.nr_cards += 1
        for card_in_hand in player1.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print()
        for card_in_hand in player2.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print("There are ", deck_size, " cards left")
        print()

for card_in_hand in player1.cards:
    print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print()
for card_in_hand in player2.cards:
    print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print("There are ", deck_size, " cards left")
    print()
if player2.points > player1.points:
    print("Player 2 wins")
elif player1.points > player2.points:
    print("Player 1 wins")
else:
    print("Draw")
