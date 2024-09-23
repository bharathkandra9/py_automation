import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# set paths for Downloads and books folder
downloads_folder = os.path.expanduser("~/Downloads")
books_folder = os.path.expanduser("~/books")


class MoveEpubHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # check for epub files
        for filename in os.listdir(downloads_folder):
            if filename.endswith(".epub"):
                src_path = os.path.join(downloads_folder, filename)
                dest_path = os.path.join(books_folder, filename)
                shutil.move(src_path, dest_path)
                print(f"Moved: {filename} to {books_folder}")


# set up event handler and Observer
event_handler = MoveEpubHandler()
observer = Observer()
observer.schedule(event_handler, downloads_folder, recursive=False)

# start monitoring
observer.start()
print(f"monitoring {downloads_folder} for new EPUB files ..")

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
