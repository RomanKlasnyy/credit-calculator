package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"strconv"
)

func main() {
	scanner := NewScanner(os.Stdin)

	fmt.Println("Enter the type (\"annuity\" or \"diff\"): ")
	typeInput := scanner.NextLine()

	if typeInput == "diff" {
		fmt.Println("Enter the credit principal: ")
		principalStr := scanner.NextLine()
		principal, _ := strconv.ParseFloat(principalStr, 64)

		fmt.Println("Enter the count of periods: ")
		periodsStr := scanner.NextLine()
		periods, _ := strconv.Atoi(periodsStr)

		fmt.Println("Enter the annual interest rate (without %): ")
		interestRateStr := scanner.NextLine()
		interestRate, _ := strconv.ParseFloat(interestRateStr, 64)

		totalPayment := 0.0
		interest := interestRate / 1200
		for i := 1; i <= periods; i++ {
			monthlyPayment := principal/float64(periods) + interest*(principal-(principal*(float64(i)-1))/float64(periods))
			fmt.Printf("Month %d: paid out %.0f\n", i, math.Ceil(monthlyPayment))
			totalPayment += math.Ceil(monthlyPayment)
		}
		fmt.Printf("Overpayment = %.0f\n", totalPayment-principal)
	} else if typeInput == "annuity" {
		fmt.Println("Enter the credit principal: ")

		fmt.Println("Enter the monthly payment: ")

		fmt.Println("Enter the count of periods: ")

		fmt.Println("Enter the annual interest rate (without %): ")

		fmt.Println("You need to enter 3 parameters to calculate the 4th!")
	} else if typeInput == "help" {
		fmt.Println("This is a Credit Calculator. Separate parameters with whitespace for results.")
		fmt.Println("principal - your credit principal; interest - annual interest rate (without typing %);")
		fmt.Println("payment - your monthly payment; periods - count full months to pay the credit principal;")
		fmt.Println()
		fmt.Println("Write \"type=diff\" to calculate the differentiated payment:")
		fmt.Println("Then, write \"--principal=... --periods=... --interest=...\"")
		fmt.Println("The result will break down your monthly payments and overpayment.")
		fmt.Println()
		fmt.Println("Write \"type=annuity\" to calculate one of the missing parameters.")
		fmt.Println("There are 4 parameters: \"--principal=... --payment=... --periods=... --interest=...\"")
		fmt.Println("Print 3 of them to calculate the 4th (Note: you can't calculate the interest rate!)")
		fmt.Println("It will calculate the missing parameter and overpayment.")
		fmt.Println()
		fmt.Println("Example 1 > go run credit_calculator.go --type=diff --principal=1000000 --periods=10 --interest=10")
		fmt.Println("Example 2 > go run credit_calculator.go --type=annuity --payment=8722 --periods=120 --interest=5.6")
	} else {
		fmt.Println("Please, choose \"diff\" or \"annuity\" for \"--type=...\" You can \"--type=help\" for more info.")
	}

	scanner.Close()
}

type Scanner struct {
	sc *bufio.Scanner
}

func NewScanner(reader io.Reader) *Scanner {
	return &Scanner{bufio.NewScanner(reader)}
}

func (s *Scanner) NextLine() string {
	s.sc.Scan()
	return s.sc.Text()
}

func (s *Scanner) Close() {
	if s.sc != nil {
		s.sc = nil
	}
}
