1.tạo môi trường venv:
py -3 -m venv venv

2.chọn trình biên dịch python bên trong venv

3.mở tab cmd mới, chạy lệnh bên dưới để dự án chạy trong môi trường venv:
venv\Scripts\activate.bat

4.trong (venv)cmd chạy lệnh bên dưới để cài đặt các thư viện có trong file requirements.txt:
pip install -r requirements.txt

5.bật database trong docker (nếu dùng database docker)

6.trong (venv)cmd chạy lệnh bên dưới để run dự án:
uvicorn app.main:app --reload

7.nếu cài thêm thư viện mới thì chạy lệnh bên dưới để cập nhật lại file requirements.txt:
pip freeze > requirements.txt
