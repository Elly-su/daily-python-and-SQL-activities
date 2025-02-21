// Car.java
public class Car {
    // Fields (attributes)
    String make;
    String model;
    int year;

    // Constructor
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    // Method to display car details
    public void displayDetails() {
        System.out.println("Car Details:");
        System.out.println("Make: " + make);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }

    // Method to simulate starting the car
    public void startCar() {
        System.out.println("The " + year + " " + make + " " + model + " is starting...");
    }

    // Main method
    public static void main(String[] args) {
        // Creating a new Car object
        Car myCar = new Car("Toyota", "Corolla", 2021);
        
        // Calling methods on the car object on the car object
        myCar.displayDetails();
        myCar.startCar();
    }
}
