# systemchecker
## Yêu cầu cần thiết (cấu hình trong file config.py)
- python3
- redis server: mặc định 127.0.0.1:6379
- 1 API chatbot telegram để gửi cảnh báo
- 1 gmail rác để gửi cảnh báo

## Cài đặt ban đầu:
- Clone toàn bộ về --> Cài đặt gói pip: pip install -r requirment.txt
- Các folder/file có trong file .gitignore có thể bỏ qua không cần clone về. Nếu bạn dự định deploy trên windows thì lấy về cũng được.
- Cho chạy định kỳ file scheduler_check.py bằng taskscheduler/crontab để gọi check host, link. Nếu có cảnh báo, sẽ add nội dung vào redis.
- Cho chạy định kỳ file cron_send.py để lấy các message từ redis và gửi đi qua email và telegram. 

## Note:
Cả 2 file đề có thể chạy độc lập, chạy song song trên nhiều máy khác nhau. Chỉ cần dùng chung redis là OK.

### Mô tả luồng:
update 25/5/2018: crontab chạy file scheduler_check.py. Nếu gặp tình trạng host không kiểm tra được sẽ add notify vào redis. Một tiến trình khác sẽ định kỳ lấy data từ redis ra ngoài để gửi. Các notify nằm trên redis đều có time flag, khi được lấy ra để gửi, nếu thời gian tạo notify đó lớn hơn 60s (con số này nằm trong file cấu hình config.py) sẽ bị reject. Phần worker lấy dữ liệu từ redis chưa có thời gian viết. Sẽ bổ sung sớm.
update 26/5/2018: Bổ sung thêm job lấy dữ liệu notify trong redis ra để gửi cảnh báo qua telegram và email.
