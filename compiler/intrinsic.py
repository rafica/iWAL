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




# this string is appended to driver variable. hence other variables used in our program shouldnt begin with 'driver'. driver is reserverd word





# ***************IMPORTANT : TO DO*********************
# CHECK FOR SYMBOLS OTHER THAN _ , NUMBERS, ALPHABETS IN DRIVERNUMBER IN START FUNCTION

# In tab function, second parameter is integer. I have written functionality for both positive integers and negative integers. positive will jump forward, negative
#   will jump backwords. But NEGATIVE INTEGERS NOT WORKING IN FUNCTION CALL. ASSIGNING TYPE 'ERROR' INSTEAD OF 'INT' . My guess is some problem with ICONST in lexer

# Test java code generated for negative input in tab function

# in addition to generating code for input, click an element, we also have to check if that element is present with the given name. Some function is there in
#   selenium to do that. If element is not present, we have to catch that and display it to the user
#**********************************************************


from csv import reader
from cStringIO import StringIO


def close_function(s, node, scope, error_flag):
    if len(node.children[1].datatype)!= 1:
        print "Line Number ", node.lineno, ": Inbuilt function 'close' takes 1 parameter, ",len(node.children[1].datatype)," given"
        close_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'close' should be a 'string', '",node.children[1].datatype[0],"' given"
        close_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'    
    else:
        driverNumber = node.children[1].code
        driverNumber = driverNumber.replace('"',"").strip()
        #delete from symbol table
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            s[key]['start'].remove(driverNumber)        
        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'
            return
                
        node.code = 'driver'+ str(driverNumber) +'.close()'    
        node.datatype = 'void'
    

def start_function(s, node, scope, error_flag):
    #check number of parameters is 1

    if len(node.children[1].datatype)!= 1:
        print "Line Number ", node.lineno, ": Inbuilt function 'start' takes 1 parameter, ",len(node.children[1].datatype)," given"
        start_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'start' should be a 'string', '",node.children[1].datatype[0],"' given"
        start_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'    
    else:
            
        driverNumber = node.children[1].code
        driverNumber = driverNumber.replace('"',"").strip() #CHECK FOR SYMBOLS?.,><> ETC AND THROW ERROR"
        #store the driver name in symbol table
        key = 0
        if key in s:
            if 'start' in s[key]:
                if driverNumber not in s[key]['start']:
                    s[key]['start'].append(driverNumber)
                else:
                    print "Line Number ",node.lineno, ": Browser with the id '", driverNumber,"' is already open"
                    node.code = "ERROR ERROR ERROR"
                    node.datatype = 'error'
                    return
            else:
                s[key]['start'] = [driverNumber]
        else:
            s[key]= {}
            s[key]['start'] = [driverNumber]
        
        node.code = 'WebDriver driver'+ str(driverNumber) +' = new ChromeDriver()'     
        node.datatype = 'void'


def open_function(s, node,scope, error_flag):

    param = node.children[1].code.split(',')
    
    if len(node.children[1].datatype)!= 2 or len(param)!=2:
        print "Line Number ", node.lineno, ": Inbuilt function 'open' takes 2 parameters, ",len(node.children[1].datatype)," given"
        open_syntax() #print syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'open' should be a 'string', '",node.children[1].datatype[0],"' given"
        open_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'         
    elif node.children[1].datatype[1]!='string':
        print "Line Number ", node.lineno, ": Second parameter of Inbuilt function 'open' should be a 'string', '",node.children[1].datatype[1],"' given"
        open_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'       
    else:
        driverNumber = param[0]
        url = param[1]
        driverNumber = driverNumber.replace('"',"").strip()
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            node.code  = 'driver'+ str(driverNumber) +'.get('+ url +')'
            node.datatype = 'void'
        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'



def input_function(s, node, scope, error_flag):
    param = node.children[1].code.split(',')
    
    if len(node.children[1].datatype)!=2 or len(param)!=2:
        print "Line Number ", node.lineno, ": Inbuilt function 'input' takes 2 parameters, ",len(node.children[1].datatype)," given"
        input_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'input' should be a 'string', '",node.children[1].datatype[0],"' given"
        input_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'         
    elif node.children[1].datatype[1]!='string':
        print "Line Number ", node.lineno, ": Second parameter of Inbuilt function 'input' should be a 'string', '",node.children[1].datatype[1],"' given"
        input_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'       
    else:
        driverNumber = param[0]
        text = param[1]
        driverNumber = driverNumber.replace('"',"").strip()
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            node.code = 'driver'+ str(driverNumber) +'.switchTo().activeElement().sendKeys('+text+')'
            node.datatype = 'void'
        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'



def inputE_function(s, node, scope, error_flag):
    param = node.children[1].code.split(',')
    
    if len(node.children[1].datatype)!=3 or len(param)!=3:
        print "Line Number ", node.lineno, ": Inbuilt function 'inputE' takes 3 parameters, ",len(node.children[1].datatype)," given"
        inputE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'inputE' should be a 'string', '",node.children[1].datatype[0],"' given"
        inputE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[1]!='string':
        print "Line Number ", node.lineno, ": Second parameter of Inbuilt function 'inputE' should be a 'string', '",node.children[1].datatype[1],"' given"
        inputE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[2]!='string':
        print "Line Number ", node.lineno, ": Third parameter of Inbuilt function 'inputE' should be a 'string', '",node.children[1].datatype[2],"' given"
        inputE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    else:
        driverNumber = param[0]
        element_name = param[1]
        text = param[2]
        driverNumber = driverNumber.replace('"',"").strip()
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            node.code = 'driver'+ str(driverNumber) +'.findElement(By.name('+ element_name +')).sendKeys('+text+')'
            node.datatype = 'void'
        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'

##    elif p[1]=='click':
##        p[0] = 'driver'+str(driverNumber) + '.switchTo().activeElement().click()'
##
##    elif p[1] == 'clickE':
##        p[0] = 'driver'+str(driverNumber)+'.findElement(By.name('+p[3]+'))'


def click_function(s, node, scope, error_flag):
    param = node.children[1].code.split(',')
    
    if len(node.children[1].datatype)!=1 or len(param)!=1:
        print "Line Number ", node.lineno, ": Inbuilt function 'click' takes 1 parameter, ",len(node.children[1].datatype)," given"
        click_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'click' should be a 'string', '",node.children[1].datatype[0],"' given"
        click_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'            
    else:
        driverNumber = param[0]
        driverNumber = driverNumber.replace('"',"").strip()
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            node.code = 'driver'+ str(driverNumber) +'.switchTo().activeElement().click()'
            node.datatype = 'void'
        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'



def clickE_function(s, node, scope, error_flag):
    param = node.children[1].code.split(',')
    
    if len(node.children[1].datatype)!=2 or len(param)!=2:
        print "Line Number ", node.lineno, ": Inbuilt function 'clickE' takes 2 parameters, ",len(node.children[1].datatype)," given"
        clickE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'clickE' should be a 'string', '",node.children[1].datatype[0],"' given"
        clickE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[1]!='string':
        print "Line Number ", node.lineno, ": Second parameter of Inbuilt function 'clickE' should be a 'string', '",node.children[1].datatype[1],"' given"
        clickE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    else:
        driverNumber = param[0]
        element_name = param[1]
        driverNumber = driverNumber.replace('"',"").strip()
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            node.code = 'driver'+str(driverNumber)+'.findElement(By.name('+element_name+')).click()'  #NOT SURE IF JAVA CODE IS CORRECT.
            node.datatype = 'void'
        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'



def clickLink_function(s, node, scope, error_flag):
    param = node.children[1].code.split(',')
    
    if len(node.children[1].datatype)!=2 or len(param)!=2:
        print "Line Number ", node.lineno, ": Inbuilt function 'clicklink' takes 2 parameters, ",len(node.children[1].datatype)," given"
        clicklink_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'clicklink' should be a 'string', '",node.children[1].datatype[0],"' given"
        clicklink_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[1]!='string':
        print "Line Number ", node.lineno, ": Second parameter of Inbuilt function 'clicklink' should be a 'string', '",node.children[1].datatype[1],"' given"
        clicklink_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    else:
        driverNumber = param[0]
        element_name = param[1]
        driverNumber = driverNumber.replace('"',"").strip()
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            node.code = 'driver'+str(driverNumber)+'.findElement(By.linkText('+element_name+')).click()'  #NOT SURE IF JAVA CODE IS CORRECT.
            node.datatype = 'void'

        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'


            
def getPageText_function(s, node, scope, error_flag):
    param = node.children[1].code.split(',')
    if len(node.children[1].datatype)!=1 or len(param)!=1:
        print "Line Number ", node.lineno, ": Inbuilt function 'getPageText' takes 1 parameters, ",len(node.children[1].datatype)," given"
        getPageText_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'getPageText' should be a 'string', '",node.children[1].datatype[0],"' given"
        getPageText_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'

    else:
        driverNumber = param[0]
        driverNumber = driverNumber.replace('"',"").strip()
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            node.code = 'driver'+str(driverNumber)+'.findElement(By.xpath("//body")).getText()'
            node.datatype = 'string'
        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'
            
'driver'+str(driverNumber)+'.findElement(By.name('+element_name+'))
    
def tab_function(s, node, scope, error_flag):
    param = node.children[1].code.split(',')
    if len(node.children[1].datatype)!=2 or len(param)!=2:
        print "Line Number ", node.lineno, ": Inbuilt function 'tab' takes 2 parameters, ",len(node.children[1].datatype)," given"
        tab_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'tab' should be a 'string', '",node.children[1].datatype[0],"' given"
        tab_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[1]!='int':
        print "Line Number ", node.lineno, ": Second parameter of Inbuilt function 'tab' should be a 'int', '",node.children[1].datatype[1],"' given"
        tab_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    else:
        driverNumber = param[0]
        jump_number = param[1]
        driverNumber = driverNumber.replace('"',"").strip()
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            if int(jump_number)>0:
                node.code = "for(int loop"+str(scope)+"=0;loop"+str(scope)+"<"+str(jump_number)+";loop"+str(scope)+"++)\n"
                node.code = node.code + 'driver'+str(driverNumber)+'.switchTo().activeElement().sendKeys(Keys.TAB)'
                node.datatype = 'void'
            else:
                node.code ="Actions builder = new Actions(driver"+str(driverNumber)+");\n"
                node.code = node.code + "for(int loop"+str(scope)+"=0;loop"+str(scope)+"<"+str(int(jump_number)*-1)+";loop"+str(scope)+"++)\n"
                node.code = node.code + "builder.keyDown(Keys.SHIFT).sendKeys(Keys.TAB).keyUp(Keys.SHIFT).build().perform()"
                node.datatype = 'void'
        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'

def tabE_function(s, node, scope, error_flag):
    param = node.children[1].code.split(',')
    if len(node.children[1].datatype)!=3 or len(param)!=3:
        print "Line Number ", node.lineno, ": Inbuilt function 'tabE' takes 3 parameters, ",len(node.children[1].datatype)," given"
        tabE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'tabE' should be a 'string', '",node.children[1].datatype[0],"' given"
        tabE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[1]!='string':
        print "Line Number ", node.lineno, ": Second parameter of Inbuilt function 'tabE' should be a 'string', '",node.children[1].datatype[1],"' given"
        tabE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[1]!='int':
        print "Line Number ", node.lineno, ": Third parameter of Inbuilt function 'tabE' should be a 'int', '",node.children[1].datatype[1],"' given"
        tabE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    else:
        driverNumber = param[0]
        jump_number = param[1]
        element_name = param[2]
        driverNumber = driverNumber.replace('"',"").strip()
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            if int(jump_number)>0:
                node.code = "WebElement element = driver"+str(driverNumber)+".findElement(By.name("+element_name+"));\n"
                node.code = "for(int loop"+str(scope)+"=0;loop"+str(scope)+"<"+str(jump_number)+";loop"+str(scope)+"++){\n"
                node.code = node.code + "element.sendKeys(Keys.TAB);"
                node.code = node.code + 'element = driver'+str(driverNumber)+'.switchTo().activeElement();}'
                node.datatype = 'void'
            else:
                node.code ="Actions builder = new Actions(driver"+str(driverNumber)+");\n"
                node.code = node.code + "new Actions(driver).moveToElement(driver"+str(driverNumber)+".findElement(By.name("+element_name+"))).perform()";
                node.code = node.code + "for(int loop"+str(scope)+"=0;loop"+str(scope)+"<"+str(int(jump_number)*-1)+";loop"+str(scope)+"++)\n"
                node.code = node.code + "builder.keyDown(Keys.SHIFT).sendKeys(Keys.TAB).keyUp(Keys.SHIFT).build().perform()"
                node.datatype = 'void'
        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'



def userInput_function(s, node, scope, error_flag):
    node.type = 'userinput_function'
    if(len(node.children[1].datatype)!=1):
        print "Line Number ", node.lineno, ": Inbuilt function 'userinput' takes 1 parameters, ",len(node.children[1].datatype)," given"
        userinput_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif(node.children[1].datatype[0]!='string'):
        print "Line Number ", node.lineno, ": Parameter of Inbuilt function 'userinput' should be a 'string', '",node.children[1].datatype[0],"' given"
        userinput_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    else:
        returntype = node.children[1].code.replace('"','')
        node.datatype = returntype
        if(returntype == "string"):
            node.code = 'new Scanner(System.in).next()'
        elif(returntype == "int"):
            node.code = 'new Scanner(System.in).nextInt()'
            print node.code
        elif(returntype == "float"):
            node.code = 'new Scanner(System.in).nextFloat()'
        else:
            print "Line Number ", node.lineno, ": only int, float, string allowed as a parameter"
            userinput_syntax() #print the syntax
            node.code = 'ERROR ERROR ERROR'
            node.datatype = 'error'

def passwordInput_function(s, node, scope, error_flag):
    node.type = 'passwordinput_function'
    if(len(node.children[1].datatype)!=0):
        print "Line Number ", node.lineno, ": Inbuilt function 'passwordinput' takes no parameters, ",len(node.children[1].datatype)," given"
        passwordinput_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'

    else:
        node.datatype = "string"
        node.code = 'new String(System.console().readPassword())'

def print_function(s, node, scope, error_flag):
    params = node.children[1].code
    quote_flag = 0
    node.code = 'System.out.println('

    file_like_object = StringIO(params)
    csv_reader = reader(file_like_object, quotechar = '"')
    
    parameter_list = []
    for row in csv_reader:            
        parameter_list = row
    for i in range(len(parameter_list)):
        if i == len(parameter_list)-1:
            if node.children[1].datatype[i].replace('"','')=='string':
                string = parameter_list[i].strip()
                if string.startswith('"') and string.endswith('"'):
                    string = string[1:-1]
                node.code = node.code + '"'+ string + '"'
            else:
                node.code = node.code + "String.valueOf("+ str(parameter_list[i])+")"
        else:
            if node.children[1].datatype[i].replace('"','')=='string':
                string = parameter_list[i].strip()
                if string.startswith('"') and string.endswith('"'):
                    string = string[1:-1]
                
                node.code = node.code + '"'+ string +'"+'
            else:
                node.code = node.code + "String.valueOf("+ str(parameter_list[i])+")" + '+'
    node.code = node.code + ")"
    node.type = 'void'
                       
        
def userInput_syntax():
    print "\nSyntax of userInput : userInput(input_datatype); "
    print "--'input_datatype'"
    print "   * is the datatype of the input"
    

def passwordInput_syntax():
    print "\nSyntax of passwordInput : passwordInput(); "

def getPageText_syntax():
    print "\nSyntax of getPageText_syntax : getPageText_syntax(browser_id); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * is of string type"
    
def tabE_syntax():
    print "\nSyntax of tabE : tabE(browser_id, element_name, jump_times); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * is of string type"
    print "   * can have letters, digits, dollar signs, or underscore characters"
    print "--'element_name'"
    print "   * is the name of the text box element"
    print "   * is of string type"
    print "--'jump_times'"
    print "   * if positive, it is the number of times Tab key has to be pressed"
    print "   * if negative, it is the number of times Shift+Tab key has to be pressed"    #<------TRIED SOMETHING NEW. NOT SURE IF IT WILL WORK. TEST IT
    print "   * is of integer type"

def tab_syntax():
    print "\nSyntax of tab : tab(browser_id, jump_times); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * is of string type"
    print "   * can have letters, digits, dollar signs, or underscore characters"
    print "--'jump_times'"
    print "   * if positive, it is the number of times Tab key has to be pressed"
    print "   * if negative, it is the number of times Shift+Tab key has to be pressed"    #<------TRIED SOMETHING NEW. NOT SURE IF IT WILL WORK. TEST IT
    print "   * is of integer type"

def close_syntax():
    print "\nSyntax of close : close(browser_id, URL); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * can have letters, digits, dollar signs, or underscore characters"
    print "   * is of string type"

def open_syntax():
    print "\nSyntax of open : open(browser_id, URL); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * can have letters, digits, dollar signs, or underscore characters"
    print "   * is of string type"
    print "--'URL'"
    print "   * should be a valid URL"
    print "   * is of string type"

def start_syntax():
    print "\nSyntax of start : start(browser_id); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * can have letters, digits, dollar signs, or underscore characters"
    print "   * is of string type"
     
def click_syntax():
    print "\nSyntax of click : click(browser_id); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * is of string type"
    print "   * can have letters, digits, dollar signs, or underscore characters"

def clickE_syntax():
    print "\nSyntax of clickE : clickE(browser_id, element_name); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * is of string type"
    print "   * can have letters, digits, dollar signs, or underscore characters"
    print "--'element_name'"
    print "   * is the name of the text box element"
    print "   * is of string type"


def clicklink_syntax():
    print "\nSyntax of clicklink : clickE(browser_id, link_text); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * is of string type"
    print "   * can have letters, digits, dollar signs, or underscore characters"
    print "--'link_text'"
    print "   * is the text of the link"
    print "   * is of string type"

    
def input_syntax():
    print "\nSyntax of input : input(browser_id, input_text); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * is of string type"
    print "   * can have letters, digits, dollar signs, or underscore characters"
    print "--'input_text'"
    print "   * is the input text for current element"
    print "   * is of string type"


def inputE_syntax():
    print "\nSyntax of inputE : inputE(browser_id, element_name, input_text); "
    print "--'browser_id'"
    print "   * is the unique name given to browser"
    print "   * is of string type"
    print "   * can have letters, digits, dollar signs, or underscore characters"
    print "--'element_name'"
    print "   * is the name of the text box element"
    print "   * is of string type"
    print "--'input_text'"
    print "   * is the input text for current URL"
    print "   * is of string type"
