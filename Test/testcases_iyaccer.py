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
    
    return_st = """
    int func(int a)
    {
    int x;
    x = a;
    return x;
    }"""


    if_st = """
    int a = 5;
    int b = 5;
    if(a == b)
    {
      a = 1;
    }"""


    if_else_st = """
    int a = 1;
    int b = 2;
    if(a==b){}
    else
    {
     a = b;
    }"""


    arithmetic_relations = """
    int a =2;
    int b =3;
    int c = 4;
    a + b;
    a - b;
    a * b;
    a / b;
    2 > 3;
    4 >= 5;
    b == c;
    b != c;
    b < 5;
    b <= 7;
    """

    logical_relations = """
    int a = 5;
    int b = 7;
    boolean c;
    c = a || b;
    c = a && b;
    c = !a;
    """

    complex_prg = """
    int a = 3;
    int c = 5;
    boolean b;
    int z;
    b = a * (a - 3) + 3 || 5 && 8;
    void func()
    {
     print("Inside function");
    }
    """
    
    def __init__(self):
        pass
