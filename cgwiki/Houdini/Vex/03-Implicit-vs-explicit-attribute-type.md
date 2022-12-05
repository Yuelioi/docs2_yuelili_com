# 隐式与显式属性类型

请注意，wrangles 隐式包含某些常见的属性类型（@P、@Cd、@N、@v、@orient、@id、@name 等），但如果有自己的属性，Houdini 默认是浮点类型，切记。

为确保 Houdini 运行正确，请在前面添加类型别名。例如，已将 @mycolour 设置为矢量，并尝试在Vex中使用它：

```cpp
// 不好
@Cd = @mycolour; // 默认作为浮点类型读取 (ie, 只读取了 @mycolour的R通道)

// 好
@Cd = v@mycolour; // 正常读取矢量值
```

我总是忘记，对Vex大喊大叫，最后, 切记在属性名称前加上“v”(属性类型)。
