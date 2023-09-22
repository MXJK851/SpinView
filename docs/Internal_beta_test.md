
# Internal beta test

It is an honour for us to invite Filipp, Wanjian, Manuel, Zhenzhu, Zhuanglin, Qingda, Zhenyang, Guoqiang, Zhiwei, Ivan to join our internal beta test.

Thank you all in advance for your time and effort to help us improve SpinView before it is released.

Here we provide step-by-step instructions for installing guide SpinView (internal-beta version).


## 1. Installing SpinView with conda virtual environment.

* To install `miniconda` please follow the instructions [here](https://docs.conda.io/en/latest/miniconda.html).

* To install `Anaconda` please follow the instructions [here](https://docs.anaconda.com/anaconda/install/).

You can choose one of the above two options to install conda.

## 2. Create a new conda environment for SpinView using the following command:

<div class="termy">
```console
$ conda create -n spinview python=3.9

Proceed ([y]/n)?     y
---> 100%
Successfully created conda environment for SpinView
```
</div>

## 3. Go to the path that have `spinview-1.0.0-py3-none-any.whl` file and install SpinView `spinview-1.0.0-py3-none-any.whl` file using the following command:


<div class="termy">
```console
$ pip install ./spinview-1.0.0-py3-none-any.whl
---> 100%
Successfully installed spinview
```
</div>

Note that user in China Mainland may need to add a pip source to make sure you can easily download all packages. (add `-i https://pypi.tuna.tsinghua.edu.cn/simple`)

<div class="termy">
```console
$ pip install ./spinview-1.0.0-py3-none-any.whl  -i https://pypi.tuna.tsinghua.edu.cn/simple
---> 100%
Successfully installed spinview
```
</div>



## 4. launch SpinView in simulation folder (sub-folder in the demo) under auto mode using the following command, remember you need to use the conda environment that you created in step 2:


<div class="termy">
```console
$ conda activate spinview

$ spinview start
```

Note: it will be a little bit slow from cold start, please wait for a while. 

</div>

<div style="text-align: center;">
<img width=500, height=300 src="/SpinView/assets/home.png" draggable="false">
</div>


## 5. You can followed the demo in features or try features with your own data:

Download the demo:

[Test.zip](/SpinView/internal_beta_test.zip){:download}

Note:

1. In UppASD demo, one trajectory is includes for 20 frames.

2. In Mumax3 demo,  10 snapshots are included for one trajectory.

3. In Spirit demo, 2 big snapshots(60*60*60), one is hopfion and another is skyrmion tube.

4. In Vampire demo, one trajectory with kagome lattice is include, in this case, rectangle mesh will not work, only trianglazation is needed for isosurface rendering.

Know problem:

1. In macos the local view windows can not close or will leave a python icon stay in your docker, see here: https://github.com/pyvista/pyvista/issues/1096, but it will not affect the main window, and the local view mode works properly when open it again. Our current suggestion is just leave the ghost windows there after close the local view windows and go back to the main window. (This problem will not happend in windows system.)