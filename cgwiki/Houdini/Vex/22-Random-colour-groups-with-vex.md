# 带有 vex 的随机颜色组

上述代码段的扩展：

```cpp
string groups[]  = detailintrinsic(0, 'primitivegroups');

foreach (string g; groups) {
    if (inprimgroup(0,g,@primnum)==1) {
        @Cd = rand(random_shash(g));
    }
}
```
