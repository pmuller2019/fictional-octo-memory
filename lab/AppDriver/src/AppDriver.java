
public class AppDriver {

    public static void main(String[] args) throws Exception {
        // BufferedReader reader = new BufferedReader(new InputStreamReader (System.in));
        // String userVehicle;
        // double userMaxSpeed, timeToMeasure, distanceCovered;
        // int userYOM, currentSpeed;
        DriveTrain driveTrain = new DriveTrain("Cummins", 350, 0);

        Vehicle v1 = new Vehicle("HellCat", 200.0, 2024, driveTrain);

        //feature adds
        v1.addFeature(new LidarFeature("LidarMod", "Range Finder"));
        v1.addFeature(new CommFeature("CommC3", "Satellite Communications"));
        v1.setOperator(new Driver("Peter", "Muller", 27, 90));
        v1.updateOperatorRating(50);
        v1.sendOperatorMessage("Stop the Vehicle");


        v1.display();
        v1.setOperator(new Robot(25, "ShadySide Robotics"));
        v1.updateOperatorRating(103);
        v1.sendOperatorMessage("Stop the Vehicle!");
        v1.display();
        
        // System.out.printf("%nPlease enter a vehicle name: ");
        // userVehicle = reader.readLine();
        // System.out.print("How fast can your car go?: ");
        // userMaxSpeed = Double.parseDouble(reader.readLine());
        // System.out.print("What year was your car made?: ");
        // userYOM = Integer.parseInt(reader.readLine());
        // Vehicle v2 = new Vehicle(userVehicle, userMaxSpeed, userYOM, driveTrain);
        // v2.display();

        // System.out.print("How much time(in seconds) would you like to travel at max speed?: ");
        // distanceCovered = v2.showDistance(Double.parseDouble(reader.readLine()));
    }

}
