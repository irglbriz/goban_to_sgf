import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import keras
from keras.models import load_model
from keras.optimizers import Adam
from keras.utils import CustomObjectScope
from keras_unet.metrics import iou, iou_thresholded

SEG_MODEL_PATH = './models/CornerSegmentationUNet.h5'
CLASS_MODEL_PATH = './models/Stone_Classifier.h5'

def init_seg_model():
    graph = tf.Graph()
    with graph.as_default():
        session = tf.Session()
        with session.as_default():
            with CustomObjectScope({'GlorotUniform': tf.keras.initializers.glorot_uniform}):
                model = load_model(SEG_MODEL_PATH, 
                               custom_objects={'iou': iou, 
                                               'iou_thresholded': iou_thresholded})
    print('Model0 initialized\n')
    return graph, session, model

def init_class_model():
    graph = tf.Graph()
    with graph.as_default():
        session = tf.Session()
        with session.as_default():
            with CustomObjectScope({'GlorotUniform': tf.keras.initializers.glorot_uniform}):
                model = load_model(CLASS_MODEL_PATH)
    print('Model1 initialized\n')
    return graph, session, model