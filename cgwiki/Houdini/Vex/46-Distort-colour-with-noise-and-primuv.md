# 用噪声和primuv扭曲颜色

翘曲小.gif

下载臀部：文件：col_distort.hip

我以前尝试过用噪音扭曲表面值，但从来没有完全正确，Jake Rice 有答案（Jake Rice 总是有答案）。从卷曲噪声开始定义失真，投射回您的表面，在该点查找颜色。简单，快速，效果很好。

```cpp
vector noise = curlnoise(@P*ch('freq')+@Time*0.5);
vector displace = noise - v@N * dot(noise, v@N); //project the noise to the surface
int prim;
vector uv;
xyzdist(0, @P + displace * ch("step_size"), prim, uv);
@Cd = primuv(0, "Cd", prim, uv);
```

我尝试使用另一个属性噪音 sop 来为噪音值获得一个漂亮的 UI，但有趣的是，没有什么比卷曲噪音看起来更好的了。
