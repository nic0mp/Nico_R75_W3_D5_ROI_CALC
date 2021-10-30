# ROI CALCULATOR
class ROICalculator():

    def __init__(self,calcIncome=0,calcExpenses=0,calcInvestment=0,cashflow=0): 
        self.calcIncome = calcIncome
        self.calcExpenses = calcExpenses
        self.calcInvestment = calcInvestment
        self.cashflow = cashflow

    def myIncome(self):
        addIncome = int(input('What is your estimated Total Income?'))
        self.calcIncome += addIncome
        print('Your Total Income is $', + sum(self.calcIncome))
        return sum(self.calcIncome)

    def myItemIncome(self):
        addIncome2 = int(input('Monthly Rental Income'))
        self.calcIncome += addIncome2
        addIncome3 = int(input('Monthly Parking ($0 if none)'))
        self.calcIncome.append(addIncome3)
        addIncome4 = int(input('Laundry Room ($0 if none)'))
        self.calcIncome.append(addIncome4)
        addIncome5 = int(input('Vending Machine ($0 if none)'))
        self.calcIncome.append(addIncome5)
        # for nums in self.calcIncome:
        #     print( nums)
        print('Your Total Income is $', + sum(self.calcIncome))
  
    def myExpenses(self):
        addExpense = int(input('What is your estimated Total Expenses?'))
        self.calcExpenses.append(addExpense)
        print('Your Total Expense is $',+sum(self.calcExpenses))

    def myItemExpenses(self):
        addExpense2 = int(input('Mortgage'))
        self.calcExpenses.append(addExpense2)
        addExpense3 = int(input('Monthly Home Owner Insurance'))
        self.calcExpenses.append(addExpense3)
        addExpense4 = int(input('Electricity'))
        self.calcExpenses.append(addExpense4)
        addExpense5 = int(input('Gas/Heat'))
        self.calcExpenses.append(addExpense5)
        addExpense6 = int(input('Water/Sewage'))
        self.calcExpenses.append(addExpense6)
        addExpense7 = int(input('HOA Fees'))
        self.calcExpenses.append(addExpense7)
        addExpense8 = int(input('Home Repair/Maintenance'))
        self.calcExpenses.append(addExpense8)
        addExpense9 = int(input('Capital Expenditure (aka Rainy Day Fund)'))
        self.calcExpenses.append(addExpense9)
        addExpense10 = int(input('Monthly Property Tax'))
        self.calcExpenses.append(addExpense10)
        print('Your Total Expense is $',+ sum(self.calcExpenses))

    def myInvestment(self):
        addInvestment = int(input('What is your estimated Total Investment'))
        self.calcInvestment.append(addInvestment)
        print('Your Total Investment is $',+ sum(self.calcInvestment))

    def myItemInvestment(self):
        addInvestment2 = int(input('What is your Down Payment?'))
        self.calcInvestment.append(addInvestment2)
        addInvestment3 = int(input('What is your total Closing cost?'))
        self.calcInvestment.append(addInvestment3)
        addInvestment4 = int(input('What is your Total Rehab cost?'))
        self.calcInvestment.append(addInvestment4)
        print('Your Total Investment is $',+ sum(self.calcInvestment))
        
        ROICalculator.myCashflow(self)
    def myCashflow(self):
        monthlyCashflow = self.calcIncome - self.calcExpenses
        self.cashflow = monthlyCashflow
        # print('Your Total Cashflow is $'+((sum(self.calcIncome)) - (sum(self.calcExpenses))))
        print('monthlyCashflow')




myROI = ROICalculator()
# income.myIncome()

def run():
    while True:
        chooseIncome = input('Provide Total Income \n 1. Estimated Total \n 2. Itemized Income')
        if chooseIncome.lower() == '1':
            myROI.myIncome()
        elif chooseIncome.lower() == '2':
            myROI.myItemIncome()

        chooseExpense = input('Provide your total Expense \n 1. Estimated Total Expense \n 2. Itemized Total Expense')
        if chooseExpense == '1':
            myROI.myExpenses()
        if chooseExpense == '2':
            myROI.myItemExpenses()

        chooseInvestment = input('Provide your total Investment \n 1. Estimated Total Investment \n 2. Itemized Total Investment')
        if chooseInvestment == '1':
            myROI.myInvestment()
        if chooseInvestment == '2':
            myROI.myItemInvestment()

        print(self.cashflow)


run()

