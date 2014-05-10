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
WebDriver drivera = new ChromeDriver();
drivera.get( "https://www.surveymonkey.com/s/5WD55L2");
for(int loopa1=0;loopa1< 1;loopa1++)
drivera.switchTo().activeElement().sendKeys(Keys.TAB);
String s = new Scanner(System.in).next();
drivera.switchTo().activeElement().sendKeys( s);
for(int loopa1=0;loopa1< 1;loopa1++)
drivera.switchTo().activeElement().sendKeys(Keys.TAB);
s=new Scanner(System.in).next();
drivera.switchTo().activeElement().sendKeys( s);
for (int loop2 = 0; loop2 <7 ; loop2++){
for(int loopa2=0;loopa2< 1;loopa2++)
drivera.switchTo().activeElement().sendKeys(Keys.TAB);
 drivera.switchTo().activeElement().sendKeys( "This is the text to be filled ...");

}

}
}