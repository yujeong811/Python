package day08;

public class RefTest {

	public static void main(String[] args) {
		int a = 0;
		int[] b = {1};
		System.out.println("a : " + a);
		System.out.println("b + " + b[0]);
		myincrease1(a);
		myincrease2(b);
		System.out.println("a : " + a);
		System.out.println("b + " + b[0]);
	}
	
	public static void myincrease1(int cnt) {
		cnt++;
	}

	public static void myincrease2(int[] arr) {
		arr[0]++;
	}
}
