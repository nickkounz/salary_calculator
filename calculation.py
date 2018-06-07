import re, csv
from bisect import bisect

def calc_monthly_income(salary):
    """
    Calculate the monthly gross income based on annual income.
    """
    if type(salary) not in [int, float]:
        raise TypeError("salary must be a non-negative real number.")
    if salary < 0:
        raise ValueError("salary cannot be negative.")
    
    monthly_gross_income = int(round(salary / 12))
    return monthly_gross_income

        


def calc_monthly_tax(salary):
    """
    Calculate the monthly tax based on the given tax rates, income brackets and tax base.
    """
    if type(salary) not in [int, float]:
        raise TypeError("salary must be a non-negative real number.")
    if salary < 0:
        raise ValueError("salary cannot be negative.")

    brackets = [18200, 37000, 80000, 180000] 
    tax_rates = [0, 19, 32.5, 37, 45]       
    base_tax = [0, 3572, 17547, 54547]
    
    i = bisect(brackets, salary)

    # 0 tax rate scenario
    if i == 0:
        return salary

    tax_rate = tax_rates[i]
    bracket = brackets[i-1]
    taxable_income = salary - bracket
    tax_in_bracket = taxable_income * tax_rate / 100
    total_tax = base_tax[i-1] + tax_in_bracket
    monthly_tax = int(round(total_tax / 12))
    return monthly_tax


def calc_net_income(salary, tax):
    """
    Calculate the monthly net income based on given salary and tax
    """
    if salary < 0 or tax < 0:
        raise ValueError("salary or tax cannot be negative.")

    if all(isinstance(i, (int,float)) for i in [salary,tax]):
        net_income = int(salary) - int(tax)
        return net_income
    else:
        raise TypeError("tax and salary must be non-negative real number.")


def calc_super(salary, super_rate):
    """
    Calculate the monthly super based on given salary
    """
    if type(salary) not in [int,float]:
        raise TypeError ("salary must be a non-negative real number.")
    if salary < 0:
        raise ValueError("salary cannot be negative.")

    m = re.findall(r'\d+%', str(super_rate))
    if len(m) == 0:
        raise TypeError ("super rate format is not supported")

    else:
        super_rate = re.findall(r'\d+', str(m[0]))
        if int(super_rate[0]) >= 0 and int(super_rate[0]) <= 50:
            sum_super = int(salary) * int(super_rate[0]) / 100
            return int(round(sum_super))
        else:
            raise ("super rate is not between 0 to 50%")


if __name__ == "__main__":
    #print(calc_monthly_tax(-5))
    with open ('input.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            first_name, last_name, salary, super_rate, payment_start_date = row[0], row[1], int(row[2]), row[3], row[4]
            name = first_name + " " + last_name
            pay_period = payment_start_date
            gross_income = calc_monthly_income(salary)
            income_tax = calc_monthly_tax(salary)
            net_income = calc_net_income(gross_income, income_tax)
            sum_super = calc_super(gross_income, super_rate)
            print(name,pay_period,gross_income,income_tax,net_income,sum_super, sep=",")
