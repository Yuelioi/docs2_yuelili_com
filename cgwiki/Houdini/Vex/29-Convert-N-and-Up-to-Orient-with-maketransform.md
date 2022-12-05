# 使用 maketransform 将 N 和 Up 转换为 Orient

东方maketransform.gif
在@N+@up 和@orient 之间交换，看起来完全一样，万岁！

下载场景：文件：convert_n_and_up_to_orient.hipnc

'坚持'你可能会说，'以前的解决方案怎么不模棱两可？'。你是对的，如果不调用向上矢量，我们根本就没有真正确定一个稳定的旋转。这几个月来一直困扰着我，这对我来说很典型，我太骄傲了，不能只问知道的人。

有一段时间我认为答案是 lookat() 函数，根据文档，它是

```cpp
lookat(vector from, vector to, vector up);
```

所以知道复制 sop 将 z 轴向下对准@N，我认为这会起作用：

```cpp
lookat( {0,0,1}, @N, @up);
```

结果……不对。有点稳定，有点错误，尝试向量的每个排列都不起作用。嘘。

今天我看了一篇关于makebasis的论坛帖子，这似乎是正确的，但不是。偶然地，我开始在 houdini 帮助中输入“make”，它弹出了 maketransform。嘿，这就是功能：

```cpp
matrix3 m = maketransform(@N,@up);
@orient = quaternion(m);
```

最终测试是设置一些随机的@N 和@up，旋转@up，然后在第二次Vex中转换为@orient。启用/禁用第二个 wrangle 应该不会导致视觉上的变化，您可以在本章顶部的 gif 中看到这一点。
