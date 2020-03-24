from mem_config_1chip8k120hz import MemConfig_1Chip8K120Hz
from mem_draw import MemDraw


def main():
    config = MemConfig_1Chip8K120Hz()

    regs = config.generate_registers()       

    draw = MemDraw()

    draw.plot(config)

if __name__ == '__main__':
    main()
