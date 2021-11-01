# ROI CALCULATOR
class ROICalculator():

    def __init__(self,calcIncome=0,calcExpenses=0,calcInvestment=0,calcCashflow=0): 
        self.calcIncome = calcIncome
        self.calcExpenses = calcExpenses
        self.calcInvestment = calcInvestment
        self.calcCashflow = calcCashflow

    def myIncome(self):
        addIncome = int(input('What is your estimated Total Income?'))
        self.calcIncome += addIncome
        # print(self.calcIncome)
        print(f'Your Total Income is ${self.calcIncome}')
        

    def myItemIncome(self):
        addIncome2 = int(input('Monthly Rental Income'))
        self.calcIncome += addIncome2
        addIncome3 = int(input('Monthly Parking ($0 if none)'))
        self.calcIncome += addIncome3
        addIncome4 = int(input('Laundry Room ($0 if none)'))
        self.calcIncome += addIncome4
        addIncome5 = int(input('Vending Machine ($0 if none)'))
        self.calcIncome += addIncome5
        # print(self.calcIncome)
        print(f'Your Total Income is ${self.calcIncome}')
  
    def myExpenses(self):
        addExpense = int(input('What is your estimated Total Expenses?'))
        self.calcExpenses += addExpense
        # print(self.calcExpenses)
        print(f'Your Total Expense is ${self.calcExpenses}')

    def myItemExpenses(self):
        addExpense2 = int(input('Mortgage'))
        self.calcExpenses += addExpense2
        addExpense3 = int(input('Monthly Home Owner Insurance'))
        self.calcExpenses += addExpense3
        addExpense4 = int(input('Electricity'))
        self.calcExpenses += addExpense4
        addExpense5 = int(input('Gas/Heat'))
        self.calcExpenses += addExpense5
        addExpense6 = int(input('Water/Sewage'))
        self.calcExpenses += addExpense6
        addExpense7 = int(input('HOA Fees'))
        self.calcExpenses += addExpense7
        addExpense8 = int(input('Home Repair/Maintenance'))
        self.calcExpenses += addExpense8
        addExpense9 = int(input('Capital Expenditure (aka Rainy Day Fund)'))
        self.calcExpenses += addExpense9
        addExpense10 = int(input('Monthly Property Tax'))
        self.calcExpenses += addExpense10
        # print(self.calcExpenses)
        print(f'Your Total Expense is ${self.calcExpenses}')

    def myInvestment(self):
        addInvestment = int(input('What is your estimated Total Investment'))
        self.calcInvestment += addInvestment
        # print(self.calcInvestment)
        print(f'Your Total Investment is ${self.calcInvestment}')

    def myItemInvestment(self):
        addInvestment2 = int(input('What is your Down Payment?'))
        self.calcInvestment += (addInvestment2)
        addInvestment3 = int(input('What is your total Closing cost?'))
        self.calcInvestment += (addInvestment3)
        addInvestment4 = int(input('What is your Total Rehab cost?'))
        self.calcInvestment += (addInvestment4)
        # print(self.calcInvestment)
        print(f'Your Total Investment is ${self.calcInvestment}')

    def myCashFlow(self):
        monthlyCashflow = self.calcIncome - self.calcExpenses
        # print(monthlyCashflow)
        print(f'Your Total Cashflow is ${monthlyCashflow}')

    def myAnnualInc(self):
        annualIncome = (self.calcIncome - self.calcExpenses) * 12
        # print(annualIncome)
        print(f'Your Annual Income is ${annualIncome}')
        
    def myCOCROI(self):
        trueROI = float(((self.calcIncome - self.calcExpenses) * 12) / self.calcInvestment)
        # print(trueROI)
        percentage = "{:.0%}".format(trueROI)
        # print(percentage)
        print(f'Your ROI is {percentage}')
        
  

myROI = ROICalculator()
# income.myIncome()

def run():
    while True:
        chooseIncome = input('What would you like to do? \n 1. Estimated Total \n 2. Itemized Income \n Q. to quit')
        if chooseIncome == '1':
            myROI.myIncome()
        elif chooseIncome == '2':
            myROI.myItemIncome()
            break
        elif chooseIncome.lower() == 'q':
            break

        chooseExpense = input('What would you like to do? \n 1. Estimated Total Expense \n 2. Itemized Total Expense \n Q. to quit')
        if chooseExpense == '1':
            myROI.myExpenses()
        if chooseExpense == '2':
            myROI.myItemExpenses()
            break
        elif chooseExpense.lower() == 'q':
            break

        chooseInvestment = input('What would you like to do? \n 1. Estimated Total Investment \n 2. Itemized Total Investment \n Q. to quit')
        if chooseInvestment == '1':
            myROI.myInvestment()
        if chooseInvestment == '2':
            myROI.myItemInvestment()
            break
        elif chooseInvestment.lower() == 'q':
            break

        myROI.myCashFlow()

        myROI.myAnnualInc()

        myROI.myCOCROI()

        # print(self.cashflow)


run()

