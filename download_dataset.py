import kagglehub
import os

# Download dataset from Kaggle
path = kagglehub.dataset_download(
    "shivamb/real-or-fake-fake-jobposting-prediction"
)

print("Dataset downloaded successfully!")
print("Dataset location:", path)

# Display downloaded files
for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))
