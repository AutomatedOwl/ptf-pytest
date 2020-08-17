import sys
sys.path.append('./example/test-factories')
import unittest
import sys
import logging
from ptf.testutils import *
import ptf
import pytest
import allure
import time
import consts
from ptf import config
from parameterized import parameterized
from data_provider import DataProvider
from ptf_example_testcase import PtfTestCase

@pytest.mark.usefixtures("cache")
class PtfExampleTests(PtfTestCase):

    @parameterized.expand(['test_send_one_pkt'])
    @allure.feature('Send Packet')
    #@pytest.mark.skip(reason="XYZ001 Ongoing Bug")
    @pytest.mark.order1
    def test_send_one_pkt(self, method):
        pytest.logger.info('Test execution:' + str(self))

        # control-plane configuration
        pytest.logger.info('Perform control-plane configuration')
        pytest.cp_factory.add_lpm_entry(
            self.get_lpm_entries(method)[consts.FIRST_LPM_ENTRY])

        # data-plane operation
        pytest.logger.info('Perform data-plane operation')
        pytest.dp_factory.send_packet(self.get_packets(method)[consts.FIRST_PACKET])
        pytest.logger.info('Packet Sent')

    @parameterized.expand(['test_send_receive_pkt'])
    @allure.feature('Send/Receive Packet')
    @pytest.mark.order2
    #@allure.issue('issue-001', 'Send/Receive Packet flaky test')
    #@pytest.mark.skip(reason="XYZ001 Ongoing Bug")
    def test_send_receive_pkt(self, method):
        pytest.logger.info('Performing ' + str(self))

        # control-plane configuration
        pytest.logger.info('Perform control-plane configuration')
        pytest.cp_factory.add_lpm_entry(
            self.get_lpm_entries(method)[consts.FIRST_LPM_ENTRY])

        # data-plane operation
        pytest.dp_factory.send_packet(self.get_packets(method)[consts.FIRST_PACKET])
        pytest.logger.info('Packet Sent')
        pytest.logger.info('Perform data-plane operation')
        pytest.dp_factory.verify_packet(self.get_packets(method)[consts.FIRST_PACKET])
        pytest.logger.info('Packet Verified')

    @parameterized.expand(['test_send_two_pkts'])
    @allure.feature('Send Packet')
    @pytest.mark.order3
    def test_send_two_pkts(self, method):
        pytest.logger.info('Performing ' + str(self))

        # control-plane configuration
        pytest.logger.info('Perform control-plane configuration')
        pytest.cp_factory.add_lpm_entry(
            self.get_lpm_entries(method)[consts.FIRST_LPM_ENTRY])

        # data-plane operation
        pytest.logger.info('Perform data-plane operation')
        pytest.dp_factory.send_packet(self.get_packets(method)[consts.FIRST_PACKET])
        pytest.logger.info('Packet Sent')
        pytest.logger.info('Perform data-plane operation')
        pytest.dp_factory.send_packet(self.get_packets(method)[consts.SECOND_PACKET])
        pytest.logger.info('Packet Sent')