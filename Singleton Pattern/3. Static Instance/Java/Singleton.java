public class Singleton {
   private static Singleton instance = new Singleton();
   private String message;

   private Singleton() {}

   public static Singleton getInstance() {
      return instance;
   }

   public void setMessage(String message) {
      this.message = message;
   }

   public void showMessage() {
      System.out.println(this.message);
   }
}
