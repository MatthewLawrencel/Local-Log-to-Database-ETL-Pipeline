def transform_logs(logs):
    transformed = []
    for line in logs:
        try:
            timestamp, level, message = line.split(", ", 2)
            transformed.append((timestamp, level, message))
        except ValueError:
            continue
    return transformed
