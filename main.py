import ttg
# base_logi_Expressions = input("enter your Expression")
def main_fun(base_logi_Expressions):
    def count_var(exp): 
        list_of_connectives=["∧","∨","⇒","¬"]
        base_logi_Expressions_to_ttg=""
        list_of_another=["(",")"]
        dic_of_var=[]
        for i in exp:
            if i == "∧":
                base_logi_Expressions_to_ttg+=" and "
            if i == "∨":
                base_logi_Expressions_to_ttg +=" or "
            if i == "⇒":
                base_logi_Expressions_to_ttg+=" => "
            if i == "¬":
                base_logi_Expressions_to_ttg+=" ~ "
            if i =="(":
                base_logi_Expressions_to_ttg+="("
            if i == ")":
                base_logi_Expressions_to_ttg+=")"
            if i not in list_of_another and i not in list_of_connectives and i != " ":
                if i not in dic_of_var:
                    dic_of_var.append(i)
                base_logi_Expressions_to_ttg+= " "+ i +" "
        return [dic_of_var, base_logi_Expressions_to_ttg]
    return(ttg.Truths(count_var(base_logi_Expressions)[0],[count_var(base_logi_Expressions)[1]], ints=False).as_tabulate(index=False, table_format='html'))
