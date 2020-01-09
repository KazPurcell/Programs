from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets

#Grab the widget

@interact(x=(0,60,1)) ##Min,max, step, 0 per hour, up to 60 per hour, $1 increase or decrease at a time

def test(x):
    untaxed = (x*40*4*12) #Salary of your choice per hour per year
    tax_rate = ((12.96/100)*untaxed) #Florida's 2020 Tax Rate
    taxed = untaxed-tax_rate # Tax Math           
    return round(taxed,2) #Return the salary rounded up to the cents.

#Salary per hour no tax reduction
