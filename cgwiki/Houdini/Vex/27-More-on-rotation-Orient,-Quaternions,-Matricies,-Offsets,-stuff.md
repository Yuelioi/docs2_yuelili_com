# 有关旋转的更多信息：Orient、Quaternions、Matricies、Offsets 等

这些东西花了一段时间才融入我的大脑，所以如果一开始没有意义，请不要担心。很多这可以通过其他方式和几个步骤来实现，但是有一个优雅的目标是很好的。

所以首先，创建一个平滑旋转的@orient。回顾一下，Houdini 提供了几种处理旋转的方法，按优先顺序排列，@orient 是最高的。东方是一个四元数，它是一个4值向量。

之前我们为此使用了一个矩阵（准确地说是 3x3 矩阵），旋转它，并通过 quaternion() 函数生成方向：

```cpp
float angle = @Time;
vector axis = rand(@ptnum);
matrix3 m = ident();
rotate(m, angle, axis);
@orient = quaternion(m);
```

原来我工作太多了。3x3 矩阵和四元数大部分是可以互换的，因此创建和操作它们的一些函数也是可以互换的。您可以直接从角度和轴创建四元数：

```cpp
float angle = @Time;
vector axis = rand(@ptnum);
@orient = quaternion(angle, axis);
```

漂亮干净。但这有一个微妙的问题，即随机轴。事实证明 rand() 向量并不像您预期​​的那样随机，它们往往都指向 xy 和 z 轴上的正值。

如果我们想要真正的随机向量，Houdini 提供了几种方法来在球体、圆锥体、半球体等上生成它。输入起来有点困难，但自动完成是你的朋友，而且结果要好得多：

```cpp
vector axis = sample_direction_uniform(rand(@ptnum));
```

即，你给它一个介于 0 和 1 之间的随机值，它会返回一个单位球体上的随机向量。整洁的。此处以轴模式在可视化工具中显示：

东方01.gif

如果我们创建一个 1 个单位高的盒子和一头猪，并将它复制到点上，我们会得到：

东方02.gif

如果我们想将猪偏移到盒子的末端怎么办？（是的，你可以先变换猪，然后再复制它，但假装我们做不到。）一种方法是取一个在 y 轴上有 1 个单位的向量（这是猪的原始方向和高度）盒子），旋转它以匹配@orient，然后取一个点并用这个修改后的向量偏移它。

这就是 qrotate 函数的作用；按四元数旋转向量。在第二次Vex中，我采用相同的观点，并将其移动（结果需要标准化）：

```cpp
vector pos = qrotate(@orient, {0,1,0} );
@P += normalize(pos);
```

现在，如果我们使用第二个点并将猪复制到它上面，并在第一个点上留下方框，然后合并结果，我们会得到：

东方03.gif

人为的例子，当然，但是在另一个东方空间中移动一个点的能力非常酷。这是一个更愚蠢的示例，其中我设置了一个在 0 和 1 之间循环的变量，并将其乘以旋转矢量，这具有在框上下滑动地理（在本例中为圆圈）的效果。我使用相同的变量为圆圈着色并缩放它们，因为，为什么不呢？在没有 qrotate 的情况下执行此操作可能会涉及邮票和其他丑陋之处。

东方04.gif

顺便说一句，这是另一种将向量旋转四元数的方法。qconvert 将四元数转换回 3x3 矩阵，然后像我们之前所做的那样将其与向量相乘。

```cpp
vector pos = {0,1,0};
matrix m = qconvert(@orient);
pos *= m;
@P += pos;
```

下载场景：文件：offset_along_orient.hipnc

Ps：Neil Dickson 提供了一些随机轮换的实用技巧；我本来用的是sample_sphere_uniform，他这样纠正我：

请注意，sample_sphere_uniform 将从单位球体*内部*的向量均匀采样，而 sample_direction_uniform 将从单位球体表面的向量均匀采样，即单位向量又名方向向量。确定要执行的转换的代码应该对向量进行归一化，因此无论哪种方式都应该没问题，但 sample_direction_uniform 会快一点。您还可以使用 sample_orientation_uniform 获得均匀的随机方向四元数，或者使用 sample_orientation_cone 在基本方向的某个角度内获得均匀的四元数。

谢谢尼尔！
