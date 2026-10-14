
import json
import time
import logging
import threading
from pathlib import Path

import schedule

from main import run_robot


# Project directory
base_dir = Path(__file__).resolve().parent

# Read configuration
with open(base_dir / "config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

# Configure logs
logs_folder = base_dir / "logs"
logs_folder.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=logs_folder / "scheduler_threading.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

# Create execution lock
execution_lock = threading.Lock()


def execute_robot():
    # Try to acquire lock without waiting
    if not execution_lock.acquire(blocking=False):
        logging.warning("Robot already running. Skipping execution.")
        return

    try:
        logging.info("Starting robot execution")

        run_robot()

        logging.info("Robot executed successfully")

    except Exception:
        logging.exception("Robot execution failed")

    finally:
        execution_lock.release()


def start_robot():
    # Run robot in a separate thread
    thread = threading.Thread(
        target=execute_robot,
        name="ReportRobot"
    )

    thread.start()


# Read scheduling settings
interval = config["interval"]
frequency = int(config["frequency"])
daily_time = config["daily_time"]

if interval in ("minutes", "hours") and frequency < 1:
    raise ValueError("Frequency must be at least 1.")

# Configure schedule
if interval == "minutes":
    schedule.every(frequency).minutes.do(start_robot)

elif interval == "hours":
    schedule.every(frequency).hours.do(start_robot)

elif interval == "days":
    schedule.every().day.at(daily_time).do(start_robot)

else:
    raise ValueError(f"Invalid interval: {interval}")


print("Robot scheduler with threading started!")
print("Press Ctrl + C to stop.")

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nScheduler stopped.")
    logging.info("Scheduler stopped by user")
