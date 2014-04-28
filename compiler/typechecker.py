import nithin, priyanka, ashima, rafica, pranita

s = {}
func_dict = {"declaration_statement_1" : nithin.declaration_statement_1,
             "" : ,
             "" : ,
             "" : ,
             "" :
             }
scope = 0

def inorder(root):
    if type(root) != Node:
        return
    else:
        for i in root.children:
            inorder(i)
        scope = func_dict[root.type](s, root, scope)

