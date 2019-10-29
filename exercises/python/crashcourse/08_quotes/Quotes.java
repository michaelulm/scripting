import java.util.Scanner;

public class Quotes {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    while (true) {
      System.out.print("Choose Quote:\n");
      System.out.print("\t a - b - c - d - e > ");
      String quote = getQuote(input.nextLine());

      System.out.printf("\n%s\n\n", quote);
    }
  }

  public static String getQuote(String s) {
    switch (s.toLowerCase().charAt(0)) {
      case 'a':
        return "Computers will understand sarcasm before Americans do. - Geoffry Hinton";
      case 'b':
        return "Do the simplest thing that could possibly work. - Kent Beck";
      case 'c':
        return "It's not a faith in technology. It's faith in people. - Steve Jobs";
      case 'd':
        return "Technology is unlocking the innate compassion we have for our fellow human beings. - Bill Gates";
      case 'e':
        return "Truth can only be found in one place: the code. - Robert C. Martin";
      default:
        return "please enter a valid option...";
    }
  }
}