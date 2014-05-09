import java.util.Scanner;
import java.io.Console;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Target  {

public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "chromedriver");
boolean x = true;
boolean y = false;
if(x && y){
int a = 1;

}WebDriver drivera = new ChromeDriver();
drivera.get( "https://www.google.com");
for(int loop1=0;loop1< 1;loop1++)
drivera.switchTo().activeElement().sendKeys(Keys.TAB);
drivera.switchTo().activeElement().sendKeys( "Search Query");

}
}