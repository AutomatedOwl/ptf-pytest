from ptf.testutils import *
import pytest
import allure

class DataPlaneFactory:
    
    def __init__(self, device, topology, layer):
        self.device = device
        self.topology = topology
        self.layer = layer

    def generate_packet(self):
        return simple_tcp_packet(eth_dst='00:11:11:11:11:11',
                                eth_src='00:22:22:22:22:22',
                                ip_dst='10.0.0.1',
                                ip_id=101,
                                ip_ttl=64)
    
    @allure.step
    def send_packet(self, pkt_bundle):
        send_packet(pytest.dataplane, pkt_bundle.ports, pkt_bundle.packet)

    @allure.step
    def verify_packet(self, pkt_bundle):
        pytest.logger.info('Verifying packet: ' + str (pkt_bundle.packet))
