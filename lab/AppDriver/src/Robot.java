public class Robot implements Operator{
    int rating;
    String manufacturer;
    String message = "";

    public Robot(int rating, String manufacturer){
        this.rating = rating;
        this.manufacturer = manufacturer;
    }

    @Override
    public String toString(){
        return "Robot Manufacturer " + manufacturer + ", Robot Rating: " + rating + ", Robot message: " + message;

    }
    @Override
    public void changeRating(int value) {
        if(0 <= value && value <= 100){
            this.rating = value;
        }else{
            System.out.println("%nUnable to update rating due to being outside allowable constraints [0,100]");
        }
    }

    @Override
    public void sendMessage(String message) {
        this.message = message;
        System.out.println("**** ROBOT OPERATOR ****");
        System.out.println(message);
        System.out.println("**** ROBOT OPERATOR ****");
    }
    
}
