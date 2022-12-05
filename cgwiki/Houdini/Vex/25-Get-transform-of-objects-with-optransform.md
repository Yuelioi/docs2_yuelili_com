# 使用 optransform 获取对象的转换

猪凸轮 optransform.gif

下载场景：文件：optransform_pig.hipnc

将位置从点复制到其他点很容易，但如果您想读取摄像机的变换，天真的方法可能是通道引用摄像机参数窗格中的所有平移/旋转/缩放值。

更好的方法是使用 optransform vex 函数。它返回给定对象的矩阵，然后您可以将您的点乘以该矩阵，或者使用 cracktransform() 来提取您需要的信息。

语法非常简单：

```cpp
matrix m = optransform('/obj/cam1');
@P *=m;
```
