"""Reads game position by classifying segments using simple model"""

import numpy as np

SEGMENT_RES = 20 # 19x20 - goban is 19x19, patches will be 20x20
BATCH_SIZE = 19

def cut_segments(img):
    segments = []
    for x in range(19):
        for y in range(19):
            segment = img[x*SEGMENT_RES:(x+1)*SEGMENT_RES, y*SEGMENT_RES:(y+1)*SEGMENT_RES]
            segments.append(segment)
    return segments

def classify_segments(segments, graph, session, model):
    X = np.zeros((361, 20, 20), dtype=float)
    X = X / 255.
    for i, segment in enumerate(segments):
        X[i,::] = segment
    with graph.as_default():
        with session.as_default():
            y = model.predict(X, BATCH_SIZE) 
    predictions = np.argmax(y, axis=0) #select most likely class
    return predictions

def read_position(warped, graph, session, model):
    segments = cut_segments(warped)
    predictions = classify_segments(segments, graph, session, model)
    position = np.reshape(predictions, (19,19))
    return position