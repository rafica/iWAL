import java.util.Scanner;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;


public class getSchedule {
	
	public static void main(String[] args) {


			
			Scanner s = new Scanner(System.in);
			System.out.println("Enter password:");
			String password = s.next();
			
			System.setProperty("webdriver.chrome.driver", "/Users/sushchat123/Desktop/chromedriver");
			WebDriver driver = new ChromeDriver();


	        driver.get("http://ssol.columbia.edu");
			
			

	        WebElement username = driver.findElement(By.name("u_id"));


	        // Enter something to search for

	        username.sendKeys("pd2438");

	        username.sendKeys(Keys.TAB);

	        WebElement passwd = driver.findElement(By.name("u_pw"));

	        passwd.sendKeys(password);


	        // Now submit the form. WebDriver will find the form for us
	//from the element

	        passwd.submit();
	        
	        driver.findElement(By.linkText("Student Schedule")).click();
	        
	        String stored_report = driver.findElement(By.xpath("//body")).getText();
	        System.out.println(stored_report);
	        
	        
	      
	    }


}
