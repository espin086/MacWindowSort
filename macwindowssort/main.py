from config import APPS
from mac_window_sort import windows_sort, close_active_applications


def main():
    close_active_applications()
    for app, position in APPS.items():
        print(app, position)
        windows_sort(app, position)


if __name__ == "__main__":
    main()
