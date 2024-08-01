public class DriveTrain {
public static final int REDLINE = 6000;

    String engineType;
    int horsepower, currentRPM;

    public DriveTrain(){

    }

    public DriveTrain(String engineType, int horsepower, int currentRPM){
        this.engineType = engineType;
        this.horsepower = horsepower;
        this.currentRPM = currentRPM;
    }
    
    public String getEngineType(){
        return this.engineType;
    }
    public void setEngineType(String engineType){
        this.engineType = engineType;
    }
    
    public int getHorsepower(){
        return this.horsepower;
    }
    public void setHorsepower(int horsepower){
        this.horsepower = horsepower;
    }
    
    public int getCurrentRPM(){
        return this.currentRPM;
    }
    public void setCurrentRPM(int currentRPM){
        this.currentRPM = currentRPM;
    }
}
