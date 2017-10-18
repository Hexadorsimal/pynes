from cpu_importer import CpuImporter


def run(filename):
    cpu = CpuImporter.load_from_file(filename)
    cpu.step()


if __name__ == '__main__':
    run('cpu/6502.yaml')
