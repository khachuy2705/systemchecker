# systemchecker
## Yêu cầu cần thiết (cấu hình trong file config.py)
- python3
- redis server: mặc định 127.0.0.1:6379
- 1 API chatbot telegram để gửi cảnh báo
- 1 gmail rác để gửi cảnh báo

## Cài đặt ban đầu:
- Clone toàn bộ về --> Cài đặt gói pip: pip install -r requirment.txt
- Cho chạy định kỳ file notify_checker.py bằng taskscheduler/crontab

### Mô tả luồng:
update 25/5/2018: crontab chạy file scheduler_check.py. Nếu gặp tình trạng host không kiểm tra được sẽ add notify vào redis. Một tiến trình khác sẽ định kỳ lấy data từ redis ra ngoài để gửi. Các notify nằm trên redis đều có time flag, khi được lấy ra để gửi, nếu thời gian tạo notify đó lớn hơn 60s (con số này nằm trong file cấu hình config.py) sẽ bị reject. Phần worker lấy dữ liệu từ redis chưa có thời gian viết. Sẽ bổ sung sớm.
