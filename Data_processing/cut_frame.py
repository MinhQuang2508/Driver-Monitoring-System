import cv2
import os

def extract_frames(video_path, output_folder):
    # Kiểm tra xem thư mục đầu ra đã tồn tại chưa
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Tạo tên thư mục con dựa trên tên video (loại bỏ phần mở rộng)
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    video_subfolder = os.path.join(output_folder, video_name)

    # Kiểm tra xem thư mục con đã tồn tại chưa
    if not os.path.exists(video_subfolder):
        os.makedirs(video_subfolder)

    # Đọc video từ đường dẫn
    cap = cv2.VideoCapture(video_path)

    # Kiểm tra xem video có hợp lệ không
    if not cap.isOpened():
        print("Không thể mở video.")
        return

    # Đọc các khung hình từ video và lưu thành ảnh
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Lưu ảnh vào thư mục con của video
        frame_name = f"frame_{frame_count:04d}.jpg"
        frame_path = os.path.join(video_subfolder, frame_name)
        cv2.imwrite(frame_path, frame)

        frame_count += 1

    # Đóng video capture
    cap.release()

# Thực hiện cắt hình ảnh từ video .avi
video_path = r"D:\data_TA\YawDD dataset\Dash\Female\9-FemaleNoGlasses.avi"
output_folder = r"D:\data_TA\YawDD dataset\Dash\Female"
extract_frames(video_path, output_folder)
