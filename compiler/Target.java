import java.util.Scanner;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Target  {

public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "chromedriver");
WebDriver driverrafica = new ChromeDriver();
int a;
a=1;
WebDriver driverrafica1 = new ChromeDriver();
driverrafica.get( "www.google.com");
driverrafica.switchTo().activeElement().sendKeys( "username");
driverrafica.switchTo().activeElement().click();
ERROR ERROR ERROR;
driverrafica1.close();

}
}