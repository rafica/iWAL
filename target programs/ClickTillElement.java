package sample_programs;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class ClickTillElement {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
 
		// This program prints the text of all links from start link to end link. These elements cant
		// be identified by id because there is no id. so instead of currentElement.getAttribute("id"), 
		// currentElement.getText() is used.
		
        WebDriver driver = new ChromeDriver();
        driver.get("http://ssol.columbia.edu");
       WebElement username = driver.findElement(By.name("u_id"));
        username.sendKeys("ra2688");
        username.sendKeys(Keys.TAB);
        WebElement passwd = driver.findElement(By.name("u_pw"));
        passwd.sendKeys("******");
        passwd.submit();
        
        
        // skipping this element because the current element is the browser.
        WebElement currentElement = driver.switchTo().activeElement();
        currentElement.sendKeys(Keys.TAB);
        
        String start = "Academic Profile";
        String end = "Transcript Ordering";
        int flag = 0;
        while(true){
        	
        	currentElement = driver.switchTo().activeElement();
        	
        	String elemText = currentElement.getText();
            if(start.equals(elemText)){
            	flag = 1;	
            }
            else if(end.equals(elemText)){
            	System.out.println(elemText);
            	break;
            }
            if(flag==1){
            	System.out.println(elemText);
            }
            currentElement.sendKeys(Keys.TAB);
        	
        }
        
	}

}
