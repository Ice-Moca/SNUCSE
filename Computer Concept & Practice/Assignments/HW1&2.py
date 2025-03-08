# 1. f1(n) 함수는 (1, …, n) 수열 여러개를 사용하여 아래와 같은 삼각형 모양을 출력한다. f1(n) 을 구현하시오.

def f1(n):
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# 2. f2(n) 함수는 숫자가 출력된 횟수를 원소로 사용하여 아래와 같은 삼각형 모양을 출력한다. f2(n) 을 구현하시오.

def f2(n):
    c = 1
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(c, end=" ")
            c += 1
        print()

# 3. f3(n) 함수는 n번째 행(row)까지는 숫자가 노출된 횟수를 원소로 사용하고, n번째 행(row) 이후에는 1씩 감소하는 횟수를 원소로 사용하여 아래와 같은 피라미드 모양을 출력한다. f3(n) 을 구현하시오.

def f3(n):
   c1 = 1
   c2 = 2*n -1
   while c1 <= 2*n-1:
       if(c1<c2):
           for i in range(c1*(c1+1)//2 + 1 - c1,c1*(c1+1)//2 + 1):
               print(i, end=" ")
       else:
           for i in range(c2*(c2+1)//2 + 1 - c2,c2*(c2+1)//2 + 1):
               print(i, end=" ")
       print()
       c1 += 1
       c2 -= 1

# 4. f4(n) 함수는 숫자가 출력된 횟수를 원소로 사용하여 아래와 같은 피라미드를 출력한다. f4(n) 을 구현하시오.

def f4(n):
    a=1
    b=2*n-1
    j=1
    while a<=2*n-1:
        if(a<b):
            for i in range(a*(a+1)//2+1-a,a*(a+1)//2+1):
                print(j,end=' ')
                j+=1
        else:
            for i in range(b*(b+1)//2+1-b,b*(b+1)//2+1):
                print(j,end=' ')
                j+=1
        print()
        a+=1
        b-=1

# 5. f5(matrix) 함수는 입력받은 matrix의 각 행(row)에 대한 합을 출력한다. F5(matrix) 을 구현하시오.

def f5(matrix):
    for i in range(len(matrix)):
        a=0
        for j in range(len(matrix[i])):
            a+=matrix[i][j]
        print(a)

# 6. f6(matrix) 함수는 matrix의 대각원소(Diagonal)에 대해서 출력한다.
# 단, matrix가 정방행렬(Square matrix)이라고 가정한다. f6(matrix) 을 구현하시오.

def f6(matrix):
    for i in range(len(matrix)):
        print(matrix[i][i])

# 7. f7(matrix) 함수는 입력 받은 matrix의 모든 col의 구성원들의  합을 반환한다. f7(matrix) 을 구현하시오.

def f7(matrix):
    for i in range(len(matrix[0])):
        m=0
        for j in range(len(matrix)):
            m+=matrix[j][i]
        print(m)

# 8. f8(matrix) 함수는 입력 받은 matrix의 모든 원소에 대한 합을 반환한다. f8(matrix) 을 구현하시오.

def f8(matrix):
    m=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            m+=matrix[i][j]
    return m

# 9. f9(matrix) 함수는 입력 받은 matrix의 각 행(row)에 존재하는 홀수를 “한 줄”로 출력한다. f2(matrix) 을 구현하시오.

def f9(matrix):
    for i in range(len(matrix)):
        for j in (matrix[i]):
            if j%2!=0:
                print(j,end=' ')
        print('')

# 10. f10(matrix1, matrix2) 함수는 matirx1과 matrix2에 대한 행렬의 합을 출력한다.
# 단, 2개의 행렬은 동일한 크기를 가지고 있다고 가정한다. f10(matrix1, marix2) 을 구현하시오.

def f10(matrix1,matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix1[i][j]+=matrix2[i][j]
    print(matrix1)

# 11. f11(matrix1, matrix2) 함수는 matrix1과 matrix2에 대해서 행렬의 곱셈을 반환한다.  
# 단, 행렬의 곱셈을 위한 matrix1의 열과 matrix2의 행의 크기는 동일하다고 가정한다. f11(matrix1, matrix2) 을 구현하시오.

def f11(mtrx1,mtrx2):
    prd=[]
    for i in range(len(mtrx1)):
        prd.append([])
        for j in range(len(mtrx2[0])):
            sum=0
            for k in range(len(mtrx1[0])):
                sum+=mtrx1[i][k]*mtrx2[k][j]
            prd[i].append(sum)
        return prd
    