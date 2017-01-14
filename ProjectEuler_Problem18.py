#Function to traverse triangle and return optimum path
def triangle_traverser(triangle):

    #Create a path_triangle (only holds best path to each index; path is a list of numbers)
    path_triangle = []

    #Traverse triangle layer by layer
    for row in range(len(triangle)):
    #for row in range(4):
        print "Layer: ",triangle[row]

        layer = triangle[row]
        
        #Deal with top layer
        if row == 0:
            path_triangle.append([layer])

        #Otherwise deal with each element
        else:
            for col in range(len(layer)):
                #print "col: ",col
                elem = layer[col]

                #First element only inherits path leftward
                if col == 0:
                    #print "in if"
                    relevant_path = path_triangle[row-1][0][:] #List slicing
                    #print "Relevant path: ",relevant_path
                    relevant_path.append(elem)
                    #print "Relevant path: ",relevant_path
                    #print path_triangle
                    path_triangle.append([relevant_path])
                    #print path_triangle

                #All other elements inherit path both ways
                elif col != row and col != 0:
                    #print "in elif 1"
                    #print path_triangle
                    relevant_path_1 = path_triangle[row-1][col-1][:]
                    #print relevant_path_1
                    #print "here: " + str(path_triangle[row-1][col])
                    relevant_path_2 = path_triangle[row-1][col][:]
                    #print relevant_path_2
                    if sum(relevant_path_1) > sum(relevant_path_2):
                        relevant_path = relevant_path_1
                    else:
                        relevant_path = relevant_path_2
                    #print relevant_path
                    relevant_path.append(elem)
                    #print relevant_path
                    #print path_triangle
                    path_triangle[row].append(relevant_path)
                    #print path_triangle

                #Last element only inherits path rightward
                elif col == row:
                    #print "in elif 2"
                    #print path_triangle
                    relevant_path = path_triangle[row-1][col-1][:]
                    #print "Relevant path: ",relevant_path
                    relevant_path.append(elem)
                    #print "Relevant path: ",relevant_path
                    path_triangle[row].append(relevant_path)
                
        #print "Path Triangle: ",path_triangle
            
    #Analyze the last row of the Path Triangle
    last_row = path_triangle[-1]
    
    longest_path = []
    longest_path_len = 0
    
    for path in last_row:
        if sum(path) > longest_path_len:
            longest_path = path
            longest_path_len = sum(path)
            
    print longest_path
    print longest_path_len


#Read file
f = open('ProjectEuler_Problem18.txt','r')
lines = f.readlines()
lines_new = []
for line in lines:
    lines_new.append(line[:-1]) #gets rid of /n char from each line

lines_split = []
for line in lines_new:
    lines_split.append(line.split(' '))
print lines_split

int_lines = []

for i in lines_split:
    int_line = []
    for j in i:
        int_line.append(int(j))
    int_lines.append(int_line)

triangle_traverser(int_lines)
