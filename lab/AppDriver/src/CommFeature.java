// class CommFeature
// Parent: VFeature
// Simulates a communication module, poorly
public class CommFeature extends VFeature{
    public CommFeature(String a, String b) {
        super(a,b);
    }

    // TBD: more realistic communications simulator
    @Override
    public String doOperation() {
        return "Comm received ack to previous message";
    }

}
