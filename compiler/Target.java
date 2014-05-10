import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.Console;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
public class Target  {
static WebElement element; 
static BufferedWriter out; 
static Actions builder;

public static void main(String[] args) throws Exception {
        System.setProperty("webdriver.chrome.driver", "chromedriver");
key k = up;
WebDriver drivera = new ChromeDriver();
drivera.get( "https://www.surveymonkey.com/s/5TKSLBH");
for(int loopa1=0;loopa1< 1;loopa1++)
drivera.switchTo().activeElement().sendKeys(Keys.TAB);
drivera.switchTo().activeElement().sendKeys( "ajfskjbdkjbnskvjbs");
for(int loopa1=0;loopa1< 1;loopa1++)
drivera.switchTo().activeElement().sendKeys(Keys.TAB);
drivera.switchTo().activeElement().click();
for(int loopa1=0;loopa1< 1;loopa1++)
drivera.switchTo().activeElement().sendKeys(Keys.TAB);

}
}