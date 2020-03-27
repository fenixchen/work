from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_DNN_ACC(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, name):
        super().__init__(name, name, DDROp.W)

    def calc_memory(self):
        name = self.name
        if name == 'DNN_ACC_1':
            DNN_ACC_1_Bandwidth = 1565.2/3*DNN_num*(IF(DNN_num == 0, 0, 1))/DNN_Addr_Interleave
            DNN_ACC_1_DDR_size = (5+9*DNN_num)*(IF(DNN_num == 0, 0, 1))/DNN_Addr_Interleave
            return DNN_ACC_1_DDR_size, DNN_ACC_1_Bandwidth
        elif name == 'DNN_ACC_2':
            DNN_ACC_2_Bandwidth = 1565.2/3*DNN_num*(IF(DNN_num == 0, 0, 1))/DNN_Addr_Interleave*(IF(DNN_Addr_Interleave == 1, 0, 1))
            DNN_ACC_2_DDR_size = (5+9*DNN_num)*(IF(DNN_num == 0, 0, 1))/DNN_Addr_Interleave*(IF(DNN_Addr_Interleave == 1, 0, 1))
            return DNN_ACC_2_DDR_size, DNN_ACC_2_Bandwidth
        elif name == 'DNN_ACC_3':
            DNN_ACC_3_Bandwidth = 1565.2/3*DNN_num*(IF(DNN_num == 0, 0, 1))/DNN_Addr_Interleave*(IF(DNN_Addr_Interleave == 1, 0, 1))*(IF(DNN_Addr_Interleave == 2, 0, 1))
            DNN_ACC_3_DDR_size = (5+9*DNN_num)*(IF(DNN_num == 0, 0, 1))/DNN_Addr_Interleave*(IF(DNN_Addr_Interleave == 1, 0, 1))*(IF(DNN_Addr_Interleave == 2, 0, 1))
            return DNN_ACC_3_DDR_size, DNN_ACC_3_Bandwidth
        elif name == 'DNN_ACC_4':
            DNN_ACC_4_Bandwidth = 1565.2/3*DNN_num*(IF(DNN_num == 0, 0, 1))/DNN_Addr_Interleave*(IF(DNN_Addr_Interleave == 1, 0, 1)) * \
                (IF(DNN_Addr_Interleave == 2, 0, 1))*(IF(DNN_Addr_Interleave == 3, 0, 1))
            DNN_ACC_4_DDR_size = (5+9*DNN_num)*(IF(DNN_num == 0, 0, 1))/DNN_Addr_Interleave*(IF(DNN_Addr_Interleave == 1, 0, 1)) * \
                (IF(DNN_Addr_Interleave == 2, 0, 1))*(IF(DNN_Addr_Interleave == 3, 0, 1))
            return DNN_ACC_4_DDR_size, DNN_ACC_4_Bandwidth
        else:
            assert False, "Unknown DNN ACC"
