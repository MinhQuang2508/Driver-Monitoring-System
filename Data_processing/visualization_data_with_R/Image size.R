
library(jpeg)

# Đường dẫn đến thư mục chứa ảnh
folder_path <- "C:/Users/DELL/Downloads/DATA for PROJECT/Train/Normal"

# Danh sách các file ảnh trong thư mục
image_files <- list.files(folder_path, pattern = ".jpg", full.names = TRUE)

# Tạo một data frame để lưu kích thước của ảnh
image_dimensions <- data.frame(File = character(), Width = numeric(), Height = numeric(), stringsAsFactors = FALSE)

# Lặp qua từng file ảnh
for (file_path in image_files) {
  # Đọc ảnh
  img <- readJPEG(file_path, native = TRUE)
  
  # Lấy kích thước của ảnh
  width <- dim(img)[2]
  height <- dim(img)[1]
  
  # Thêm thông tin vào data frame
  image_dimensions <- rbind(image_dimensions, data.frame(File = file_path, Width = width, Height = height))
}

# In ra kết quả
print(image_dimensions)
