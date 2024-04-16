 
from PyQt6.QtWidgets import  QWidget,  QLabel, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from fyp.view.animate_arrow import AnimateArrow
from fyp.view.animate_label import LabelAnimator
from fyp.view.trust_meter import TrustMeter
from fyp.view.iteration_labels import IterationLabels
from fyp.view.instruction_labels import SetupLabel, Step1Label, Step2Label, Step3Label
from fyp.presenter.animation_presenter import AnimationPresenter


 
 
 
class ZeroKnowledge(QWidget):
    def __init__(self):
        super().__init__()

        self.animation_presenter = AnimationPresenter()
        
        
        self.setupTitle()    

        self.setupIterationDetails()
        
        self.setupTrustMeter()
        
        self.initSetupLabel()
        self.initStep1Label()        
        self.initStep2Label()
        self.initStep3Label()
        
        self.setupAnimation()
        #self.setupConnections()
        
       
        self.setupButton()
        
        self.setupLayouts()
        
        


    def setupLayouts(self):
        self.overall_layout = QVBoxLayout(self)
        self.animation_horizontal_layout = QHBoxLayout()

        self.overall_layout.addWidget(self.title_label)

        # Add Iteration details
        self.overall_layout.addWidget(self.iterationDetails)

        self.setupSpacer(20,25)
        #setupAnimation
        self.animation_horizontal_layout.addWidget(self.prover_label)
        self.animation_horizontal_layout.addWidget(self.arrow_widget)
        self.animation_horizontal_layout.addWidget(self.verifier_label)
        self.overall_layout.addLayout(self.animation_horizontal_layout)
        
        self.setupSpacer(20,25)

        # Trust meter
        self.overall_layout.addWidget(self.label_trust_meter)
        self.overall_layout.addWidget(self.trust_meter)
        

        self.setupSpacer(20,5)

        # Setup 
        self.overall_layout.addWidget(self.instruction_labels)
        self.overall_layout.addWidget(self.setup_label2)

        # Step1
        self.overall_layout.addWidget(self.step1_labels)
        self.overall_layout.addWidget(self.step1_label2)

        # Step2
        self.overall_layout.addWidget(self.step2_labels)
        self.overall_layout.addWidget(self.step2_label2)
        self.overall_layout.addWidget(self.step2_label3)
        
        # Step3
        self.overall_layout.addWidget(self.step3_labels)
        self.overall_layout.addWidget(self.step3_label2)
        self.overall_layout.addWidget(self.step3_label3)
        self.setupSpacer(20,15)

        # SetupButton
        self.overall_layout.addWidget(self.toggle_glow_button)



        

    def setupTrustMeter(self):
        self.trust_meter = TrustMeter()

        self.label_trust_meter = QLabel("Trust Meter")
        self.label_trust_meter.setObjectName("label_trust_meter")
        self.label_trust_meter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

    def setupConnections(self):
        #self.animation_presenter = AnimationPresenter()
        self.animation_presenter.iterationUpdated.connect(self.iterationDetails.updateIterationLabel)  # Connect signal to slot
        self.animation_presenter.certaintyUpdated.connect(self.iterationDetails.updateCertaintyLabel)
        self.animation_presenter.percentageUpdated.connect(self.trust_meter.updateTrustLevel)
        #self.animation_presenter.updateYValue.connect(self.instruction_labels.updateLabel2)

        # LETTERS TO UPDATE VALUES, Digit to update based in click

        # STEP 0
        self.animation_presenter.countUpdated0.connect(self.instruction_labels.start)
        self.animation_presenter.countUpdated0.connect(self.arrow_widget.startTopArrowAnimation)
        
        self.animation_presenter.updateYValue.connect(self.topLabelAnimator0.start)
        self.animation_presenter.updateYValue.connect(self.updateSetupLabel) # happens at 0
        self.animation_presenter.updateYValue.connect(self.updateTopAnimationYValue)
        

        # STEP 1
        self.animation_presenter.countUpdated1.connect(self.step1_labels.start)
        self.animation_presenter.countUpdated1.connect(self.arrow_widget.startTopArrowAnimation)

        self.animation_presenter.updateSValue.connect(self.topLabelAnimator0.stop)
        self.animation_presenter.updateSValue.connect(self.topLabelAnimator1.start)
        self.animation_presenter.updateSValue.connect(self.updateStep1Label)
        self.animation_presenter.updateSValue.connect(self.updateTopAnimationSValue)


        # STEP 2
        self.animation_presenter.countUpdated2.connect(self.arrow_widget.stopTopArrowAnimation)
        self.animation_presenter.countUpdated2.connect(self.arrow_widget.startBottomArrowAnimation)
        self.animation_presenter.countUpdated2.connect(self.step2_labels.start)

        self.animation_presenter.updateBValue.connect(self.updateStep2Label)
        self.animation_presenter.updateBValue.connect(self.topLabelAnimator1.stop)
        self.animation_presenter.updateBValue.connect(self.bottomLabelAnimator.start)
        self.animation_presenter.updateBValue.connect(self.updateBottomAnimationBValue)
        self.animation_presenter.userResultStr.connect(self.updateStep2Label3)
        

        # STEP 3
        self.animation_presenter.countUpdated3.connect(self.arrow_widget.stopBottomArrowAnimation)
        self.animation_presenter.countUpdated3.connect(self.bottomLabelAnimator.stop)
        self.animation_presenter.countUpdated3.connect(self.step3_labels.start)

        self.animation_presenter.countUpdated3.connect(self.arrow_widget.startTopArrowAnimation)
        self.animation_presenter.countUpdated3.connect(self.topLabelAnimatorR.start)
        self.animation_presenter.signalValue.connect(self.updateRXValue)
        

        self.animation_presenter.updateNValue.connect(self.updateStep3Label2)
        self.animation_presenter.updateNYValue.connect(self.updateStep3Label3)
        
        
        
        # STEP 4
        self.animation_presenter.countUpdated4.connect(self.step1_labels.stop)
        self.animation_presenter.countUpdated4.connect(self.step2_labels.stop)
        self.animation_presenter.countUpdated4.connect(self.step3_labels.stop)
        self.animation_presenter.countUpdated4.connect(self.arrow_widget.stopTopArrowAnimation)
        self.animation_presenter.countUpdated4.connect(self.topLabelAnimatorR.stop)

        self.animation_presenter.updateRestartValue.connect(self.restartSetup)
      


    def initSetupLabel(self):
        self.instruction_labels = SetupLabel()
        self.setup_label2 = QLabel("This proof: y = ...")
        self.setup_label2.setIndent(96)
        self.setup_label2.setObjectName("setup_text_label2")
        
    def updateSetupLabel(self, y_value):
        self.setup_label2.setText(f"This proof: <font color='gold'><b><i>y = {y_value} </i></b></font>" )


    def initStep1Label(self):
        self.step1_labels = Step1Label()
        self.step1_label2 = QLabel("This Iteration: s = ... ")
        self.step1_label2.setIndent(100)
        self.step1_label2.setObjectName("step1_text_label2")

    def updateStep1Label(self, s_value):
        self.step1_label2.setText(f"This iteration: <b><i><font color='gold'>s = {s_value}</font></i></b>")


    
    def initStep2Label(self):
        self.step2_labels = Step2Label()
        self.step2_label2 = QLabel("This Iteration: b = ...")
        self.step2_label2.setIndent(100)
        self.step2_label2.setObjectName("step2_text_label2")

        self.step2_label3 = QLabel("Verifier Given: ...")
        self.step2_label3.setIndent(100)
        self.step2_label3.setObjectName("step2_text_label3")

    def updateStep2Label(self, b_value):
        self.step2_label2.setText(f"This iteration: <b><i><font color='gold'>b = {int(b_value)}</font></i></b>")

    def updateStep2Label3(self, r_value):
        self.step2_label3.setText(r_value)


        

    def initStep3Label(self):
        self.step3_labels = Step3Label()
        self.step3_label2 = QLabel("If b = 1, Check:   s = r² (mod N)")
        self.step3_label2.setIndent(100)
        self.step3_label2.setObjectName("step3_text_label2")

        self.step3_label3 = QLabel("If b = 0, Check:   (s ⋅ y) = (r ⋅ x)²(mod N)")
        self.step3_label3.setIndent(100)
        self.step3_label3.setObjectName("step3_text_label3")

    def updateStep3Label2(self, n_value):
        self.step3_label2.setText(f"If b = 1, Check:   s = r² (mod N)      -> <b><i><font color='gold'>N = {int(n_value)}</font></i></b>")

    def updateStep3Label3(self, s_r):
        self.step3_label3.setText(f"If b = 0, Check:   (s ⋅ y) = (r ⋅ x)²(mod N)  -> <b><i><font color='gold'>(s ⋅ y)= {s_r}</font></i></b>")



    
    def restartSetup(self, restart_value):
        if restart_value == 1:
            self.step1_label2.setText(f"This iteration: <b><i><font color='gold'>s = ...</font></i></b>")
            self.step2_label2.setText(f"This iteration: <b><i><font color='gold'>b = ...</font></i></b>")
            self.step2_label3.setText(f"This iteration: <b><i><font color='gold'>r = ...</font></i></b>")
            self.step3_label3.setText(f"If b = 0, Check:   (s ⋅ y) = (r ⋅ x)²(mod N)  ---> <b><i><font color='gold'>s = ...</font></i></b>")
        

    def setupIterationDetails(self):
        self.iterationDetails = IterationLabels()
        

    def setupSpacer(self, width, height):
        self.spacer = QSpacerItem(width, height, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.overall_layout.addItem(self.spacer)


    
    def setupTitle(self):
        self.title_label = QLabel("Zero Knowledge Protocol")
        self.title_label.setObjectName("title_label")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        


    def showEvent(self, event):
        super().showEvent(event)

        self.calculatePositions()
        self.setupAnimationPositions()
        self.setupConnections()
        

    
    def calculatePositions(self):
        """ Calculate the positions boundaries for animated labels """

        self.top_prover_x = (self.prover_label.pos().x() + self.prover_label.width())     # Add prover position + offset
        self.top_prover_y = (self.prover_label.pos().y() - int(self.prover_label.height() / 2))   # Add prover position + offset
        self.top_verifier_x = (self.verifier_label.pos().x())   # Add verifier position + offset
        self.top_verifier_y = (self.verifier_label.pos().y() - int(self.verifier_label.height() / 2)) # Add verifier position + offset

        self.bottom_prover_x = (self.prover_label.pos().x() + self.prover_label.width())     # Add prover position + offset
        self.bottom_prover_y = (self.prover_label.pos().y() + int(self.prover_label.height() / 2) + 35 ) # Add prover position + offset  
        self.bottom_verifier_x = (self.verifier_label.pos().x()) # Add verifier position + offset
        self.bottom_verifier_y = (self.verifier_label.pos().y() + int(self.verifier_label.height() / 2) + 35) # Add verifier position + offset


    def setupAnimation(self):
        # Prover image
        self.prover_label = QLabel(self)
        self.prover_label.setPixmap(QPixmap('fyp/resources/prover.png'))
        self.prover_label.setFixedSize(64, 64)
     
 
        # ArrowWidget instance
        # AnimateArrow instance
        self.arrow_widget = AnimateArrow(self)  # Use AnimateArrow
        
 
        # Verifier image
        self.verifier_label = QLabel(self)
        self.verifier_label.setPixmap(QPixmap('fyp/resources/verifier.png'))
        self.verifier_label.setFixedSize(64, 64)
      



        
    def setupAnimationPositions(self):

        # Initialize LabelAnimators for top and bottom animations with these coordinates
        self.topLabelAnimator0 = LabelAnimator(self, "y = ...", self.top_prover_x, self.top_prover_y, self.top_verifier_x, self.top_verifier_y)
        self.topLabelAnimator1 = LabelAnimator(self, "s = ...", self.top_prover_x, self.top_prover_y, self.top_verifier_x, self.top_verifier_y)
        self.topLabelAnimatorR = LabelAnimator(self, "r", self.top_prover_x, self.top_prover_y, self.top_verifier_x, self.top_verifier_y)
        self.topLabelAnimatorRX = LabelAnimator(self, "r ⋅ x", self.top_prover_x, self.top_prover_y, self.top_verifier_x, self.top_verifier_y)
        self.bottomLabelAnimator = LabelAnimator(self,"b = ...", self.bottom_verifier_x, self.bottom_verifier_y, self.bottom_prover_x, self.bottom_prover_y)

    

    def updateTopAnimationYValue(self, y_value):
        self.topLabelAnimator0.setText(f"y = {int(y_value)}")

    def updateTopAnimationSValue(self, s_value):
        self.topLabelAnimator1.setText(f"s = {int(s_value)}")

    def updateBottomAnimationBValue(self, b_value):
        self.bottomLabelAnimator.setText(f"b = {int(b_value)}")

    def updateRXValue(self, value):
        if value == 0:
            self.topLabelAnimatorR.setText("r ⋅ x")
        elif value == 1:
            self.topLabelAnimatorR.setText("r") 





        

    def setupButton(self):
        self.toggle_glow_button = QPushButton("Toggle Animation", self)
        self.toggle_glow_button.setFixedHeight(35)
        self.toggle_glow_button.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
    
        # Connect button click to presenter's method
        self.toggle_glow_button.clicked.connect(self.animation_presenter.handle_button_click)


        
        
 

