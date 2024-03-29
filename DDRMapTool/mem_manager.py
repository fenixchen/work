from mem_common import *
from mem_block import MemBlock
import mem_agents
from mem_allocator import MemAllocator
from mem_global_var import GV


class MemManager:
    def __init__(self):
        self._agent_list = []
        self._block_list = []
        self._init_agents()

    def _init_agents(self):
        block = self._add_block("MEMC_MC_L")
        self._add_agent(mem_agents.MemAgent_KMC_0(), block)
        self._add_agent(mem_agents.MemAgent_KMC_1(), block)
        self._add_agent(mem_agents.MemAgent_RO('KMC_5', 'KMC_0', 'MC_L_YC_HF_DEC_CUR'), block)
        self._add_agent(mem_agents.MemAgent_RO('KMC_4', 'KMC_0', 'MC_L_YC_HF_DEC_PRE'), block)
        self._add_agent(mem_agents.MemAgent_RO('KMC_7', 'KMC_1', 'MC_L_YC_LF_DEC_CUR'), block)
        self._add_agent(mem_agents.MemAgent_RO('KMC_6', 'KMC_1', 'MC_L_YC_LF_DEC_PRE'), block)

        block = self._add_block("MEMC_MC_R")
        self._add_agent(mem_agents.MemAgent_KMC_8(), block)
        self._add_agent(mem_agents.MemAgent_KMC_9(), block)
        self._add_agent(mem_agents.MemAgent_RO('KMC_11', 'KMC_8', 'MC_R_YC_HF_DEC_CUR'), block)
        self._add_agent(mem_agents.MemAgent_RO('KMC_10', 'KMC_8', 'MC_R_YC_HF_DEC_PRE'), block)
        self._add_agent(mem_agents.MemAgent_RO('KMC_13', 'KMC_9', 'MC_R_YC_LF_DEC_CUR'), block)
        self._add_agent(mem_agents.MemAgent_RO('KMC_12', 'KMC_9', 'MC_R_YC_LF_DEC_PRE'), block)

        block = self._add_block("MEMC_ME1/2_LOGO")
        self._add_agent(mem_agents.MemAgent_KME_0(), block)
        self._add_agent(mem_agents.MemAgent_RO('KME_1', 'KME_0', 'IP_ME1_NR_R'), block)
        self._add_agent(mem_agents.MemAgent_RO('KME_3', 'KME_0', 'ME1_CUR_R'), block)
        self._add_agent(mem_agents.MemAgent_RO('KME_2', 'KME_0', 'ME1_PRE_R'), block)
        self._add_agent(mem_agents.MemAgent_RO('KMV_11', 'KME_0', 'ME2_CUR_R'), block)
        self._add_agent(mem_agents.MemAgent_RO('KMV_10', 'KME_0', 'ME2_PRE_R'), block)
        self._add_agent(mem_agents.MemAgent_KME_8(), block)
        self._add_agent(mem_agents.MemAgent_RO('KME_9', 'KME_8', 'IP_LOG_R'), block)
        self._add_agent(mem_agents.MemAgent_KME_10(), block)
        self._add_agent(mem_agents.MemAgent_RO('KME_11', 'KME_10', 'IP_MASK_R'), block)
        self._add_agent(mem_agents.MemAgent_KME_12(), block)
        self._add_agent(mem_agents.MemAgent_RO('KME_13', 'KME_12', 'Pixel_LOGO_R'), block)
        self._add_agent(mem_agents.MemAgent_KME_14(), block)
        self._add_agent(mem_agents.MemAgent_RO('KME_15', 'KME_14', 'HOG_history_R'), block)

        block = self._add_block("MEMC_Vector_Logo")
        self._add_agent(mem_agents.MemAgent_KMV_01(), block)
        self._add_agent(mem_agents.MemAgent_RO('KMV_07', 'KMV_01', 'ME2_Loop_PH_R'), block)
        self._add_agent(mem_agents.MemAgent_KMV_02(), block)
        self._add_agent(mem_agents.MemAgent_RO('KMV_03', 'KMV_02', 'ME1_Loop_PPI_R'), block)

        self._add_agent(mem_agents.MemAgent_KMV_04(), block)
        self._add_agent(mem_agents.MemAgent_RO('KMV_08', 'KMV_04', 'ME1_VBUF_PPFV_R'), block)
        self._add_agent(mem_agents.MemAgent_RO('KMV_09', 'KMV_04', 'ME1_VBUF_PFVPI_R'), block)

        self._add_agent(mem_agents.MemAgent_KMV_05(), block)
        self._add_agent(mem_agents.MemAgent_RO('KMV_06', 'KMV_05', 'ME1_Loop_PFVPI_R'), block)

        block = self._add_block('TOP_TCON_OD_L')
        self._add_agent(mem_agents.MemAgent_OD_W(), block)
        self._add_agent(mem_agents.MemAgent_RO('OD_R', 'OD_W', 'TOP_OD_R_L'), block)

        block = self._add_block('TOP_TCON_OD_R')
        self._add_agent(mem_agents.MemAgent_TOP_OD_W(), block)
        self._add_agent(mem_agents.MemAgent_RO('TOP_OD_R', 'TOP_OD_W', 'TOP_OD_R_R'), block)

        block = self._add_block('TOP_DEMURA')
        self._add_agent(mem_agents.MemAgent_TOP_DEMURA_R(), block)

        block = self._add_block('BOT_TCON_OD')
        self._add_agent(mem_agents.MemAgent_BOT_OD_W(), block)
        self._add_agent(mem_agents.MemAgent_RO('BOT_OD_R', 'BOT_OD_W', 'BOT_OD_R'), block)

        block = self._add_block('BOT_DEMURA')
        self._add_agent(mem_agents.MemAgent_BOT_DEMURA_R(), block)

        block = self._add_block('OSD')
        self._add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_IN_1), block)
        self._add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_IN_2), block)
        self._add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_ALPHA), block)
        self._add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_R_1), block)
        self._add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_R_2), block)
        self._add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_ALPHA_R), block)

        block = self._add_block('3D_NR/SR')
        self._add_agent(mem_agents.MemAgent_VIDEO_IN(mem_agents.VideoInType.VIDEO_IN_1), block)
        self._add_agent(mem_agents.MemAgent_VIDEO_IN(mem_agents.VideoInType.VIDEO_IN_2), block)
        self._add_agent(mem_agents.MemAgent_VIDEO_IN(mem_agents.VideoInType.VIDEO_IN_3), block)
        self._add_agent(mem_agents.MemAgent_VIDEO_IN(mem_agents.VideoInType.VIDEO_IN_4), block)

        self._add_agent(mem_agents.MemAgent_RO('SRP_READ_1', 'SRP_FIR_WRITE_1', 'SRP_READ_1'), block)
        self._add_agent(mem_agents.MemAgent_RO('SRP_READ_2', 'SRP_FIR_WRITE_2', 'SRP_READ_2'), block)
        self._add_agent(mem_agents.MemAgent_RO('SRP_READ_3', 'SRP_FIR_WRITE_3', 'SRP_READ_3'), block)
        self._add_agent(mem_agents.MemAgent_RO('SRP_READ_4', 'SRP_FIR_WRITE_4', 'SRP_READ_4'), block)

        self._add_agent(mem_agents.MemAgent_SRP_W(mem_agents.SRPType.SRP_FIR_WRITE_1), block)
        self._add_agent(mem_agents.MemAgent_SRP_W(mem_agents.SRPType.SRP_FIR_WRITE_2), block)
        self._add_agent(mem_agents.MemAgent_SRP_W(mem_agents.SRPType.SRP_FIR_WRITE_3), block)
        self._add_agent(mem_agents.MemAgent_SRP_W(mem_agents.SRPType.SRP_FIR_WRITE_4), block)

        self._add_agent(mem_agents.MemAgent_SRP_W(mem_agents.SRPType.SRP_NR_OUT_WRITE_1), block)
        self._add_agent(mem_agents.MemAgent_SRP_W(mem_agents.SRPType.SRP_NR_OUT_WRITE_2), block)
        self._add_agent(mem_agents.MemAgent_SRP_W(mem_agents.SRPType.SRP_NR_OUT_WRITE_3), block)
        self._add_agent(mem_agents.MemAgent_SRP_W(mem_agents.SRPType.SRP_NR_OUT_WRITE_4), block)

        self._add_agent(mem_agents.MemAgent_MV_W_3DRS(), block)
        self._add_agent(mem_agents.MemAgent_MV_R_3DRS(), block)
        self._add_agent(mem_agents.MemAgent_CNT_W_3DRS(), block)
        self._add_agent(mem_agents.MemAgent_CNT_R_3DRS(), block)

        block = self._add_block('AISR')
        self._add_agent(mem_agents.MemAgent_AISR_R(), block)
        self._add_agent(mem_agents.MemAgent_AISR_W_1(), block)
        self._add_agent(mem_agents.MemAgent_AISR_W_2(), block)
        self._add_agent(mem_agents.MemAgent_AISR_MAP(), block)

        block = self._add_block('Local_AI')
        self._add_agent(mem_agents.MemAgent_LOCAL_AI_W(), block)
        self._add_agent(mem_agents.MemAgent_LOCAL_AI_R(), block)

        block = self._add_block('2D_NR')
        self._add_agent(mem_agents.MemAgent_2D_NR_DECONTOUR_W(), block)
        self._add_agent(mem_agents.MemAgent_2D_NR_DECONTOUR_R(), block)
        self._add_agent(mem_agents.MemAgent_2D_NR_BMNR_W(), block)
        self._add_agent(mem_agents.MemAgent_2D_NR_BMNR_R(), block)

        block = self._add_block('Local_Contrast')
        self._add_agent(mem_agents.MemAgent_LOCAL_CONTRAST_1_W(), block)
        self._add_agent(mem_agents.MemAgent_LOCAL_CONTRAST_1_R(), block)
        self._add_agent(mem_agents.MemAgent_LOCAL_CONTRAST_2_W(), block)
        self._add_agent(mem_agents.MemAgent_LOCAL_CONTRAST_2_R(), block)

        block = self._add_block('DNN_IN')
        self._add_agent(mem_agents.MemAgent_DNN_IN('DNN_IN_1'), block)
        self._add_agent(mem_agents.MemAgent_DNN_IN('DNN_IN_2'), block)
        self._add_agent(mem_agents.MemAgent_DNN_IN('DNN_IN_3'), block)
        self._add_agent(mem_agents.MemAgent_DNN_IN('DNN_IN_4'), block)

        block = self._add_block('DNNA_YOLO')
        self._add_agent(mem_agents.MemAgent_DNN_ACC('DNN_ACC_1'), block)
        self._add_agent(mem_agents.MemAgent_DNN_ACC('DNN_ACC_2'), block)
        self._add_agent(mem_agents.MemAgent_DNN_ACC('DNN_ACC_3'), block)
        self._add_agent(mem_agents.MemAgent_DNN_ACC('DNN_ACC_4'), block)

        block = self._add_block('CADENCE_DETECT_FOR_3DNR_SR')
        self._add_agent(mem_agents.MemAgent_PLDD_W(), block)
        self._add_agent(mem_agents.MemAgent_PLDD_R(), block)

        block = self._add_block('SRP_OUT_W')
        self._add_agent(mem_agents.MemAgent_SRP_OUT_W('SRP_OUT_W_1'), block)
        self._add_agent(mem_agents.MemAgent_SRP_OUT_W('SRP_OUT_W_2'), block)
        self._add_agent(mem_agents.MemAgent_SRP_OUT_W('SRP_OUT_W_3'), block)
        self._add_agent(mem_agents.MemAgent_SRP_OUT_W('SRP_OUT_W_4'), block)

        block = self._add_block('LOCAL_DIMMING')
        self._add_agent(mem_agents.MemAgent_LOCAL_DIMMING_W(), block)
        self._add_agent(mem_agents.MemAgent_LOCAL_DIMMING_R(), block)

        block = self._add_block('LDG_R')
        self._add_agent(mem_agents.MemAgent_LDG_R('LDR_R1'), block)
        self._add_agent(mem_agents.MemAgent_LDG_R('LDR_R2'), block)
        self._add_agent(mem_agents.MemAgent_LDG_R('LDR_R3'), block)
        self._add_agent(mem_agents.MemAgent_LDG_R('LDR_R4'), block)

        block = self._add_block('CPU')
        self._add_agent(mem_agents.MemAgent_CPU(), block)

    def reset_memory(self):
        for agent in self._agent_list:
            agent.reset_memory()

    def _add_block(self, block_name):
        block = MemBlock(block_name)
        return block

    def _add_agent(self, agent, block):
        self._agent_list.append(agent)
        block.add_agent(agent)
        p_verbose('%s, %-20s, %-20s, bandwidth:%8.2fM, size:%8.2fM, IP:%s' % (
            agent.op_str, agent.module_name, agent.name, agent.bandwidth_m, agent.size_m, agent.block_name))

    def plot(self):
        pass

    @property
    def agent_list(self):
        return self._agent_list

    def get_agent(self, name):
        for agent in self._agent_list:
            if agent.name == name:
                return agent
        return None

    def allocate_agent_memory(self):

        # Process pre-located memory
        for i in range(GV.DDR_count):
            reg_dict = {}
            p_debug('>>> Allicate pre-located memory in <DDR%s>' % (i + 1))

            # Process write agent with start_addr or ddr_tag
            for agent in self._agent_list:
                if agent.unused or agent.ddr_tag.value != i or agent.ddr_op == DDROp.R:
                    continue
                if agent.start_addr is None:
                    continue
                agent.allocate_memory(reg_dict)
                if not agent.allocated:
                    p_error(agent.debug_info)
                    assert False
                p_verbose("Pre-locate %s" % agent.alloc_info)
                reg_dict['%s_start_addr' % agent.name] = agent.start_addr
        # Process agent with DDR tag but no start address
        allocator_list = [MemAllocator(DDRTag(i)) for i in range(GV.DDR_count)]
        for i in range(GV.DDR_count):
            p_debug('>>> Allocate un-located agent in <DDR%s>' % (i + 1))
            allocator = allocator_list[i]
            for agent in self._agent_list:
                if agent.unused or agent.ddr_tag.value != i or agent.ddr_op == DDROp.R:
                    continue
                allocator.add_agent(agent)
            allocator.fit()
            reg_dict = {}
            for agent in allocator.unallocated_agents:
                agent.allocate_memory(reg_dict)
                if not agent.allocated:
                    p_error('Allocate memory for %s(%.2f) on %s failed, no enought memeory' % (
                        agent.name, agent.size_m, agent.ddr_tag.name))
                else:
                    reg_dict['%s_start_addr' % agent.name] = agent.start_addr
                    p_verbose("Allocate start_addr %s" % agent.alloc_info)

        # Process agent without DDR
        for agent in self._agent_list:
            if agent.unused or agent.ddr_op == DDROp.R or agent.ddr_tag != DDRTag.NONE:
                continue
            if agent.allocated:
                continue
            for i in range(GV.DDR_count):
                allocator = allocator_list[i]
                if allocator.allocate_memory(agent):
                    p_debug('>>> Allocate un-tagged agent %s success at DDR%d - [0x%08X, 0x%08X]:%.2fM' % (
                        agent.name, i + 1, agent.start_addr, agent.end_addr, agent.size_m))
                    break
            if not agent.allocated:
                p_debug('>>> Allocate un-tagged agent %s failed' % (agent.name))

        # process read only agent
        for agent in self.agent_list:
            if agent.ddr_op == DDROp.R and agent.write_agent_name is not None:
                write_agent = self.get_agent(agent.write_agent_name)
                assert write_agent is not None, "Cannot find write agent <%s>" % agent.write_agent_name
                agent.init_memory(write_agent.ddr_tag, write_agent.start_addr)
        self._agent_list.sort()
