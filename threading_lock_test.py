
import threading
import time

# Shared variable
total_reports = 0

# Create a lock
lock = threading.Lock()


def process_reports(robot_name):
    global total_reports

    for i in range(3):

        with lock:
            current_total = total_reports

            time.sleep(1)

            total_reports = current_total + 1

            print(
                f"{robot_name} | "
                f"Report {i + 1} | "
                f"Total: {total_reports}"
            )


# Create threads
thread_1 = threading.Thread(
    target=process_reports,
    args=("Robot 1",)
)

thread_2 = threading.Thread(
    target=process_reports,
    args=("Robot 2",)
)

# Start threads
thread_1.start()
thread_2.start()

# Wait for completion
thread_1.join()
thread_2.join()

print(f"\nFinal total: {total_reports}")
