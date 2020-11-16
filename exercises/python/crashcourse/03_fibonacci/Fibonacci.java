public class Fibonacci {
  public static void main(String[] args) {
    int n1 = 0,
        n2 = 1,
        n3,
        count = 15;

    System.out.printf("%d %d ", n1, n2);
    for (int i = 0; i < count; i++) {
      n3 = n1 + n2;
      System.out.printf("%d ", n3);
      n1 = n2;
      n2 = n3;
    }
  }
}

/**
 * Expected Output:
 * 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
 */

/**
 * HINT: * pythons `print`-functions has an optional
 * parameter 'end' (default value = '\n')
 * -> https://docs.python.org/3/library/functions.html#print
 */