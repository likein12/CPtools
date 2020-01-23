def z(i,j):
    return i*W + j

for i in range(H):
    for j in range(W):
        if i!=H-1:
            if S[i][j]=="." and S[i+1][j]==".":
                e_list[z(i,j)].append(z(i+1,j))
                e_list[z(i+1,j)].append(z(i,j))
        if j!=W-1:
            if S[i][j]=="." and S[i][j+1]==".":
                e_list[z(i,j)].append(z(i,j+1))
                e_list[z(i,j+1)].append(z(i,j))