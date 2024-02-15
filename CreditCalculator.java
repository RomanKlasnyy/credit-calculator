import java.util.Scanner;

public class CreditCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the type (\"annuity\" or \"diff\"): ");
        String type = scanner.nextLine();

        if ("diff".equals(type)) {
            System.out.println("Enter the credit principal: ");
            double principal = scanner.nextDouble();
            System.out.println("Enter the count of periods: ");
            int periods = scanner.nextInt();
            System.out.println("Enter the annual interest rate (without %): ");
            double interestRate = scanner.nextDouble();

            double totalPayment = 0;
            double interest = interestRate / 12 / 100;
            for (int i = 1; i <= periods; i++) {
                double monthlyPayment = principal / periods + interest * (principal - (principal * (i - 1)) / periods);
                System.out.printf("Month %d: paid out %.0f\n", i, Math.ceil(monthlyPayment));
                totalPayment += Math.ceil(monthlyPayment);
            }
            System.out.printf("Overpayment = %.0f\n", totalPayment - principal);
        } else if ("annuity".equals(type)) {

            System.out.println("Enter the credit principal: ");

            System.out.println("Enter the monthly payment: ");

            System.out.println("Enter the count of periods: ");

            System.out.println("Enter the annual interest rate (without %): ");

            System.out.println("You need to enter 3 parameters to calculate the 4th!");
        } else if ("help".equals(type)) {
            System.out.println("This is a Credit Calculator. Separate parameters with whitespace for results.");
            System.out.println("principal - your credit principal; interest - annual interest rate (without typing %);");
            System.out.println("payment - your monthly payment; periods - count full months to pay the credit principal;");
            System.out.println();
            System.out.println("Write \"type=diff\" to calculate the differentiated payment:");
            System.out.println("Then, write \"--principal=... --periods=... --interest=...\"");
            System.out.println("The result will break down your monthly payments and overpayment.");
            System.out.println();
            System.out.println("Write \"type=annuity\" to calculate one of the missing parameters.");
            System.out.println("There are 4 parameters: \"--principal=... --payment=... --periods=... --interest=...\"");
            System.out.println("Print 3 of them to calculate the 4th (Note: you can't calculate the interest rate!)");
            System.out.println("It will calculate the missing parameter and overpayment.");
            System.out.println();
            System.out.println("Example 1 > java CreditCalculator --type=diff --principal=1000000 --periods=10 --interest=10");
            System.out.println("Example 2 > java CreditCalculator --type=annuity --payment=8722 --periods=120 --interest=5.6");
        } else {
            System.out.println("Please, choose \"diff\" or \"annuity\" for \"--type=...\" You can \"--type=help\" for more info.");
        }

        scanner.close();
    }
}
