import time
import logging
from ptf_example_tests import PtfExampleTests

class UnittestTestRunner(PtfExampleTests):
    
    def runTest(self):
        print
        print "Sending L2 packet port 1 -> port 2 [access vlan=10])"
    
        # # switch_init(self.client)
        # # vlan_id = 10
        # # port1 = port_list[1]
        # # port2 = port_list[2]
        # # mac1 = '00:11:11:11:11:11'
        # # mac2 = '00:22:22:22:22:22'
        # # mac_action = 1

        # self.client.sai_thrift_create_vlan(vlan_id)
        # vlan_port1 = sai_thrift_vlan_port_t(port_id=port1, tagging_mode=0)
        # vlan_port2 = sai_thrift_vlan_port_t(port_id=port2, tagging_mode=0)
        # self.client.sai_thrift_add_ports_to_vlan(vlan_id, [vlan_port1, vlan_port2])

        # sai_thrift_create_fdb(self.client, vlan_id, mac1, port1, mac_action)
        # sai_thrift_create_fdb(self.client, vlan_id, mac2, port2, mac_action)

        # pkt = simple_tcp_packet(eth_dst='00:11:11:11:11:11',
        #                         eth_src='00:22:22:22:22:22',
        #                         ip_dst='10.0.0.1',
        #                         ip_id=101,
        #                         ip_ttl=64)

        # try:
        #     # in tuple: 0 is device number, 2 is port number
        #     # this tuple uniquely identifies a port
        #     send_packet(self, (0, 2), pkt)
        #     verify_packets(self, pkt, device_number=0, ports=[1])
        #     # or simply
        #     # send_packet(self, 2, pkt)
        #     # verify_packets(self, pkt, ports=[1])
        # finally:
        #     sai_thrift_delete_fdb(self.client, vlan_id, mac1, port1)
        #     sai_thrift_delete_fdb(self.client, vlan_id, mac2, port2)

        #     self.client.sai_thrift_remove_ports_from_vlan(vlan_id, [vlan_port1, vlan_port2])
        #     self.client.sai_thrift_delete_vlan(vlan_id)
