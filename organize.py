import os
from pathlib import Path

SUBDIRECTORIES = {
    "Documents": ['.pdf','.rtf','.txt'],
    "Audio":['.m4a','.m4b','.mp3'],
    "Videos": ['.mov','.avi','.mp4'],
    "Photos": ['.jpg','.jpeg','.png']
}
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'Others' #If filetype doesn't exist in our dictionary

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()