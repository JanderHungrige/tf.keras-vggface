# tf.keras-vggface

Here you can find the modl from rcmalli converted to tf.keras. 

`Original: https://github.com/rcmalli/keras-vggface`

Install via:

`pip install git+https://github.com/JanderHungrige/tf.keras-vggface`


### import
like this:
```
from keras_vggface_TF.vggfaceTF import VGGFace
from keras_vggface_TF import utils
```

If pretrained weigths are used, the weigths are automatically downloaded from rcmalli (links included in utils.py). 

### example:
```
from keras_vggface_TF.vggfaceTF import VGGFace
pretrained_model = VGGFace(model='resnet50', include_top=True, input_shape=(224, 224, 3), pooling='avg')  # pooling: None, avg or max
```
### Recommened Libraries: 

Tensorflow>=1.15.3

### Future
weights from quantisation aware training will be uploaded by me in time.
