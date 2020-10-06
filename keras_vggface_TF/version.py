__version__ = '0.7'

def pretty_versions():
    #import keras
    import tensorflow as tf
    #k_version = keras.__version__
    t_version = tf.__version__
    return "keras-vggface : {}, tensorflow : {} ".format(__version__,t_version)
