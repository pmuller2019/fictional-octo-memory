import java.util.ArrayList;


public class Vehicle {
    String name;
    Double maxSpeed;
    int yearOfManufacture, currentSpeed = 0;
    DriveTrain driveTrain;
    private ArrayList<VFeature> features = new ArrayList<>();
    Operator operator;


    public Vehicle (String name, Double maxSpeed, int yearOfManufacture, DriveTrain driveTrain){
        this.name = name;
        this.maxSpeed = maxSpeed;
        this.yearOfManufacture = yearOfManufacture;
        this.driveTrain = driveTrain;
        }

    public void display(){
        System.out.printf("Vehicle name: %s%nVehicle max speed: %f%nVehicle Year of Manufacture: %d%nCurrent Speed: %d%n", name, maxSpeed, yearOfManufacture, currentSpeed);
        //Drivetrain info
        System.out.printf("Vehicle Engine Type: %s%nEngine Horsepower: %d%nEngine's Current RPM: %d%n",driveTrain.getEngineType(), driveTrain.getHorsepower(), driveTrain.getCurrentRPM());
       
        //features info
        for (VFeature feature : features){
        System.out.printf("Feature Name: %s, Feature Description: %s, Feature Operation: %s%n",feature.getFeatureName(), feature.getFeatureDescription(), feature.doOperation());
        }

        //operator info
        System.out.printf(operator.toString());
        
    }

    void updateOperatorRating(int value){
        operator.changeRating(value);
    }

    void sendOperatorMessage(String message){
        operator.sendMessage(message);
    }


    public Double showDistance(double timeToMeasure){
        // 200 km per hour = 200/3600 km per sec, times the number of seconds = km travelled, x 1000 for km to meters
        Double distanceCovered = maxSpeed * 1000 * timeToMeasure / 3600;
        System.out.println("You travelled " + distanceCovered + " meters.");
        return distanceCovered;
    }
    public void addFeature(VFeature feature){
        features.add(feature);
    }

    // getters/setters
    public int getCurrentSpeed(){
        return this.currentSpeed;
    }

    public void setCurrentSpeed(int currentSpeed){
        this.currentSpeed = currentSpeed;
    }

    public Operator getOperator(){
        return this.operator;
    }
    public void setOperator(Operator operator){
        this.operator = operator;
    }
    public void setDriveTrain(DriveTrain driveTrain) {
        this.driveTrain = driveTrain;
    }

    public DriveTrain getDriveTrain() {
        return this.driveTrain;
    }
}
