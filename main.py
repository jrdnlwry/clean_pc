# main.py
import os
import csv
from config import DATA_PATH, OUTPUT_PATH, CSV_FILENAME, DATE_FORMAT
from clean_pc.deprecated.data_collector import get_file_metadata
from logger import logger

def export_to_csv(file_metadata_list, output_path, filename):
    csv_file_path = os.path.join(output_path, filename)
    fieldnames = ["file", "name", "type", "location", "size (bytes)", "created", "modified", "accessed"]

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(file_metadata_list)
    return csv_file_path

def main():
    logger.info("Starting data collection...")
    # Gather metadata
    data = get_file_metadata(DATA_PATH, DATE_FORMAT)

    # Export to CSV
    csv_path = export_to_csv(data, OUTPUT_PATH, CSV_FILENAME)
    print(f"Metadata has been exported to {csv_path}")
    logger.info("Data collection finished!")

if __name__ == "__main__":
    main()