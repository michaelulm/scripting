import java.util.Random;

public class PasswordGeneratorAdvanced {
  public static void main(String[] args) {
    String ASCII = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    Random rnd = new Random();
    String pass = "";
    int length = 8;


    while (pass.length() != length) {
      int idx = rnd.nextInt(ASCII.length());
      char c = ASCII.charAt(idx);
      int occurrence = 0;
      for (int i = 0; i < pass.length(); i++) {
        if (pass.charAt(i) == c) {
          occurrence++;
        }
      }
      if (occurrence >= 2) {
        continue;
      }
      pass += ASCII.charAt(idx);
    }

    System.out.printf("Password: %s\n", pass);
  }
}

/**
 * Expected (possible) output:
 * Password: wBWktR68
 */