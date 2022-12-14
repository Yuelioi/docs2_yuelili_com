# 直接沿轴删除没有法线的点

来自杰出的 Matt Ebb 的绝妙秘诀。我在立方体上散布点，它们应该有指向 X、-X、Y、-Y、Z、-Z 之一的法线。这是现实生活，有些点轻微旋转，这破坏了我的最终结果。

我需要一种方法来识别直接沿 X/Y/Z 轴没有法线的点，并删除它们。马特想出了这个宝石：

```cpp
if (max(abs(normalize(@N))) != 1) {
  removepoint(0,@ptnum);
}
```

这里发生了什么？

normalize(@N) - 采用@N 并使其长度为 1。
abs() - 使值为正，因此 {1,0,0} 将保持不变，但 {0,-1,0} 将变为 {0,1,0}
max() - 给定一个向量，返回该向量的最大分量。

那么，这是什么意思？让我们采用 3 个示例向量并通过该过程运行它：

{1,0,0} - 如果我们对其进行归一化，它会返回相同的向量。腹肌吧，也一样。获取最大值将返回 1。我们测试它是否等于 1，它是，所以该点仍然存在。
{0,-1,0} - 对其进行标准化，再次保持不变。吸收它，它变成{0,1,0}。Max返回1，所以这个点也留下来。
{1,-1,0} - 对其进行归一化，返回 { 0.707, -0.707,0}。Abs 它现在是 { 0.707, 0.707,0}。最大值为 0.707，因此未通过测试。

简单，聪明。干杯马特！
