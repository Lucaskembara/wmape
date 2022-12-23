import numpy as np

def wmape(true, pred):
    true = np.exp(np.array(true)) - 1
    pred = np.exp(np.array(pred)) -1

    score = np.sum([abs(true_i - pred_i) for true_i, pred_i in zip(true, pred)]) / np.sum([np.abs(true_i) for true_i in true])
    return score