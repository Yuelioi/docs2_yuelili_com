# 示例：按阈值随机删除点

在 Matt Ebb 向我展示这个之后，我每天使用它一百万次。Vex撒点：

```cpp
if ( rand(@ptnum) > ch('threshold') ) {
   removepoint(0,@ptnum);
}
```

使用plug按钮创建阈值滑块，现在在 0 和 1 之间向上滑动，会看到点被随机删除。这是怎么回事：

rand(@ptnum) -- 每个点根据 id 获得一个介于 0 和 1 之间的随机数
`> ch('threshold')` -- 将该随机数与阈值滑块进行比较。如果大于阈值...
removepoint(0,@ptnum) -- ...删除点。0 表示第一个输入，即连接到此Vex中的任何内容，@ptnum 是对该点的引用。
