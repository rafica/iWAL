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
System.out.println("Enter your UNI :");
String s1 = new Scanner(System.in).next();
driverdriver1.switchTo().activeElement().sendKeys( s1);
for(int loopdriver11=0;loopdriver11< 1;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
System.out.println("Enter your password :");
String s2 = new String(System.console().readPassword());
driverdriver1.switchTo().activeElement().sendKeys( s2);
for(int loopdriver11=0;loopdriver11< 1;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
driverdriver1.switchTo().activeElement().click();
for(int loopdriver11=0;loopdriver11< 15;loopdriver11++)
driverdriver1.switchTo().activeElement().sendKeys(Keys.TAB);
driverdriver1.switchTo().activeElement().click();
String s = driverdriver1.findElement(By.xpath("//body")).getText();
System.out.println(s);
out = new BufferedWriter(new FileWriter("grades.txt"));
out.write( s);
out.close();

}
}