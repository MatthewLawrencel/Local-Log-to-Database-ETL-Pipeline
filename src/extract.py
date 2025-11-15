import os

def extract_logs(log_dir):
    logs = []
    for filename in os.listdir(log_dir):
        if filename.endswith(".log"):
            with open(os.path.join(log_dir, filename), "r") as file:
                for line in file:
                    logs.append(line.strip())
    return logs
