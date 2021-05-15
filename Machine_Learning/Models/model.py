import numpy as np
import matplotlib.pyplot as plt

class Model(object):

    def __init__(self):
        pass
    
    def evaluate(self, loader):
        raise NotImplementedError
    
    def predict(self, data):
        raise NotImplementedError

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
                
                self.learning_algorithm()

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
                    train_error=training_loss,
                    valid_error=validation_loss,
                    test_error=testing_loss,
                    title="PLA: Loss")
            plot_accuracy(np.linspace(0, epochs, len(validation_acc)), 
                    train_accuracy=training_acc,
                    valid_accuracy=validation_acc, 
                    test_accuracy=testing_acc,
                    title="PLA Accuracy")

        # returning statistics
        return final_train_loss, final_train_acc, final_valid_loss, final_valid_acc, final_test_loss, final_test_acc