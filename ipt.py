import os
import socket

# Địa chỉ IP của mạng cục bộ
network = '192.168.1.'

# Tạo file để ghi kết quả
with open('active_ips.txt', 'w') as f:
    # Kiểm tra từng IP trong mạng
    for i in range(1, 256):
        ip = network + str(i)
        try:
            # Sử dụng hàm gethostbyaddr để kiểm tra IP
            socket.gethostbyaddr(ip)
            f.write(ip + '\n')
        except socket.herror:   # Nếu không thể truy cập IP, bỏ qua
            pass
