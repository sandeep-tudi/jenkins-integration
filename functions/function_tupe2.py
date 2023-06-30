# A function that would give the details of the employee who has worked most number of hours

work_hours = [('ajjan',1000),('Suresh',800),('sandeep',200), ('someone', 5000)]
def employee_of_the_month(work_hours):
    great_of_the_month = ''
    employee_hours = 0
    for employee,hours in work_hours:
        if hours > employee_hours:
            employee_hours = hours
            great_of_the_month = employee

        else:
            pass
    return (great_of_the_month,employee_hours)

name,hours= employee_of_the_month(work_hours)

print(hours)





