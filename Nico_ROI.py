# ROI CALCULATOR
class ROICalculator():

    def __init__(self):
        self.calcIncome = []

    def myIncome(self):
        
        if chooseIncome == 1:
            income1 = input('What is your estimated Total Income?')
            self.calcIncome.append()
        elif chooseIncome == 2:
            income2 = input('Monthly Rental Income')
            self.calcIncome.append()
            income3 = input('Monthly Parking ($0 if none)')
            income4 = input('Laundry Room ($0 if none)')
            income5 = input('Vending Machine ($0 if none)')


myROI = ROICalculator()
# income.myIncome()

def run():
    while True:
        chooseIncome = input('What would you like to do? \n 1. Estimated Total \n 2. Itemized Income')

        if chooseIncome == '1':
            myROI.chooseIncome()

