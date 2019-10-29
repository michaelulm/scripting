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