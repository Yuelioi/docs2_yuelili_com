# 用 vex 和矩阵缩放

矩阵vex demo.gif

下载场景：文件：vex_matrix_scale.hipnc

当然有很多方法，如果你有多边形，这可能是最简单的方法：

```cpp
matrix3 m = ident();
scale(m,chv('scale'));
@P *= m;
```

首先我们用 ident() 定义一个空矩阵。接下来我们使用向量缩放该矩阵，这里我很懒，从 UI 获取该向量，所以 chv('scale') 从通道读取向量，而 scale(m, myvector) 直接缩放矩阵到位，请注意该调用没有返回类型。最后要应用它，您只需将点乘以前面讨论的矩阵即可。

但是，如果您有基本体，例如基本球体或基本锥体，请记住在基本体的中心只有一个点，因此缩放不会有任何效果。相反，原语有自己的隐藏矩阵，称为内在变换。要设置它，您可以使用 setprimitiveintrinsic 函数，矩阵的设置和缩放是相同的。

```cpp
matrix3 m = ident();
scale(m,chv('scale'));
setprimintrinsic(0,'transform',0,m);
```

严格来说，这是一个原始操作，所以我们真的应该改为原始操作，但在这种情况下，点和 prim 共享相同的 id，所以这并不重要。函数调用需要知道要处理的几何输入、内在属性的名称、哪个 prim，以及最后要设置的值。

所以

```cpp
setpriminstrinsic ( input, instrinsic_name, which_prim, what_value);
```

成为

```cpp
setpriminstrinsic ( 0, 'transform', 0, m);
```
