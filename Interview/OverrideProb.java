public class SuperTest { // ��SuperTest�ǹ�����, Ӧ����Ϊ SuperTest.java ���ļ�������
    public Integer getLength() {
        return new Integer(4);
    }
}

class OverrideProb extends SuperTest{
    // OverrideProb�е�getLength()�޷�����SuperTest�е�getLength()
    //��������Long��Integer������
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
