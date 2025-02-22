from pathlib import Path

from modules._platform import get_platform
from modules.settings import get_library_folder
from PyQt5.QtCore import QThread, pyqtSignal


class LibraryDrawer(QThread):
    build_found = pyqtSignal("PyQt_PyObject")
    finished = pyqtSignal()
    build_released = pyqtSignal()

    def __init__(self, folders=("stable", "daily", "experimental", "custom")):
        QThread.__init__(self)
        self.folders = folders
        self.builds_count = 0
        self.build_released.connect(self.handle_build_released)

    def run(self):
        library_folder = Path(get_library_folder())
        platform = get_platform()

        if platform == "Windows":
            blender_exe = "blender.exe"
        elif platform == "Linux":
            blender_exe = "blender"
        elif platform == "macOS":
            blender_exe = "Blender/Blender.app/Contents/MacOS/Blender"

        for folder in self.folders:
            path = library_folder / folder

            if path.is_dir():
                for build in path.iterdir():
                    if (path / build / blender_exe).is_file():
                        self.builds_count = self.builds_count + 1
                        self.build_found.emit(folder / build)

                        # Limit build info reader threads to 5
                        while self.builds_count > 4:
                            QThread.msleep(250)

        # Wait until all builds are drawn on screen
        while self.builds_count > 0:
            QThread.msleep(250)

        self.finished.emit()

    def handle_build_released(self):
        self.builds_count = self.builds_count - 1
