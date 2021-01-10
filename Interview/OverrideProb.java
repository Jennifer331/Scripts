public class SuperTest { // 类SuperTest是公共的, 应在名为 SuperTest.java 的文件中声明
    public Integer getLength() {
        return new Integer(4);
    }
}

class OverrideProb extends SuperTest{
    // OverrideProb中的getLength()无法覆盖SuperTest中的getLength()
    //返回类型Long与Integer不兼容
    public Long getLength() {
        return new Long(5);
    }

    public static void main(String[] args) {
        SuperTest sooper = new SuperTest();
        OverrideProb sub = new OverrideProb();

        System.out.println(sooper.getLength().toString() + "," +
        sub.getLength().toString());
    }
}
