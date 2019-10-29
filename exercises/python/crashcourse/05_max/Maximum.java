public class Maximum {
  public static void main(String[] args) {
    int[] numbers = {17, -8, 252, 1, 12, 0, 35, 77, -113};

    int max = getMax(numbers);
    System.out.printf("The max is: %d\n", max);
  }

  public static int getMax(int[] numbers) {
    if (numbers.length < 1) {
      return 0;
    }

    int max = numbers[0];
    for (int i = 1; i < numbers.length; i++) {
      if (numbers[i] > max) {
        max = numbers[i];
      }
    }

    return max;
  }
}

