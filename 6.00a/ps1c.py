annual_salary=input('Enter your starting annual salary:')
annual_income=annual_salary
semi_annual_raise=0.07
roi=0.04
total_cost=1000000
down_payment=0.25*float(total_cost)
high=10000
low=0
current_saving=0
num_of_searches=0
epsilon=100.0
abs_val=1000000000
rate=int((high+low)/2)
while abs_val >= epsilon:
    for num_of_months in range(37):
        if num_of_months in range(6,1000+1,6):
            annual_salary=(1+float(semi_annual_raise))*float(annual_salary)
        monthly_salary_saving=(float(rate)/10000)*(float(annual_salary)/12)
        if num_of_months==0:
            current_saving=0
        elif num_of_months==1:
            current_saving=monthly_salary_saving
        else: 
            investment=current_saving*roi/12
            current_saving=investment+current_saving+monthly_salary_saving
#            print('current_saving', current_saving)
        abs_val=abs(current_saving-down_payment)
    if current_saving < down_payment:
        low=rate
    else:
        high=rate
    num_of_searches+=1
    rate=int((high+low)/2)
    if rate==9999:
        print('mission impossible')
        break
#    print('rate', rate)
#    print('num_of_searches', num_of_searches-1)
    current_saving=0
    investment=0
    num_of_months=0
    annual_salary=annual_income
print('best savings rate', float(rate)/10000)
print('num_of_searches', num_of_searches-1)