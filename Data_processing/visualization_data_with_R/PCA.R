
library(jpeg)
library(pracma)
library(ggplot2)

# Function to read and preprocess images
read_and_preprocess_images <- function(folder_path, class_label) {
  file_list <- list.files(folder_path, pattern = ".jpg", full.names = TRUE)
  images <- lapply(file_list, function(file) {
    img <- readJPEG(file)
    img_vector <- as.vector(img)
    data.frame(img = img_vector, class = class_label)
  })
  do.call(rbind, images)
}

# Set your folder paths for normal and Sleepy images
normal_folder <- "C:/Users/DELL/Downloads/DATA for PROJECT/Train/Normal"
sleepy_folder <- "C:/Users/DELL/Downloads/DATA for PROJECT/Train/Sleepy"

# Read and preprocess images
normal_images <- read_and_preprocess_images(normal_folder, "normal")
sleepy_images <- read_and_preprocess_images(sleepy_folder, "Sleepy")

# Combine normal and Sleepy images
all_images <- rbind(normal_images, sleepy_images)

# Extract features (pixel values) and labels
features <- as.matrix(all_images[, -ncol(all_images)])
labels <- all_images$class

# Perform PCA
pca_result <- prcomp(features, center = TRUE, scale. = TRUE)

# Extract principal components
pc_data <- data.frame(labels, pca_result$x[, 1:2])

# Plot the PCA results
pca_plot <-ggplot(pc_data, aes(x = PC1, y = PC2, color = labels)) +
  geom_point() +
  labs(title = "PCA on Sleepy and Normal Images")
plot(pca_plot)