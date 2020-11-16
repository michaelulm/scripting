public class CaesarCipher {
  public static final int SHIFT = 13;
  public static final int MOD = 26;
  public static final int LC = 97;
  public static final int UC = 65;

  public static void main(String[] args) {
    String message = "TOP Secret";
    String encrypted = encrypt(message);
    String decrypted = decrypt(encrypted);

    System.out.printf("MESSAGE: %s\n", message);
    System.out.printf("ENCRYPTED: %s\n", encrypted);
    System.out.printf("DECRYPTED: %s\n", decrypted);
  }

  public static String encrypt(String text) {
    String result = "";
    for (char character : text.toCharArray()) {
      if (Character.isUpperCase(character)) {
        result += (char)(((int)character + SHIFT - UC) % MOD + UC);
      } else if(Character.isLowerCase(character)) {
        result += (char)(((int)character + SHIFT - LC) % MOD + LC);
      } else {
        result += character;
      }
    }
    return result;
  }

  public static String decrypt(String text) {
    String result = "";
    for (char character : text.toCharArray()) {
      if (Character.isUpperCase(character)) {
        result += (char)(((int)character + (MOD - SHIFT) - UC) % MOD + UC);
      } else if (Character.isLowerCase(character)) {
        result += (char)(((int)character + (MOD - SHIFT) - LC) % MOD + LC);
      } else {
        result += character;
      }
    }
    return result;
  }
}

/**
 * Expected output:
 * MESSAGE: TOP Secret
 * ENCRYPTED: GBC Frperg
 * DECRYPTED: TOP Secret
 */

/**
 * HINT: Take a look on python standard functions
 * `ord()` > https://docs.python.org/3/library/functions.html#ord <
 * `chr()` > https://docs.python.org/3/library/functions.html#chr <
 * to convert string to number (unicode representation)
 * and vice versa.
 */