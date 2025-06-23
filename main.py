from utils.updater import check_for_update
from tray import setup_tray

def main():
    check_for_update()
    setup_tray()

if __name__ == "__main__":
    main()
