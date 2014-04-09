package sample_programs;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class RepeatClicks {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

        WebDriver driver = new ChromeDriver();
      // And now use this to visit Google
        driver.get("http://www.brainbashers.com/10seconds.asp");
        // Alternatively the same thing can be done like this driver.navigate().to("http://www.google.com");
		
		
		
		// Find the text input element by its name
        WebElement area = driver.findElement(By.name("clickhere"));
        
        for(int i =0;i<20;i++){
        	
        	area.click();
        }
        /*
         * 
        // Enter something to search for
        username.sendKeys("ra2688");
        username.sendKeys(Keys.TAB);
        WebElement passwd = driver.findElement(By.name("u_pw"));

        passwd.sendKeys("*****");

        // Now submit the form. WebDriver will find the form for us from the element

        passwd.submit();
     //Close the browser
*/
	}

}
