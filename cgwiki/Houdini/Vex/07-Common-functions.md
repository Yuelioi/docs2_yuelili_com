# 常用函数

这些出现在我 99% 的Vex中：

fit() - 取一个介于 2 值之间的数字，将其拟合在另外 2 个值之间，通常为 0-1。例如，将 @u 从范围 -5,20 重新映射到 0-1： foo = fit(@u, -5, 20, 0, 1);
rand() - 生成一个介于 0 和 1 之间的随机数。通常将点 id 提供给它，因此每个点都会得到一个随机数：foo = rand(@ptnum);
sin(), cos() - 三角函数，但以弧度表示。
radians() - 将数字从度数转换为弧度：foo = radians(90);
length() - 测量向量的长度。例如，测量一个点到原点的距离：dist = length(@P);
distance() - 测量两点之间的距离：dist = distance(@P, v@mypoint);
