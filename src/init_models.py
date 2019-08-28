import tensorflow as tf
from keras.models import load_model
from keras.optimizers import Adam
from keras_unet.metrics import iou, iou_thresholded

SEG_MODEL_PATH = './models/CornerSegmentationUNet.h5'
CLASS_MODEL_PATH = './models/Stone_Classifier.h5'

# since we are working with multiple models, we have to switch graphs and sessions between use:
# with graph_var.as_default():
#      with session_var.as_default():
#             model.predict(INPUT)
#
# since we saved model including optimizer state and custom metrics,
# we need to compile it accordingly even though we don't need training capabilities here

def init_seg_model():
    graph = tf.Graph()
    with graph.as_default():
        session = tf.Session()
        with session.as_default():
            model = load_model(SEG_MODEL_PATH, 
                               custom_objects={'iou': iou, 
                                               'iou_thresholded': iou_thresholded})
            model.compile(optimizer=Adam(lr=1e-4),
                  loss='binary_crossentropy',
                  metrics=[iou, iou_thresholded])
    return graph, session, model

def init_class_model():
    graph = tf.Graph()
    with graph.as_default():
        session = tf.Session()
        with session.as_default():
            model = load_model(CLASS_MODEL_PATH)
            model.compile(optimizer='adam', 
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])
    return graph, session, model