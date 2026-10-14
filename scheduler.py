import schedule
import time
from datetime import datetime
from main import run_robot
import logging
from pathlib import Path
import json

# Project folder
base_dir = Path(__file__).resolve().parent

# read JSON configuration
config_path = base_dir / "config.json"

with open(config_path, "r", encoding="utf-8") as file:
    config = json.load(file)

# Configure logging
logs_folder = Path(__file__).resolve().parent / "logs"
logs_folder.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=logs_folder / "scheduler.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

def execute_robot():
    try:
        logging.info("Starting robot execution")

        run_robot()

        logging.info("Robot executed successfuly")

    except Exception:
        logging.exception("Robot execution failed")

# Read scheduling settings
interval = config["interval"]
frequency = int(config["frequency"])
daily_time = config["daily_time"]

if interval in ("minutes", "hours") and frequency < 1:
    raise ValueError("Frequency must be at least 1.")

elif interval == "minutes":
    # Schedule the robot
    schedule.every(frequency).minutes.do(execute_robot)

elif interval == "hours":
    schedule.every(frequency).hours.do(execute_robot)
    
elif interval == "days":
    schedule.every(frequency).days.at(daily_time).do(execute_robot)

else:
    raise ValueError(f"Invalid interval: {interval}"
                     )

# Other scheduling options:
# schedule.every(1).hours.do(run_robot)
# schedule.every().day.at("08:00").do(run_robot)

print(f"Robot started | Interval: {interval}")
print("Press Ctrl + C to stop.")

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nRobot stopped by user.")
    logging.info("Scheduler stopped by user")