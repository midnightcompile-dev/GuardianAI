cpu_history = []


def add_cpu(cpu):
    cpu_history.append(cpu)


def get_average_cpu():
    if len(cpu_history) == 0:
        return 0

    return sum(cpu_history) / len(cpu_history)