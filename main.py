import sys
from PyQt6.QtWidgets import QApplication
from fyp.view.overall_structure import OverallStructure
from fyp.utils import load_stylesheet



def main():
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    screen = app.primaryScreen()

    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)
    
    
    # Create an instance of your application's main structure/widget
    mainWindow = OverallStructure()
    mainWindow.show()  # Make the main window visible


    # Enter the application's main event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
