# Vex vs hscript vs vops vs 其他一切

Vex 通常比使用 hscript 更快，并且扩展性更好。

Vops 很棒，但通常简单的事情，在 vex 只需2行，而在 vops 需要 7 或 8 个节点。也就是说，某些操作在 vops 中更容易，例如使用噪波或加载其他模式，或者在不完全知道您的目标构建东西时。完成后，如果您认为更好，可以随时重新编写设置。

对于其他 sops，wrangle 可以完成其他几个 sops 的工作，通常效率更高，并且能够轻松制作 UI 元素。一些例子：

point sop - 很多老的 tuts 使用 point sops。不。拒绝吧。
attribcreate sop - 在Vex中更快更容易。您可能想要使用 attribcreate 的唯一原因是获取局部变量，但只能将它们与点 sop 一起使用，我们觉得这很糟糕。
vop 绑定和 vop 绑定导出 - 使用 @ 快捷方式获取和设置点属性比在 vops 中更容易。
在 vops 中提升参数 - 再次，ch('foo') vs r.click，绑定，摆弄名称，意识到它的错误，在半挂起状态下获取参数，呃
hscript 中的通道引用 - 与 ch() 的自动绑定是蜜蜂的膝盖(bees knees)。那个小插头按钮是有史以来最好的东西。

这有点陈词滥调，所有的 sops 和 vops 在某些时候都是有用的，但Vex的速度和优雅所向披靡。
