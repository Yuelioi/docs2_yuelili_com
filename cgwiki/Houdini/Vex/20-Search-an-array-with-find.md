# 使用 find 搜索数组

来自 Houdini 军队 Tomas Slancik 的超级好建议。

假设您要在第 1、25、225、35 帧上将 int attib 设置为 1。也就是说，这里没有模式，只有特定的框架。

我最初天真的方法是将它全部放在带有一堆 OR 的 if 语句中（在 Vex 中，像大多数 C 派生语言一样，OR 是 2 个垂直管道，||）：

```cpp
int myint = 0;
if (@Frame == 1 || @Frame == 25 || @Frame == 225 || @Frame == 35) {
    myint=1;
}
```

Tomas 提出了一种使用数组和 find() 函数的更简洁的方法：

```cpp
int myint = 0;
int frames[] = {1, 25 , 66, 225 ,35, 666, 999, 123, 534};
if (find(frames, @Frame)>=0) {
     myint=1;
}
```

好的！
