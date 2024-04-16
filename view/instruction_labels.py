from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QGraphicsOpacityEffect, QHBoxLayout, QSizePolicy, QSpacerItem
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QPropertyAnimation



class SetupLabel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupInstructions()
        


    def setupInstructions(self):
        self.setup_label_layout = QHBoxLayout(self)
        self.setup_label_layout.setContentsMargins(0, 0, 0, 0)
        
        self.complete_label = QLabel(self)
        self.complete_label.setPixmap(QPixmap('fyp/resources/correct_32.png'))
        self.complete_label.setFixedSize(32, 32)
        self.complete_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.complete_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setup_label_layout.addWidget(self.complete_label)


        self.setup_text_label = QLabel("""  <b><I> Setup:</I></b> Prover computes: <b>y = x² mod N</b>, and sends to verifier.""" )
                                    
        self.setup_text_label.setObjectName("setup_text_label")
        self.setup_label_layout.addWidget(self.setup_text_label)


        self.opacity_effect = QGraphicsOpacityEffect(self.complete_label)
        self.complete_label.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0)

        # Set up the animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(5000)  # Duration of the animation in milliseconds


        self.spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)


    def start(self):
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.start()

    def stop(self):
            self.animation.stop()
            self.opacity_effect.setOpacity(0)


class Step1Label(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupStep1()


    def setupStep1(self):
        self.setup_label1_layout = QHBoxLayout(self)
        self.setup_label1_layout.setContentsMargins(0, 0, 0, 0)

        self.step1_label = QLabel(self)
        self.step1_label.setPixmap(QPixmap('fyp/resources/correct_32.png'))
        self.step1_label.setFixedSize(32, 32)
        self.step1_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.step1_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setup_label1_layout.addWidget(self.step1_label)

        self.step1_text_label = QLabel("""  <b><I> Step 1:</I></b> Prover computes: <b>s = r² mod N</b>, and sends to verifier.""" )

        self.step1_text_label.setObjectName("step1_text_label")
        self.setup_label1_layout.addWidget(self.step1_text_label)


        self.opacity_effect = QGraphicsOpacityEffect(self.step1_label)
        self.step1_label.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0)

        # Set up the animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(5000)  # Duration of the animation in milliseconds


        self.spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)          

  

    def start(self):
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.start()

    def stop(self):
            self.animation.stop()
            self.opacity_effect.setOpacity(0)
            


class  Step2Label(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupStep2()

    def setupStep2(self):
        self.setup_setup2_layout = QHBoxLayout(self)
        self.setup_setup2_layout.setContentsMargins(0, 0, 0, 0)

        self.step2_label = QLabel(self)
        self.step2_label.setPixmap(QPixmap('fyp/resources/correct_32.png'))
        self.step2_label.setFixedSize(32, 32)
        self.step2_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.step2_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setup_setup2_layout.addWidget(self.step2_label)

        self.step2_text_label = QLabel("""  <b><I> Step 2:</I></b> Verifier Chooses: <b>bit 1</b>, or <b>bit 0</b>, chosen randomly.""" )

        self.step2_text_label.setObjectName("step2_text_label")
        self.setup_setup2_layout.addWidget(self.step2_text_label)


        self.opacity_effect = QGraphicsOpacityEffect(self.step2_label)
        self.step2_label.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0)

        # Set up the animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(5000)



    def start(self):
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.start()

    def stop(self):
            self.animation.stop()
            self.opacity_effect.setOpacity(0)


class Step3Label(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupStep3()

    def setupStep3(self):
        self.setup_setup3_layout = QHBoxLayout(self)
        self.setup_setup3_layout.setContentsMargins(0, 0, 0, 0)

        self.step3_label = QLabel(self)
        self.step3_label.setPixmap(QPixmap('fyp/resources/correct_32.png'))
        self.step3_label.setFixedSize(32, 32)
        self.step3_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.step3_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setup_setup3_layout.addWidget(self.step3_label)

        self.step3_text_label = QLabel("""  <b><I> Step 3:</I></b> Verifier checks: If result passes, continue to next round.""" )

        self.step3_text_label.setObjectName("step3_text_label")
        self.setup_setup3_layout.addWidget(self.step3_text_label)

        self.opacity_effect = QGraphicsOpacityEffect(self.step3_label)
        self.step3_label.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0)

        # Set up the animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(5000)



    def start(self):
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.start()

    def stop(self):
            self.animation.stop()
            self.opacity_effect.setOpacity(0)