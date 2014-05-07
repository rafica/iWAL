import java.util.Scanner;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Target  {

public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "chromedriver");
int a;
a=-11;
if(a==1){a=1;
}WebDriver driverrafica = new ChromeDriver();
WebDriver drivernithin = new ChromeDriver();
driverrafica.get( "https://www.google.com");
drivernithin.get( "https://ssol.columbia.edu");
for(int loop1=0;loop1< 1;loop1++)
driverrafica.switchTo().activeElement().sendKeys(Keys.TAB);
driverrafica.switchTo().activeElement().sendKeys( "username");

}
}