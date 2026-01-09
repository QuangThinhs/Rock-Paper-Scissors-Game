```plaintext
 Online Rock-Paper-Scissors (RPS) Multiplayer Engine
Hệ thống trò chơi Kéo-Búa-Bao trực tuyến dựa trên lập trình Socket, hỗ trợ đa người chơi kết nối đồng thời, tích hợp xác thực tài khoản và lưu trữ dữ liệu tập trung.
________________________________________
 Mục lục
1.	Kiến trúc hệ thống
2.	Tính năng chính
3.	Công nghệ sử dụng
4.	Đặc tả giao thức mạng (Protocol)
5.	Cấu trúc cơ sở dữ liệu
6.	Hướng dẫn cài đặt
7.	Phân công nhân sự
________________________________________
 Kiến trúc hệ thống
Dự án tuân thủ mô hình Centralized Server (Máy chủ tập trung). Server đóng vai trò là thực thể duy nhất có quyền quyết định (Authority), đảm bảo tính công bằng và chống gian lận.
•	Server-side: Xử lý đa luồng (Threading) để quản lý hàng nghìn kết nối đồng thời. Mỗi Client được phục vụ bởi một Thread riêng biệt.
•	Client-side: Giao diện đồ họa (GUI) tương tác người dùng, gửi tín hiệu điều khiển và nhận phản hồi trạng thái từ Server.
•	Database: Hệ quản trị cơ sở dữ liệu MySQL (thông qua XAMPP) lưu trữ định danh người dùng và lịch sử đấu.
________________________________________
 Tính năng chính
•	Authentication: Đăng ký/Đăng nhập tài khoản bảo mật.
•	Real-time Matchmaking: Hệ thống hàng đợi tự động ghép cặp 2 người chơi vào một phòng đấu (Room).
•	Game Logic Engine: Xử lý phân định thắng thua, hòa và xử lý các trường hợp ngoại lệ (người chơi ngắt kết nối đột ngột).
•	Leaderboard: Bảng xếp hạng thời gian thực dựa trên tỉ lệ thắng.
•	Chat System: Nhắn tin trong phòng chờ và trong trận đấu.
________________________________________
 Công nghệ sử dụng
•	Ngôn ngữ chính: Python 3.9+
•	Networking: Thư viện socket (TCP/IP Protocol).
•	Concurrency: Thư viện threading.
•	Database Interface: mysql-connector-python.
•	GUI Framework: Tkinter hoặc Pygame.
•	Data Serialization: JSON (để đóng gói gói tin chuyên nghiệp).
________________________________________
 Đặc tả giao thức mạng (Protocol)
Hệ thống sử dụng định dạng dữ liệu JSON để truyền tải thông tin giữa Client và Server nhằm đảm bảo khả năng mở rộng.
Header (Type)	Mô tả dữ liệu gửi đi	Phản hồi từ đối phương
AUTH_LOGIN	{"user": "abc", "pass": "123"}	{"status": "success", "user_id": 1}
MATCH_FIND	{"action": "join_queue"}	{"status": "matched", "opponent": "xyz"}
GAME_MOVE	{"choice": "ROCK"}	{"result": "WIN", "opp_choice": "SCISSORS"}
CHAT_MSG	{"msg": "Hello world!"}	Broadcast cho người chơi cùng phòng
________________________________________
 Cấu trúc cơ sở dữ liệu
1. Bảng users
Column	Type	Description
id	INT (PK)	Định danh duy nhất
username	VARCHAR(50)	Tên đăng nhập (Unique)
password	VARCHAR(255)	Mật khẩu (Encrypted)
elo	INT	Điểm xếp hạng
2. Bảng match_history
Column	Type	Description
match_id	INT (PK)	Mã trận đấu
player1_id	INT (FK)	ID người chơi 1
player2_id	INT (FK)	ID người chơi 2
winner_id	INT	ID người thắng
________________________________________
 Cấu trúc dự án (Project Structure)
Plaintext
RPS-Project/
├── server/
│   ├── core.py           # Khởi tạo Socket, lắng nghe kết nối
│   ├── handlers.py       # Xử lý logic game và matchmaking
│   └── database.py       # CRUD operations với MySQL
├── client/
│   ├── app.py            # Điểm khởi đầu ứng dụng Client
│   ├── network.py        # Module gửi/nhận dữ liệu từ Server
│   └── ui/               # Chứa các màn hình giao diện (Login, Game, Lobby)
├── shared/
│   └── constants.py      # Chứa Port, IP, các mã lệnh Protocol
└── assets/               # Hình ảnh, âm thanh sử dụng trong game
________________________________________
⚙️ Hướng dẫn cài đặt
1.	Database: Mở XAMPP, tạo DB rps_db và chạy script SQL đính kèm trong thư mục database/.
2.	Cài đặt thư viện:
Bash
pip install mysql-connector-python
3.	Chạy Server: Chạy python server/core.py trên máy chủ.
4.	Chạy Client: Chạy python client/app.py trên các máy khách cùng mạng Wi-Fi.
________________________________________
👥 Phân công nhân sự
•	Leader: Thiết kế hệ thống, lập trình Server Core, Quản lý tiến độ.
•	Dev 1 (Network): Lập trình Module Socket Client, xử lý Protocol JSON.
•	Dev 2 (UI/UX): Thiết kế giao diện đồ họa, xử lý sự kiện nút bấm.
•	Dev 3 (Database): Thiết kế SQL, viết module kết nối Python-MySQL qua XAMPP.
________________________________________
Lưu ý: Mọi thay đổi về Protocol phải được Leader thông qua trước khi cập nhật vào mã nguồn chính.