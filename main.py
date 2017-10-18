from system.cpu import Processor


def run(filename):
    cpu = Processor.load(filename)
    cpu.step()


if __name__ == '__main__':
    run('system/cpu/6502.yaml')
