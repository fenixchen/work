from mem_config_1chip8k120hz import MemConfig_1Chip8K120Hz
from mem_common import DDRTag, DDROp
#from mem_draw import MemDraw


def main():
    config = MemConfig_1Chip8K120Hz()
    regs = config.generate_registers()
    
    print(">>> DDR Mapping Result R")
    mapping = config.get_ddr_mapping()
    for i, agents in enumerate(mapping):
        print("    %s" % DDRTag(i).name)
        for agent in agents:
            if agent.ddr_op == DDROp.W:
                continue
            print("        %-8s, %8.2fM, " % (agent.name, agent.bandwidth_m))          

    print(">>> DDR Mapping Result W")
    mapping = config.get_ddr_mapping()
    for i, agents in enumerate(mapping):
        print("    %s" % DDRTag(i).name)
        for agent in agents:
            if agent.ddr_op == DDROp.R:
                continue
            print("        %-8s, 0x%08X, %8.2fM, %8.2fM" % (agent.name, agent.absolute_addr, agent.size_m, agent.bandwidth_m))

      
    #draw = MemDraw(None)
    #draw.plot()

if __name__ == '__main__':
    main()
