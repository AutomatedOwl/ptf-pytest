import sys
sys.path.append('./example/test-factories')
from controlplane_factory import ControlPlaneFactory
from dataplane_factory import DataPlaneFactory
from data_provider import DataProvider
from collections import namedtuple
import unittest
import sys
import logging
import ptf
import pytest
import allure
from ptf import config
from parameterized import parameterized
from os import path
from _pytest.fixtures import SubRequest
from pytest import fixture

@pytest.mark.usefixtures("cache")
class PtfTestCase(unittest.TestCase):

    # Namespace configuration
    def pytest_namespace(self):
        return {'logger': None}
        return {'dataplane': None}
        return {'cp_factory': None}
        return {'dp_factory': None}
        return {'PacketBundle': None}
        return {'test_config_map: {}'}

    @classmethod
    def setUpClass(self):
        # Define logger
        pytest.logger = self.get_logger()
        pytest.logger.info('Setting-Up PTF Example Test Case')

        # Initialize dataplane object
        self.dataplane = ptf.dataplane.DataPlane(config)
        pytest.dataplane = self.dataplane

        # Initialize controlplane factory
        pytest.dp_factory = DataPlaneFactory('get_device()', 'get_topology()', 'get_test_layer()')

        # Initialize dataplane factory
        pytest.cp_factory = ControlPlaneFactory('get_device()', 'get_topology()', 'get_test_layer()')

        # Initialize dataprovider
        pytest.data_provider = DataProvider('get_device()', 'get_topology()', 'get_test_layer()')
        pytest.test_config_map = {}

    @classmethod
    def tearDownClass(self):
        # Define logger
        pytest.logger.info('Tearing down PTF Example Test Case')
        self.dataplane.kill()

    # Getter method for logger
    @classmethod
    def get_logger(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        logging.basicConfig()
        logger = logging.getLogger()
        logger.addHandler(stream_handler)
        logger.level = logging.INFO
        return logger
    
    @allure.step
    def setup_method(self, method):
        if hasattr(method, '__name__'):
            pytest.logger.info('Perform test configuration by data-provider')
            test_name = self.get_test_name(method)
            pytest.test_config_map[test_name] = pytest.data_provider.get_data_per_test(test_name)

    def get_test_name(self, method):
        if hasattr(method, '__name__'):
            return method.__name__.split('_0')[0]
    
    def get_packets(self, method):
        return pytest.test_config_map[method].packets

    def get_lpm_entries(self, method):
        return pytest.test_config_map[method].lpm_entries
