# 自定义 UI 元素

插件按钮是一个方便的功能，它只是扫描任何通道引用，并创建默认类型和默认值。创建通道后，可以右键单击 wrangle 节点并选择“编辑参数界面”（或使用参数面板中的齿轮菜单），然后根据需要更改浮动范围、默认值、标签。

我经常将默认矢量通道转换为颜色通道。并在 vex 中制作尽可能多的矢量通道，例如：

```cpp
v@colour1 = chv('col1');
v@colour2 = chv('col2');
v@colour3 = chv('col3');
v@colour4 = chv('col4');
```

然后会点击插件按钮，编辑参数界面，按住 Shift 键选择制作的所有通道，并将类型字段更改为“color”，为了更加漂亮，将“显示颜色为”更改为“hsv 滑块” . 最方便。