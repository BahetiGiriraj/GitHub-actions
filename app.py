import os
from datetime import datetime

print("Hello from GitHub Actions!")

print(f"Current Time: {datetime.now()}")

app_name = os.getenv("APP_NAME", "Not Set")
print(f"App Name: {app_name}")

print("Workflow completed successfully!")
