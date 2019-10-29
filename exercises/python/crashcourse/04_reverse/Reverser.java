public class Reverser {
  public static void main(String[] args) {
    String[] strings = {"first", "second", "third", "fourth", "fifth"};
    String[] reversed = new String[strings.length];

    for (int i = 0; i < strings.length; i++) {
      reversed[strings.length-i-1] = strings[i];
    }

    for (String s : reversed) {
      System.out.println(s);
    }
  }
}