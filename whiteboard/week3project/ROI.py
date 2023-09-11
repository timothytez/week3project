#property investment $1,600,000
#32 unit apartment building (2bed 2bath per unit)
#down payment 10%
#refinishing supplies $30,000 per unit + ($10,000 per unit for refinishing workers) = $320,000
#new gym $30,000
#new laundry facility $30,000
#coffee shop $70,000
#parking garage $15,000
investment = 625,000

#annual debt service(interest/morgage) $16,719.62
#cost of supplies for coffee shop $10,000
#cost of supplies for gym $600
#property tax at .87% ($1,160 per month)
#insurance $100 per unit = $3,200 per month
#HOA $100 per unit = $3,200 per month
#repairs $100 per unit = $3,200 per month
#cap-ex $100 per unit = $3,200
#property manager $5,000
#staff including coffee shop workers(6), maintenace(4), leasing office staff(4) = $46,666
expenses = 86,545.62

#rent $2,000 * 32 units = $64,000
#laundry avg. $50 per unit (50*32) = $1600
#gym fee $50 per unit (50*32) = $1600
#parking fee $100 per unit (100*32) = $3,200
#coffee shop income (([avg. bill=7]*[avg.200 customers per day]*[365 days]= $511,000)/(12))= $42,583.33
income = 112,983.33


def ROI(investment, expenses, income):

    cash_flow = income - expenses
    annual_cash_flow = cash_flow*12


    ROI = (annual_cash_flow/investment)*100

    print(ROI)

ROI(investment, expenses, income)