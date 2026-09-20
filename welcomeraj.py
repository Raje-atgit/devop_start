import os
import datetime

# 1. Look for a custom name variable. If none is provided, default to "Guest"
user_name = os.getenv("USER_NAME", "Guest")

# 2. Get the current time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Print the personalized banner
print("\n=========================================")
print(f"🚀 WELCOME, {user_name.upper()}!")
print("   Your custom containerized script ran!")
print(f"⏰ Execution Time: {current_time}")
print("=========================================")
