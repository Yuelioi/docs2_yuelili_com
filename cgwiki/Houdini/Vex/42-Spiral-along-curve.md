# 沿曲线螺旋

曲线上的螺旋 small.gif

下载臀部：文件：spiral_along_curve.hip

聪明人HowieM的提示导致了这个令人愉快的干净设置。该曲线具有来自重采样的@curveu，以及用于生成法线、切线、双切线（存储为@N、@t、@bt）的多边形。

每个点都沿着@N 移动，但首先我们围绕切线@t 旋转@N。通过随时间和@curveu 控制旋转量，我们可以生成螺旋线。

因为除了练习之外，我最近一直在做很多四元数的事情，所以我使用 qrotate 函数完成了这项工作。添加了混合香料的一些随机偏移的能力。

```cpp
float speed, angle, rand;
vector dir;
vector4 q;

dir = @N;
speed = @Time * ch('speed');
angle = speed+@curveu*ch('spirals');
q = quaternion(v@t*angle);
dir = qrotate(q, dir);
rand = 1+rand(@ptnum)*ch('rand_offset');
@P += dir*ch('offset')*rand;
```
