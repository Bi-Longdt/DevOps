#script kiểm tra xem ứng dụng Flask có đang phản hồi không bằng cách kiểm tra mã trạng thái HTTP 200 OK. 
#Nếu ứng dụng Flask đang chạy, mã trạng thái HTTP 200 OK sẽ được trả về. Nếu không, mã trạng thái HTTP 503 Service Unavailable sẽ được trả về.
#!/bin/bash

# Assuming your Flask app is running on port 5000
APP_PORT=5000

# Check if the Flask app is responding
curl -Is http://localhost:${APP_PORT} | head -n 1 | grep "200 OK"

# Additional monitoring steps...
