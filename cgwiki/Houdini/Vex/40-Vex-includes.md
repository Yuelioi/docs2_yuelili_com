# Vex包括

Vex包含记录.gif

您可以在外部文件中创建函数库，然后像在 C 中一样将它们拉入。

首先，在您的 houdini 首选项文件夹下创建一个 vex/includes 文件夹。因此，就我在 Windows 上的情况而言，它位于我的文档文件夹 houdini16.0/vex/include 中。我在那里创建了一个文本文件 foo.h，并定义了一个简单的函数：

```cpp
function float addfoo(float a; float b) 
{
 float result = a + b;
 return result;
}
```

具体细节是我定义了一个函数，它接受 2 个 float 变量，并返回一个 float。

在 houdini 中我做了一个Vex，它调用了上面的函数：

```cpp
#include "foo.h"
@a = addfoo(3,4);
```

我遇到的一个轻微问题是更新 foo.h，但 houdini 不会检测到更改。我认为切换旁路标志就足够了，但不行。事实证明，如果 houdini 检测到您的Vex的代码更改，它只会触发 vex 重新编译。幸运的是，这可以像添加空格或回车一样简单，然后当您按下 ctrl-enter 时，您将获得更新。

如果你想把你的包含放在其他地方，你可以附加到系统变量 HOUDINI_VEX_PATH。
