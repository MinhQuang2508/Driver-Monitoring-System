import os
import shutil

def merge_image_folders(source_dir, destination_dir):
    # Tạo thư mục đích nếu nó không tồn tại
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Biến số thứ tự để đặt tên chung cho các tệp tin hình ảnh
    index = 1

    # Lặp qua các thư mục con trong thư mục nguồn
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Kiểm tra nếu tệp tin là hình ảnh
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                source_path = os.path.join(root, file)
                # Đặt tên mới cho tệp tin đích
                destination_file_name = f'Normal_{index}.jpg'  # Thay đổi phần mở rộng nếu cần
                destination_path = os.path.join(destination_dir, destination_file_name)
                # Di chuyển hình ảnh vào thư mục đích với tên mới
                shutil.move(source_path, destination_path)
                # Tăng biến số thứ tự cho tệp tin tiếp theo
                index += 1

# Thư mục nguồn chứa các thư mục con chứa hình ảnh
source_directory = r'C:\Users\admin\Desktop\Normal'
# Thư mục đích để gộp tất cả các hình ảnh vào
destination_directory = r'D:\data_TA\YawDD dataset\Dash\Normal'

# Gộp hình ảnh từ các thư mục con vào thư mục đích
merge_image_folders(source_directory, destination_directory)
