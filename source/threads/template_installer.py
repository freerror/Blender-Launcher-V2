from pathlib import Path
from re import match
from shutil import copytree

from modules.settings import get_library_folder
from PyQt5.QtCore import QThread, pyqtSignal


class TemplateInstaller(QThread):
    started = pyqtSignal()
    progress_changed = pyqtSignal("PyQt_PyObject", "PyQt_PyObject")
    finished = pyqtSignal()

    def __init__(self, manager, dist):
        QThread.__init__(self)
        self.manager = manager
        self.dist = dist

    def run(self):
        self.progress_changed.emit(0, "Copying Data...")
        library_folder = Path(get_library_folder())
        template = library_folder / "template"

        if not template.is_dir():
            template.mkdir()

        for directory in self.dist.iterdir():
            if match(r"\d+\.\d+.*", directory.name) is not None:
                source = template.as_posix()
                dist = directory.as_posix()
                copytree(source, dist, dirs_exist_ok=True)
                self.finished.emit()
                return

        self.finished.emit()
        return
