# 用于模拟的求解器 sop 和 wrangles

生活游戏解算器.gif

下载场景：文件：game_of_life_solver.hip

当您将Vex放到求解器中时，另一种乐趣就会打开。正如其他地方多次提到的那样，求解器 sop 让您可以访问前一帧，这意味着您可以在其中放置一个 wrangle 并将其连接到“prev_frame”节点，您可以进行模拟和累积效果。在这个例子中，我对 Conways 的“生命游戏”（简单的元胞自动机）进行了松散的近似。很多年前的逻辑我都记不太清了，大概是这样的：

寻找活跃的邻居北/南/东/西，以及我自己的活跃状态。
如果有 1 个活跃的邻居，而我很活跃，那么我现在已经死了。
如果有 2 个活跃的邻居，而我已经死了，那么我现在就活跃了。
如果有 4 个活跃的邻居，我就死定了。

设置一些随机模式作为起点，然后运行求解器，您将得到一个改变的模式。然后将其馈入下一帧，这会改变模式，将模式馈入下一帧等。

求解器中的Vex非常简单：

```cpp
int left = prim(0,'Cd',@primnum-1);
int right = prim(0,'Cd',@primnum+1);
int top = prim(0,'Cd',@primnum+30);
int bottom = prim(0,'Cd',@primnum-30);

int total = left+right+top+bottom;

if (total==1 && @Cd ==1 ){
 @Cd =0 ;
}

if (total==2 && @Cd ==0 ){
 @Cd =1 ;
}

if (total==4)  {
 @Cd =0;
}
```
