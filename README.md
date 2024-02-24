# Smart File Organizer

This script organizes files in a specified directory into categories like documents, images, music, archives, videos, and others, including folders.

## Setup

- Create virtual environment : `python3 -m venv .pyenv`
- Install requirements: `pip install -r requirements.txt`
- Run the script: `python manager.py /path/to/directory`

## Usage

Use the following command to organize files in a directory:

```bash
python manager.py /path/to/directory
```


### `config.py`

Here, we define the file categories and any ignored folders.

```python
CATEGORIES = {
    "a_document": ["application/pdf", "application/msword", "application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"],
    "a_image": ["image/jpeg", "image/png", "image/gif"],
    "a_music": ["audio/mpeg", "audio/x-wav"],
    "a_archive": ["application/zip", "application/x-tar", "application/gzip"],
    "a_video": ["video/mp4", "video/x-msvideo"],
}

IGNORED_FOLDERS = ["a_document", "a_image", "a_music", "a_archive", "a_video", "a_other", "a_folder"]
```

### Report 

A report is printed out at the end of script execution showing all unknown mime types and category copied bytes:

```bash

$ python manager.py ~/toto/

File Organizer Report
Unknown MIME Types:

Total File Sizes by Category:
a_document: 0 bytes
a_image: 0 bytes
a_music: 0 bytes
a_archive: 0 bytes
a_video: 0 bytes
a_other: 0 bytes
```