import numpy as np

data=np.loadtxt(input())
sh=data.shape

n_data = data

for i in range(sh[0]):
    if n_data[i][i]==0:
        for j in range(i+1,sh[0]):
            if n_data[j][i] != 0:
                a = n_data[j,:].copy()
                n_data[j] = n_data[i]
                n_data[i]=a
                break
    if n_data[i][i]!=0:
        for j in range(sh[0]):
            if i!=j:
                n_data[j]-=n_data[i]*(n_data[j][i]/n_data[i][i])

n=sh[0]

for i in range(sh[0]):
    if n_data[i][i]!=0:
        n_data[i]/=n_data[i][i]
    else:
        n=i
        break

k=0
for i in range(n, sh[0]):
    if n_data[i][sh[1]-1]!=0:
        k=1
        break

if k==0:
    matrix_u=n_data[:n,:].copy()
    shm = matrix_u.shape

    solution = matrix_u[:, shm[0]:].copy()
    solution[:, :solution.shape[1] - 1] = -solution[:, :solution.shape[1] - 1]

    m = np.hstack((np.eye(solution.shape[1] - 1), np.zeros((solution.shape[1] - 1, 1))))
    solution = np.vstack((solution, m))

if k==1:
    print("Not Solving")
else:
    if solution.shape[1]<10:
        for i in range(solution.shape[1]):
            print("solution", i+1, ":")
            for j in range(solution.shape[0]):
                print("x", j+1, " = ", solution[j][i])
    else:
        f = open('LinearEqSolved.txt', 'w')
        for i in range(solution.shape[1]):
            f.write("solution " + str(i+1) + ":" + '\n')
            for j in range(solution.shape[0]):
                f.write("x"+ str(j+1)+ " = "+ str(solution[j][i]) + '\n')


#C:\Информатика\t.txt