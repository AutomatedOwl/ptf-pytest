import unittest
import logging
logging.basicConfig()
LOGGER = logging.getLogger(__name__)
from ptf.testutils import *
import pytest
import allure
import time

@pytest.mark.usefixtures("cache")
class PtfExampleTests(unittest.TestCase):
   
    @pytest.fixture(autouse=True)
    def example_fixture(self):
        return 'test_fixture'

    @allure.step
    def passing_step(self):
        pass

    def test_second(self):
        for x in range(6):
          LOGGER.info('Hello World PTF Pytest Second')
        assert True
        self.passing_step()

    def test_ptf(self):
        for x in range(6):
          LOGGER.info('Hello World PTF Pytest First')
        assert True
        self.passing_step()

        # try:
        #     # in tuple: 0 is device number, 2 is port number
        #     # this tuple uniquely identifies a port
        pkt = simple_tcp_packet(eth_dst='00:11:11:11:11:11',
                                eth_src='00:22:22:22:22:22',
                                ip_dst='10.0.0.1',
                                ip_id=101,
                                ip_ttl=64)
        #send_packet(self, (0, 2), pkt)