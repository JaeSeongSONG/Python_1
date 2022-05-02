
3   1 5 15 35 70 126
2   1 4 10 20 35 56
1   1 3  6 10 15 21
0   1 2  3  4  5  6

0 1 3 6 10 15 21
case = int( input() )

for i in range( case ):
    k = int( input() )
    n = int( input() )
    
    1 3 6 10 15
    k-2층의 n번째 값까지 전부 더함 + k-1층의 n-1번째 값까지 전부 더함
   
    k = 3
    n = 4
    
    (1 ,4) + (2, 3)
    
    k층 -> 1 이후 k+1값으로 증가
    
    k_0 = list( range( 1, 15 ) )
    
    k_1 = list()
    num = 0
    for i in range( 1, 15 ):
        num += i
        num.append(k_1)
    
    









