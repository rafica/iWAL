import java.util.Scanner;import org.openqa.selenium.By;import org.openqa.selenium.Keys; import org.openqa.selenium.WebDriver;import org.openqa.selenium.WebElement;import org.openqa.selenium.chrome.ChromeDriver;public class Target  {    public static void main(String[] args) {        System.setProperty("webdriver.chrome.driver", "/Users/nithin/Desktop/Spring_2014/PLT/project/tools/chromedriver");        WebDriver driver1 = new ChromeDriver(); String url = "http://ssol.columbia.edu/" ; driver1.get(url); String username = "username" ; driver1.switchTo().activeElement().sendKeys(username); String password = "password" ; driver1.findElement(By.name(password)).sendKeys(username); driver1.close();} }