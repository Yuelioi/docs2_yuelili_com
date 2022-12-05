# 创建 UI 控件

假设有这个：

```cpp
@Cd.r = sin( @P.x * 5 );
```

但想将 5 更改为另一个数字。可以继续使用不同的数字更改代码，或将 5 替换为 ch('scale') ：

```cpp
@Cd.r = sin( @P.x * ch('scale') );
```

ch() 告诉 Houdini 去寻找一个通道，也就是 Houdini 的 UI 组件，通常是一个滑块。点击文本编辑器右侧的小插头图标，Houdini 会自动扫描 vex 代码，发现目前尚不存在该通道，就会 wrangle UI 的底部创建了一个名为“scale”的通道。开始滑动它，此时会看到颜色更新。

可以使用多种通道类型。ch() 和 chf() 都会创建了一个浮点通道。其他类型：

```cpp
// 整数通道
i@myint = chi('myint');

// 矢量通道
v@myvector = chv('awesome');

// 随机通道
f@foo = chramp('myramp',@P.x);
```

最后一个非常方便，在一行中您可以读取一个值 (@Px)，通过 UI ramp 小部件重新映射它，并将其提供给@foo。假定输入值在 0-1 范围内，通常必须在斜坡之前调整这些值。拟合函数 fit(value、oldmin、oldmax、newmin、newmax)。例如，在 -0.5 和 6 之间重新映射 X，然后使用渐变将这些值输入红色通道：

```cpp
float tmp = fit(@P.x, -0.5,6,0,1);
@Cd.r = chramp('myramp',tmp);
```

为什么要停在那里呢？使用 UI 滑块定义起点和终点！

```cpp
float min = ch('min');
float max = ch('max');
float tmp = fit(@P.x, min,max,0,1);
@Cd = 0; // 在下一步之前将颜色重置为黑色的小技巧
@Cd.r = chramp('myramp',tmp);
```
