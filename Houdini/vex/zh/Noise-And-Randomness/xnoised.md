# xnoised

`void xnoised(float x, float &v, float &dvdx)`

`void xnoised(float x, vector &v, vector &dvdx)`

`void xnoised(float x, float y, float &v, float &dvdx, float &dvdy)`

`void xnoised(float x, float y, vector &v, vector &dvdx, vector &dvdy)`

`void xnoised(vector xyz, float &v, float &dvdx, float &dvdy, float &dvdz)`

`void xnoised(vector xyz, vector &v, vector &dvdx, vector &dvdy, vector &dvdz)`

`void xnoised(vector4 xyzw, float &v, float &dvdx, float &dvdy, float &dvdz, float &dvdw)`

`void xnoised(vector4 xyzw, vector &v, vector &dvdx, vector &dvdy, vector &dvdz, vector &dvdw)`

这将计算单纯的噪声值，以及沿每个轴的噪声导数。这可以相当有效地进行，因为有分析性导数可用。

参见 VEX 语言指南中的[噪声和随机性](.../random.html)以获得更多信息。

## See also

- [xnoise](xnoise.html)

|
noise

[anoise](anoise.html)

[curlnoise](curlnoise.html)

[curlnoise2d](curlnoise2d.html)

[curlxnoise](curlxnoise.html)

[curlxnoise2d](curlxnoise2d.html)

[cwnoise](cwnoise.html)

[flownoise](flownoise.html)

[flowpnoise](flowpnoise.html)

[hscript_noise](hscript_noise.html)

[hscript_rand](hscript_rand.html)

[hscript_snoise](hscript_snoise.html)

[hscript_sturb](hscript_sturb.html)

[hscript_turb](hscript_turb.html)

[mwnoise](mwnoise.html)

[noise](noise.html)

[noised](noised.html)

[onoise](onoise.html)

[pnoise](pnoise.html)

[xnoise](pxnoise.html)

[pxnoised](pxnoised.html)

[snoise](snoise.html)

[vnoise](vnoise.html)

[wnoise](wnoise.html)

[xnoise](xnoise.html)

[xnoised](xnoised.html)
