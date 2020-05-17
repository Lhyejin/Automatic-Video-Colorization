## tensorflow 2.0 version (use tf.compat.v1)


### Requirement
require packages : environment.yml or conda-gpu-cuda10.yml (in preprocess folder)
we tested on Cuda 10.0 + cudnn 7.5 + T4

```
$conda env create -f environment.yml or conda_gpu_cuda10.yml
```


tf 2.0.0 module don't support tf.contrib, so we change slim.conv2d to layers.conv2d (temporary)

**inference of original pre-trained model**
```
# change pre-trained model variable name using preprocess/change_conv2d.py
python main_woflow_up.py --model ckpt_woflow --use_gpu 1 --test_dir test_sample0
```


### Training

**prepare**

make optical flow map (more information in pytorch_pwc folder)

use pytorch_pwc/run_data.py

**training**
```
python main_whole_up.py --h
```

### inference
```
python test_main_whole.py --h
```
