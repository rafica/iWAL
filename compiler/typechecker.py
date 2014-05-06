import nithin, priyanka, ashima, rafica, pranita

import iyaccer

symbol_table = {}
func_dict = {   "declaration_statement_1" : nithin.declaration_statement_1,
                "declaration_statement_2" : nithin.declaration_statement_2,
                "translation_unit_1" : ashima.translation_unit_1,
                "translation_unit_2" : ashima.translation_unit_2,
                "statement_1" : ashima.statement_1,
                "statement_2" : ashima.statement_2,
                "statement_3" : ashima.statement_3,
                "statement_4" : ashima.statement_4,
                "statement_5" : ashima.statement_5,
                "statement_6" : ashima.statement_6,
                "statement_7" : ashima.statement_7,
                "additive_expression_1" : ashima.additive_expression_1,
                "additive_expression_2" : ashima.additive_expression_2,
                "additive_expression_3" : ashima.additive_expression_3,
                "constant_1" : ashima.constant_1,
                "constant_2" : ashima.constant_2,
                "constant_3" : ashima.constant_3,
                "expression_statement_1" : ashima.expression_statement_1,
                "expression_statement_2" : ashima.expression_statement_2,
                "type_1" : priyanka.type_1,
                "type_2" : priyanka.type_2,
                "type_3" : priyanka.type_3,
                "type_4" : priyanka.type_4,
                "type_5" : priyanka.type_5,
                "type_6" : priyanka.type_6,
                "logical_OR_expression_1" : priyanka.logical_OR_expression_1,
                "logical_OR_expression_2" : priyanka.logical_OR_expression_2,
                "expression_1" : priyanka.expression_1,
                "expression_3" : priyanka.expression_3,
                "relational_expression_1" : pranita.relational_expression_1,
                "relational_expression_2" : pranita.relational_expression_2,
                "relational_expression_3" : pranita.relational_expression_3,
                "relational_expression_4" : pranita.relational_expression_4,
                "relational_expression_5" : pranita.relational_expression_5,
                "logical_AND_expression_1" : pranita.logical_AND_expression_1,
                "logical_AND_expression_2" : pranita.logical_AND_expression_2,
                "primary_expression_1" : pranita.primary_expression_1,
                "primary_expression_2" : pranita.primary_expression_2,
                "primary_expression_3" : pranita.primary_expression_3,
                "primary_expression_4" : pranita.primary_expression_4,
                "primary_expression_5" : pranita.primary_expression_5,
                "multiplicative_expression_1" : pranita.multiplicative_expression_1,
                "multiplicative_expression_2" : pranita.multiplicative_expression_2,
                "multiplicative_expression_3" : pranita.multiplicative_expression_3,
                "assignment_expression_1" : rafica.assignment_expression_1,
                "assignment_expression_2" : rafica.assignment_expression_2,
                "assignment_expression_3" : rafica.assignment_expression_3,
                "assignment_expression_4" : rafica.assignment_expression_4,
                "external_declaration_1"  : rafica.external_declaration_1,
                "external_declaration_2"  : rafica.external_declaration_2,
                "selection_statement_1"   : rafica.selection_statement_1,
                "selection_statement_2"   : rafica.selection_statement_2,
                "compound_statement_1"    : rafica.compound_statement_1,
                "compound_statement_2"    : rafica.compound_statement_2,
                "function_expression_1"  : nithin.function_expression_1,
                "parameter_declaration_1"  : ashima.parameter_declaration_1,
                "parameter_declaration_2"  : ashima.parameter_declaration_2,
                "statement_8"  : ashima.statement_8,
                "equality_expression_1" : priyanka.equality_expression_1,
                "equality_expression_2" : priyanka.equality_expression_2,
                "equality_expression_3" : priyanka.equality_expression_3,
                "break_statement_1" : priyanka.break_statement_1,
                "statement_list_1" : pranita.statement_list_1,
                "statement_list_2" : pranita.statement_list_2,
                "parameter_list_1" : pranita.parameter_list_1,
                "parameter_list_2" : pranita.parameter_list_2,
                "return_statement_1" : pranita.return_statement_1,
                "return_statement_2" : pranita.return_statement_2,
                "function_definition_1" : nithin.function_definition_1,
                "function_definition_2" : nithin.function_definition_2,
                "empty_1" : nithin.empty_1,
                "parameter_declaration_list_1" : nithin.parameter_declaration_list_1,
                "parameter_declaration_list_2" : nithin.parameter_declaration_list_2,
                "iteration_statement_1" : ashima.iteration_statement_1,
                "iteration_statement_2" : ashima.iteration_statement_2
             }

scope_incrementers = ['function_definition_1', 'function_definition_2', 'iteration_statement_1', 'iteration_statement_2', 'selection_statement_1', 'selection_statement_2']
loops = ['iteration_statement_1', 'iteration_statement_2']
loop_controls = ['continue_statement_1', 'break_statement_1']
functions = ['function_definition_1', 'function_definition_2']
function_return = ['return_statement_1', 'return_statement_2']
loopFlag = 0
functionFlag = 0
def postorder(root, scope, loopFlag, functionFlag):

    if root.__class__.__name__ != 'Node':
        return
    else:
        if root.type in scope_incrementers:
            scope = scope + 1
        if root.type in loop_controls:
            if not loopFlag:
                print "error: "+root.type + " is not inside a loop"
        elif root.type in function_return:
            if not functionFlag:
                print "error: "+root.type + " is not inside a function"
        if root.type in loops:
            loopFlag = 1
        elif root.type in functions:
            functionFlag = 1
        
        for i in root.children:
            postorder(i, scope, loopFlag, functionFlag)
            
        func_dict[root.type](symbol_table, root, scope)
        
        if root.type in scope_incrementers:
            if scope in symbol_table:
                del symbol_table[scope]

    
            
            
        
