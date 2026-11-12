from fitting_functions import*
#a
m=2
x=3
b=4
y=(linear(m,x,b))
print(y)

#b
x_units = "meters"
y_units = "kg"
slope=(slope_units(x_units,y_units))
print(slope)


#c
print_equation(m,b,y_units,slope)
