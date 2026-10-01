package Ejercicio11;

public class TestAnimal {
    public static void main(String[] args) {
        Animal animal = new Animal("Generic Animal");
        System.out.println(animal);

        Mammal mammal = new Mammal("Generic Mammal");
        System.out.println(mammal);

        Cat cat = new Cat("Whiskers");
        System.out.println(cat);
        cat.greets();

        Dog dog = new Dog("Buddy");
        System.out.println(dog);
        dog.greets();
        dog.greets(dog);
    }
}