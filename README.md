# credit_calculator
This is a Credit Calculator! My first project with the CLI interaction. You can write --type=help to get started.

Download the file, go to it's location with the Command Line Interpreter (CLI), and run the python file.
You can start by typing > python credit_calc.py --type=help

principal - your credit principal; interest - annual interest rate (without typing "%");
payment - your monthly payment; periods - count full months to pay the credit principal;

Write "type=diff" to calculate the differentiated payment:
Then, write "--principal=... --periods=... --interest=..."
The result will break down your monthly payments and overpayment.

Write "type=annuity" to calculate one of the missing parameters.
There are 4 parameters: "--principal=... --payment=... --periods=... --interest=..."
Print 3 of them to calculate the 4th (Note: you can't calculate the interest rate!)
It will calculate the missing parameter and overpayment.

Example 1 > python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10
Example 2 > python credit_calc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
