from PyQt6.QtCore import QFile, QTextStream

def load_stylesheet():
    # Define the path to your stylesheet within the function
    # Update this path to match your project structure and where your QSS file is located
    path = "fyp/view/styles.qss" 

    # Now everything related to loading the stylesheet is within this function
    file = QFile(path)
    if not file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
        print(f"Failed to open the stylesheet file at path: {path}")
        return ""

    stream = QTextStream(file)
    stylesheet = stream.readAll()
    file.close()  # Make sure to close the QFile
    return stylesheet
