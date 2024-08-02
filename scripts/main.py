from App import App
from Config import Constants, Images

if __name__ == '__main__':
    App.start_app(App((Constants.WIDTH_WINDOW, Constants.HEIGHT_WINDOW), Constants.TITLE_WINDOW, Images.ICON_WINDOW))