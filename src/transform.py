def transform_logs(logs):
    transformed = []

    for line in logs:
        try:
            timestamp, level, message = line.split(", ", 2)
            transformed.append((timestamp, level, message))
        except ValueError:
            # Skip lines that do not follow the expected format
            continue
    
    return transformed
