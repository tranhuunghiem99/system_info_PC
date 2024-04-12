# import psutil
# import GPUtil

# # Thông tin về CPU
# print("CPU Info:")
# print(psutil.cpu_percent())
# print(psutil.cpu_count())

# # Thông tin về RAM
# print("RAM Info:")
# print(psutil.virtual_memory())

# # Thông tin về ổ cứng
# print("Disk Info:")
# print(psutil.disk_usage('/'))

# # Thông tin về card đồ họa
# print("GPU Info:")
# gpus = GPUtil.getGPUs()
# for gpu in gpus:
#     print(gpu)

# # Thông tin về các driver
# print("Driver Info:")
# print(psutil.disk_partitions())
# ==========2========
# import os
# import psutil
# import platform

# # System model and type
# system_model = platform.machine()
# system_type = platform.system()

# # OS Name and Version
# os_name = platform.platform()
# os_version = platform.version()

# # BIOS version and mode
# # Note: This information may not be available through Python and may require using system-specific tools or libraries.
# bios_version = "Not available"
# bios_mode = "Not available"

# # Baseboard manufacturer
# # Note: This information may not be available through Python and may require using system-specific tools or libraries.
# baseboard_manufacturer = "Not available"

# # User name
# user_name = os.getlogin()

# # Installed physical memory
# installed_memory = psutil.virtual_memory().total / (1024 ** 3)  # in GB

# # Processor
# processor = platform.processor()

# # Print the information
# print(f"System Model: {system_model}")
# print(f"System Type: {system_type}")
# print(f"OS Name & Version OS: {os_name} {os_version}")
# print(f"BIOS version: {bios_version}")
# print(f"BIOS mode: {bios_mode}")
# print(f"Baseboard manufacturer: {baseboard_manufacturer}")
# print(f"User Name: {user_name}")
# print(f"Installed physical memory: {installed_memory} GB")
# print(f"Processor: {processor}")
# ====3====
import os
import psutil
import platform

# System model and type
system_model = platform.machine()
system_type = platform.system()

# OS Name and Version
os_name = platform.platform()
os_version = platform.version()

# BIOS version and mode
# Note: This information may not be available through Python and may require using system-specific tools or libraries.
bios_version = "Not available"
bios_mode = "Not available"

# Baseboard manufacturer
# Note: This information may not be available through Python and may require using system-specific tools or libraries.
baseboard_manufacturer = "Not available"

# User name
user_name = os.getlogin()

# Installed physical memory
installed_memory = psutil.virtual_memory().total / (1024 ** 3)  # in GB

# Processor
processor = platform.processor()

# Hard drive capacity
hard_drive_capacity = psutil.disk_usage('/').total / (1024 ** 3)  # in GB

# Print the information
print(f"System Model: {system_model}")
print(f"System Type: {system_type}")
print(f"OS Name & Version OS: {os_name} {os_version}")
print(f"BIOS version: {bios_version}")
print(f"BIOS mode: {bios_mode}")
print(f"Baseboard manufacturer: {baseboard_manufacturer}")
print(f"User Name: {user_name}")
print(f"Installed physical memory: {installed_memory} GB")
print(f"Processor: {processor}")
print(f"Hard drive capacity: {hard_drive_capacity} GB")