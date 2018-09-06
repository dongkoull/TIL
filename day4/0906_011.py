import numpy as np
# print(np.__version__) #버전 체크

list1= [1,2,3,4]
a = np.array(list1)
print('array=',a)
print(a.shape) #rank:1, shape:(4, )
b=np.array([[1,2,3],[4,5,6]])#rank : 2, shape : (2,3)
print(b[1,1])
print(type(b))

##벡터화 연산#
##개념 : 배열의 각 요소에 대한 반복 연산을 하나의 명령으로
# 벡터화 연산을 하지 않은 일반적인 반복문 연산(속도가 느림)
data=[1,2,3,4,5]
ans=[]
for i in data:
    ans.append(2*i)
print(ans)
# 벡터화 연산(for 반복문이 없음) -> 속도 무척 빠름
x = np.array(data)
# print(2*x)# x는 array
# print(2*data)#data는 list

a=np.array([1,2,3])
b=np.array([10,20,30])
# print(a*2+b)
# print(a==2)
# print(b>10)
# print((a==2)&(b>10))
# print(a.shape)#shape
# print(a.ndim)#rank
# print(a.dtype)

a = np.zeros(4)
print(a)
print(type(a)) #자료구조? <class 'numpy.ndarray'>
print(a.dtype) #자료형? float64
##==================================================
# a =np.zeros((2,2))
# print(a)
# a= np.ones((2,3))
# print(a)
# a=np.full((2,3),5)
# print(a)
# a=np.eye(5)
# print(a)
#-----------------------------------------------------
# print(np.array(range(20)).reshape(4,5)) #1차원(20,)->2차원(4,5)
# c = np.array(range(20)).reshape(4,5)
#
# print(len(c))
# print(len(c[0])) #0 번 째 열의 길이 = 열에는 요소(값) 개수
# print(c.ndim) #rank 2차원
# print(c)
# print(c>10) # True, False 값으로
# print(c[c>10]) #상당히 어렵 T인 것들만 참조
# print('='*50)
# c[c>10]=99
# print(c)

#-------------------------------------------------------
arr = np.arange(0,3*2*4) #24
print(len(arr))
v=arr.reshape([3,2,4])
# print(v)
# print(len(v))
# print(len(v[0]))
# print(len(v[0][0]))

a = np.arange(0,3*4)
# a.reshape(3,4)
# print(a)

b= np.array([0,1,2,3,4])
# print(b)
# print(b[2])
# print(b[-1])
# 다차원 배열을 슬라이싱 할 때 사용되는 콤마(,)로 차원을 구분(축)
# a=a.reshape(3,4)
#
# print("="*50)
# print(a)  #(3,4)
# print(a[0,1])
# print(a[-1,-1])
# print(a[0, : ])

##두번째 열 전체를 추출
# print(a[:,1])

##인덱싱:행 지정, 슬라이싱:추출 열 지정
##두번째 행의 두번째 열부터 끝까지 추출
print('='*50)
# print(a[1,1:])
# print(a[:2,:2]) #01 45
# print(a[1,:]) #주의
# print(a[1:2,:])
# print(a[1,:].shape)
# print(a[1:2,:].shape)
##---------------------------------
##리스트 -> np.array -> 배열 -> reshape -> 인덱싱
##임의의 numpy배열 a에 대해, a [[row1,row2],[co1,col2]]??
print('='*50)
# a = np.array([[1,2],[3,4],[5,6]])
# print(a.shape)
# print(a)
# print(a[[0,1,2],[0,1,0]]) #array
# print(a[0,0],a[1,1],a[2,0]) #하나하나 스칼라 값 , 숫자값
# print([a[0,0],a[1,1],a[2,0]]) #list
# print(np.array([a[0,0],a[1,1],a[2,0]]))#array
# print(type(a[0,0]))

a = np.array([[1,2],[3,4],[5,6]])

s = a[[0,1],[1,1]]
print(s) #[2 4]


##부울린 값 참조

lst=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

x=np.array(lst)

bool_ind_arr = np.array([
    [False,True,False],
    [True,False,True],
    [False,True,False]
])
# print(type(lst))
# print(type(bool_ind_arr))
## T값들만 참조해서 2,4,6,8을 뽑아오고 싶다.

res= x[bool_ind_arr]
print(res) # 1
print('='*50)
##x= np.array([[1,2,3],[4,5,6],[7,8,9]])
bool_ind = (x%2==0)
# print(bool_ind)
print(x[bool_ind]) # 2

print('='*50)
print(x[(x%2==0)])  # 3


