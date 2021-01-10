public class ThreadProb {
    static {
        System.out.print("a");
    }

    static class Bar implements Runnable {
        static {
            System.out.print("b");
        }

        Bar() {
            System.out.print("c");
        }

        @Override
        public void run() {
            System.out.print("d");
        }
    }

    public static void main(String[] args) {
        System.out.print("e");
        Thread t1 = new Thread(new Bar());
        Thread t2 = new Thread(new Bar());
        t1.run();
        t2.start();
        System.out.print("f");
        /*
        aebccdfd
        The difference is that Thread.start() starts a thread that calls the
        run() method, while Runnable.run() just calls the run() method on the
        current thread.
        */
    }
}
