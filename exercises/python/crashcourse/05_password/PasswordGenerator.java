import java.util.Random;

public class PasswordGenerator {
  public static void main(String[] args) {
    String ascii = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    Random rnd = new Random();
    String pass = "";
    int length = 8;

    for (int i = 0; i < length; i++) {
      int idx = rnd.nextInt(ascii.length());
      pass += ascii.charAt(idx);
    }

    System.out.printf("Password: %s\n", pass);
  }
}