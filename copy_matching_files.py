from pathlib import Path
import shutil

def copy_matching_files(src_folder, dest_folder, match_folder):
    # Create the destination directory if it doesn't exist
    dest_folder.mkdir(parents=True, exist_ok=True)

    # Create a set of jpeg file names
    jpeg_files = {f.stem for f in match_folder.iterdir() if f.is_file() and f.name != '.DS_Store'}

    # Copy matching files from the source folder to the destination folder
    for src_file in src_folder.iterdir():
        if src_file.is_file() and src_file.name != '.DS_Store':
            if src_file.stem in jpeg_files:
                dest_file = dest_folder / src_file.name
                shutil.copy2(src_file, dest_file)
                print(f'Copying {src_file.name} to the destination folder.')

if __name__ == "__main__":
    # Your paths
    raw_path = Path('/Users/rubens/Desktop/Photos')
    destination_path = raw_path / 'RAW Selected'
    jpeg_path = raw_path / 'JPEG selected'

    copy_matching_files(raw_path, destination_path, jpeg_path)
