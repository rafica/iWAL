import nithin, priyanka, ashima, rafica, pranita

symbol_table = {}
func_dict = {"declaration_statement_1" : nithin.declaration_statement_1,
             "" : ,
             "" : ,
             "" : ,
             "" :
             }
scope = 0

def postorder(root, scope):
    if type(root) != Node:
        return
    else:
        if root.type=='function_definition_1' or root.type=='function_definition_2':
            scope = scope + 1
        for i in root.children:
            postorder(i, scope)
        scope = func_dict[root.type](symbol_table, root, scope)
