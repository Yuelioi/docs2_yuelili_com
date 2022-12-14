# 将 vex 和 vops 与片段混合

通常我会先在 vops 开始做，然后发现我的一部分节点只要几行 vex 就能搞定。此时，我将放入一个“片段”vop，然后得到一些类似于Vex节点的东西。这样编写所需代码，并且与周围的 vops 愉快地共存。

现在，无需使用 @ 前缀，连接到代码片段中的任何属性对 vex 编辑器都是可见的。因此，如果连接 P 和用户定义的属性“myvector”，您只需键入代码

```cpp
P = P * myvector;
```

无论作为输入连接到代码段，都将成为输出。不会神奇地将结果提供给下游 sops，它的行为类似于 vop 节点，因此在上面的示例中，您需要手动将 outP 输出连接到 P（或您需要的任何其他内容）。

“内联代码”vop 类似，但需要更多的掌握来龙去脉(handholding)。因为我在 vops 中的 vex 一般不复杂，一个片段足矣，但为了以防万一，这是我之前的“内联代码”注释：

默认情况下，内联代码 vop 上没有输出，在参数界面的底部，以转到第一个禁用的输出，设置其类型（例如矢量），并为其命名（例如，P）。然后你会看到一个“P”出现在节点的右侧，准备好连接到其他东西。因为我怕忘记，所以倾向于明确命名，例如“outP”而不是“P”。

要为该输出分配值，请使用 $ 前缀。例如，我想通过 Cd.r 来驱动 Py。在 UI 上将输出定义为 outP。

```cpp
P.y=Cd.r;    
$outP=P;
```
