from src.extract import extract_logs
from src.transform import transform_logs
from src.load import load_to_db
import sys

def main(log_dir):
    print("Extracting logs...")
    logs = extract_logs(log_dir)
    print("Transforming logs...")
    transformed_data = transform_logs(logs)
    print("Loading into database...")
    load_to_db(transformed_data)
    print("✅ Data successfully loaded into logs.db")
    print("🎯 Pipeline completed successfully!")

if __name__ == "__main__":
    log_dir = "logs"
    if len(sys.argv) > 2 and sys.argv[1] == "--log_dir":
        log_dir = sys.argv[2]
    main(log_dir)
