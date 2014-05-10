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
    {
    void findSum(int a,int b){
        int result = a+b;
    }
    }"""
    
    def __init__(self):
        pass
