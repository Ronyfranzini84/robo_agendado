from datetime import datetime
from pathlib import Path
from report import generate_report

# Create the logs folder
logs_folder = Path(__file__).resolve().parent / "logs"
logs_folder.mkdir(parents=True, exist_ok=True)

# Generate Excel report
file_path = generate_report()

# Get current date and time
now = datetime.now()

# Format date and time
execution_time = now.strftime("%d/%m/%Y %H:%M:%S")

# Define the log file
log_file =logs_folder / "execucoes.txt"

# Register the execution
with open(log_file, "a", encoding="utf-8") as file:
    file.write(f"Robot executed at: {execution_time} | Report: {file_path}\n")

print(f"Robot executed successfully: {execution_time}")