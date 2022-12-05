# 使用 vex 和点云模糊属性

电脑模糊img.gif

下载场景：文件：pc_blur.hipnc

还有一个学过但没真正理解的东西，忘记了，又学了又忘记了，然后又害怕了一阵子，现在终于有了了解（我觉得）。

你在网格上有 Cd，你想模糊它。一种方法是遍历每个点，查看其邻居，将结果相加，然后除以邻居的数量。因为它是一个网格，而且点编号是一致的，你可以做类似的事情

int width = 50; // say the grid is 50 points wide
vector left = point(0,'Cd', @ptnum-1);
vector right = point(0,'Cd', @ptnum+1);
vector top = point(0,'Cd', @ptnum+50);
vector bottom = point(0,'Cd', @ptnum-50);
@Cd = left + right + top + bottom;
@Cd /= 4.0;

有效，但笨重，而且它只适用于网格。使用 neighbor() 和 neighbourcount() 函数更通用（从 odforce post 借用）：

int neighbours = neighbourcount(0, @ptnum);
vector totalCd = 0;
for (int i = 0; i < neighbours; i++)
{
    int neighPtnum = neighbour(0, @ptnum, i);
    totalCd += point(0, "Cd", neighPtnum);
}
@Cd = totalCd/neighbours;

Groovy，现在很好，很通用。

然而，还有一种更简洁的方法，使用点云：

int mypc = pcopen(0, 'P', @P, 1, 8);
@Cd = pcfilter(mypc, 'Cd');

pcopen() 旨在打开磁盘上的点云 (.pc) 文件，但通过使用 0 引用，Vex会将传入的地理区域视为点云。您需要告诉它如何在云中找到值，99.999% 的时间您将使用当前点 (@P) 的位置在云 ('P') 中查找位置。它搜索最大距离 (1)，并返回最大数量的点 (8)。Pcopen() 返回一个句柄，以便您稍后可以引用点云，这里我将其存储在变量“mypc”中。

pcfilter() 的目的是查看点云的结果，并返回您指定的属性的过滤（模糊，平均，称其为您想要的）结果。在这里，我们告诉它使用我们刚刚打开的云，并查找 Cd 属性。因为 pcopen 返回了当前点附近最接近的 8 个 Cd 结果，pcfilter 将返回这 8 个点的平均值。换句话说，我们只是通过其周围的 8 个点对 Cd 进行了模糊处理，本质上是一个 1 像素的模糊处理。

添加一些通道，我们可以用滑块控制模糊：

```cpp
float maxdist = ch('maxdist'); 
int blur = chi('blur');
int pc = pcopen(0, 'P', @P, maxdist, blur);
@Cd = pcfilter(pc, 'Cd');
```

maxdist 并没有真正影响结果，它更多的是为了速度；如果您知道搜索永远不必大于某个距离，那么这些点云函数可以运行得更快。另请注意，pcfilter() 比之前基于邻居的方法做得更聪明，它知道给予远点的重要性低于近点。

另一个用途是基于 vex 的平滑功能，在多边形网格模式下用很多轴划分的盒子上试试这个。这里唯一的区别不是模糊 Cd，而是模糊 P：

```cpp
float maxdist = ch('maxdist'); 
int blur = chi('blur');
int pc = pcopen(0, 'P', @P, maxdist, blur);
@P = pcfilter(pc, 'P');
```

有多种操作点云的函数，大多数都以“pc”为前缀，因此在 vex 文档中可以轻松地组合在一起：http ://www.sidefx.com/docs/houdini15.0/vex/functions/ （跳过到“点云和 3d 图像”部分）

奇怪的是 1：基于网格的方法基本上就是卷积滤波器在图像处理中所做的。这个看起来像边缘检测过滤器的特定版本称为拉普拉斯过滤器，这个词我偶尔会看到，但并没有真正理解。现在我有点做。更多信息：http ://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm

好奇点 2：如果您以前没有使用过点云，您可能想知道它们为什么存在，它们比做 point() 或 neighbor() 查找等有什么好处。它们只是存储 3d 数据的另一种方式，但是通过剥离边缘和多边形，可以采取一些捷径来使某些操作更快。获取几何子部分的过滤结果就是这样一种操作，其他操作正在快速迭代近点，或者用简单的平均值近似远点的块。过去 10 年的渲染在很大程度上依赖于点云来实现环境遮挡和次表面散射等效果，但随着强力路径追踪变得可行，渲染已经不再受欢迎。尽管如此，这仍然是 Houdini 中几何处理的一个方便技巧。
