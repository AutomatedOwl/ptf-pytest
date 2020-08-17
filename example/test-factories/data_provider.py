from ctr_table import CtrTable
from lpm_table import LpmTable
from sp_table import SpTable
from collections import namedtuple
from ptf.testutils import *
import consts
import allure

class DataProvider:
    
    # Create data bundles for tests
    PacketBundle = namedtuple("PacketBundle", ["ports", "packet"])
    LpmEntry = namedtuple("LpmEntry", ["sai_def", "ports", "vlan"])
    ScratchEntry = namedtuple("ScratchEntry", ["sai_def", "ports", "vlan"])
    CounterEntry = namedtuple("CounterEntry", ["sai_def", "ports", "vlan"])

    # Create test data bundle as namedtuple
    TestDataBundle = namedtuple("TestDataBundle", ["lpm_entries", "sp_entries", "ctr_entries", "packets"])
    TestDataBundle.__new__.__defaults__ = (None,) * len(TestDataBundle._fields)

    def __init__(self, device, topology, layer):
        self.device = device
        self.topology = topology
        self.test_config_map = self.config_data_for_tests() 

    def config_data_for_tests(self):
        # Map each test to configuration
        return {
        "test_send_one_pkt": self.get_common_data(),
        "test_send_two_pkts": self.get_common_data(),
        "test_send_receive_pkt": self.TestDataBundle(packets = [
            self.PacketBundle(consts.PORT_0, self.generate_packet(consts.IP_ID_0)),
            self.PacketBundle(consts.PORT_2, self.generate_packet(consts.IP_ID_2))],
                    lpm_entries = [self.LpmEntry(consts.SAI_DEF, consts.PORT_0, consts.VLAN_0),
                                         self.LpmEntry(consts.SAI_DEF, consts.PORT_1, consts.VLAN_1)])
        }

    def get_common_data(self):
        return self.TestDataBundle(packets = [
                    self.PacketBundle(consts.PORT_0, self.generate_packet(consts.IP_ID_0)),
                    self.PacketBundle(consts.PORT_1, self.generate_packet(consts.IP_ID_1))],
                    lpm_entries = [self.LpmEntry(consts.SAI_DEF, consts.PORT_0, consts.VLAN_0),
                                         self.LpmEntry(consts.SAI_DEF, consts.PORT_1, consts.VLAN_1)])

    @allure.step
    def get_data_per_test(self, test_method):
        print("Test method: " + test_method)
        #print("TEST CONFIG: " + str(self.test_config_map))
        return self.test_config_map[test_method]

    def generate_packet(self, id):
        return simple_tcp_packet(eth_dst='00:11:11:11:11:11',
                            eth_src='00:22:22:22:22:22',
                            ip_dst='10.0.0.1',
                            ip_id=id,
                            ip_ttl=64)
        