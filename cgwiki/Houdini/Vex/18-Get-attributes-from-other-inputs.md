# 从其他输入获取属性

如前所述，您有 2 个相似的网格输入一个 wrangle，并且您想要访问第二个网格的匹配 P：

```cpp
vector otherP = point(1,"P", @ptnum);
// do something with it
```

另一种方法是在您想要的属性前加上 @opinput1_ 前缀。这隐含地使用了相同的 ptnum，从而节省了对 point() 的调用：

```cpp
vector otherP = @opinput1_P;
```

与普通 @ 语法相同的规则适用，它会猜测已知属性的类型（P、N、v 等），除非您另有说明，否则任何其他内容都将默认为 float：

```cpp
float foo   = @opinput1_myfloat;   // fine, default is float
float bar  = f@opinput1_myfloat;   // explicit type
float myvector  = @opinput1_thevector;   // bug, as thevector will be returned as float
float workingvector  = v@opinput1_thevector;   // better
```

当然，要访问连接到第 3 个或第 4 个插槽的任何其他地理区域，请增加数字（您现在可能已经猜到 0 是第一个输入）：

```cpp
float two   = @opinput1_myfloat;
float three = @opinput2_myfloat;
float four  = @opinput3_myfloat;
```

我希望他们选择了一个比 opinputN_ 更短的字符串，因为在实践中有时感觉就像键入 point() 更快，但是嘿，有选项真好。:)
