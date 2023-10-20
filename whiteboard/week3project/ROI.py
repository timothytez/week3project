class MyROI:
    
    
    def __init__(self, income, expenses, cashFlow, ConC, Invest):
        self.income = income
        self.expenses = expenses
        self.cashFlow = cashFlow
        self.ConC = ConC
        self.Invest = Invest
        
        
    def Income(self):
        self.income = float(input('Enter Total Rental Income (Amount before expenses)\n(example input: 5000) '))
        
        
    def Expenses(self):
        self.expenses = float(input('Enter Property Expenses(Repair and maintenance cost)\n(example input: 3000) '))
        
        
    def CashFlow(self):
        self.cashFlow = self.income - self.expenses
        print(f"Your CASHFLOW is {self.cashFlow}")
   
        
    def Inv(self):
        dp = float(input('Enter your Down Payment amount '))
        self.Invest += dp
        close = float(input('Enter Total Closing Cost '))
        self.Invest += close
        repair = float(input('Enter Total Repair Cost '))
        self.Invest += repair
        misc = float(input('Enter any other investment cost '))
        self.Invest += misc
        print(f'Your total investment is {self.Invest}')
        
        
    def ROI(self):
        acf = self.cashFlow * 12
        self.roi = acf/self.Invest * 100
        print(f'Your estimated ROI is {self.roi}%.\nIf this is incorrect, please review your and try again. ')
        
        
    def View(self):
        print(f'Total Rental Income: {self.income}')
        print(f'Total Property Expense: {self.expenses}')
        print(f'Total Cash Flow: {self.cashFlow}')
        print(f'Total Investment Value: {self.Invest}. \nThis value includes: \n - Down Payment \n - Total Closing Cost \n - Extra Expenses')
        print(f'Your Estimated ROI is {self.roi}% ')
        
        
def Driver():
    while True:
        print('We need to calculate')
        estamate.Income()
        estamate.Expenses()
        estamate.CashFlow()
        estamate.Inv()
        estamate.ROI()
        response = input('What would you like to do? [Q]uit, [R]eview your info, or [S]tart over? ').upper
        if response == 'Q':
            break
        elif response == 'S':
            continue
        elif response == 'R':
            estamate.View()
            response_2 = input('Would you like to [Q]uit, or [S]tart over? [C]hange my info? ').upper
            if response_2 == 'Q':
                break
            elif response_2 == 'S':
                continue
            elif response_2 == 'C':
                response_3 = input('What would you like to edit?\n[I]ncome, [E]xpenses, [T]otal investment ').upper
                if response_3 == 'I':
                    estamate.Income()
                    estamate.CashFlow()
                    response = input('Would you like to [Q]uit, [R]eview your info, or [s]tart over? ').upper    
                elif response_3 == 'E':
                    estamate.Expenses()
                    estamate.CashFlow()
                    response = input('Would you like to [Q]uit, [R]eview your info, or [S]tart over? ').upper
                elif response_3 == 'T':
                    estamate.TotalInv
                    response = input('Would you like to [Q]uit, [R]eview your info, or [S]tart over? ').upper
        

estamate = MyROI(0, 0, 0, 0, 0)

Driver()