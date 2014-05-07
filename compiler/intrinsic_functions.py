##
##    if (p[1]=='start' or p[1]=='close' or p[1]=='click') and not p[3]=='':
##        print 'In line number',p.lineno(2),'...',p[1],'does not take any arguments'
##        errorFlag = 1
##
##    elif (p[1]=='input' or p[1]=='clickE' or p[1]=='tab') and (not len(param)==1 or param[0]==''):
##        print 'In line number',p.lineno(2),'...',p[1],'takes 1 argument'
##        param = ['"error"']
##        errorFlag = 1
##
##    elif (not len(param)==2 or param[0]=='') and (p[1]=='inputE'):                                                  ## If your function needs exactly 2 parameters append it here
##        print 'In line number',p.lineno(2),'...',p[1],'takes 2 arguments'
##        param = ['"error1"', '"error2"']
##        errorFlag = 1
##
##    if p[1]=='start':
##        driverNumber+=1
##        p[0] = 'WebDriver driver'+ str(driverNumber) +' = new ChromeDriver()'
##            
##    elif p[1]=='open':                      ###################  JAVA will handle the error for this ; errors can be : 1) URL might not be a string, 2) Mutiple parameters might be passed.
##        p[0] = 'driver'+ str(driverNumber) +'.get('+p[3]+')'
##
##    elif p[1]=='close':
##        p[0] = 'driver'+ str(driverNumber) +'.close()'
##        driverNumber = driverNumber - 1
##
##    elif p[1]=='input':
##       p[0] = 'driver'+ str(driverNumber) +'.switchTo().activeElement().sendKeys('+param[0]+')'
##       
##    elif p[1]=='inputE':
##       p[0] = 'driver'+ str(driverNumber) +'.findElement(By.name('+param[1]+')).sendKeys('+param[0]+')'
##       
##    elif p[1]=='click':
##        p[0] = 'driver'+str(driverNumber) + '.switchTo().activeElement().click()'
##
##    elif p[1] == 'clickE':
##        p[0] = 'driver'+str(driverNumber)+'.findElement(By.name('+p[3]+'))'
##
##    elif p[1] == 'tab':
##        p[0] = 'driver'+str(driverNumber)+'.switchTo().activeElement().sendKeys(Keys.TAB)'
##        
##    else:
##        p[0] = p[1] + ' ( ' + p[3] + ' ) '

def open_function():
    pass
