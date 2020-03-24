import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mem_common import DDR_COUNT, DDROp


BAR_WIDTH = 60
BAR_MARGIN = 120
BAR_HEIGHT = 512

class MemDraw:
    def __init__(self):
        self._colors = None
        self._ddr_names = ['DDR1', 'DDR2', 'DDR3', 'DDR4']
        self._ddr_pos = range(BAR_WIDTH, BAR_MARGIN * 5, BAR_MARGIN)

    def _plot_agent(self, agent, agent_index):        
        rects = plt.bar(self._ddr_pos[agent.ddr_tag.value], 
                        agent.size_m, bottom=agent.start_addr/1024/1024, 
                        facecolor=self._colors[agent_index], edgecolor='None',
                        width=BAR_WIDTH, alpha=0.5)
        rect = rects[0]
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, 
                 rect.get_y() + height / 2.0, agent.name, ha='center', va='center',
                 size=9)

        plt.hlines(y=rect.get_y() + rect.get_height(), 
                   xmin=rect.get_x() + rect.get_width(), 
                   xmax=rect.get_x() + BAR_MARGIN - rect.get_width() / 2)

        plt.text(rect.get_x() + rect.get_width(), 
                 rect.get_y() + rect.get_height(), 
                 '0x%08X' % agent.start_addr, ha='left', va='top', size=9)

    def _get_cmap(self, mapping):
        # generate color map
        agent_count = 0
        for agents in mapping:
            for agent in agents:
                if agent.ddr_op == DDROp.R:
                    continue
                agent_count += 1
        cmap = plt.cm.get_cmap("hsv")
        color_values = []
        color_value = 0.0
        step_value = 1.0 / agent_count
        while color_value < 1:
            color_values.append(color_value)
            color_value += step_value    
        random.shuffle(color_values)            
        return cmap(color_values)

    def plot(self, config):        
        fig = plt.figure()        
        mapping = config.get_ddr_mapping()
        self._colors = self._get_cmap(mapping)

        agent_index = 0
        for agents in mapping:
            for agent in agents:                 
                if agent.ddr_op == DDROp.R:
                    continue
                print(agent)
                self._plot_agent(agent, agent_index)
                agent_index += 1

        axes = plt.gca()
        for i in range(DDR_COUNT):
            rect = patches.Rectangle((self._ddr_pos[i] - BAR_WIDTH / 2, 0), BAR_WIDTH, BAR_HEIGHT, facecolor='none', edgecolor='k', alpha=0.5)
            axes.add_patch(rect)

        plt.xlim(0, self._ddr_pos[3] + BAR_WIDTH)
        plt.ylim(0, BAR_HEIGHT + 16)
        yticks = range(0, 512 + 16, 16)        
        plt.yticks(yticks, yticks)

        plt.xticks(self._ddr_pos, self._ddr_names)
        plt.title('DDR Memory Usage for %s' % config.name)
        plt.ylabel('Memory Amount (M)')
        fig.tight_layout()
        plt.get_current_fig_manager().window.state('zoomed')        
        plt.show()
              
