package sample_programs;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class HelloWorld {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//System.out.println("Hello World !!");

        WebDriver driver = new ChromeDriver();
      // And now use this to visit Google
        driver.get("http://ssol.columbia.edu");
        // Alternatively the same thing can be done like this driver.navigate().to("http://www.google.com");
	}

}
