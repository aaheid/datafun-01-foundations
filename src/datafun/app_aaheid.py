"""src/datafun/app_aaheid.py - Project script (Customized).
Author: aaheid
"""
import logging
import os
import statistics
from typing import Final
from datafun_toolkit.logger import get_logger, log_header

LOG = get_logger("P01", level="INFO")

def main():
    log_header(LOG, "P01")
    print("!!! SCRIPT RUNNING WITH AAHEID CUSTOMIZATIONS !!!")
    
    sample_numbers = [4, 5, 5, 4, 3, 5, 4, 5, 2, 4]
    summary_table = {
        "Total Records": len(sample_numbers),
        "Maximum Value": max(sample_numbers),
        "Minimum Value": min(sample_numbers),
        "Average Score": sum(sample_numbers) / len(sample_numbers)
    }

    print("\n=== CUSTOM ANALYTICAL SUMMARY REPORT ===")
    for key, value in summary_table.items():
        print(f"{key:<20}: {value}")
    print("========================================\n")

    print("=== TEXT VISUALIZATION: SCORE FREQUENCY ===")
    for score in sorted(set(sample_numbers)):
        count = sample_numbers.count(score)
        print(f"Score {score} | {"*" * count} ({count})")
    print("===========================================\n")

    output_directory = "outputs"
    output_file_path = os.path.join(output_directory, "report_aaheid.txt")
    os.makedirs(output_directory, exist_ok=True)

    with open(output_file_path, "w") as file:
        file.write("ANALYTICAL REPORT FOR AAHEID\n============================\n")
        for key, value in summary_table.items():
            file.write(f"{key}: {value}\n")
    print(f"Success: Final report written to {output_file_path}")

if __name__ == "__main__":
    main()
