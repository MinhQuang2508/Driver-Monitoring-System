import os

def rename_and_move_images(source_folder, destination_folder):
    # Tạo thư mục đích nếu nó không tồn tại
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Lấy danh sách tất cả các tệp tin trong thư mục nguồn
    image_files = [file for file in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, file))]

    # Biến số thứ tự
    index = 1
    
    # Lặp qua từng tệp tin
    for file_name in image_files:
        # Lấy đường dẫn đến tệp tin
        old_file_path = os.path.join(source_folder, file_name)
        
        # Kiểm tra nếu tệp tin là hình ảnh
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Tạo tên mới cho tệp tin
            new_file_name = f"Normal_{index}.jpg"
            new_file_path = os.path.join(destination_folder, new_file_name)
            
            # Di chuyển và đổi tên tệp tin
            os.rename(old_file_path, new_file_path)
            
            # Tăng biến số thứ tự cho tệp tin tiếp theo
            index += 1

# Thư mục nguồn chứa các tệp tin cần được đổi tên và di chuyển
source_folder = r'D:\data_TA\YawDD dataset\Dash\cầnchuyenten'
# Thư mục đích để lưu các tệp tin đã được đổi tên
destination_folder = r'D:\data_TA\YawDD dataset\Dash\Normal'

# Gọi hàm để đổi tên và di chuyển các tệp tin
rename_and_move_images(source_folder, destination_folder)
