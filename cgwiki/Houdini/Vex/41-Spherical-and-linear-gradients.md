# 球形和线性渐变

渐变二向上.gif

下载场景：文件：gradient_spherical_vs_linear.hip

来自 Patreon 支持者的有趣问题。您有 2 个位置，并希望使用它们在某些地理区域上定义渐变。当我问他是否想要球形渐变（所以点 1 是中心，点 2 定义半径），或者他是否想要线性渐变（所以 p1 定义起点，p2 定义终点），他说“是”二者皆是。

球形渐变很简单，核心是测量从你的几何体到一个点的距离，在这种情况下是 p1。为此有一个内置的 vex 函数，所以我们将使用它。视觉上的结果通常不是您想要的，因为它在中心为 0（因为从球体中心到这些点的距离为 0），并且随着几何体的距离逐渐增加。

相反，您想反转它，使其在中间为 1，然后在您指定的半径处变为 0。怎么做？好吧，很容易让颜色为 1，然后减去距离结果。但是为了确保距离在我们想要的确切半径处是黑色的，我们可以将距离除以半径（即 p1 和 p2 之间的距离）：

```cpp
vector p1 = point(1,'P',0);
vector p2 = point(1,'P',1);

float r = distance(p1,p2);
@Cd = (r-distance(@P, p1))/r;
```

线性梯度问题更有趣。我最初的策略是将 p1 设置为原点（所以一种方法是减去 @P - p1），然后计算一个四元数，该四元数将旋转位置以与 p1->p2 向量对齐。它有效，但过于复杂。这是代码：

```cpp
vector p1 = point(1,'P',0);
vector p2 = point(2,'P',0);
vector xaxis = {1,0,0};
vector aim = normalize(p2-p1);
float d = distance(p1,p2);
@Cd = @P-p1; // set origin to sit on p1

vector4 q = dihedral(aim,xaxis); 
@Cd = qrotate(q, @Cd);
@Cd = @Cd.x / d; // normalize
```

同事Ben Skinner向我指出了一种更简洁的方法。点积比较矢量方向。我们能做的只是将位置（以 p1 为原点）与 p1->p2 的向量进行比较。如果该矢量是平行的，它将是白色的，当它转向时，它会变暗并最终在垂直于我们想要的矢量时变成黑色。再次规范化以保持值正确：

```cpp
vector p1, p2, v1, v2;

p1 = point(1,'P',0);
p2 = point(1,'P',1);

v1 = @P-p1; // treat p1 as origin;
v2 = normalize(p2-p1);

float r = distance(p1,p2);
@Cd = dot(v1,v2)/r;
```
