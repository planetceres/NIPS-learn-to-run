import numpy as np

class Model(object):

    def predict(self, input_layer):
        output_layer = np.expand_dims(input_layer.flatten(), 0)
        output_layer = output_layer / np.linalg.norm(output_layer)
        for layer in self.weights:
            output_layer = np.dot(output_layer, layer)
        return output_layer[0]

    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights
