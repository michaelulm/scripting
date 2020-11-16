import java.util.Scanner;

public class UserInput {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    String firstName = "";
    String lastName = "";

    System.out.print("Please enter your first name: ");
    firstName = input.nextLine();

    System.out.print("Please enter your last name: ");
    lastName = input.nextLine();

    System.out.printf("Hello %s %s\n", firstName, lastName);
  }
}

/**
 * Expected output:
 * Please enter your first name: Maria
 * Please enter your last name: Musterfrau
 * Hello Maria Musterfrau
 */