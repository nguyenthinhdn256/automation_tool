import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.run()