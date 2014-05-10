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
WebDriver driverdriver1 = new ChromeDriver();
driverdriver1.get( "https://ssol.columbia.edu");
for(int loopdriver11=0;loopdriver11< 1;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
driverdriver1.switchTo().activeElement().sendKeys( "pd2438");
String s = new String(System.console().readPassword());
for(int loopdriver11=0;loopdriver11< 1;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
driverdriver1.switchTo().activeElement().sendKeys( s);
for(int loopdriver11=0;loopdriver11< 1;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
Thread.sleep(1000);
driverdriver1.switchTo().activeElement().click();

}
}