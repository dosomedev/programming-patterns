public class Singleton {
   private static Singleton instance;
   private String message;

   private Singleton() {}

   public static synchronized Singleton getInstance() {
      if (instance == null) {
         instance = new Singleton();
      }
      return instance;
   }

   public void setMessage(String message) {
      this.message = message;
   }

   public void showMessage() {
      System.out.println(this.message);
   }
}
