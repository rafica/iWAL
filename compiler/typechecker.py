import nithin, priyanka, ashima, rafica, pranita

symbol_table = {}
func_dict = {"declaration_statement_1" : nithin.declaration_statement_1
             "" : ,
             "" : ,
             "" : ,
             "" :
             }
scope = 0

scope_incrementers = ['function_definition_1', 'function_definition_2', 'iteration_statement_1', 'iteration_statement_2', 'selection_statement_1', 'selection_statement_2']

def postorder(root, scope):
    if type(root) != Node:
        return
    else:
        if root.type in scope_incrementers:
            scope = scope + 1
        for i in root.children:
            postorder(i, scope)
            
        func_dict[root.type](symbol_table, root, scope)
        
        if root.type in scope_incrementers:
            symbol_keys = s.keys()
            for j in s.keys():
                if j[2]==scope:
                    pass
