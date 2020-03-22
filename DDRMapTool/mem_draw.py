import matplotlib.pyplot as plt

class MemDraw:
    def __init__(self, data):
        self._data = data
    def plot(self):
        fig = plt.figure(figsize=(10, 8))
        plt.bar([10], [128], color='red', edgecolor='k', width=4, label='test')
        plt.bar([20], [256], color='blue', edgecolor='k', width=4)
        plt.bar([30], [256], color='yellow', edgecolor='k', width=4)
        plt.bar([40], [256], color='black', edgecolor='k', width=4)

        plt.bar([10], [64], bottom=[128], color='pink', edgecolor='k', width=4)

        plt.bar([10], [320], bottom=[192], color='none', edgecolor='k', width=4)

        plt.text(10, 32, "KMC_0", horizontalalignment='left', fontsize=9)

        plt.text(10, 154, "KMC_1", horizontalalignment='left', fontsize=9)

        plt.ylim(0, 544)

        yticks = []
        unit = 0
        while  True:
            yticks.append(unit)
            unit += 16
            if unit > 512:
                break

        plt.yticks(yticks, yticks)
        plt.xticks([10, 20, 30, 40], ["DDR0", "DDR1", "DDR2", "DDR3"])

        plt.title('DDR Memory Usage')
        plt.ylabel('Memory Amount (M)')
        fig.tight_layout()
        plt.show()
        