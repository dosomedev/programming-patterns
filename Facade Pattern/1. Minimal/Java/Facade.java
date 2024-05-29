public class Facade {
    private SubsystemClass1 subsystemClass1;
    private SubsystemClass2 subsystemClass2;

    public Facade(
        SubsystemClass1 subsystemClass1,
        SubsystemClass2 subsystemClass2
    ) {
        this.subsystemClass1 = subsystemClass1;
        this.subsystemClass2 = subsystemClass2;
    }

    public void subsystemOperation() {
        this.subsystemClass1.operationOne();
        this.subsystemClass2.operationTwo();
    }
}
