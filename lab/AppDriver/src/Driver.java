public class Driver implements Operator{
    String firstName, lastName, combinedUserDataString;
    int age, rating;
    String message = "";

    public Driver(String firstName, String lastName, int age, int rating){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.rating = rating;
    }


    @Override
    public String toString(){
        combinedUserDataString = "Name: " + firstName + " " + lastName + ", Age: " + age + ", Rating " + rating + ", " + message;
        return combinedUserDataString;
    }
    @Override
    public void changeRating(int value) {
        if(0 <= value && value <= 100){
            this.rating = value;
        }else{
            System.out.println("Unable to update rating due to being outside allowable constraints [0,100]");
        }
    }

    @Override
    public void sendMessage(String message) {
        this.message = message;
    }
    
    //getters and setters
    public String getFirstName() {
        return firstName;
    }
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }



}
