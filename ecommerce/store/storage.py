import os
from django.core.files.storage import FileSystemStorage

class NonLockingFileSystemStorage(FileSystemStorage):
    def _save(self, name, content):
        # Get the proper name for the file
        full_path = self.path(name)

        # Create any intermediate directories that do not exist
        directory = os.path.dirname(full_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Save the file without using file locking
        with open(full_path, 'wb') as f:
            for chunk in content.chunks():
                f.write(chunk)
        
        return name
