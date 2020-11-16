import java.util.Scanner;

public class GreatestCommonDivisorAdvanced {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    System.out.println("GCT calculator, enter 2 numbers and get there GCT");
    System.out.println("To exit press CTRL-C");

    System.out.println("\n----------\n");

    while (true) {
      int first, second;
      System.out.print("Please enter first number: ");
      first = input.nextInt();

      System.out.print("Please enter second number: ");
      second = input.nextInt();

      int gct = gct(first, second);
      System.out.printf("The GCT of %d and %d is %d\n\n", first, second, gct);
    }
  }

  public static int gct(int n1, int n2) {
    int numerator = n1,
        denomirator = n2,
        rest = -1;
    if (n1 < n2) {
      numerator = n2;
      denomirator = n1;
    }

    while (rest != 0) {
      rest = numerator % denomirator;
      numerator = denomirator;
      denomirator = rest;
    }

    return numerator;
  }
}

/**
 * Expected (possible) output:
 * GCT calculator, enter 2 numbers and get there GCT
 * To exit press CTRL-C
 * 
 * ----------
 * 
 * Please enter first number: 136
 * Please enter second number: 16
 * The GCT of 136 and 16 is 8
 */