import os
import shutil
import magic
from config import CATEGORIES, IGNORED_FOLDERS

class FileOrganizer:
    def __init__(self, path):
        self.path = path
        self.unknown_mimetypes = set()
        self.category_sizes = {category: 0 for category in CATEGORIES.keys()}
        self.category_sizes["a_other"] = 0  # Include 'a_other' in size tracking

    def organize(self):
        """
        Organize files in the given directory path by moving them to their respective categories
        """
        for item in os.listdir(self.path):
            item_path = os.path.join(self.path, item)
            if os.path.isdir(item_path):
                if item in IGNORED_FOLDERS:
                    continue
                self.move_item(item_path, "a_folder")
            else:
                category = self.get_category(item_path)
                self.move_item(item_path, category)
                self.update_size(item_path, category)
        self.generate_report()

    def get_category(self, item_path):
        """
        Get the category of the given file path based on its MIME type
        """
        filetype = magic.from_file(item_path, mime=True)
        for category, types in CATEGORIES.items():
            if filetype in types:
                return category
        self.unknown_mimetypes.add(filetype)
        return "a_other"

    def move_item(self, item_path, category):
        """
        Move the given item to the destination category
        """
        destination = os.path.join(self.path, category)
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.move(item_path, destination)

    def update_size(self, item_path, category):
        """
        Update the size of the given item to the category size
        """
        self.category_sizes[category] += os.path.getsize(item_path)

    def generate_report(self):
        """
        Generate a report of unknown MIME types and total file sizes by category
        """
        print("File Organizer Report")
        print("Unknown MIME Types:")
        for mimetype in self.unknown_mimetypes:
            print(f"- {mimetype}")
        print("\nTotal File Sizes by Category:")
        for category, size in self.category_sizes.items():
            print(f"{category}: {size} bytes")
