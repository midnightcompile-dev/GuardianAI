previous_processes = set()


def get_previous_processes():
    return previous_processes


def update_processes(process_names):
    global previous_processes
    previous_processes = set(process_names)