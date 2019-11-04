public class GreatestCommonDivisor {
  public static void main(String[] args) {
    int num1 = 61;
    int num2 = 1792;
    int numerator, denomirator, rest = -1;
    if (num1 < num2) {
      numerator = num2;
      denomirator = num1;
    } else {
      numerator = num1;
      denomirator = num2;
    }

    while (rest != 0) {
      rest = numerator % denomirator;
      numerator = denomirator;
      denomirator = rest;
    }

    System.out.printf("The gcd of %d and %d is %d.\n", num1, num2, numerator);
  }
}