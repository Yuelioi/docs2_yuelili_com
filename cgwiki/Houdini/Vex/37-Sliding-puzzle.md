# 滑动拼图

幻灯片拼图.gif

下载场景：文件：slide_puzzle.hip

感觉有一种更优雅的方法可以做到这一点，但是在等待渲染时快速尝试，把它留在这里作为对我自己的嘲讽以改进它......

这在求解器 sop 中使用了一些 vex，其想法是每个时间间隔开始时的一块（块 0）查看其邻居，并随机选择一个。对于剩余的时间间隔，它从当前位置插值到目标邻居，同时让邻居做相反的事情。在解算器之后我隐藏了那块，所以看起来其余的块正在洗牌到备用槽中。

解决方案中缺乏优雅归结为我通常使用求解器的问题；我总是偏离 1，或者计算在我的循环中偏离了一点点，所以碎片卡住了，或者加倍，或者做其他愚蠢的事情。在这里，我必须仔细检查这些棋子是否无意中将它们的当前位置和目标位置设置为相同的值，其余位置是否干净整洁，以及其他一些我认为不需要做的繁琐的事情。总有一天我会拥有一个令人惊叹的精巧算法心智库，但不是今天……不是今天……
