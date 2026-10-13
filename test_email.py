from report import generate_report
from email_sender import send_email

# Generate Excel report
file_path = generate_report()

# Send report by email
send_email(file_path)

print("Robot finished successfully!")
