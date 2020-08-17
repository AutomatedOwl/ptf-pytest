import pytest
import allure

class LpmTable:
            
    def __init__(self, device, topology, layer):
        self.device = device
        self.topology = topology
        self.layer = layer

    @allure.step
    def add_entry(self, lpm_entry):
        assert lpm_entry.vlan != 1, "Failed on VLAN 1"
        pytest.logger.info('Adding entry: ' + str (lpm_entry))
        
