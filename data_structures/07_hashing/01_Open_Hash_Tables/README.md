## Open Hash Tables 开放哈希表(Closed Addressing 链地址法)

### 插入数字序列

103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5, 14, 12, 7, 23

hash 函数是**模除**

**insert: 103**
![](./images/01.png)

**insert: 9**
![](./images/02.png)

**insert: 1**
![](./images/03.png)

**insert: 7**
![](./images/04.png)

**insert: 11**
![](./images/05.png)

**insert: 15**
![](./images/06.png)

**insert: 25**
![](./images/07.png)

**insert: 201**
![](./images/08.png)

**insert: 209**
![](./images/09.png)

**insert: 107**
![](./images/10.png)

**insert: 5**
![](./images/11.png)

**insert: 14**
![](./images/12.png)

**insert: 12**
![](./images/13.png)

**insert: 7**
![](./images/14.png)

**insert: 23**
![](./images/15.png)

### 插入字符串序列

qwe, rty, uio

hash 函数是**先使用字符串计算成数字，然后模除**

**insert: qwe**
![](./images/30.png)

**insert: rty**
![](./images/31.png)

**insert: uio**
![](./images/32.png)
