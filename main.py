import itertools
import pandas as pd
list_of_connectives=["∧","∨","<",">","=","⇒","¬","=>","~","^","\/","/\\","<=>","⇔","or","not","and"]
def main_fun(a):
    def list_to_string(s):  
        
        str1 = ""  
        
          
        for ele in s:  
            str1 += " "+ele+" "   
        
     
        return str1  
    def implies(x,y):
        return (not(x) or y)
    def tautology(x,y):
        return (x==y)            
    
     
    def gen_true_false_propositions(my_proposition):
        
        dic_true_false={}
        for i in my_proposition:
            dic_true_false[i]=[]
    
        for boolean_collection in itertools.product([False, True], repeat=len(my_proposition)):
            for i,boolean in enumerate(list(boolean_collection)):
                dic_true_false[my_proposition[i]].append(boolean)
        return dic_true_false
    
    def split_formula(formula):
        global list_of_connectives
        new_formula=""
        my_propositions=[]
        for char in formula:
            if char  not in list_of_connectives and char!=" " and char!="(" and char!=")" and char != "\\" and char != "/" and char not in my_propositions:
                my_propositions.append(char)
        # print(formula)
        # for i in formula:
        #     print(i)
        for i in formula.split(" "):
                if i == "∧" or i =="/\\" or i ==  "^" or i=="and":
                    new_formula+=" and "
                if i == "∨" or i =="\/" or i =="or":
                    new_formula +=" or "
                if i == "⇒" or i =="=>":
                    new_formula+=" => "
                if i == "¬" or i=="~" or i =="not":
                    new_formula+=" not "
                if i == "<=>" or i=="⇔":
                    new_formula+=" <=> "
                if i =="(":
                    new_formula+=" ( "
                if i == ")":
                    new_formula+=" ) "
                if i !=" " and i not in list_of_connectives and i != "(" and i!=")":
                    new_formula+=i
        
        return (my_propositions,new_formula)
    
    propositions,formula=split_formula(a)
    base_true_false= gen_true_false_propositions(propositions)
    formula= formula.replace("(","( ")
    formula= formula.replace(")"," )")
    
    formula2=formula.split(' ') 
    for index,i in enumerate(formula2): 
        if i=="p" or  i=="q" or i=="r": 
            formula2[index]="True"
    formula2=list_to_string(formula2)
    
    def part_form(formula):
        global list_of_connectives
        parted_comp_prop=[]
        if "<=>" in formula:
            parted_comp_prop=formula.split(" <=> ")
            parted_comp_prop.append(formula)
        elif "<=>" not in formula and "=>" in formula:
            parted_comp_prop=formula.split(" => ")
            parted_comp_prop.append(formula)
        else :
            parted_comp_prop=[" "+formula]
        return parted_comp_prop
    #     for part in parted_comp_prop:
    #         counter_of_conn=0
    #         split_count=0
    #         for i,char in enumerate(part.split(" ")):
    #             # print(char, char in list_of_connectives)
    #             if char in list_of_connectives:
    #                 counter_of_conn+=1
    #                 # print('aaa')
    #             if counter_of_conn==2:
    #                 parted_comp_prop.append(part[split_count:i+2])
    #                 counter_of_conn=0
    #                 split_count=i
    #     print(parted_comp_prop)
    
    parted_formula=part_form(formula)
    result_true_false=base_true_false
    true_false_parted_formula={}
    # for i in base_true_false:
    #     # print(i)
    #     # print(base_true_false[i])
    for i in parted_formula:
        true_false_parted_formula[i]=[]
    for formula in true_false_parted_formula:
        # print(formula,"formlua")
        counter=0
        counter_max=len(base_true_false[propositions[0]])
        while counter < counter_max:
            tab={}
            for key in base_true_false:
                tab[key]=str(base_true_false[key][counter])
            formula2=" "+formula
            for prop in tab:
                formula2=formula2.replace(" "+prop+" "," "+tab[prop]+" ")
                formula2=formula2.replace(" "+prop," "+tab[prop]+" ")
            if "=>" in formula2 and "<=>" not in formula2:
                index_of_problem=formula2.index("=")
                formula2_1=formula2[:index_of_problem]
                formula2_2=formula2[index_of_problem+2:]
                true_false_parted_formula[formula].append(str(implies(eval(formula2_1),eval(formula2_2))))
            elif "<=>" in formula2:
                index_of_problem=formula2.index("<")
                formula2_1=formula2[:index_of_problem]
                formula2_2=formula2[index_of_problem+3:]
                true_false_parted_formula[formula].append(str(tautology(eval(formula2_1),eval(formula2_2))))
            else:
                true_false_parted_formula[formula].append(eval(formula2))
            counter+=1
    # for i in true_false_parted_formula:
    #     print(i)
    #     print(true_false_parted_formula[i])
    result_true_false.update(true_false_parted_formula)
    
    # for i in  result_true_false:
    #     print(i,"formule")
    #     print(result_true_false[i])
    
    df = pd.DataFrame(result_true_false)
    return(df.to_html())