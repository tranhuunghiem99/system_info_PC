# import platform
# import getpass
# import psutil

# # Lấy thông tin hệ thống
# system_info = {
#     "System Model": platform.machine(),
#     "System Type": platform.architecture()[0],
#     "OS Name & Version": platform.platform(),
#     "User Name": getpass.getuser(),
#     "Installed Physical Memory": str(psutil.virtual_memory().total),
#     "Processor": platform.processor(),
# }

# # Ghi thông tin hệ thống vào file
# with open('system_info.txt', 'w') as f:
#     for key, value in system_info.items():
#         f.write(f"{key}: {value}\n")

import platform
import getpass
import psutil
import wmi

# Khởi tạo WMI object
c = wmi.WMI()

# Lấy thông tin hệ thống
system_info = {
    "System Model": platform.machine(),
    "System Type": platform.architecture()[0],
    "OS Name & Version": platform.platform(),
    "BIOS Version": c.Win32_BIOS()[0].BIOSVersion,
    "Disk": str(psutil.disk_usage('/').total),
    "User Name": getpass.getuser(),
    "Installed Physical Memory": str(psutil.virtual_memory().total),
    "Processor": platform.processor(),
}

# Ghi thông tin hệ thống vào file
with open('system_info.txt', 'w') as f:
    for key, value in system_info.items():
        f.write(f"{key}: {value}\n")
