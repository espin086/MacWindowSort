from config import APPS
from mac_window_sort import windows_sort


for app, position in APPS.items():
    print(app, position)
    windows_sort(app, position)
