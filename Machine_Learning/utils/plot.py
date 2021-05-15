import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_loss(x, train_loss=None, valid_loss=None, test_loss=None, title=None):
    if train_loss != None:
        plt.plot(x, train_loss, label="Training Loss")
    if valid_loss != None:
        plt.plot(x, valid_loss, label="Validation Loss")
    if test_loss != None:
        plt.plot(x, test_loss, label="Testing Loss")
    
    if title == None:
        plt.title("Training Loss")
    else:
        plt.title(title)
    
    plt.xlabel("Epochs")
    plt.xlim(left=0)
    plt.ylabel("Loss")
    plt.legend(loc="upper right")
    plt.show()
    plt.clf()

def plot_accuracy(x, train_accuracy=None, valid_accuracy=None, test_accuracy=None, title=None):
    if train_accuracy != None:
        plt.plot(x, train_accuracy, label="Training Accuracy")
    if valid_accuracy != None:
        plt.plot(x, valid_accuracy, label="Validation Accuracy")
    if test_accuracy != None:
        plt.plot(x, test_accuracy, label="Testing Accuracy")
    
    if title == None:
        plt.title("Accuracy")
    else:
        plt.title(title)

    plt.xlabel("Epochs")
    plt.xlim(left=0)
    plt.ylabel("Accuracy")
    plt.yticks(np.arange(0, 1.1, step=0.1))
    plt.grid(linestyle='-', axis='y')
    plt.legend(loc="lower right")
    plt.show()
    plt.clf()

def plot_confusion_matrix(confusion_matrix, class_names, title=None, figsize=(10,7), fontsize=14):
    """ Prints a confusion matrix, as returned by `sklearn.metrics.confusion_matrix`, as a heatmap.
    Arguments
    ---------
    confusion_matrix: `numpy.ndarray`
        The numpy.ndarray object returned from a call to `sklearn.metrics.confusion_matrix`.
        Similarly constructed ndarrays can also be used.
    class_names: list
        An ordered list of class names, in the order they index the given confusion matrix.
    figsize: tuple
        A 2-long tuple, the first value determining the horizontal size of the ouputted figure,
        the second determining the vertical size. Defaults to (10,7).
    fontsize: int
        Font size for axes labels. Defaults to 14.
    Returns
    -------
   `matplotlib.figure.Figure`
        The resulting confusion matrix figure
    """
    df_cm = pd.DataFrame( confusion_matrix, index=class_names, columns=class_names )
    fig = plt.figure(figsize=figsize)
    try:
        heatmap = sns.heatmap(df_cm, annot=True, fmt="d")
    except Valueloss:
        raise Valueloss("Confusion matrix values must be integers.")

    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)
    plt.subplots_adjust(left=0.27, bottom=0.25, right=0.97, top=0.95)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    if title != None:
        plt.title(title)

    plt.show()
