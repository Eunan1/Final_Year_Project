from PyQt6.QtCore import Qt, QObject, pyqtSignal
import random





class AnimationPresenter(QObject):
    """

    Manages the sequence of animations and interactions in a demonstration of the Zero-Knowledge Protocol.

    This class uses signals to communicate updates to slots within zero_knowledge.py.
    The updates are used to trigger start and stop animation methods.

    There are two types of signals used here:
    Iteration Signal:   Signal sent based on an updated iteration of the button pressed.
    Value Signal:       Signal sent based on an updated value of a certain variable.

    Iteration Signals -     Used to carry out necessary general methods that need to happen after a specific button press.
    Example           -     Signal countUpdated3 is sent to zero_knowledge.py to start and stop various animation processes when the button count = 3

    Value Signals -     Used to update certain values in the proof.
    Example       -     All the values that need updating throughout the proof such as 'y', 'N', 's', 'b', 'N * y', 'r', are sent through these

    Attributes:
        iterationUpdated (pyqtSignal): Signal emitted with the current iteration count.
        certaintyUpdated (pyqtSignal): Signal emitted with the current certainty value as a float.
        percentageUpdated (pyqtSignal): Signal emitted with the current percentage completion as a float.
        countUpdatedMinus1 to countUpdated5 (pyqtSignal): Signals for different states of the animation process.
        updateYValue (pyqtSignal): Signal to update 'y' value in the proof.
        updateNValue (pyqtSignal): Signal to update 'N' value in the proof.
        updateSValue (pyqtSignal): Signal to update 's' value during Step 1 of the proof.
        updateBValue (pyqtSignal): Signal to update 'b' value during Step 2 of the proof.
        updateNYValue (pyqtSignal): Signal to update modified 'N * y' value.
        updateRValue (pyqtSignal): Signal to update 'r' value.
        updateRestartValue (pyqtSignal): Signal to indicate a restart in the proof demonstration.
        userResultInt (pyqtSignal): Signal to emit the result as an integer.
        userResultStr (pyqtSignal): Signal to emit the result as a formatted string.
        signalValue (pyqtSignal): Signal to emit specific state flags for conditional operations.

    The presenter reacts to button clicks to progress through the proof steps, emitting signals to update
    UI components and calculations dynamically. It manages the state of the proof through a series of calculated
    values and random conditions, thus demonstrating a Zero-Knowledge Protocol dynamically.

    """
    # Value Signals
    iterationUpdated = pyqtSignal(int)
    certaintyUpdated = pyqtSignal(float)
    percentageUpdated = pyqtSignal(float)

    # Iteration Signals
    countUpdatedMinus1 = pyqtSignal(int)
    countUpdated0 = pyqtSignal(int)
    countUpdated1 = pyqtSignal(int)
    countUpdated2 = pyqtSignal(int)
    countUpdated3 = pyqtSignal(int)
    countUpdated4 = pyqtSignal(int)
    countUpdated5 = pyqtSignal(int)

    # Updated value signals
    updateYValue = pyqtSignal(float)
    updateNValue = pyqtSignal(float)
    updateSValue = pyqtSignal(float)
    updateBValue = pyqtSignal(float)
    updateNYValue = pyqtSignal(int)
    updateRValue = pyqtSignal(float)

    updateRestartValue = pyqtSignal(int)
    userResultInt = pyqtSignal(int)
    userResultStr = pyqtSignal(str)
    signalValue = pyqtSignal(int)
    

    def __init__(self):
        """
        Initialize the object with click_count set to -1, iteration_count set to 0, 
        click_count starts at -1 to ensure setup is executed only once.
        x set to a random integer between 1 and 99, and N set to a random integer between 1 and 99.
        """
        super().__init__()

        self.click_count = -1
        self.iteration_count = 0

        self.x = random.randint(1, 99)
        self.N = random.randint(1, 99)  # Assuming N is also randomly generated for demonstration


    def handle_button_click(self):
        """
        A function to handle button clicks, updating various values and emitting signals based on the number of clicks.

        Each time button is pressed the function gets called.
        Starts by incrementing click_count by 1.
        Enters the if statement that matches the state of click_count.
        Carries out basic methods and emits relevant signals.
        """


        # Increment the click count on every button press
        self.click_count += 1

        # Setup Iteration only gets entered once at the beginning as initial set = -1
        if self.click_count == 0:
            self.y = self.setupCalculation(self.x, self.N)

                    # Check and adjust y if it is zero
            while self.y == 0:
                self.x = random.randint(1, 99)
                self.y = self.setupCalculation(self.x, self.N)

            self.updateYValue.emit(self.y)  # Emit the new value of y
            
            self.countUpdated0.emit(self.click_count)
            
        # click_count = 1, Step 1
        elif self.click_count == 1:
            
            self.r = random.randint(1, 99)
            self.s = self.Step1Calculation(self.r, self.N)

            while self.s == 0:
                self.r = random.randint(1, 99)
                self.s = self.Step1Calculation(self.r, self.N)

            self.updateSValue.emit(self.s)
            self.updateRValue.emit(self.r)
            self.countUpdated1.emit(self.click_count)

        # click_count = 2, Step 2
        elif self.click_count == 2:

            self.countUpdated2.emit(self.click_count)
            self.b_float = self.randomBit()
            self.b = int(self.b_float) 
            self.updateBValue.emit(self.b)
         
           
        # click_count = 3, Step 3
        elif self.click_count == 3:

            self.countUpdated3.emit(self.click_count)

            if self.b == 1:
                self.user_result = self.r
                self.result_string = f"Verifier Given: <b><i><font color='gold'>r =  {str(self.user_result)}</color></i></b>"
                self.signal = 1 
            elif self.b == 0:
                self.user_result = self.r * self.x
                self.result_string = f"Verifier Given: <b><i><font color='gold'> r ⋅ x = {str(self.user_result)}</color></i></b>"
                self.signal = 0

            self.userResultInt.emit(self.user_result)
            self.userResultStr.emit(self.result_string)
            self.updateNValue.emit(self.N)
            self.signalValue.emit(self.signal)
            

            self.s_y = int(self.s * self.y)
            self.updateNYValue.emit(self.s_y)
             
            
            # Retrieve the value of r here?

        # click_count = 4, Everything resets and TrustMeter animation shown
        elif self.click_count == 4:
            self.countUpdated4.emit(self.click_count)


            self.iteration_count += 1
            self.iterationUpdated.emit(self.iteration_count)

            # Calculate and emit new certainty and percentage values
            certainty_value = self.certaintyValue(self.iteration_count)
            percentage_value = self.percentageValue(self.iteration_count)

            self.certaintyUpdated.emit(certainty_value)
            self.percentageUpdated.emit(percentage_value)

            self.restart_value = 1
            self.updateRestartValue.emit(self.restart_value)

            self.click_count = 0  # Reset or adjust as needed for further behavior
            
    


    def certaintyValue(self, count):
        """
        Calculate the certainty in the prover value based on the count.
        For use in IterationLabel.
        
        Parameters:
            count (int): The count used to calculate the certainty value.
        
        Returns:
            float: The calculated certainty value rounded to 2 decimal places.
        """
        return round(1 - (1 / (2**count)), 2)
    
    
    
    def percentageValue(self, count):
        """
        Calculate the percentage certainty in the prover based on the count parameter.
        For use in TrustMeter.

        Parameters:
            count (int): The count used in the calculation.

        Returns:
            float: The calculated percentage value rounded to 2 decimal places.
        """
        return round(((1 / (2**count)) * 100), 2)
    
    
    
    def setupCalculation(self, x, N):
        """
        Setup calculation function that computes y as the result of x squared modulo N.
        
        Parameters:
            x (int): The secret number.
            N (int): The modulo divisor.
        
        Returns:
            int: The result of the calculation.
        """
        y = (x ** 2) % N
        return y
    
    
    
    def Step1Calculation(self, r, N):
        """
        Function to compute s in the proof.

        Parameters:
            r (int): the random number.
            N (int): The modulo divisor.

        Returns:
            int: the result of the calculation.
        """
        s = (r ** 2) % N
        return s
    
    
    
    def randomBit(self):
        """
        Generate a random bit and return it.

        Returns:
            int: A random bit (0 or 1).
        """
        random_bit = random.randint(0, 1)
        return random_bit
    


    

    
    




