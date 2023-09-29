
# Method 1(recommend)



## 1. Installing SpinView with conda virtual environment.

* To install `miniconda` please follow the instructions [here](https://docs.conda.io/en/latest/miniconda.html).

* To install `Anaconda` please follow the instructions [here](https://docs.anaconda.com/anaconda/install/).

## 2. Create a new conda environment for SpinView using the following command:

<div class="termy">
```console
$ conda create -n spinview python=3.9
$ conda create -n spinview python=3.9

Proceed ([y]/n)?     y
---> 100%
Successfully created conda environment for SpinView
```
</div>

## 3. Install SpinView using the following command:

<div class="termy">
```console
$ conda activate spinview
$ pip install spinview
---> 100%
Successfully installed spinview
```
</div>


Note that user in `China mainland` may need to add a pip source to make sure you can easily download all packages. (add `-i https://pypi.tuna.tsinghua.edu.cn/simple`)

<div class="termy">
```console
$ pip install spinview  -i https://pypi.tuna.tsinghua.edu.cn/simple
---> 100%
Successfully installed spinview
```
</div>


## 4. launch SpinView in simulation folder under auto mode using the following command:


<div class="termy">
```console
$ spinview start
```
</div>

Note: it will be a little bit slow from cold start, please wait for a while. 

Note: it will be a little bit slow from cold start, please wait for a while. 

<div style="text-align: center;">
<img width=500, height=300 src="/SpinView/assets/home.png" draggable="false">
</div>

Note:

1. When using Client(VTKjs) mode, manually reload the webpage is needed. 
2. Suggest to use local view instead of increase the quality of server mode.


