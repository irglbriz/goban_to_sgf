"""Reads game position by classifying segments using simple model"""

import numpy as np
from collections import Counter

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
    for i, segment in enumerate(segments):
        X[i,::] = segment
    X = X / 255.
    with graph.as_default():
        with session.as_default():
            y = model.predict(X, BATCH_SIZE)
    predictions = np.argmax(y, axis=1) #select most likely class
    return predictions

def read_position(warped, graph, session, model):
    segments = cut_segments(warped)
    assert len(segments) == 361, "Not 361 segments cut!"
    predictions = classify_segments(segments, graph, session, model)
    assert predictions.shape == (361,), "Wrong shape of stone predictions!"
    counts = Counter(predictions)
    print(f"Found {counts[0]} empty fields, {counts[1]} black stones, and {counts[2]} white stones.")
    position = np.reshape(predictions, (19,19))
    return position