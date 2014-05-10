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
            node.code = 'driver'+str(driverNumber)+'.findElement(By.linkText('+element_name+')).click()' 
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
                node.code = "for(int loop"+str(driverNumber)+str(scope)+"=0;loop"+str(driverNumber)+str(scope)+"<"+str(jump_number)+";loop"+str(driverNumber)+str(scope)+"++)\n"
                node.code = node.code + 'driver'+str(driverNumber)+'.switchTo().activeElement().sendKeys(Keys.TAB)'
                node.datatype = 'void'
            else:
                node.code ="Actions builder = new Actions(driver"+str(driverNumber)+");\n"
                node.code = node.code + "for(int loop"+str(driverNumber)+str(scope)+"=0;loop"+str(driverNumber)+str(scope)+"<"+str(int(jump_number)*-1)+";loop"+str(driverNumber)+str(scope)+"++)\n"
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
    elif node.children[1].datatype[2]!='int':
        print "Line Number ", node.lineno, ": Third parameter of Inbuilt function 'tabE' should be a 'int', '",node.children[1].datatype[1],"' given"
        tabE_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    else:
        driverNumber = param[0]
        jump_number = param[2]
        element_name = param[1]
        driverNumber = driverNumber.replace('"',"").strip()
        key = 0
        if key in s and 'start' in s[key] and driverNumber in s[key]['start']:
            if int(jump_number)>0:
                node.code = "element = driver"+str(driverNumber)+".findElement(By.name("+element_name+"));\n"
                node.code = node.code + "for(int loop"+str(driverNumber)+str(scope)+"=0;loop"+str(driverNumber)+str(scope)+"<"+str(jump_number)+";loop"+str(driverNumber)+str(scope)+"++){\n"
                node.code = node.code + "element.sendKeys(Keys.TAB);"
                node.code = node.code + 'element = driver'+str(driverNumber)+'.switchTo().activeElement();}'
                node.datatype = 'void'
            else:
                node.code ="builder = new Actions(driver"+str(driverNumber)+");\n"
                node.code = node.code + "new Actions(driver"+str(driverNumber)+").moveToElement(driver"+str(driverNumber)+".findElement(By.name("+element_name+"))).perform();\n";
                node.code = node.code + "for(int loop"+str(driverNumber)+str(scope)+"=0;loop"+str(driverNumber)+str(scope)+"<"+str(int(jump_number)*-1)+";loop"+str(driverNumber)+str(scope)+"++)\n{"
                node.code = node.code + "builder.keyDown(Keys.SHIFT).sendKeys(Keys.TAB).keyUp(Keys.SHIFT).build().perform();}"
                node.datatype = 'void'
        else:
            print "Line Number ",node.lineno, ": Browser with the id '",driverNumber,"' does not exist"
            node.code = "ERROR ERROR ERROR"
            node.datatype ='error'



def userInput_function(s, node, scope, error_flag):
    node.type = 'userinput_function'
    if(len(node.children[1].datatype)!=1):
        print "Line Number ", node.lineno, ": Inbuilt function 'userInput' takes 1 parameters, ",len(node.children[1].datatype)," given"
        userInput_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif(node.children[1].datatype[0]!='string'):
        print "Line Number ", node.lineno, ": Parameter of Inbuilt function 'userInput' should be a 'string', '",node.children[1].datatype[0],"' given"
        userInput_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    else:
        returntype = node.children[1].code.replace('"','')
        node.datatype = returntype
        if(returntype == "string"):
            node.code = 'new Scanner(System.in).next()'
        elif(returntype == "int"):
            node.code = 'new Scanner(System.in).nextInt()'
        elif(returntype == "float"):
            node.code = 'new Scanner(System.in).nextFloat()'
        else:
            print "Line Number ", node.lineno, ": only int, float, string allowed as a parameter"
            userInput_syntax() #print the syntax
            node.code = 'ERROR ERROR ERROR'
            node.datatype = 'error'

def passwordInput_function(s, node, scope, error_flag):
    node.type = 'passwordinput_function'
    if(len(node.children[1].datatype)!=0):
        print "Line Number ", node.lineno, ": Inbuilt function 'passwordinput' takes no parameters, ",len(node.children[1].datatype)," given"
        passwordInput_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'

    else:
        node.datatype = "string"
        node.code = 'new String(System.console().readPassword())'

def print_function(s, node, scope, error_flag):
    params = node.children[1].code
    quote_flag = 0
    node.code = 'System.out.println('

    if params[0] == '"':
        quote_flag = 1
    file_like_object = StringIO(params)
    csv_reader = reader(file_like_object, quotechar = '"')
    
    parameter_list = []
    for row in csv_reader:            
        parameter_list = row
    for i in range(len(parameter_list)):
        if i == 0 and quote_flag == 1:
            string = parameter_list[i].strip()
            string = '"'+string+'"'
            if i != len(parameter_list) - 1:
                string = string + '+'
            node.code = node.code + string
        elif i == len(parameter_list)-1:
            if node.children[1].datatype[i].replace('"','')=='string':
                string = parameter_list[i].strip()
                node.code = node.code + string 
            else:
                node.code = node.code + "String.valueOf("+ str(parameter_list[i])+")" 
        else:
            if node.children[1].datatype[i].replace('"','')=='string':
                string = parameter_list[i].strip()
                
                node.code = node.code + string + '+'
            else:
                node.code = node.code + "String.valueOf("+ str(parameter_list[i])+")" + '+'
    node.code = node.code + ")"
    node.type = 'void'
                       
def writeToFile_function(s, node, scope, error_flag):
    param = node.children[1].code.split(',')
    node.type = 'writeToFile_function'
    if(len(node.children[1].datatype)!=2):
        print "Line Number ", node.lineno, ": Inbuilt function 'writeToFile' takes 2 parameters, ",len(node.children[1].datatype)," given"
        writeToFile_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif(node.children[1].datatype[0]!='string'):
        print "Line Number ", node.lineno, ": Parameter of Inbuilt function 'writeToFile' should be a 'string', '",node.children[1].datatype[0],"' given"
        writeToFile_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif(node.children[1].datatype[0]!='string'):
        print "Line Number ", node.lineno, ": Parameter of Inbuilt function 'writeToFile' should be a 'string', '",node.children[1].datatype[0],"' given"
        writeToFile_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    else:
        path = param[0]
        text = param[1]
        node.code = 'out = new BufferedWriter(new FileWriter('+path+'));\nout.write('+text+');\n'
        node.code = node.code + 'out.close()'

def sleep_function(s, node, scope, error_flag):
    if len(node.children[1].datatype)!= 1:
        print "Line Number ", node.lineno, ": Inbuilt function 'sleep' takes 1 parameter, ",len(node.children[1].datatype)," given"
##        start_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='int':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'sleep' should be a 'int', '",node.children[1].datatype[0],"' given"
        sleep_syntax()
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'    
    else:
            
        sleepTime = node.children[1].code
        
        node.code = 'Thread.sleep('+sleepTime+')'     
        node.datatype = 'void'

def tap_function(s, node, scope, error_flag):
    param = node.children[1].code.split(',')
    if len(node.children[1].datatype)!=2 or len(param)!=2:
        print "Line Number ", node.lineno, ": Inbuilt function 'tap' takes 2 parameters, ",len(node.children[1].datatype)," given"
##        tab_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[0]!='string':
        print "Line Number ", node.lineno, ": First parameter of Inbuilt function 'tap' should be a 'string', '",node.children[1].datatype[0],"' given"
##        tab_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    elif node.children[1].datatype[1]!='key':
        print "Line Number ", node.lineno, ": Second parameter of Inbuilt function 'tap' should be a 'key', '",node.children[1].datatype[1],"' given"
##        tab_syntax() #print the syntax
        node.code = 'ERROR ERROR ERROR'
        node.datatype = 'error'
    else:
        driverNumber = param[0]
        key = param[1].strip()
        driverNumber = driverNumber.replace('"',"").strip()
        key = key.upper()
        node.code = 'driver'+str(driverNumber)+'.switchTo().activeElement().sendKeys(Keys.'+key+')'
        node.datatype = 'void'
    
def writeToFile_syntax():
    print "\nSyntax of writeToFile : writeToFile(file_path,string_to_write); "
    print "--'file_path'"
    print "   * is the path of the file to which you want to write"
    print "--'string_to_write'"
    print "   * is the string which you want to write to the file"

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

def sleep_syntax():
    print "\nSyntax of sleep : sleep(sleep_time); "
    print "--'sleep_time'"
    print "   * is the time for which you want your current thread (program) to sleep"
    
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
