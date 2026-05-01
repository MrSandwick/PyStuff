# Code Documentation: MNIST Digit Classifier with TensorFlow

**Language:** Python
**Framework:** TensorFlow / Keras
**Dependencies:** TensorFlow, NumPy, Matplotlib
**Dataset:** MNIST Handwritten Digits

---

## Table of Contents

1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [Data Loading and Preparation](#data-loading-and-preparation)
4. [Data Visualization](#data-visualization)
5. [Model Architecture](#model-architecture)
6. [Model Compilation](#model-compilation)
7. [Model Training](#model-training)
8. [Prediction Visualization — view_classify](#view_classify)
9. [Single Image Prediction](#single-image-prediction)
10. [Model Evaluation](#model-evaluation)
11. [Full Code Flow](#full-code-flow)
12. [Parameters Reference](#parameters-reference)

---

## Overview

This script builds, trains, and evaluates a **feed-forward neural network** using TensorFlow and Keras to classify handwritten digits from the MNIST dataset. The model takes a 28x28 grayscale image as input and predicts which digit (0–9) it represents by outputting a probability distribution across 10 classes.

**Final output:** Classification accuracy on 10,000 test images.

---

## Dependencies

```python
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
```

| Library | Purpose |
|---|---|
| `tensorflow` | Core ML framework — model building, training, and evaluation |
| `tensorflow.keras.layers` | Individual layer types (Flatten, Dense) |
| `tensorflow.keras.models` | Model container (Sequential) |
| `matplotlib.pyplot` | Plotting images and probability charts |
| `numpy` | Numerical operations and array manipulation |

---

## Data Loading and Preparation

```python
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_images = train_images.astype('float32') / 255
test_images  = test_images.astype('float32') / 255
```

### Loading

`tf.keras.datasets.mnist.load_data()` downloads and unpacks the MNIST dataset directly into four arrays:

| Variable | Shape | Description |
|---|---|---|
| `train_images` | `(60000, 28, 28)` | 60,000 training images |
| `train_labels` | `(60000,)` | Integer labels 0–9 for training images |
| `test_images` | `(10000, 28, 28)` | 10,000 test images |
| `test_labels` | `(10000,)` | Integer labels 0–9 for test images |

### Normalization

Raw pixel values are stored as integers in the range **0–255**. They are cast to `float32` and divided by `255` to scale them to the range **0.0–1.0**.

```python
train_images = train_images.astype('float32') / 255
test_images  = test_images.astype('float32') / 255
```

**Why normalize:**
Large input values cause unstable and slow weight updates during training. Scaling inputs to 0–1 keeps values consistent and helps the model converge faster.

### Dataset Info Print

```python
print('Number of images in the training dataset:', train_images.shape[0])
print('Number of images in the testing dataset:', test_images.shape[0])
print(f"Shape of the images in the training dataset: {train_images[0].shape}")
```

Prints the number of samples in each split and confirms the shape of individual images `(28, 28)`.

**Expected output:**
```
Number of images in the training dataset: 60000
Number of images in the testing dataset: 10000
Shape of the images in the training dataset: (28, 28)
```

---

## Data Visualization

```python
fig, axes = plt.subplots(1, 10, figsize=(10, 10))
for i in range(10):
    axes[i].imshow(train_images[i].reshape(28, 28), cmap='gray')
    axes[i].set_title(train_labels[i])
    axes[i].axis('off')
plt.show()
```

**Description:**
Displays the first 10 training images in a single row, each with its corresponding label as the title.

**Step-by-step:**

| Step | Code | Description |
|---|---|---|
| Create figure | `plt.subplots(1, 10)` | 1 row, 10 columns of subplots |
| Loop | `for i in range(10)` | Iterates over the first 10 images |
| Display image | `imshow(..., cmap='gray')` | Renders the 28x28 pixel array as a grayscale image |
| Set title | `set_title(train_labels[i])` | Shows the correct digit label above each image |
| Hide axes | `axis('off')` | Removes axis ticks and borders for clean display |
| Render | `plt.show()` | Displays the full figure |

**Parameters:**

| Parameter | Value | Description |
|---|---|---|
| `figsize` | `(10, 10)` | Overall figure size in inches |
| `cmap` | `'gray'` | Grayscale colormap for pixel rendering |

---

## Model Architecture

```python
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
```

**Description:**
Defines a feed-forward neural network using the `Sequential` class. Layers are stacked in order and data flows through them one by one from input to output.

### Layer Breakdown

#### Layer 1 — Flatten

```python
layers.Flatten(input_shape=(28, 28, 1))
```

| Property | Value |
|---|---|
| Type | Flatten |
| Input shape | `(28, 28, 1)` — 2D grayscale image with 1 channel |
| Output shape | `(784,)` — 1D flat vector |
| Learnable parameters | None |

Reshapes the 28x28 pixel matrix into a single vector of 784 values. Dense layers require 1D input, so this layer acts as a bridge between the raw image and the network.

#### Layer 2 — Dense Hidden Layer 1

```python
layers.Dense(128, activation='relu')
```

| Property | Value |
|---|---|
| Type | Dense (fully connected) |
| Neurons | 128 |
| Input | 784 values from Flatten layer |
| Activation | ReLU |
| Learnable parameters | `(784 x 128) + 128 = 100,480` |

Each of the 128 neurons receives input from all 784 values. ReLU activation (`max(0, x)`) removes negative values and introduces non-linearity, allowing the network to learn complex patterns.

#### Layer 3 — Dense Hidden Layer 2

```python
layers.Dense(64, activation='relu')
```

| Property | Value |
|---|---|
| Type | Dense (fully connected) |
| Neurons | 64 |
| Input | 128 values from previous layer |
| Activation | ReLU |
| Learnable parameters | `(128 x 64) + 64 = 8,256` |

A second hidden layer with fewer neurons. Continues refining the feature representations learned by the first hidden layer.

#### Layer 4 — Dense Output Layer

```python
layers.Dense(10, activation='softmax')
```

| Property | Value |
|---|---|
| Type | Dense (fully connected) |
| Neurons | 10 |
| Input | 64 values from previous layer |
| Activation | Softmax |
| Learnable parameters | `(64 x 10) + 10 = 650` |

Outputs a probability for each of the 10 digit classes (0–9). Softmax normalizes the raw scores so all 10 outputs sum to exactly 1.0. The class with the highest probability is the model's predicted digit.

### Architecture Summary

| Layer | Type | Neurons | Activation | Output Shape |
|---|---|---|---|---|
| 1 | Flatten | — | None | `(784,)` |
| 2 | Dense | 128 | ReLU | `(128,)` |
| 3 | Dense | 64 | ReLU | `(64,)` |
| 4 | Dense | 10 | Softmax | `(10,)` |

**Total trainable parameters: 109,386**

---

## Model Compilation

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

**Description:**
Configures the model for training by specifying the optimizer, loss function, and evaluation metrics.

### Parameters

#### `optimizer='adam'`

Adam (Adaptive Moment Estimation) is an advanced gradient descent algorithm. It adapts the learning rate for each weight individually, making training faster and more stable than standard gradient descent.

#### `loss='sparse_categorical_crossentropy'`

The loss function used for multi-class classification when labels are provided as integers (not one-hot encoded). It measures how far the predicted probability distribution is from the true label.

- Lower loss = better predictions
- A perfect prediction for the true class yields a loss near 0

#### `metrics=['accuracy']`

Tracks and reports classification accuracy during training and evaluation. Accuracy is calculated as:

```
accuracy = correct predictions / total predictions
```

---

## Model Training

```python
history = model.fit(
    train_images,
    train_labels,
    epochs=5
)
```

**Description:**
Trains the model on the training dataset using backpropagation. The `fit` method returns a `History` object stored in `history`, which contains accuracy and loss values recorded after each epoch.

**Parameters:**

| Parameter | Value | Description |
|---|---|---|
| `train_images` | `np.ndarray (60000, 28, 28)` | Input training images |
| `train_labels` | `np.ndarray (60000,)` | Correct digit labels for training images |
| `epochs` | `5` | Number of full passes through the training dataset |

**What happens each epoch:**
1. All 60,000 training images are passed through the network (forward pass)
2. Loss is calculated for each prediction using the loss function
3. Gradients are computed via backpropagation
4. Weights are updated by the Adam optimizer to reduce loss
5. Accuracy and loss are reported for that epoch

**Returns:** `History` object — contains `history.history['accuracy']` and `history.history['loss']` lists for each epoch.

---

## Prediction Visualization — `view_classify`

```python
def view_classify(image, probabilities):
    fig, (ax1, ax2) = plt.subplots(figsize=(6, 9), ncols=2)
    ax1.imshow(image)
    ax1.axis('off')
    ax2.barh(np.arange(10), probabilities)
    ax2.set_aspect(0.1)
    ax2.set_yticks(np.arange(10))
    ax2.set_yticklabels(np.arange(10))
    ax2.set_title('Class Probability')
    ax2.set_xlim(0, 1.1)
    plt.tight_layout()
```

**Description:**
A utility function that displays a test image side-by-side with a horizontal bar chart showing the model's predicted probability for each digit class (0–9).

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `image` | `np.ndarray (28, 28)` | The test image to display |
| `probabilities` | `np.ndarray (10,)` | Output probabilities for each digit class from `model.predict` |

**Layout:**

| Subplot | Content | Description |
|---|---|---|
| `ax1` (left) | `imshow(image)` | Renders the grayscale digit image |
| `ax2` (right) | `barh(...)` | Horizontal bar chart of class probabilities (0.0 to 1.0) |

**Key settings:**

| Setting | Value | Description |
|---|---|---|
| `figsize` | `(6, 9)` | Figure dimensions in inches |
| `ncols` | `2` | Two side-by-side subplots |
| `set_xlim` | `(0, 1.1)` | X-axis spans 0 to 1.1 to fit probability values |
| `set_yticks` | `np.arange(10)` | Y-axis tick positions for digits 0–9 |
| `set_aspect` | `0.1` | Controls bar chart proportions |

**Returns:** `None` — renders the plot directly.

---

## Single Image Prediction

```python
image, label = test_images[0], test_labels[0]
probabilities = model.predict(image.reshape(1, 28, 28, 1))
view_classify(image, probabilities[0])
```

**Description:**
Selects the first test image, runs it through the trained model, and visualizes the result using `view_classify`.

**Step-by-step:**

| Step | Code | Description |
|---|---|---|
| Select image | `test_images[0]` | Takes the first image from the test set |
| Select label | `test_labels[0]` | The true digit label for that image |
| Reshape | `.reshape(1, 28, 28, 1)` | Adds batch dimension (1) and channel dimension (1) required by the model |
| Predict | `model.predict(...)` | Returns array of shape `(1, 10)` — probabilities for each class |
| Index result | `probabilities[0]` | Extracts the 1D array of 10 probabilities |
| Visualize | `view_classify(...)` | Displays the image and probability chart |

**Note on reshaping:**
The model expects input of shape `(batch_size, 28, 28, 1)`. A single image has shape `(28, 28)`, so `.reshape(1, 28, 28, 1)` adds the required batch and channel dimensions before prediction.

---

## Model Evaluation

```python
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f'Accuracy of the neural network on the {test_images.shape[0]} test images: {test_accuracy * 100:.2f}%')
```

**Description:**
Evaluates the trained model on the full test set of 10,000 images that were not used during training. Reports the final loss and accuracy.

**Parameters passed to `model.evaluate`:**

| Parameter | Value | Description |
|---|---|---|
| `test_images` | `np.ndarray (10000, 28, 28)` | Unseen test images |
| `test_labels` | `np.ndarray (10000,)` | True labels for test images |

**Returns:**

| Variable | Type | Description |
|---|---|---|
| `test_loss` | `float` | Final loss value on the test set |
| `test_accuracy` | `float` | Fraction of correctly classified images (0.0–1.0) |

**Output format:**
```
Accuracy of the neural network on the 10000 test images: 97.93%
```

`test_accuracy * 100` converts the decimal fraction to a percentage. `:.2f` formats it to two decimal places.

---

## Full Code Flow

```
1.  Import libraries (TensorFlow, Keras, NumPy, Matplotlib)
2.  Load MNIST dataset into train/test splits
3.  Normalize pixel values from 0–255 to 0.0–1.0
4.  Print dataset shape information
5.  Visualize first 10 training images with labels
6.  Define Sequential model:
      - Flatten layer  (28x28 -> 784)
      - Dense 128      (ReLU)
      - Dense 64       (ReLU)
      - Dense 10       (Softmax)
7.  Compile model (Adam optimizer, cross-entropy loss, accuracy metric)
8.  Train model on 60,000 training images for 5 epochs
9.  Select first test image and reshape for prediction
10. Run model.predict to get class probabilities
11. Visualize image and probabilities with view_classify
12. Run model.evaluate on all 10,000 test images
13. Print final accuracy
```

---

## Parameters Reference

| Parameter | Location | Value | Description |
|---|---|---|---|
| `float32` | Data prep | — | Data type for normalized pixel values |
| `255` | Normalization | — | Divisor to scale pixels to 0–1 |
| `input_shape` | Flatten layer | `(28, 28, 1)` | Expected shape of each input image |
| `units` | Dense layer 1 | `128` | Number of neurons in first hidden layer |
| `units` | Dense layer 2 | `64` | Number of neurons in second hidden layer |
| `units` | Output layer | `10` | One neuron per digit class |
| `activation` | Hidden layers | `'relu'` | Activation for hidden layers |
| `activation` | Output layer | `'softmax'` | Activation for probability output |
| `optimizer` | Compile | `'adam'` | Adaptive gradient descent optimizer |
| `loss` | Compile | `'sparse_categorical_crossentropy'` | Loss function for integer-labeled multi-class classification |
| `epochs` | Training | `5` | Number of full passes through training data |
| `figsize` | Visualization | `(6, 9)` | Size of the prediction plot figure |

---

*Documentation for: MNIST Digit Classifier — Kie Codes Neural Network Tutorial | Framework: TensorFlow / Keras*