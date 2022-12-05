# 在 vex 中按程序访问组名

下载场景：文件：group_random_delete_vex.hipnc

对这个很满意。一个朋友（嘿 Jonno）有一个很大的复杂对象，里面有很多基元组，他想随机删除这些组的基元。我的第一反应是“呸，简单”，但仔细观察后发现并没有那么明显。是的，您可以使用爆炸或删除节点顶部的组下拉列表，甚至可以使用通配符和简单的表达式来选择内容，但除非有文本处理风格的技巧，您可以使用（例如，所有组都被命名为“group_123”） ，这可不好。

所需要的是获取所有组的数组，然后您可以通过索引引用它们（因此与其说“left_foot”，不如说“grouplist[2]”）。稍微挖掘一下，发现组名存储在一个详细的内在属性中。Houdini 隐藏了一些“奖励”属性，比如用于棱镜的完整变换矩阵，或者它们的表面积，它们可以从地理电子表格下拉列表中找到。地理组存储在详细信息级别。有了这个，我们可以将组提取到一个字符串数组中，然后做我们想做的：

```cpp
s[]@groups  = detailintrinsic(0, 'primitivegroups');
i[]@prims =  expandprimgroup(0, s[]@groups[1]);
```

第一行获取组数组，并将其存储在另一个属性“组”中，这样​​我们就可以在地理电子表格中查看并查看它是否有效。

第二行读取第二组 ( groups[1] )，获取该组中所有 primnums 的列表，并将其存储在一个属性中，再次查看它是否正常工作。

这里更进一步，使用上面的逻辑，每帧删除一个随机组：

```cpp
string groups[]  = detailintrinsic(0, 'primitivegroups');
int rand = int(rand(@Frame)*len(groups));
int prims[] =  expandprimgroup(0, groups[rand]);

// delete the prims
int p;
foreach (p; prims) {
 removeprim(0,p,1);
}
```

值得指出的是，如果您自己定义组，您最好使用一个属性来识别片段，并使用它来做任何随机的事情。例如，为每个 prim 分配一个 @piece 属性，并基于该属性进行删除：

```cpp
i@piece = @ptnum%3;

if (@piece==1) {
 removeprim(0,@primnum,1);
}
```

但是，如果您有重叠的组，则不起作用，在这种情况下，它对您来说是花哨的 shmantz 内在Vex魔法。
