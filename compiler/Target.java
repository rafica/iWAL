import java.util.Scanner;
import java.io.Console;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Target  {
public static int func1(int a) {
 String s = "string";
 int b = 2;
 a=a + 1;
 return a ; }
public static int func2(int a) {
 a=a + 1;
 return a ; }
public static int func3(int a) {
 a=a + 1;
 return a ; }
public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "chromedriver");
key k = space;
boolean x = true;
boolean y = false;
y=!y;
if(y){
int a = 1;

}WebDriver drivera = new ChromeDriver();
drivera.get( "https://www.google.com");
for(int loop1=0;loop1< 1;loop1++)
drivera.switchTo().activeElement().sendKeys(Keys.TAB);
drivera.switchTo().activeElement().sendKeys( "Search Query");
}
}