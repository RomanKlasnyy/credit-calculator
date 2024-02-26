import argparse
from math import ceil, floor, pow, log

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--type', help='Type "annuity" or "diff" (differentiated)')
    parser.add_argument('--principal', help='Your credit principal', type=float)
    parser.add_argument('--payment', help='Your monthly payment', type=float)
    parser.add_argument('--periods', help='Periods (in months)', type=int)
    parser.add_argument('--interest', help='The interest rate (do not type "%")', type=float)

    args = parser.parse_args()

    if args.type == 'diff':
        if args.principal >= 0 and args.periods > 0 and args.interest:
            p = args.principal
            n = args.periods
            i_rate = args.interest / 1200
            pay = 0
            for i in range(args.periods):
                m_pay = p / n + i_rate * (p - (p * i) / n)
                print(f'Month {i + 1}: paid out {ceil(m_pay)}')
                pay += ceil(m_pay)
            print(f'Overpayment = {int(pay - p)}')
        else:
            print('Please, enter your credit principal, periods (in months) and annual interest (without %)')
            print('All these parameters should not be negative! Except for interest rate :)')
    elif args.type == 'annuity':
        args_count = 0
        if args.principal:
            args_count += 1
        if args.payment:
            args_count += 1
        if args.periods:
            args_count += 1
        if args.interest:
            args_count += 1
        if args_count == 3:
            if not args.periods:
                c_prin = args.principal
                m_pay = args.payment
                c_int = args.interest
                i = c_int / 1200
                n = log((m_pay / (m_pay - i * c_prin)), 1 + i)
                n = ceil(n)
                if n == 1:
                    print('You need 1 month to repay this credit!')
                elif n < 12:
                    print(f'You need {n} months to repay this credit!')
                elif n == 12:
                    print('You need 1 year to repay this credit!')
                elif n == 13:
                    print(f'You need 1 year and 1 month to repay this credit!')
                elif n % 12 == 0:
                    print(f'You need {int(n / 12)} years to repay this credit!')
                elif n < 24:
                    print(f'You need 1 year and {n - 12} months to repay this credit!')
                elif n % 12 == 1:
                    print(f'You need {floor(n / 12)} years and {n % 12} month to repay this credit!')
                else:
                    print(f'You need {floor(n / 12)} years and {n % 12} months to repay this credit!')
                print(f'Overpayment = {int((m_pay * n) - c_prin)}')
            if not args.payment:
                c_prin = args.principal
                p_count = args.periods
                c_int = args.interest
                i = c_int / 1200
                a = c_prin * (i * pow((1 + i), p_count) / (pow((1 + i), p_count) - 1))
                print(f'Your annuity payment = {ceil(a)}!')
                print(f'Overpayment = {(ceil(a) * p_count) - c_prin}')
            if not args.principal:
                m_pay = args.payment
                p_count = args.periods
                c_int = args.interest
                i = c_int / 1200
                c_prin = m_pay * (1 / (i * pow((1 + i), p_count) / (pow((1 + i), p_count) - 1)))
                print(f'Your credit principal = {floor(c_prin)}!')
                print(f'Overpayment = {int((m_pay * p_count) - floor(c_prin))}')
            else:
                print("It's impossible to calculate the interest rate!")
        else:
            print('You need to enter 3 parameters to calculate the 4th!')
    elif args.type == 'help':
        print('This is a Credit Calculator. Separate parameters with whitespace for results.')
        print('principal - your credit principal; interest - annual interest rate (without typing "%");')
        print('payment - your monthly payment; periods - count full months to pay the credit principal;')
        print()
        print('Write "type=diff" to calculate the differentiated payment:')
        print('Then, write "--principal=... --periods=... --interest=..."')
        print('The result will break down your monthly payments and overpayment.')
        print()
        print('Write "type=annuity" to calculate one of the missing parameters.')
        print('There are 4 parameters: "--principal=... --payment=... --periods=... --interest=..."')
        print("Print 3 of them to calculate the 4th (Note: you can't calculate the interest rate!)")
        print('It will calculate the missing parameter and overpayment.')
        print()
        print('Example 1 > python credit_calculator.py --type=diff --principal=1000000 --periods=10 --interest=10')
        print('Example 2 > python credit_calculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6')
    else:
        print('Please, choose "diff" or "annuity" for "--type=..." You can "--type=help" for more info.')
