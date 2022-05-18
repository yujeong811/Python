package day02;

public class OopTest {
	public static void main(String[] args) {
		Human hum =  new Human();
		System.out.println(hum.age);
		System.out.println(hum.skill_lang);
		hum.getOld();
		hum.momstouch(10);
		System.out.println(hum.age);
		System.out.println(hum.skill_lang);
	}
}
