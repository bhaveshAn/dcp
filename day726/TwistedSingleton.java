/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Implement the singleton pattern with a twist.First, instead of storing one instance, store two instances.
And in every even call of getInstance(), return the first instance and in every odd call of getInstance(),
return the second instance.
*/

import java.util.Objects;

public class TwistedSingleton {

    public static class Car {

        int serialNumber;

        public Car(int serialNumber) {
            this.serialNumber = serialNumber;
        }
    }

    private static boolean isEven = true;
    private static Car car1;
    private static Car car2;

    public static Car getInstance(){

        isEven = !isEven;
        if (isEven) {
            if (Objects.nonNull(car2)) return car2;
            car2 = new Car(2);
            return car2;
        } else {
            if (Objects.nonNull(car1)) return car1;
            car1 = new Car(1);
            return car1;
        }
    }

    public static void main(String[] args){

        for (int i = 1; i < 10; i++){
            System.out.println(TwistedSingleton.getInstance().serialNumber);
        }
    }
}
