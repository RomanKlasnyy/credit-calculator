#include <stdio.h>
#include <string.h>

int main() {
    char type[10];
    printf("Enter the type (\"annuity\" or \"diff\"): ");
    scanf("%s", type);

    if (strcmp(type, "diff") == 0) {
        double principal, interestRate;
        int periods;

        printf("Enter the credit principal: ");
        scanf("%lf", &principal);
        printf("Enter the count of periods: ");
        scanf("%d", &periods);
        printf("Enter the annual interest rate (without %%): ");
        scanf("%lf", &interestRate);

        double totalPayment = 0;
        double interest = interestRate / 12 / 100;
        for (int i = 1; i <= periods; i++) {
            double monthlyPayment = principal / periods + interest * (principal - (principal * (i - 1)) / periods);
            printf("Month %d: paid out %.0f\n", i, ceil(monthlyPayment));
            totalPayment += ceil(monthlyPayment);
        }
        printf("Overpayment = %.0f\n", totalPayment - principal);
    } else if (strcmp(type, "annuity") == 0) {
        double principal, monthlyPayment, interestRate;
        int periods;

        printf("Enter the credit principal: ");
        scanf("%lf", &principal);
        printf("Enter the monthly payment: ");
        scanf("%lf", &monthlyPayment);
        printf("Enter the count of periods: ");
        scanf("%d", &periods);
        printf("Enter the annual interest rate (without %%): ");
        scanf("%lf", &interestRate);

        double interest = interestRate / 12 / 100;
        double x = 1 + interest;
        double pow_x_n = 1;
        for (int i = 0; i < periods; i++) {
            pow_x_n *= x;
        }
        double numerator = principal * interest * pow_x_n;
        double denominator = pow_x_n - 1;
        double annuity = monthlyPayment == 0 ? numerator / denominator : monthlyPayment;

        printf("Your annuity payment = %.0f!\n", ceil(annuity));
        printf("Overpayment = %.0f\n", ceil(annuity) * periods - principal);
    } else if (strcmp(type, "help") == 0) {
        printf("This is a Credit Calculator. Separate parameters with whitespace for results.\n");
        printf("principal - your credit principal; interest - annual interest rate (without typing %%);\n");
        printf("payment - your monthly payment; periods - count full months to pay the credit principal;\n\n");
        printf("Write \"type=diff\" to calculate the differentiated payment:\n");
        printf("Then, write \"--principal=... --periods=... --interest=...\"\n");
        printf("The result will break down your monthly payments and overpayment.\n\n");
        printf("Write \"type=annuity\" to calculate one of the missing parameters.\n");
        printf("There are 4 parameters: \"--principal=... --payment=... --periods=... --interest=...\"\n");
        printf("Print 3 of them to calculate the 4th (Note: you can't calculate the interest rate!)\n");
        printf("It will calculate the missing parameter and overpayment.\n\n");
        printf("Example 1 > ./credit_calculator diff\n");
        printf("Example 2 > ./credit_calculator annuity\n");
        printf("Note: Do not forget to compile your .c file before run!\n");
    } else {
        printf("Please, choose \"diff\" or \"annuity\" for \"--type=...\" You can \"--type=help\" for more info.\n");
    }

    return 0;
}
