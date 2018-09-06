import numpy as np
import matplotlib.pyplot as plt
a = np.array([[1,2,3],[4,5,6]])
b = np.ones_like(a)
# print(b)

##데이터 생성 함수
##0~1 범위 내에서 균등 간격으로 5개의 수를 생성
a = np.linspace(0,100) #몇개로 생성해라는 수가 없을때는 50개로 생성
# print(a)
a = np.linspace(0,5,5)
# print(a)
# plt.plot(a,'o')
# plt.show()
##-------------------------------------------------------------

a = np.arange(0,10,2,np.float)
print(type(a))
print(a)
# plt.plot(a,'o')
# plt.show()

## 난수관련 np.random
#
mean = 0
std = 1
a = np.random.normal(mean,std, 5)
print(a)
print("==")
# plt.hist(a,bins=10)
# plt.show()

##균등분포(0~1)
# a=np.random.rand(100)
# print(a)
# plt.hist(a,bins=10)
# plt.show()

# a =np.random.randint(-100,100,size=10000)
# print(a)

# plt.hist(a,bins=10)
# plt.show()

# a=np.random.randint(0,10,(2,3))
# print(a)
# b=np.random.randint(0,10,(2,3))
# print(b)
# np.save("myarr1",a) #'myarr1.npy   save(): 배열을 바이너리 형태로 저장
# np.savez("myarr2",a,b)
# print('**')
# print(np.load('myarr1.npy'))


# npzfiles=np.load('myarr2.npz')
# print(npzfiles.files)
# print(npzfiles['arr_0'])
# print(npzfiles['arr_1'])
# print(np.load('myarr2.npz'))
##----------------------------------------------------
print(np.loadtxt('simple.csv',dtype=np.int))

data =np.loadtxt('hight.csv',delimiter=",",skiprows=1,dtype={
    'names':('order','name','height(cm)'),'formats' :('i','S20','i')})
# print(data)

##savetxt함수: 배열을 텍스트 파일로 저장
data = np.random.random((3,4))
# print(data)
# np.savetxt('saved.csv',data,delimiter=',')
# print(np.loadtxt('saved.csv',delimiter=','))

##배열상태확인
print('==')
# arr=np.random.random((5,2,3))
# print(type(arr))
# print(arr.shape)
# print(len(arr))
# print(arr.ndim)
# print(arr)
# print(arr.dtype)
# print(arr.astype(np.int))
# arr=arr.astype(np.int)
# arr=arr.astype(np.float)
# print(arr)
print('===')

# print(np.info(np.ndarray.dtype))

a= np.arange(1,5).reshape(2,2)
print(a)
b= np.arange(9,5,-1).reshape(2,2)
print(b)
print(np.dot(a,b))


# print(a+b) #각각의 요소끼리 뺄셈
c= np.arange(1,10)
d= np.arange(9,0,-1)
print(np.dot(c,d)) #내적구하는 함수
print('====')

a= np.arange(1,10).reshape(3,3)
print(a)
b= np.arange(9,0,-1).reshape(3,3)
print(b)
# print(a==b)
# print(np.array_equal(a,b))


# (1 2 3) (4 5 6) #백터


# print(np.add(a,b))
# print(np.divide(a,b))
# print(np.multiply(a,b))

# print(b)
# print(np.exp(b)) ##
# print(np.sqrt(b))
## 삼각함수
# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))
# print(np.log(a))
# print(a)
# print(a.sum()) #axis
# print(np.sum(a))
# ## axis =0, 행을 기준으로 각 행의 동일한 인덱스 요소를 그룹화 해라.
# ## axis =1, 열을 기준으로 각 열의 요소를 그룹화 해라.
# print(a.sum(axis=1))

