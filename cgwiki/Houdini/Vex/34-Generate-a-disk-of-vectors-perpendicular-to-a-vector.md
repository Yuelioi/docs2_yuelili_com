# 生成垂直于矢量的矢量圆盘

矢量磁盘.gif

下载场景：文件：disk_around_vector.hip

我的第一个 H16 演示场景，万岁！

```cpp
vector aim;
vector4 q;

aim = chv('aim');
@N = sample_circle_edge_uniform(rand(@ptnum));
q = dihedral({0,0,1}, aim);
@N = qrotate(q,@N);
@N *= ch('scale');
```

使用另一个超级方便的 sample_something_something 函数， 如果给定一个介于 0 和 1 之间的随机数， sample_circle_edge_uniform会在圆的边缘生成随机向量。圆盘的位置固定在 xy 平面上（即垂直于 {0,0, 1}). 要将该向量圆盘旋转到我们想要的位置，请使用前面概述的二面角/qrotate 技巧。这里我有一个球体并将其位置读取为目标向量。
