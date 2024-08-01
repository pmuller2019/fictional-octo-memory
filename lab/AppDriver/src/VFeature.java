// class VFeature
//    Started with "Feature", but there's a Java thing with
//    that name, so I renamed it
// Models a generic feature or mod to be added dynamically to
//    a Vehicle to perform various tasks
// TBD: change either to an abstract class (there is no generic
//    feature) or to an Interface
public abstract class VFeature {
    protected String featureName = "";
    protected String featureDescription = "";

    // Overloaded constructor
    public VFeature(String featureName, String featureDescription) {
        this.featureName = featureName;
        this.featureDescription = featureDescription;
    }

    // Getters and setters
    public String getFeatureName() { return featureName; }
    public void setFeatureName(String featureName) { this.featureName = featureName; }

    public String getFeatureDescription() { return featureDescription; }
    public void setFeatureDescription(String featureDescription) {
        this.featureDescription = featureDescription;
    }

    // Simulates the feature doing something and returning some kind of
    //    status. Generic VFeature doesn't do anything
    // TBD: return an Operation object instead, containing multiple
    //      pieces of data from the feature
    public abstract String doOperation();
}
