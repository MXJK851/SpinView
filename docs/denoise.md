
# Denoise


### For interactive objects:
* Using Ctrl + left click to rolate the object
* Using Shift + left click to move the object
* Using middle wheel to scale the object
* You can also try other VTKjs keyboard shortcuts



Note that denoise is not limit to small 2D data, here we use 2D system as a demo is just because the performance limit of Github pages. You can find more complex demo in our paper.


## original data:
In this demo, thermal fluctuation make the texture can not be seen or understand clearly.

<div style="text-align: center;">
<iframe width=700, height=500 frameBorder=0 seamless="seamless" scrolling="no" src="/SpinView/assets/html/denoise_org.html"></iframe>
</div>


## Denoise using `FFT` filter:
This feature is apply a rectanglar low pass filter to the data (after FFT). Then apply revised FFT to get orginal data back.

<div style="text-align: center;">
<img width=300, height=300 src="/SpinView/assets/gif/denoise_fft.gif" draggable="false">
</div>

<div style="text-align: center;">
<iframe width=700, height=500 frameBorder=0 seamless="seamless" scrolling="no" src="/SpinView/assets/html/denoise_fft.html"></iframe>
</div>

But it is worthy to note that, distortions of denoising is always exist when using FFT, here I give a extreme case where the data is distorted a lot.:


<div style="text-align: center;">
<img width=300, height=300 src="/SpinView/assets/gif/denoise_fft2.gif" draggable="false">
</div>

<div style="text-align: center;">
<iframe width=700, height=500 frameBorder=0 seamless="seamless" scrolling="no" src="/SpinView/assets/html/denoise_fft2.html"></iframe>
</div>


## Denoise using `Butterworth` filter:
This feature is first transfer the data into squance of 1D data (can be viewed as signal) then apply Butterworth filter to each 1D data. Then transfer the data back to orignal vector field data. 
Note that, this feature may not good as FFT low pass filter, may improve in the future.

<div style="text-align: center;">
<img width=300, height=300 src="/SpinView/assets/gif/denoise_bt.gif" draggable="false">
</div>

<div style="text-align: center;">
<iframe width=700, height=500 frameBorder=0 seamless="seamless" scrolling="no" src="/SpinView/assets/html/denoise_bt.html"></iframe>
</div>
