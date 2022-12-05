# 数组

标准的 vex 数组变量就像大多数 C 风格的语言：

```cpp
int myarray[] = {1,2,3,4};

int foo = myarray[2];
```

您也可以通过在类型声明和 @ 之间插入“[]”来创建数组属性：

```cpp
i[]@things = {1,2,3,4};

int foo = i[]@things[3];
```

您也可以使用之前的 opintputN 语法，看起来很乱但很有效。例如，从第二个输入读取一个 float 数组并将其存储在本地 vex 变量数组中：

```cpp
float otherthings[]  = f[]@opinput1_thearray;

int foo = otherthings[4];
```

你可以追加你想要的数组索引并变得更难阅读：

```cpp
int foo = f[]@opinput1_thearray[4];
```
