from ctr_table import CtrTable
from lpm_table import LpmTable
from sp_table import SpTable
from collections import namedtuple
import allure

class ControlPlaneFactory:

    def __init__(self, device, topology, layer):
        self.device = device
        self.topology = topology
        self.ctr_table = CtrTable(device, topology, layer)
        self.lpm_table = LpmTable(device, topology, layer)
        self.sp_table = SpTable(device, topology, layer)
    
    @allure.step
    def add_lpm_entry(self, lpm_entry):
        self.lpm_table.add_entry(lpm_entry)

    