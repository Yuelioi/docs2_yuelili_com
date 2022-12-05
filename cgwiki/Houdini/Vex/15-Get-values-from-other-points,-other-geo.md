# 从其他点、其他几何体获取值

下一步的基础工作（可能在上面顺便提到过）。

如果你想要当前点的颜色，可以使用@Cd。但想要5号点的颜色呢？

```cpp
float otherCd = point(0, "Cd", 5);
```

point() 函数允许查询其他点的属性（第一个 0 表示“该point wrangle的第一个输入”）。如果您有其他节点连接到 point wrangle 的第二个输入口：

```cpp
float otherCd = point(1, "Cd", 5);
```

通常这用于在相似节点之间传输或混合属性。例如，您有 2 个节点，并希望将颜色设置为两者相加。点编号将相同，因此您可以使用相同的 ptnum 来获得第二个节点，并执行您需要的操作：

```cpp
vector otherCd = point(1, "Cd", @ptnum);
@Cd += otherCd;
```
