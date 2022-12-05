# 确保唯一名称

Vex唯一名称.PNG

来自可爱的朋友兼同事Ben Skinner的好问题。假设我们有一些带有@name 属性的基元，并且有几个共享相同的名称。我们怎样才能使名字独一无二？

懒惰的答案只是将 primnum 附加到名称：

```cpp
@name += '_' + itoa(@primnum);
```

有效，但有点生硬。如果有些名字没有重复，我们可以保持不变吗？有一些 vex 函数可以识别唯一的属性值，这里我们将使用findattribval​​count。如果有超过 1 个唯一值，此代码段将仅运行重命名：

```cpp
int count = findattribvalcount(0,'prim','name', @name);
if (count>1) {
  @name += '_'+itoa(@primnum);
}
```

也有效。但是结果有点乱，因为 primnum 后缀是任意的而不是有序的。理想情况下，如果有 4 个 prims 共享名称“thomas”，则它们的名称应为“thomas_0、thomas_1、thomas_2、thomas_3”。我们可以使用findattribval​​ 来做到这一点，它创建一个原始数数组。如果数组的长度大于 1，则使用find获取数组中该 prim 的索引，并将其用作后缀：

```cpp
int prims[] = findattribval(0,'prim','name', @name);
if (len(prims)>1){
    int pr = find(prims, @primnum);
    s@name +='_'+itoa(pr);
}
```
