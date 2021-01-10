public class ReferenceProb {
    private int ID;
    private int switchCount;

    public ReferenceProb(int param1) {
        ID = param1;
        switchCount = 0;
    }

    public static void SwapAndCount (ReferenceProb obja, ReferenceProb objb) {
        ReferenceProb temp = obja;
        obja.switchCount++;
        obja = objb;
        objb = temp;
        objb.switchCount++;
    }
    public static void main(String[] args) {
        ReferenceProb obja = new ReferenceProb(10);
        ReferenceProb objb = new ReferenceProb(20);

        SwapAndCount(obja, objb);
        System.out.println("Test result is obja: ID = " + obja.ID + ", switchCount = " + obja.switchCount);
        System.out.println("Test result is objb: ID = " + objb.ID + ", switchCount = " + objb.switchCount);
        /*
        Test result is obja: ID = 10, switchCount = 2
        Test result is objb: ID = 20, switchCount = 0
        */
    }
}
