
library(fs)
library(dplyr)

# Định nghĩa hàm đếm số lượng ảnh trong thư mục
count_files <- function(path) {
  fs::dir_tree(path, recurse = TRUE) %>% 
    purrr::keep(fs::is_file) %>%  # Giữ lại chỉ các file (không phải thư mục)
    length() %>%  # Đếm số lượng file
    dplyr::tibble(n_files = .)  # Chuyển kết quả thành tibble
}

# Đường dẫn tới thư mục Sleepy và Normal
path_sleepy <- "C:/Users/DELL/Downloads/DATA for PROJECT/Train/Sleepy"
path_normal <- "C:/Users/DELL/Downloads/DATA for PROJECT/Train/Normal"

# Đếm số lượng ảnh trong thư mục Sleepy và Normal
sleepy_count <- count_files(path_sleepy)
normal_count <- count_files(path_normal)

# Hiển thị số lượng ảnh trong từng nhóm
cat("Number of images in Sleepy category:", sleepy_count$n_files, "\n")
cat("Number of images in Normal category:", normal_count$n_files, "\n")

# Tạo biểu đồ cột để so sánh số lượng ảnh trong từng nhóm
barplot(c(sleepy_count$n_files, normal_count$n_files), 
        names.arg = c("Sleepy", "Normal"),
        xlab = "Category",
        ylab = "Number of Images",
        main = "Number of Images in Sleepy and Normal Categories",
        col = c("blue", "green"),
        ylim = c(0, max(sleepy_count$n_files, normal_count$n_files) + 10))

# Tính tỷ lệ số lượng ảnh trong từng nhóm so với tổng số lượng ảnh
total_images <- sum(sleepy_count$n_files, normal_count$n_files)
sleepy_percentage <- sleepy_count$n_files / total_images * 100
normal_percentage <- normal_count$n_files / total_images * 100

# Hiển thị tỷ lệ
cat("Percentage of images in Sleepy category:", sleepy_percentage, "%\n")
cat("Percentage of images in Normal category:", normal_percentage, "%\n")

# Thực hiện kiểm định thống kê (nếu cần)
# Ví dụ: Kiểm định t tham số đôi
t.test(sleepy_count$n_files, normal_count$n_files)
