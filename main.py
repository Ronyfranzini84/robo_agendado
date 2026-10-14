from datetime import datetime
from pathlib import Path
from report import generate_report
from email_sender import send_email

def run_robot():
    # Generate Excel report
    file_path = generate_report()

    # Send excel by email
    send_email(file_path)

    # Format date and time
    execution_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Create the logs folder
    logs_folder = Path(__file__).resolve().parent / "logs"
    logs_folder.mkdir(parents=True, exist_ok=True)

    # Define the log file
    log_file =logs_folder / "execucoes.txt"

    # Register the execution
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"Robot executed at: {execution_time} | Report: {file_path}\n")

    print(f"Robot executed successfully: {execution_time}")

if __name__ == "__main__":
    run_robot()