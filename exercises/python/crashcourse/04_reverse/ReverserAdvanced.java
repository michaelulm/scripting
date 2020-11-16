public class ReverserAdvanced {
  public static void main(String[] args) {
    String[] strings = {"first", "second", "third", "fourth", "fifth"};
    String[] reversed = new String[strings.length];

    for (int i = 0; i < strings.length; i++) {
      String s = strings[i];
      String r = "";
      for (char c : s.toCharArray()) {
        r = c + r;
      }
      reversed[strings.length-i-1] = r;
    }

    for (String s : reversed) {
      System.out.println(s);
    }
  }
}

/**
 * Expected output:
 * htfif
 * htruof
 * driht
 * dnoces
 * tsrif
 */