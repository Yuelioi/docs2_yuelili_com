# 将四元数与 qmultiply 组合

东方俯仰偏航roll.gif

下载场景：文件：orient_qmultiply_compose.hip

跟拉夫加朵学的一招，干杯！

上面示例中的某处是 2 个四元数技巧，对事物使用 qmultiply，并从角度/轴对创建四元数。Raph 向我展示了一种结合这些知识的优雅方式。假设您有一堆具有任意方向的点，并且您希望将它们全部在 x 轴上旋转 20 度，但在它们的局部旋转轴上。

你可以做的是创建一个临时四元数，它围绕原点 x 20 度，然后将其与原始四元数 qmultiply。简单的！

创建临时四元数比您想象的要容易；四元数函数可以取一个角度和轴，甚至更懒，定义轴向量，然后缩放该向量。轴矢量的长度将用作旋转量。例如：

```cpp
vector4 foo = quaternion({1,0,0}*0.2));
```

所以这是围绕 x 轴 ( 1,0,0 ) 旋转 0.2 弧度（大约 11 度）。

要将其添加到现有的方向，请使用 qmultiply：

```cpp
@orient = qmultiply(@orient, foo);
```

对此进行扩展，您可以为局部 x、y、z 定义临时四元数，使用通道来设置旋转量，并将每个四元数 qmultiply 到 @orient 上。这就是下面的Vex所做的，提供简单的 xyz 控制（我将其命名为 pitch/yaw/roll 因为它听起来更酷）。

```cpp
vector4 pitch = quaternion({1,0,0}*ch('pitch'));
vector4 yaw   = quaternion({0,1,0}*ch('yaw'));
vector4 roll  = quaternion({0,0,1}*ch('roll'));

@orient = qmultiply(@orient, pitch);
@orient = qmultiply(@orient, yaw);
@orient = qmultiply(@orient, roll);
```

一个很好的额外技巧是通过@ptnum 驱动旋转量，例如

```cpp
float speed  = rand(@ptnum,123) * @Time;
float offset = rand(@ptnum,456);
float flap = sin(speed+offset);

vector4 pitch = quaternion({1,0,0}*flap);

@orient = qmultiply(@orient, pitch);
```

这样一来，所有方向都将沿其局部 x 轴摆动，但具有独立的速度和偏移量。
