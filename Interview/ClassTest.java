public class ClassTest {
    public static void main(String[] args) {
        Parent obj = new Child();
        Child obj2 = new Child();
        obj.func();
        obj2.func();
    }
    /* Result:
    load Parent
    load Child
    init Parent
    init Child
    init Parent
    init Child
    call Parent
    call Child
    */
}

class Parent {
    static {
        System.out.println("load Parent");
    }

    public Parent() {
        System.out.println("init Parent");
    }

    static void func() {
        System.out.println("call Parent");
    }
}

class Child extends Parent {
    static {
        System.out.println("load Child");
    }

    public Child() {
        System.out.println("init Child");
    }

    static void func() {
        System.out.println("call Child");
    }
}
