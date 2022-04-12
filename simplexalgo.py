#Initialisation

def s_m(Z: "int", A: "list", B: "list", C: "list", maximisation: "bool"):
    
    s_m.runs = 0
    s_m.Z = Z
    s_m.A = A
    s_m.B = B
    s_m.C = C
    s_m.maximisation = maximisation
    s_m.optimal = True
    s_m.entering_index = 0
    s_m.leave_index = 0
    s_m.rhs_min = 0
    


    for i in range(0,100):

        #Optimality Test, maximisation should be set to:
        #- True if it is a maximisation problem
        #- False if it is a minimisation problem
        def optimality_test(): 

            if s_m.maximisation == True:
                return True if min(A) < 0 else False

            if s_m.maximisation == False:
                return True if max(A) > 0 else False
        s_m.optimal = optimality_test()
        


        #This checks wether the result of the optimality test was optimal and breaks out of theloop if thats the case
        if s_m.optimal == False: 
            break


        s_m.runs += 1

        #determines the entering variable column
        def entering_variable():
            ev_index = s_m.A.index(min(A)) if maximisation == True else s_m.A.index(max(A))
            return ev_index if s_m.optimal == True else None

        s_m.entering_index = entering_variable()

    


        #determines the leaving variable row
        def leaving_variable():
            spr = []  #spr --> smallest positive ratio
            unchanged_rows = []

            for row in range(len(s_m.B)): 
                spr.append(B[row][s_m.entering_index])

            
            for row in range(len(s_m.C)):
                if spr[row] == 0:
                    spr[row] = -1
                    unchanged_rows.append(0)
                   

                else:
                    spr[row]= (s_m.C[row]/spr[row])
                    unchanged_rows.append(1)
                    

            

            lv_index = spr.index(min([i for i in spr if i > 0]))
            spr_min = min([i for i in spr if i > 0])

            return lv_index, spr_min, unchanged_rows

        s_m.leave_index, s_m.rhs_min, s_m.unchanged_list = leaving_variable()

        
        

        


        def new_pivot_equation():

            pivot_element = s_m.B[s_m.leave_index][s_m.entering_index]

            s_m.B[s_m.leave_index] = [(s_m.B[s_m.leave_index][i]/pivot_element) for i in range(len(s_m.B[s_m.leave_index]))] 
            s_m.C[s_m.leave_index] = s_m.C[s_m.leave_index]/pivot_element

            return s_m.B, s_m.C
        s_m.B, s_m.C = new_pivot_equation()
      




        def new_basic_solution():
            A_coefficient = s_m.A[s_m.entering_index]

            s_m.Z = s_m.Z - A_coefficient*s_m.C[s_m.leave_index]
            
            for i in range(len(s_m.A)):
                s_m.A[i] = s_m.A[i] - (A_coefficient*s_m.B[s_m.leave_index][i])

            

            for row in range(len(s_m.B)):

                if row != s_m.leave_index:

                    B_coefficient = s_m.B[row][s_m.entering_index]

                    if s_m.unchanged_list[row] == 1:

                        s_m.C[row] = s_m.C[row] - B_coefficient*s_m.rhs_min

                        for column in range(len(s_m.B[row])):
                            
                            s_m.B[row][column] = s_m.B[row][column] - (B_coefficient*s_m.B[s_m.leave_index][column])
       
            return s_m.A, s_m.B, s_m.C, s_m.Z 
        
        s_m.A, s_m.B, s_m.C, s_m.Z = new_basic_solution()

    return s_m.A, s_m.B, s_m.C, s_m.Z


        




