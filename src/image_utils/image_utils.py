import os

from PyQt5.QtGui import QIcon


def create_qicon_from_filename(filename:str) -> QIcon:
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    image_path = os.path.join("image", filename)
    return QIcon(os.path.join(parent_dir, image_path))