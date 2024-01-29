import cv2
import numpy as np
import os
import joblib
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt
import random

test_eye_open_dir = r'E:\SVM_classify\data\test\normal'
test_eye_closed_dir = r'E:\SVM_classify\data\test\sleep'

X_test, y_test = [], []

for filename in os.listdir(test_eye_open_dir):
    img = cv2.imread(os.path.join(test_eye_open_dir, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (80, 80))
    img_1d = img.flatten() / 255
    X_test.append(img_1d)
    y_test.append(1)

for filename in os.listdir(test_eye_closed_dir):
    img = cv2.imread(os.path.join(test_eye_closed_dir, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (80, 80))
    img_1d = img.flatten() / 255
    X_test.append(img_1d)
    y_test.append(0)

X_test = np.array(X_test)
y_test = np.array(y_test)

clf = joblib.load('svm_model125.plk')

predictions = clf.predict(X_test)
accuracy = np.mean(predictions == y_test)

precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

conf_mat = confusion_matrix(y_test, predictions)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', ax=axes[0, 0])
axes[0, 0].set_xlabel('Predicted')
axes[0, 0].set_ylabel('Actual')
axes[0, 0].set_title('Confusion Matrix')

axes[0, 1].bar(['Precision'], [precision], color='skyblue')
axes[0, 1].set_title('Precision')

axes[1, 0].bar(['Recall'], [recall], color='lightgreen')
axes[1, 0].set_title('Recall')

axes[1, 1].bar(['F1 Score'], [f1], color='lightcoral')
axes[1, 1].set_title('F1 Score')

plt.tight_layout()

# Function to display random images
def display_random_images(X_test, y_test, predictions, num_images=10):
    indices = random.sample(range(len(X_test)), num_images)

    fig, axes = plt.subplots(2, 5, figsize=(15, 8))
    fig.suptitle('Random Images from Test Set', fontsize=16)

    for i, idx in enumerate(indices):
        img = X_test[idx].reshape((80, 80))
        true_label = 'Open' if y_test[idx] == 1 else 'Closed'
        pred_label = 'Open' if predictions[idx] == 1 else 'Closed'

        axes[i // 5, i % 5].imshow(img, cmap='gray')
        axes[i // 5, i % 5].axis('off')
        axes[i // 5, i % 5].set_title(f'True: {true_label}\nPred: {pred_label}')

    plt.show()

# Display random images from the test set
display_random_images(X_test, y_test, predictions)

plt.show()

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
