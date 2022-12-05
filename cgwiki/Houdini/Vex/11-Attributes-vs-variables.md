# 属性与变量

上面给出的示例都使用 @ 语法来获取和设置点的属性。如果有多个Vex，或者如果不需要Vex之外的那些属性，几何电子表格就会开始变得非常混乱，所有额外的点数据都会占用内存，尤其是当您有复杂的场景时。

相反，可以创建仅存在于Vex中的变量。语法类似于其他 c 风格的语言；用完整的词定义类型，不要在变量上使用前缀：

```cpp
float foo;
vector bar = {0,0,0};
matrix m;

foo = 8;
bar.x += foo;
```

Point 属性和 vex 变量存在于不同的世界中，因此可以拥有相同名称，并且它们可以共存。我倾向于在实践中避免这种情况，很容易在不想要的地方添加一个@，或者在你需要的地方删除一个，然后破坏东西：

```cpp
float dist = length(@P);  // 局部vex变量, 仅存在本 wrangle

@dist = dist;  // 创建一个点属性, @dist, 并分配局部变量 'dist'. 全局共享
```

重写前面的示例以使用变量，并首先执行声明变量的正式操作，以便清楚地看到发生了什么：

```cpp
float d;
float speed;
float falloff;
 
d = length(@P);
speed = @Time * ch('speed');
falloff = fit(d, ch('start'), ch('end'),1,0);
 
@P.y = sin(d*ch('scale')+speed);
@P.y *= ch('height');
@P.y *= chramp('falloff', falloff);
```
