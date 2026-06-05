# shutil module
# shutil (Shell Utilities) is a built-in Python module that provides
# high-level operations for working with files and directories.
# It offers functions for copying, moving, deleting, archiving,
# and managing files and folders throughout a project's workflow.

# Here is a simple example of an asset management system.
# In this program, assets are organized based on their file formats.
# Texture files are moved to the texture folder,
# audio files are moved to the audio folder,
# and 3D model files are moved to the model folder.

# The program also displays disk storage information,
# including the total, used, and free space available on the system.
# This can help developers monitor storage usage when managing assets.

import shutil
import os

source_folder = "IncomingAssets"

texture_folder = "game_project/assets/texture"
audio_folder = "game_project/assets/audio"
model_folder = "game_project/assets/model"

# Create destination folders if they do not already exist
os.makedirs(texture_folder, exist_ok=True)
os.makedirs(audio_folder, exist_ok=True)
os.makedirs(model_folder, exist_ok=True)

# Organize assets based on their file formats
for asset in os.listdir(source_folder):
    source_path = os.path.join(source_folder, asset)

    if asset.endswith((".png", ".jpg", ".jpeg")):
        destination = os.path.join(texture_folder, asset)
        shutil.move(source_path, destination)
        print(f"Texture imported: {asset}")

    elif asset.endswith((".wav", ".mp3")):
        destination = os.path.join(audio_folder, asset)
        shutil.move(source_path, destination)
        print(f"Audio imported: {asset}")

    elif asset.endswith((".obj", ".fbx")):
        destination = os.path.join(model_folder, asset)
        shutil.move(source_path, destination)
        print(f"Model imported: {asset}")

# Display disk storage information
total, used, free = shutil.disk_usage(".")

print("\nDisk Information")
print(f"Total: {total // (1024 ** 3)} GB")
print(f"Used : {used // (1024 ** 3)} GB")
print(f"Free : {free // (1024 ** 3)} GB")
