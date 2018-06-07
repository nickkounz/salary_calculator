# Salary Calculator
Generate the payslip based on given csv.
## The challenge 
The app is designed to get the input and generate the below output.

* Input
```
(first name, last name, annual salary, super rate (%), payment start date):
David,Rudd,60050,9%,01 March – 31 March
Ryan,Chen,120000,10%,01 March – 31 March
```

* Output
```
(name, pay period, gross income, income tax, net income, super):
David Rudd,01 March – 31 March,5004,922,4082,450
Ryan Chen,01 March – 31 March,10000,2696,7304,1000

```
* Tax Brackets
```
The following rates for 2012-13 apply from 1 July 2012.
Taxable income		    Tax on this income
0 - $18,200			    Nil
$18,201 - $37,000		19c for each $1 over $18,200
$37,001 - $80,000		$3,572 plus 32.5c for each $1 over $37,000
$80,001 - $180,000		$17,547 plus 37c for each $1 over $80,000
$180,001 and over		$54,547 plus 45c for each $1 over $180,000
The tax table is from ATO: http://www.ato.gov.au/content/12333.htm
```

## The idea
* Write a function for each output element. So that each function can be re-used and maintained seperately.
* Rather than use the comparisions between the income and the tax brackets, I decide to use python bisect based on Bisection Algorithm to find the income within the brackets in a much efficient way.
* Because we are dealing with the csv type source, so the app needs to handle the Type, Value Errors from the source csv.

## Run the Application

### Prerequisite
You should be able to run the app on all platforms, such as Windows, Linux and Mac OS. Just to make sure you have docker installed.
### Preparation
You can choose either copy the git repo and build the image yourself or pull it straight from the docker hub.
* Build the image yourself
```
docker build -t nickkounz/calculation:1.0 .
```
* Pull from docker hub repository
```
docker pull nickkounz/calculation:1.0
```
### Calculate the salary
* Stand up the container
```
docker run -it --rm --name=python_calculator nickkounz/calculation:1.0 sh
```
* Run the app
```
# python calculation.py
---------------------output------------------------
David Rudd,01 March - 31 March,5004,922,4082,450
Ryan Chen,01 March - 31 March,10000,2696,7304,1000
```

## Unit Test
There 3 test functions
* Test the result of the calculation
* Test the value error
* Test the type error

### Run the test
```
# python -m unittest
----------------------output-----------------------
Ran 3 tests in 0.001s

OK
```

## Exit
Once finished just exit the container and it will be removed after the exit.
```
exit
```