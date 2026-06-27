import argparse
import os

# command line parser
parser = argparse.ArgumentParser(
    description="Game Texture Asset Organizer"
)

parser.add_argument(
    "folder",
    help="Folder containing texture files"
)

args = parser.parse_args()

# validate folder exists before doing anything
if not os.path.isdir(args.folder):
    print(f"\nError: folder '{args.folder}' not found.")
    print("Please check the path and try again.")
    exit(1)

# supported texture formats
texture_formats = [".png", ".jpg", ".jpeg"]

print("\nScanning Folder:", args.folder)
print("-" * 40)

total_files = 0

# scan all files
for filename in os.listdir(args.folder):

    file_path = os.path.join(args.folder, filename)

    # check extension
    if os.path.isfile(file_path):

        name, extension = os.path.splitext(filename)

        if extension.lower() in texture_formats:

            total_files += 1

            # convert to game-engine friendly format
            # (lowercase + underscores — name normalization only,
            #  not pixel compression or format conversion)
            new_name = (
                name.lower()
                .replace(" ", "_")
                + extension.lower()
            )

            new_path = os.path.join(
                args.folder,
                new_name
            )

            # rename file
            os.rename(file_path, new_path)

            print(f"Processed:  {filename}")
            print(f"Renamed To: {new_name}\n")

print("-" * 40)
print("Total Texture Files Processed:", total_files)