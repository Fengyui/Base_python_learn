
# coding: utf-8

# # 循环

# In[13]:


#写一个乘法口诀表
for i in range(1,10):
    for j in range(1,10):
        print(j,"*",i,"=",i*j,end="\t")
        if j==i:
            print("\n")


# # List

# In[ ]:


numbers = [1,2,3,4,5]


# In[2]:


items = list("asdfgh")
items


# In[59]:


lst1 = [numbers,items]


# In[60]:


lst1.append([1,2,3])
lst1


# In[61]:


lst1.extend([1,2,3])#添加的是列表里面的数
lst1


# In[62]:


lst1.insert(1,56)
lst1


# In[63]:


lst1.remove(56)#去掉遍历列表见到的第一个56
lst1


# In[64]:


lst1.pop()
lst1


# In[67]:


lst1.index(2)


# In[68]:


lst1.reverse()
lst1


# In[69]:


len(lst1)


# In[50]:


lst2 = list(range(10))
lst2 = list('ajsgd')


# In[55]:


#寻找索引对应的值
lst2[3]


# In[53]:


lst2.index('d')


# In[56]:


lst2[5::-1]


# In[11]:


lst2.count(2)#计2的个数


# In[25]:


lst3 = lst2
lst3


# In[26]:


lst3 is lst2


# In[28]:


lst3.append('a')
lst3,lst2


# In[32]:


lst3==lst2


# In[33]:


lst3 is lst2


# In[29]:


lst4 = lst2.copy()
lst4


# In[30]:


lst4 == lst2


# In[31]:


lst4 is lst2


# In[17]:


items2 = list('hgvbx')


# In[18]:


items2


# In[19]:


items2.sort()


# In[20]:


items2


# # 字典

# In[21]:


dt1 = {'one':1,'two':2,'three':3}
dt2 = dict(onde=1,two=9,three=3)


# In[23]:


dt1,dt2


# In[34]:


dtf = {}
for i in range(3):
    fruit = input("fruit name:  ")
    num = int(input("number:   "))
    dtf[fruit] = num


# In[35]:


dtf


# In[37]:


n = dtf.get("orange")
n


# In[70]:


dtf['apple']


# In[42]:


lstf = list(dtf.keys())
lstf


# In[44]:


lstv=list(dtf.values())
lstv


# In[45]:


lsti = list(dtf.items())
lsti


# In[ ]:


dtf.pop('balana')


# In[47]:


for k,v in dtf.items():
    dtf[k] = 10*v
    print(k,'----',dtf[k])


# In[73]:


#统计字符串中字符的个数
str = 'All statistical techniques that simultaneously analyze multiple measurements on individuals or objects under investigation'
lstt = list(str)
lstt.count('e')


# In[ ]:


# 统计字符串中字符出现的次数，计入dictt中
strr = 'All statistical techniques that simultaneously analyze multiple measurements on individuals or objects under investigation'
lstt = list(strr)
dictt = {}
for i in set(strr):
    num = lstt.count(i)
    dictt[i] = num
dictt


# In[95]:


del dictt[' ']#删除键值的操作
dictt


# In[92]:


dictt.popitem()#删除最后一个统计到的键值对
dictt


# In[93]:


dictt


# In[89]:


dictt.pop('z',1)#指定删除键值对
dictt


# In[78]:


#统计字符串中字符出现的次数，计入dt中
strr = 'All statistical techniques that simultaneously analyze multiple measurements on individuals or objects under investigation'
dt = dict()
for s in strr:
    if s not in dt.keys():
        dt[s] = 1
    else:
        dt[s] =dt[s]+1
dt            


# # tuple

# In[7]:


#tuple#数据具有永久性#不支持赋值
t1 = 1,'cat'
t2 = 123,456,'hello'
type(t1),type(t2)


# In[8]:


for i in t1:
    print(i)


# In[5]:


#unpacking拆包,必须数是对应的
x,y,z = t2
print(x)
print(y)
print(z)


# In[6]:


#打包拆包的应用
x,y = y,x
print(x)
print(y)


# In[55]:


#tuple解决fib
def fib(n):
    a,b = 0,1
    for i in range(n):
#        print(i,a)
        print(b)
        a,b = b,a+b    
fib(10)


# In[9]:


t3 = (list(range(1,4)),list('acd'))
type(t3)


# In[11]:


#在里面的列表里添加删除，没有改变tuple的对象
print(t3)
print(id(t3[0]))
t3[0].append(4)#添加在list里，不影响id，还是在同一个空间里的，所以对象没有改变
print(t3)
print(id(t3[0]))


# # set

# In[ ]:


#set={2,3,4}
empty_set = set()


# In[13]:


s2 = {1,2,3,4,2}
s2


# In[12]:


s3 = {1,'a',('a',3)}
s3


# In[14]:


for x in s2:
    print(x)


# In[19]:


s4 = set([1,2,'a'])
lst = list({2,3,5})
#s5 = set(dt3.keys())


# In[20]:


s4,lst


# In[21]:


a = set("asdfgh")
b = set("fdrvb")
a,b


# In[22]:


c = a^b
d = a|b
e = a-b
c,d,e


# In[24]:


#判断单词是不是由lets集合组成的（1）
word = "bded"
lets = "qweuiobgseaj"

for i in word:
    if i not in lets:
        print("not")
        break
else:
    print("yes")


# In[27]:


#判断单词是不是由lets集合组成的（2）
ws = set(word)
l_s = set(lets)
if ws<=l_s:
    print("yes")
else:
    print("no")


# In[28]:


#判断单词是不是由lets集合组成的（3）#判断一个集合是否属于另一个集合即可
if set(word)<=set(lets):
    print("yes")
else:
    print("no")


# In[ ]:


#zip
lst1 = ["apple","orange","peach"]
lst2 = [2,3,4]
for k,v in zip(lst1,lst2):
    print(k,v)


# In[36]:


#词频统计
sent = "python is my favoriate language,you're so cute   ,someone like you ~~,do what shhhh"


# In[37]:


chset = "abcdefghijklmnopqrstuvwxyz-' "
sent = sent.lower()#小写字母
for c in sent:
    if c not in chset:
        sent = sent.replace(c," ")
sent


# In[38]:


wd_lst = sent.split(" ")#通过空格切分
wd_lst


# In[42]:


dt = {}
for k in wd_lst:
    if k not in dt.keys():
        dt[k] = 0
    dt[k]+=1
dt


# In[47]:


del dt[" "]
dt


# In[48]:


wd_s = set(wd_lst)
dt1 = {}
for k in wd_s:
    dt1[k] = wd_lst.count(k)


# In[49]:


dt1


# In[52]:


del dt1[""]
dt1


# In[53]:


#enumerate
for index,color in enumerate(["red","green","blue"]):
    print(index,color)


# In[58]:


#zip
que = ["name","tel","add"]
ans = ["lihua","1123","green"]
for q,a in zip(que,ans):
    print("what's your {0}? {1}".format(q,a).upper())


# # (2)元组
# 编写一个函数来计算两个正整数的 GCD。算法：gcd(a, b)在数学上等于 gcd(b, a % b)，而且
# gcd(a, 0) == a。

# In[18]:


def gcd(a,b):
    if b==0:
        print(a)
    else:
        gcd(b,a%b)


# In[ ]:


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)


# In[19]:


gcd(25,10)


# In[ ]:


def gcd(a,b):
    while b>0:
        a,b = b,a%b
        gcd(a,b)
    return a

