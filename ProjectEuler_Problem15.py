#Alternative algorithm, since brute force doesn't work for 20x20 grid
def smarter_paths(pos):
    #TOP-LEFT: pos; BOTTOM-RIGHT: (0,0)

    #Base Case
    if pos == (0,0):
        lattice_dict[(0,0)] = 1
        return 1 #Define: 1 way to get from (0,0)->(0,0)

    #Recursive Case
    else:
        #If problem has already been solved for this pos, use the stored value
        if lattice_dict.has_key(pos):
            return lattice_dict[pos]

        #If point is along right wall ...
        elif pos[0] == 0:
            lattice_dict[pos] = smarter_paths((pos[0],pos[1]-1))
            return lattice_dict[pos] + 1

        #If point is along bottom wall ...
        elif pos[1] == 0:
            lattice_dict[pos] = smarter_paths((pos[0]-1,pos[1]))
            return lattice_dict[pos] + 1

        #Otherwise a fork is possible ...
        else:
            lattice_dict[pos] = smarter_paths((pos[0],pos[1]-1)) + smarter_paths((pos[0]-1,pos[1]))
            return lattice_dict[pos]

#Permute layer function
def permute_layer(n):

    point_list = []

    for i in range(n):
        point_list.append((n,i))

    for i in range(n):
        point_list.append((i,n))

    point_list.append((n,n))

    return point_list

#Call function
lattice_dict = {}

for i in range(21): #0->20 inclusive

    points = permute_layer(i)

    for point in points:
        num_paths = smarter_paths(point)

    print lattice_dict[(i,i)]

#Test cases
##print lattice_dict[(0,0)]
##print lattice_dict[(0,1)]
##print lattice_dict[(1,0)]
##print lattice_dict[(1,1)]
    
