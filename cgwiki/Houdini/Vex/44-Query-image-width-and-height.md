# 查询图片宽高

Vex uv tex 修复.gif

下载臀部：文件：uv_scale_from_image.hip

```cpp
string map=chs('image');
float x, y;
teximport(map, 'texture:xres', x);
teximport(map, 'texture:yres', y);
@ratio = x/y;
```

teximport 函数允许您查询图像的一些属性（完整列表在这里：https ://www.sidefx.com/docs/houdini/vex/functions/teximport.html ），比将图像加载到 cops 并查询它更快方法。此示例使用它来缩放对象的 uv，以便 uv 与输入图像的比例相匹配。
