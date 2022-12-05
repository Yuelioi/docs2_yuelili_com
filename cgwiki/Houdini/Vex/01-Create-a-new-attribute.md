# # 创建新属性

想定义一个新的浮点属性'foo'？只需输入

```cpp
cpp
@foo;
```

按 ctrl-enter，查看几何电子表格，就看到了浮点属性。@代表是一个属性，默认类型是 float(浮点)。

如何初始化？

```cpp
cpp
@foo=1;
```

想要矢量属性？在“@”之前添加“v”。初始化的话，如果只是数字，请用大括号，如果使用函数或其他属性，请使用 set() ：

```cpp
cpp
v@myvector={1,0,3};
v@other=set(0, @P.x, 1);  
```

可以使用不同前缀设置属性的类型。float是默认属性类型，因此一般不用f@作为前缀。

```cpp
cpp
// 浮点与整数
f@myfloat = 12.234; // float
i@myint = 5; // integer

// 向量
u@myvector2 = {0.6, 0.5}; // vector2 (2 floats)
v@myvector = {1,2,3}; // vector (3 floats)
p@myquat = {0,0,0,1}; // quaternion / vector4 / 4 floats

// 矩阵
2@mymatrix2 = {1,2,3,4}; // matrix2 (2x2 floats)
3@mymatrix3 = {1,2,3,4,5,6,7,8,9}; // matrix3 (3x3 floats)
4@mymatrix4 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}; // matrix (4x4 floats)

// 字符串和字典
s@mystring = 'a string'; // string
d@mydict = {}; // dict, 只能实例化为空类型
d@mydict['key'] = 'value'; // 可以在实例化后设置值
```

sidefx 文档在这里：<https://www.sidefx.com/docs/houdini/vex/snippets.html#attributes>
