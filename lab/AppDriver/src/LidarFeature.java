// class LidarFeature
// Parent: VFeature
// Simulates LIght Detection And Ranging for light-based
//    remote object sensing, poorly
public class LidarFeature extends VFeature {

    public LidarFeature(String featureName, String featureDescription) {
        super(featureName, featureDescription);
    }

    // TBD: More realistic Lidar simulator
    @Override
    public String doOperation() {
        return "Lidar shows target at 1000m";
    }
}
