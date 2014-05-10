class iWALTestCases(object):
    """
    Wrapper class for iyaccer test cases. These are iWAL code
    snippets
    """

    compound = """
    { int i=0;int j=1;int k=2;
    }"""

    repeat = """
    {
    repeat(5){
        print("test");
    }
    }"""

    until = """
    {
    int x = 5;
    until(x>0){
    x = x-1;
    }
    }"""

    function_definition = """
    void findSum(int a,int b){
        int result = a+b;}
    """

    break_statement = """
    {int i=1;
    if(i>3){
    break;
    }
    else{
    i=i+1;
    }
    print(i);
    }"""

    continue_statement = """
    {
    repeat(3){
        print("test");
    }
    }"""

    function_call = """
    void printNum(double x){
        print(x);
    }
    printNum(5);
    """

    declarations = """
    int x=2;
    double y=0.23;
    boolean z=true;
    key press=enter;
    """
    def __init__(self):
        pass
