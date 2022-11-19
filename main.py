import numpy as np 
# Costs for the operations
INS_COST = 1
DEL_COST = 1
SUB_COST = 2

def find_minimum_edit_distance(source_string, target_string) :

    # Create a dp matrix of dimension (source_string + 1) x (destination_matrix + 1)
    dp  = np.array([[0] * (len(source_string) + 1)] * (len(target_string) + 1)) 
    #dp = np.array([[0] * (len(source_string) + 1) for i in range(len(target_string) + 1)])
    #dp = [[0] * (len(source_string) + 1)] * (len(target_string) + 1)
    print("\n\n Phase one : Create the required  matrix dimension:")
    print(dp)
    
    
    # Phase two :Initialize the required values of the matrix
    # ex// R/:0 1 2 3 4 5 .. /&/ C/:1 2 3 4 .. 
    for i in range(1, len(target_string) + 1) :
        dp[i][0] = dp[i - 1][0] + INS_COST;       
        #print("\n",i, end=" ");
    for i in range(1, len(source_string) + 1) :
        dp[0][i] = dp[0][i - 1] + DEL_COST; 
    print("\n Phase two :Initialize the required values of the matrix")   
    print(dp)
    
    
    
    # Phase three : Maintain the record of opertions done
    # Record is one tuple. Eg : (INSERT, 'a') or (SUBSTITUTE, 'e', 'r') or (DELETE, 'j')
    operations_performed = []
    # Build the matrix following the algorithm
    for i in range(1, len(target_string) + 1) :
        for j in range(1, len(source_string) + 1) :
            if source_string[j - 1] == target_string[i - 1] :
                dp[i][j] = dp[i - 1][j - 1];
                
            else :
                dp[i][j] =  min(dp[i - 1][j] + INS_COST, \
                                dp[i - 1][j - 1] + SUB_COST, \
                                dp[i][j - 1] + DEL_COST);
    print("\n Phase three : record The Edit Distance matrix values")            
    print(dp)
    # print or display   "The Edit Distance Table"
    print("\n Display Edit Distance matrix:")
    s1=0
    for t in range(len(source_string)):
        if s1 ==0:
            print("         ",source_string[t],end='')
        else:
            print("    ",source_string[t],end='')
        s1=1
    print("\n")
    
    q=0; s=0
    for i in dp:
        #if j!=0:
        #for i in range(len(target_string)):
        if q <= len(target_string) and s>0:
            print(target_string[q],end='   ')
            q=q+1
        s=s+5
        for j in i:
            if s==5:
                print("   ",j, end=" ") 
            else:           
                print(j, end="     ")      
        print("\n")           
    print()
    
    print("\nPhase No.4 : Performe Backtrack operations ")  
    print("\n")
    
    # Initialization for backtracking
    i = len(target_string)
    j = len(source_string)

    # Backtrack to record the operation performed
    while (i != 0 and j != 0) :
        # If the character of the source string is equal to the character of the destination string,
        # no operation is performed
        if target_string[i - 1] == source_string[j - 1] :
            i -= 1
            j -= 1
        else :
            # Check if the current element is derived from the upper-left diagonal element
            if dp[i][j] == dp[i - 1][j - 1] + SUB_COST :
                operations_performed.append(('SUBSTITUTE', source_string[j - 1], target_string[i - 1]))
                i -= 1
                j -= 1
            # Check if the current element is derived from the upper element
            elif dp[i][j] == dp[i - 1][j] + INS_COST :
                operations_performed.append(('INSERT', target_string[i - 1]))
                i -= 1
            # Check if the current element is derived from the left element
            else :
                operations_performed.append(('DELETE', source_string[j - 1]))
                j -= 1
    #print(operations_performed)
    # If we reach top-most row of the matrix
    while (j != 0) :
        operations_performed.append(('DELETE', source_string[j - 1]))
        j -= 1

    # If we reach left-most column of the matrix
    while (i != 0) :
        operations_performed.append(('INSERT', target_string[i - 1]))
        i -= 1

    
    #print(operations_performed)


    # Reverse the list of operations performed as we have operations in reverse
    # order because of backtracking
    operations_performed.reverse()
    return [dp[len(target_string)][len(source_string)], operations_performed]


if __name__ == "__main__":

    # Get the source and target string
    print("Enter the source string :")
    source_string = input().strip()
    print("Enter the target string :")
    target_string = input().strip()

    # Find the minimum edit distance and the operation performed
    distance, operations_performed = find_minimum_edit_distance(source_string, target_string)

    # Count the number of individual operations
    insertions, deletions, substitutions = 0, 0, 0
    for i in operations_performed :
        if i[0] == 'INSERT' :
            insertions += 1
        elif i[0] == 'DELETE' :
            deletions += 1
        else :
            substitutions += 1

    # Print the results
    print("Minimum edit distance : {}".format(distance))
    print("Number of insertions : {}".format(insertions))
    print("Number of deletions : {}".format(deletions))
    print("Number of substitutions : {}".format(substitutions))
    print("Total number of operations : {}".format(insertions + deletions + substitutions))

    print("Actual Operations :")
    for i in range(len(operations_performed)) :

        if operations_performed[i][0] == 'INSERT' :
            print("{}) {} : {}".format(i + 1, operations_performed[i][0], operations_performed[i][1]))
        elif operations_performed[i][0] == 'DELETE' :
            print("{}) {} : {}".format(i + 1, operations_performed[i][0], operations_performed[i][1]))
        else :
            print("{}) {} : {} by {}".format(i + 1, operations_performed[i][0], operations_performed[i][1], operations_performed[i][2]))

