# 分支结构的求解器和Vex

Vex 分支器 demo.gif

下载场景：文件：vex_brancher.hipnc

我看了Simon Holmedal 的这段精彩视频，讲述了他为 Nike 所做的工作，许多有趣的分支结构、有机增长、分形，这些都是非常鼓舞人心的东西。

事实上如此鼓舞人心，我不得不尝试复制他的一个实验。它核心的 Vex 代码非常简单。我用@active=1 标记一个（或多个）起点，然后在求解器 sop 中运行此代码：

```cpp
if (@active ==0) {
    float maxdist = ch('maxdist');
    int maxpoints = 5;
    int pts[] = nearpoints(0,@P, maxdist, maxpoints);
    int pt ;
    
    foreach  (pt;pts) {
        if (point(0,'active',pt)==1) {
            @active=1;
            int prim = addprim(0,'polyline');
            addvertex(0,prim,@ptnum);
            addvertex(0,prim,pt);
            @age = @Frame;
            return;
        }
    }
}
```

鉴于我已将其发布在 vex 教程页面上，我将逐行解释：

if (@active ==0) {

仅在非活动点上运行以下代码，即在尚未连接成线的点上。

```cpp
    float maxdist = ch('maxdist');
int maxpoints = 5;
int pts[] = nearpoints(0,@P, maxdist, maxpoints);
int pt ;
```

设置一些变量来为 nearpoints() 函数提供数据。给 nearpoints() 一个位置，它返回最近点的数组（它们的 id 的数组，或者 @ptnum's，如果你使用的是 vex 术语）。您还可以告诉它要返回的总点数和要搜索的最大距离（这里我使用通道滑块设置）。我还创建了一个 pt 变量以在以下循环中使用。

```cpp
    foreach  (pt;pts) {
```

这是在 vex 中调用循环的便捷方法；您可以要求 vex 只循环遍历数组中的元素，而不是通常的 C 递增计数器的方法。在这里，每次循环运行时，pt 都将设置为之前由 nearpoints() 函数找到的下一个点。

```cpp
        if (point(0,'active',pt)==1) {
```

获取我们正在测试的点的@active 属性，如果它处于活动状态，则运行下一段代码。

```cpp
@active=1;
```

因为我们找到了一个活跃点，所以我们将自己标记为活跃。因为这个 vex 只会在非活动点上运行（记住这个Vex的第一行），所以这会阻止所有点不断尝试寻找连接。

```cpp
int prim = addprim(0,'polyline');
addvertex(0,prim,@ptnum);
addvertex(0,prim,pt);
```

从找到的点到我自己创建一条线。这在其他地方有更详细的介绍，但想法是您以线模式创建一个空图元，然后向该图元添加 2 个顶点，形成一条线。

```cpp
@age = @Frame;
```

将当前帧存储为 @age 属性。稍后我们可以使用它来按年龄为结构着色；靠近起点的点将具有低年龄，远离起点的点将具有高年龄。

```cpp
return;
```

一旦找到活动点，就停止运行 foreach 循环。如果这条线被注释掉，它将尝试将自己连接到任何最近的活动点。这可以创建链接到现有边的边，从而失去分支外观。它本身看起来很酷（注释掉该行并查看），但我想要分支。

臀部有一个稍微漂亮的版本，它也试图只选择遵循一些卷曲噪声流线的点，这会产生有趣的漩涡状分支。它也可以很好地处理散布在体积内的点，从而制作出很酷的 3d 结构。
