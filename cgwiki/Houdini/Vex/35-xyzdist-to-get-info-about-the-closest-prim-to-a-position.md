# xyzdist 获取关于最接近某个位置的 prim 的信息

Xyzdist 可视化.gif

下载场景：文件：xyzdist_example.hipnc

如果你用过 ray sop，这是类似的事情。最简单的，给它一个位置，它会告诉你到最近的图元的距离。更有用的是，它还可以告诉您该图元的原色，以及该原色上最接近您位置的 uv。有了这些信息，您就可以计算出 prim 上的位置。

与矩阵 rotate() 函数一样，primnum 和 uv 是通过指针设置的，因此您首先创建所需的变量，然后在函数内调用它们：

```cpp
float distance;
int myprim;
vector myuv;
distance = xyzdist(1,@P, myprim, myuv);
```

要获得那个 uv 在那个 prim 上的确切位置，以及 prim 的颜色：

```cpp
vector mypos = primuv(1,'P', myprim ,myuv);
@Cd = prim(1,'Cd', myprim);
```

上面设计的 gif 显示了所有这一切。一个点围绕着多色猪运行。xyzdist 找到距离、primnum、最近的 prim 的 uv，在该位置创建一个点，从最近的 prim 设置它的颜色，从轨道点到新点绘制一条红线，最后是一个线框球体在新点上生成，它的颜色也与它当前所在的prim相匹配，它的半径是根据从xyzdist返回的距离设置的，所以它总是刚好接触到轨道点。
