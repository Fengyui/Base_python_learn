
# coding: utf-8

# # 函数

# In[4]:


#判断一个数是不是偶数
def pan_even(x):
    if x%2==0:
        print("是偶数")
    else:
        print("不是偶数")


# In[5]:


pan_even(2)


# In[6]:


#更常用，以便后续操作
def is_even(x):
    if x%2==0:
        yesno = True
    else:
        yesno = False
    return yesno


# In[8]:


a = is_even(3)
a


# In[10]:


for i in range(1,10):
    if is_even(i):
        y = 3*i
    else:
        y = i*i


# In[11]:


def f(x):
    return x,x**2,x**3
#函数可返回多个值，打包成一个tuple


# In[13]:


f(3)


# In[14]:


x = 2#定义了global变量


# In[21]:


def func(y):
    z = 5
    print("x=",x)
    print(locals())
    print(globals()['y'])#看全局变量的值
    print(x,y,z)#优先局部变量


# In[22]:


func(3)#定义的local变量


# In[29]:


#pass by value
def passby01(x):
    y = x**2
    return y


# In[33]:


a = 5
print(passby01(a))
print(a)#不会改变实参的值


# In[24]:


#pass by reference
def passby02(x):
    x.append(100)
    return x
#是地址的赋值关系不是copy，所以改变原来的数据


# In[26]:


a = [1,2,3,4]
b = passby02(a)
b


# In[27]:


a#此时形参的变化改变了实参的值


# In[34]:


def ask_yn(prompt,retries=4,complaint='y/n'):#可以设定默认参数
    print("prompt:",prompt)
    print("retries:",retries)
    print("complaint:",complaint)


# In[35]:


ask_yn(2)#但必须输入没有定义好的值,也可以对默认参数进行修改输入(预先设定好默认值，就不需要设置了)


# In[37]:


ask_yn("your name?",3,complaint = 'y')#也可以直接根据参数名字进行赋值，且位置赋值一定放在关键字赋值之前<所以complaint这个名字要放在后面>


# # modules

# In[38]:


#.py文件就是一个module
#放在同一个文件夹下就可以调用module：import simplemath as sth  sth.func()#调用其中的函数
#if __name__=="__mian__"下的代码在其他代码中调用该模块时不会运行，在本模块中会运行
#也可调用在同一文件夹下的其他文件夹里的py模块，from wenjianjai import simplemath as sth即可


# In[ ]:


#该模块放在了python大数据分析的文件里


# ### 可变的位置参数赋值

# In[ ]:


def getsum(x,y):
    return x+y#这种函数只能输入两个参数就是固定的


# In[3]:


def fun01(*num):#num可以是任意类型的数据结构
    print(type(num))
    sumnum = 0
    for n in num:
        print(n)
        sumnum+=n
    print("sum=",sumnum)


# In[4]:


fun01(1,2,3,4)


# In[ ]:


eval()函数查一下


# In[11]:


def pro(*num,scale=10):
    p = scale
    print("scale=",scale)
    for n in num:
        print("n=",n)
        p*=n
    return p


# In[12]:


pro(1,2,3)#scale只能使用关键字参数去取值，前面的位置参数都会放在num里的tuple里面去


# In[31]:


def auth(quote,**speaker_info):
    print(type(speaker_info))
    print(">",quote)
    print("-"*(len(quote)+5))#设置分隔的长度
    for k,v in speaker_info.items():
        print(k,v,sep=":")


# In[32]:


auth("student_indo",name="sala",age=18)#把相应的信息存入其中的字典


# In[33]:


lst = list(range(1,10))
lst


# In[34]:


fun01(*lst)


# In[37]:


dt = dict(one= 1)


# In[38]:


auth("try:",**dt)


# In[39]:


def foo(a,b,c=1,*d,e=2,**f):#只能关键字赋值  d将可变的赋值赋到list中，f将可变的赋值赋到字典中
    print("a:",a)
    print("b:",b)
    print("c:",c)
    print("d:",d)
    print("e:",e)
    print("f:",f)


# In[40]:


foo(1,2,3,4,5,6,7,8,e=2)


# In[44]:


foo(1,2,3,4,5,6,7,8,e=8,name="sala",age=18)#直接对自己类型进行设置就会直接对应


# In[42]:


def auth2(**speaker_info):
    print(type(speaker_info))
    for k,v in speaker_info.items():
        print(k,v,sep=":")


# In[43]:


auth2(name="sala",age=18)#把相应的信息存入其中的字典


# In[46]:


def foo2(*d,**f):
    print("d:",d)
    print("f:",f)


# In[47]:


foo(1,2,3,4,5,6,7,8,name="sala",age=18)


# In[48]:


print("one","two",sep="/",end="\n")
print("three","four")

