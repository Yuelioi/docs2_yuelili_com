# getderiv

在这一页

- [衍生品选项](#衍生品-选项)
- [例子](#例子)

|

[displace](../contexts/displace.html)
[fog](../contexts/fog.html)
[light](../contexts/light.html)
[shadow](../contexts/shadow.html)
[surface](../contexts/surface.html)

`void getderiv(float attr, string attrName, int isVertexAttr, float s, float t, float &du, float &dv, ...)`

`void getderiv(<vector>attr, string attrName, int isVertexAttr, float s, float t, <vector>&du, <vector>&dv, ...)`

::: info Note

内涵(s) 如果导数被查询到的是多边形网格，那么它就会被作为细分曲面进行相互采样。

## Arguments

`attr`

属性值。

`attrName`

要评估的属性的名称。

`isVertexAttr`

设置为`1`表示该属性是一个顶点类型。

`s`

参数 S 的阴影值。这应该从`s`全局变量中传递。

`t`

参数<类型>阴影值。这应该由`t`全局变量传递。

`du`

属性在 U 方向的衍生物。

`dv`

属性在 V 方向上的衍生物。

## 衍生品期权

[¶](#derivatives-options)

计算导数的函数需要额外的参数，以便对导数计算进行调整。

## Arguments

`int`
`=0`

"`extrapolate`", 导数是否 "平滑 "地跨越补丁边界。在大多数情况下，这是真的，如果外推法被打开，导数计算对 C2 表面来说应该是精确的。然而，当 VEX 变量以高频率变化时（例如，高频率的位移图导致 P 变量的高频率变化），导数计算的外推可能导致补丁边界之间不连续的夸张。

`int`
`=1`

"`smooth'"，在斑块上非均匀地调整差值的大小。这通常会减少位移/纹理明暗器中的补丁不连续。然而，在一些奇怪的情况下，你可能想把这个功能关掉。

```c
N = computenormal(P, "extrapolate", 1, "smooth", 0);

```

## Examples

```c
// Get derivatives of point attribute 'N'
vector dNdu, dNdv;
getderiv(N, "N", 0, s, t, dNdu, dNdv);

```

## See also

- [Du](Du.html)
- [Dv](Dv.html)

|
math

[Du](Du.html)

[Dv](Dv.html)

[Dw](Dw.html)

[abs](abs.html)

[acos](acos.html)

[asin](asin.html)

[atan](atan.html)

[atten](atten.html)

[avg](avg.html)

[cbrt](cbrt.html)

[ceil](ceil.html)

[cos](cos.html)

[cosh](cosh.html)

[cracktransform](cracktransform.html)

[cross](cross.html)

[degrees](degrees.html)

[dot](dot.html)

[erf](erf.html)

[erf_inv](erf_inv.html)

[erfc](erfc.html)

[exp](exp.html)

[floor](floor.html)

[frac](frac.html)

[fuzzify](fuzzify.html)

[getderiv](getderiv.html)

[isfinite](isfinite.html)

[isnan](isnan.html)

[log](log.html)

[log10](log10.html)

[max](max.html)

[min](min.html)

[pow](pow.html)

[product](product.html)

[radians](radians.html)

[resample_linear](resample_linear.html)

[rint](rint.html)

[shl](shl.html)

[shr](shr.html)

[shrz](shrz.html)

[sign](sign.html)

[sin](sin.html)

[sinh](sinh.html)

[solvecubic](solvecubic.html)

[solvepoly](solvepoly.html)

[solvequadratic](solvequadratic.html)

[solvetriangleSSS](solvetriangleSSS.html)

[sqrt](sqrt.html)

[sum](sum.html)

[tan](tan.html)

[tanh](tanh.html)

[trunc](trunc.html)

[variance](variance.html)

|
shading

[Du](Du.html)

[Dv](Dv.html)

[Dw](Dw.html)

[area](area.html)

[ashikhmin](ashikhmin.html)

[atten](atten.html)

[blinn](blinn.html)

[blinnBRDF](blinnBRDF.html)

[chiang](chiang.html)

[computenormal](computenormal.html)

[cone](cone.html)

[cvex_bsdf](cvex_bsdf.html)

[diffuse](diffuse.html)

[diffuseBRDF](diffuseBRDF.html)

[dsmpixel](dsmpixel.html)

[environment](environment.html)

[fastshadow](fastshadow.html)

[filtershadow](filtershadow.html)

[filterstep](filterstep.html)

[fresnel](fresnel.html)

[frontface](frontface.html)

[getderiv](getderiv.html)

[getfogname](getfogname.html)

[getglobalraylevel](getglobalraylevel.html)

[getgroupid](getgroupid.html)

[getlocalcurvature](getlocalcurvature.html)

[getmaterialid](getmaterialid.html)

[getobjectid](getobjectid.html)

[getobjectname](getobjectname.html)

[getprimid](getprimid.html)

[getptextureid](getptextureid.html)

[getraylevel](getraylevel.html)

[getrayweight](getrayweight.html)

[getsamplestore](getsamplestore.html)

[getsmoothP](getsmoothP.html)

[getuvtangents](getuvtangents.html)

[ggx](ggx.html)

[gradient](gradient.html)

[hair](hair.html)

[henyeygreenstein](henyeygreenstein.html)

[isotropic](isotropic.html)

[israytracing](israytracing.html)

[isshadingRHS](isshadingRHS.html)

[lightstate](lightstate.html)

[matchvex_blinn](matchvex_blinn.html)

[matchvex_specular](matchvex_specular.html)

[objectstate](objectstate.html)

[phong](phong.html)

[phongBRDF](phongBRDF.html)

[phonglobe](phonglobe.html)

[ptexture](ptexture.html)

[rayhittest](rayhittest.html)

[rayimport](rayimport.html)

[reflect](reflect.html)

[refract](refract.html)

[renderstate](renderstate.html)

[resolvemissedray](resolvemissedray.html)

[sample_geometry](sample_geometry.html)

[scatter](scatter.html)

[setsamplestore](setsamplestore.html)

[specular](specular.html)

[specularBRDF](specularBRDF.html)

[sssapprox](sssapprox.html)

[teximport](teximport.html)

[texture](texture.html)

[trace](trace.html)

[translucent](translucent.html)

[uvunwrap](uvunwrap.html)

[volume](volume.html)

[wireblinn](wireblinn.html)

[wirediffuse](wirediffuse.html)
