public class Sum {
  public static void main(String[] args) {
    int sum = 0;
    for (int i = 1; i < 10; i++) {
      sum += i;
    }
    System.out.println("The sum is: " + sum);
  }
}

/**
 * Expected output:
 * The sum is: 45
 */

/**
 * HINT: there is no `for (i = 0; i < n; i++)` in python!
 * take a look on `range()` > https://docs.python.org/3/library/stdtypes.html#range <
 */