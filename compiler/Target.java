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
String s = new Scanner(System.in).next();
driverdriver1.switchTo().activeElement().sendKeys( s);
s=new String(System.console().readPassword());
for(int loopdriver11=0;loopdriver11< 1;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
driverdriver1.switchTo().activeElement().sendKeys( s);
for(int loopdriver11=0;loopdriver11< 1;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
driverdriver1.switchTo().activeElement().click();
for(int loopdriver11=0;loopdriver11< 21;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
driverdriver1.switchTo().activeElement().click();
for(int loopdriver11=0;loopdriver11< 36;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
driverdriver1.switchTo().activeElement().sendKeys( "646");
driverdriver1.switchTo().activeElement().sendKeys( "462");
driverdriver1.switchTo().activeElement().sendKeys( "1606");
for(int loopdriver11=0;loopdriver11< 2;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
driverdriver1.switchTo().activeElement().click();

}
}