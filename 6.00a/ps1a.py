# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 17:19:18 2017

@author: KAMALDEEN
"""

annual_salary=input('Enter your starting annual salary:')
portion_to_save=input('Enter the percent of your salary to save:')
total_cost=input('Enter the cost of your dream home:') 
#semi_annual_raise=input('Enter the semiannual raise, as a decimal:')
current_saving=0
num_of_months=0
roi=0.04
investment=0
monthly_salary_saving=(float(portion_to_save)*float(annual_salary))/12
down_payment=0.25*float(total_cost)
#print (down_payment)
while current_saving < down_payment:
    if num_of_months==0:
        current_saving=0
    elif num_of_months==1:
        current_saving=monthly_salary_saving
    else:
        investment=current_saving*roi/12
#        current_saving=investment+(monthly_salary_saving*num_of_months) '''wrong algorithm'''
        current_saving=investment+current_saving+monthly_salary_saving
#    print('investment',investment)
#    print('current_saving', current_saving)
#    print("no of months", num_of_months )
    num_of_months+=1
print ('num_of_months=',num_of_months-1)
        
