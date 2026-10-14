import threading
import time
from datetime import datetime

def download_report():
    print("Starting report download...")
    time.sleep(3)
    print("Report download successfully!")

def generate_excel():
    print("Starting Excel generation...")
    time.sleep(3)
    print("Excel generated successfully!") 

# Create threads
thread_1 = threading.Thread(target=download_report)
thread_2 = threading.Thread(target=generate_excel)

# Start threads
start_time = datetime.now()

thread_1.start()
thread_2.start()

# Wait for both threads
thread_1.join()
thread_2.join()

end_time = datetime.now()

duration = (end_time - start_time).total_seconds()

print(f"\nTotal execution time: {duration:.2f} seconds")
print("All tasks completed!")