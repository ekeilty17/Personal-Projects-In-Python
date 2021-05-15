# to add packages from parent directory
import sys
sys.path.append("..")

# imports
from MNIST.load_MNIST import get_training_data, get_testing_data
from utils.batch_loader import BatchLoader
from utils.split import train_test_split
from utils.plot import *

import numpy as np
import matplotlib.pyplot as plt

class LinearModel(object):

    def __init__(self, dim, loss_fnc="MSE", seed=None):
        
        self.Loss = {
            "MSE": self.MSE_Loss,
            "CE": self.CE_Loss
        }
        
        np.random.seed(seed)
        self.weights = np.random.rand(dim)
        self.bias = np.random.rand(1)[0]
        self.act_fnc = lambda x: x
        self.loss_fnc = self.Loss[loss_fnc]

    def evaluate(self, loader):
        correct = 0.0
        running_loss = 0.0
        total_samples = 0.0
        for data, labels in loader:
            predictions = self.predict(data)
            running_loss += sum(self.loss_fnc(predictions, labels))
            correct += sum(predictions == labels)
            total_samples += labels.shape[0]
        return running_loss / total_samples, correct / total_samples

    def MSE_Loss(self, y, label):
        return (y - label)**2 / 0.5
    
    def CE_Loss(self, y, label):
        return 0

    def Cost(self, Y, labels):
        return sum(self.loss_fnc(Y, labels)) / Y.shape[0]

# Preception Learning Algorithm
class PLA(LinearModel):

    def __init__(self, dim, loss_fnc="MSE", seed=None):
        super(PLA, self).__init__(dim, loss_fnc=loss_fnc, seed=seed)
        #self.weights = np.random.rand(dim)
        #self.bias = np.random.rand(1)[0]
        self.act_fnc = lambda x: -1 if x < 0 else 1

    def predict(self, data):
        Z = np.dot(data, self.weights) + self.bias
        return np.vectorize(self.act_fnc)(Z)

    def train(self, train_loader, valid_loader=None, test_loader=None, epochs=1, eval_freq=1, plot=True, confusion_matrix=False):
        
        training_loss = []
        validation_loss = []
        testing_loss = []
        training_acc = []
        validation_acc = []
        testing_acc = []
        
        evaluated_data = 0
        total_batches = 0
        running_loss = 0.0
        running_acc = 0.0
        for e in range(epochs):
            for i, (data, labels) in enumerate(train_loader):
                total_batches += 1
                evaluated_data += labels.shape[0]
                
                # getting loss and accuracy
                predictions = self.predict(data)
                running_loss += sum(self.loss_fnc(predictions, labels))
                running_acc += sum(predictions == labels)

                # vectorized
                incorrect_labels = (labels - predictions)/2
                self.weights += np.sum(np.multiply(data, incorrect_labels[:, np.newaxis]), axis=0)
                self.bias += np.sum(incorrect_labels)

                # not vectorized
                """
                for d, label, prediction in zip(data, labels, predictions):
                    if prediction != label:
                        self.weights += label * d
                        self.bias += label
                """

                # adding loss and accuracy to plots
                if total_batches % eval_freq == 0:
                    
                    training_string = ""
                    validation_string = ""
                    testing_string = ""

                    if plot:
                        training_loss.append( running_loss / evaluated_data )
                        training_acc.append( running_acc / evaluated_data  )
                        
                        #loss, acc = self.evaluate(train_loader)
                        #training_loss.append( loss )
                        #training_acc.append( acc )

                        training_string = f"\ttraining loss: {training_loss[-1]:.4f}"

                        if valid_loader != None:
                            loss, acc = self.evaluate(valid_loader)
                            validation_loss.append( loss )
                            validation_acc.append( acc )
                            
                            validation_string = f"\tvalidation accuracy: {validation_acc[-1]:.4f}"
                        
                        if test_loader != None:
                            loss, acc = self.evaluate(test_loader)
                            testing_loss.append( loss )
                            testing_acc.append( acc )

                            testing_string = f"\ttesting accuracy: {testing_acc[-1]:.4f}"
                    
                    print(f"epoch: {e+1:4d}\tbatch: {i+1:5d}{training_string}{validation_string}{testing_string}")


        # gettings final statistics
        final_train_loss, final_train_acc = self.evaluate(train_loader)       # Training
        final_valid_loss, final_valid_acc = self.evaluate(valid_loader)       # Validation
        final_test_loss, final_test_acc = self.evaluate(test_loader)          # Testing
        
        training_loss.append( final_train_loss )
        validation_loss.append( final_valid_loss )
        testing_loss.append( final_test_loss )
        training_acc.append( final_train_acc )
        validation_acc.append( final_valid_acc )
        testing_acc.append( final_test_acc )

        # plottings statistics
        if plot:
            plot_loss(np.linspace(0, epochs, len(training_loss)), 
                    train_loss=training_loss,
                    valid_loss=validation_loss,
                    test_loss=testing_loss,
                    title="PLA: Loss")
            plot_accuracy(np.linspace(0, epochs, len(validation_acc)), 
                    train_accuracy=training_acc,
                    valid_accuracy=validation_acc, 
                    test_accuracy=testing_acc,
                    title="PLA Accuracy")

        # returning statistics
        return final_train_loss, final_train_acc, final_valid_loss, final_valid_acc, final_test_loss, final_test_acc

if __name__ == "__main__":
    
    seed = 100

    # getting training and testing data
    train_images, train_labels = get_training_data("../MNIST/data")
    test_images, test_labels = get_testing_data("../MNIST/data")

    # getting validation data
    train_images, train_labels, valid_images, valid_labels = train_test_split( (train_images, train_labels), n=10000 )
    
    # flattening images
    dim = train_images.shape[1] * train_images.shape[2]
    train_images = train_images.reshape(-1, dim)
    valid_images = valid_images.reshape(-1, dim)
    test_images = test_images.reshape(-1, dim)

    # reformat labels to be a binary classifier (even and odd)
    train_labels = np.vectorize(lambda n: 1 if n % 2 == 0 else -1)(train_labels)
    valid_labels = np.vectorize(lambda n: 1 if n % 2 == 0 else -1)(valid_labels)
    test_labels = np.vectorize(lambda n: 1 if n % 2 == 0 else -1)(test_labels)

    train_loader = BatchLoader((train_images, train_labels), batch_size=1, seed=seed)
    valid_loader = BatchLoader((valid_images, valid_labels), batch_size=None, seed=seed)
    test_loader = BatchLoader((test_images, test_labels), batch_size=None, seed=seed)

    """
    NN = PLA(dim)
    for i, (images, labels) in enumerate(test_loader):
        print(NN.predict(images))
        break
    """

    # creating model
    NN = PLA(dim, seed=seed)
    statistics = NN.train(train_loader, valid_loader, test_loader, epochs=5, eval_freq=10000, plot=False)

    # printing statistics
    training_loss, training_acc, validation_loss, validation_acc, testing_loss, testing_acc = statistics
    print(f"Training\tLoss: {training_loss:.4f}\tAccuracy: {training_acc*100:.2f}%")
    print(f"Validation\tLoss: {validation_loss:.4f}\tAccuracy: {validation_acc*100:.2f}%")
    print(f"Testing\t\tLoss: {testing_loss:.4f}\tAccuracy: {testing_acc*100:.2f}%")

    """
    images, labels = get_testing_data()
    print("Full Dataset:", images.shape, '\t', labels.shape)

    for i, (images, labels) in enumerate(BatchLoader((images, labels), batch_size=550)):
        print(f"batch {i+1}:", images.shape, '\t', labels.shape)
    """