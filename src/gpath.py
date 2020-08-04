import os

GLOBAL_SETTING_PATH = os.path.abspath(os.path.dirname(__file__))
PATH_ASSETS = os.path.join(GLOBAL_SETTING_PATH, "assets/")  # src folder
PATH_SRC = os.path.join(GLOBAL_SETTING_PATH, "/")

PATH_MAP = os.path.join(GLOBAL_SETTING_PATH, "maps/")

PATH_IMAGE = PATH_ASSETS + "image/"
PATH_BACKGROUND = PATH_ASSETS + "background/"
PATH_SOUND = PATH_ASSETS + "sound/"
PATH_SPIRE = PATH_ASSETS + "sprite/"

GAME_ICON = PATH_IMAGE + "icon.png"

if __name__ == "__main__":
    print(PATH_ASSETS)
