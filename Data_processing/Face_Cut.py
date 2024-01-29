import os
import cv2
import face_recognition

def detect_and_crop_faces(input_folder, output_folder):
    # Tạo thư mục đầu ra nếu nó không tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lặp qua tất cả các tệp trong thư mục đầu vào
    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        # Đọc ảnh từ tệp đầu vào
        image = cv2.imread(input_path)

        # Tìm khuôn mặt trong ảnh
        face_locations = face_recognition.face_locations(image)

        # Lặp qua tất cả các khuôn mặt được tìm thấy và cắt ảnh
        for face_location in face_locations:
            top, right, bottom, left = face_location

            # Cắt ảnh theo bounding box của khuôn mặt
            face_image = image[top:bottom, left:right]

            # Lưu ảnh khuôn mặt vào thư mục đầu ra
            cv2.imwrite(output_path, face_image)

if __name__ == "__main__":
    input_folder = r"D:\data_TA\YawDD dataset\Dash\Male\14-MaleNoGlasses"
    output_folder = r"D:\data_TA\YawDD dataset\Dash\Male\FACE-14-MaleNoGlasses"

    detect_and_crop_faces(input_folder, output_folder)
