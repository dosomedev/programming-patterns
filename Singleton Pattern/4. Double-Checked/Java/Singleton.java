public class Singleton {
   private volatile static Singleton instance;
   private String message;

   private Singleton() {}

   public static Singleton getInstance() {
      if (instance == null) {
         synchronized (Singleton.class) {
            if (instance == null) {
               instance = new Singleton();
            }
         }
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
