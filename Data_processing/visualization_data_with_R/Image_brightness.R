library(fs)
library(dplyr)
library(ggplot2)
library(imager)

# Định nghĩa hàm brightness_histogram
brightness_histogram <- function(path) {
  # Lấy danh sách tất cả các file trong thư mục
  all_files <- fs::dir_ls(path, recurse = TRUE)
  
  # Đọc các file ảnh và tính độ sáng
  brightness_values <- sapply(all_files, function(file) {
    img <- imager::load.image(file)  # Sử dụng load.image để đọc ảnh
    mean(img)  # Tính độ sáng trung bình của ảnh
  })
  
  # Tạo dataframe từ các giá trị độ sáng
  df <- data.frame(brightness = brightness_values)
  
  # Tạo histogram
  ggplot(df, aes(x = brightness)) +
    geom_histogram(binwidth = 0.01, fill = "blue", color = "black") +
    labs(title = "Brightness Histogram", x = "Brightness", y = "Frequency")
}

# Đường dẫn tới thư mục Sleepy và Normal
path_sleepy <- "C:/Users/DELL/Downloads/DATA for PROJECT/Train/Sleepy"
path_normal <- "C:/Users/DELL/Downloads/DATA for PROJECT/Train/Normal"

# Trực quan hóa độ sáng của thư mục Sleepy
sleepy_histogram <- brightness_histogram(path_sleepy)
sleepy_histogram

# Trực quan hóa độ sáng của thư mục Normal
normal_histogram <- brightness_histogram(path_normal)
normal_histogram

print(sleepy_histogram)
print(normal_histogram)
