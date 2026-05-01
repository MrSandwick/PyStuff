# Lecture Notes: Neural Network for MNIST Digit Classification with TensorFlow

**Course:** Kie Codes — Neural Network Tutorial
**Topic:** Image Classification using a Feed-Forward Neural Network
**Dataset:** MNIST Handwritten Digits
**Tools:** Python, TensorFlow, NumPy, Matplotlib, Jupyter Notebook

---

## Table of Contents

1. [Overview](#overview)
2. [Part 1 — Project Setup and Data Preparation (0:40 - 2:31)](#part-1)
3. [Part 2 — Neural Network Architecture (2:31 - 4:11)](#part-2)
4. [Part 3 — Training and Evaluation (4:11 - 8:40)](#part-3)
5. [Summary](#summary)
6. [Key Terms](#key-terms)

---

## Overview

This tutorial demonstrates how to build a feed-forward neural network using TensorFlow to classify handwritten digits from the MNIST dataset. The model accepts a 28x28 grayscale image as input and outputs a probability distribution over 10 possible classes (digits 0 through 9). Final test accuracy achieved: **97.93%**.

---

## Part 1 — Project Setup and Data Preparation (0:40 - 2:31)

### Environment Setup (0:40 - 1:15)

The project is developed inside a **Jupyter Notebook** running within a **virtual environment**. Required libraries are installed at the start:

- **TensorFlow** — model building and training
- **NumPy** — numerical operations
- **Matplotlib** — visualization

Using a virtual environment isolates project dependencies and ensures reproducibility across different machines.

### The MNIST Dataset (1:21 - 2:07)

MNIST is a standard benchmark dataset for image classification tasks.

| Property | Value |
|---|---|
| Training images | 60,000 |
| Test images | 10,000 |
| Image dimensions | 28 x 28 pixels |
| Color space | Grayscale |
| Pixel value range | 0 to 255 |
| Number of classes | 10 (digits 0–9) |

### Data Normalization

Raw pixel values range from 0 to 255. Before training, the data is normalized by dividing all pixel values by 255, scaling the range to **0.0 – 1.0**.

```python
x_train, x_test = x_train / 255.0, x_test / 255.0
```

**Reason:** Large input values cause unstable weight updates during training. Normalizing inputs keeps values small and consistent, which leads to faster convergence and more stable learning.

---

## Part 2 — Neural Network Architecture (2:31 - 4:11)

The model is built using TensorFlow's `Sequential` class, which allows layers to be stacked linearly. The network is a **feed-forward architecture**, meaning data flows in one direction — from input to output with no loops.

### Layer Structure

#### Layer 1 — Flatten (Input Layer) (3:24 - 3:40)

```python
tf.keras.layers.Flatten(input_shape=(28, 28))
```

Converts the 2D image (28x28 grid) into a 1D vector of **784 values**. This is required because Dense layers expect flat 1D input, not a 2D matrix.

- Input shape: `(28, 28)`
- Output shape: `(784,)`
- No learned parameters — purely a reshaping operation

#### Layer 2 — Dense Hidden Layer 1 (3:41 - 3:58)

```python
tf.keras.layers.Dense(128, activation='relu')
```

- **128 neurons**, each fully connected to all 784 inputs
- **Activation:** ReLU (Rectified Linear Unit)
  - Returns the input value if positive, 0 if negative
  - Formula: `f(x) = max(0, x)`
  - Introduces non-linearity, enabling the network to learn complex patterns beyond simple linear relationships

#### Layer 3 — Dense Hidden Layer 2 (3:41 - 3:58)

```python
tf.keras.layers.Dense(64, activation='relu')
```

- **64 neurons**, each fully connected to all 128 outputs from the previous layer
- Same ReLU activation
- A smaller layer that further distills the learned features

#### Layer 4 — Dense Output Layer (3:59 - 4:10)

```python
tf.keras.layers.Dense(10, activation='softmax')
```

- **10 neurons** — one per digit class (0 through 9)
- **Activation:** Softmax
  - Converts raw output scores (logits) into a probability distribution
  - All 10 output values sum to 1.0
  - The class with the highest probability is the model's prediction

### Architecture Summary

| Layer | Type | Neurons | Activation | Purpose |
|---|---|---|---|---|
| 1 | Flatten | 784 | None | Reshape 28x28 to 1D vector |
| 2 | Dense | 128 | ReLU | Learn high-level features |
| 3 | Dense | 64 | ReLU | Refine learned features |
| 4 | Dense | 10 | Softmax | Output class probabilities |

---

## Part 3 — Training and Evaluation (4:11 - 8:40)

### Training Process — Backpropagation (4:43 - 6:53)

The model learns through **backpropagation**, an algorithm that adjusts weights based on prediction errors:

1. A training sample is passed forward through the network (forward pass)
2. The output is compared to the true label using the **loss function**
3. The error is propagated backwards through each layer (backward pass)
4. Each weight is adjusted slightly in the direction that reduces the error
5. This repeats for every training sample across all epochs

#### Loss Function — Sparse Categorical Cross-Entropy

Used for multi-class classification with integer labels. Measures the difference between the model's predicted probability distribution and the true label.

- A perfect prediction yields a loss close to 0
- A wrong prediction yields a higher loss, triggering larger weight updates

#### Optimizer — Adam

Adam (Adaptive Moment Estimation) is an advanced gradient descent optimizer that:

- Adapts the learning rate individually for each weight
- Combines the benefits of momentum and adaptive learning rates
- Converges faster and more reliably than standard gradient descent

### Training Execution (6:54 - 7:06)

```python
model.fit(x_train, y_train, epochs=5)
```

The model is trained for **5 epochs** — meaning it passes through all 60,000 training images 5 complete times. With each epoch, the weights are refined and training accuracy increases.

| Epoch | Description |
|---|---|
| 1 | Initial weight adjustments — accuracy improves rapidly |
| 2–4 | Continued refinement — diminishing improvements |
| 5 | Final pass — model converges on near-optimal weights |

### Testing and Visualization (7:17 - 8:28)

#### Single Prediction Visualization (7:17 - 8:04)

A test image is displayed alongside a bar chart of the model's predicted probabilities for each digit class (0–9). This demonstrates that the model does not just output a single label but a full probability distribution — showing how confident it is in each possible answer.

#### Full Test Set Evaluation (8:05 - 8:28)

```python
model.evaluate(x_test, y_test)
```

All 10,000 test images — unseen during training — are passed through the trained model.

**Result: 97.93% accuracy**

The model correctly classified 9,793 out of 10,000 handwritten digit images.

---

## Summary

| Component | Detail |
|---|---|
| **Dataset** | MNIST — 60,000 train / 10,000 test images |
| **Input** | 28x28 grayscale image, normalized to 0–1 |
| **Architecture** | Feed-forward Sequential network, 4 layers |
| **Hidden activations** | ReLU |
| **Output activation** | Softmax (10-class probability distribution) |
| **Loss function** | Sparse Categorical Cross-Entropy |
| **Optimizer** | Adam |
| **Training duration** | 5 epochs |
| **Test accuracy** | 97.93% |

---

## Key Terms

| Term | Definition |
|---|---|
| **Feed-forward network** | A neural network where data flows in one direction only — input to output |
| **Sequential model** | A TensorFlow model where layers are stacked in linear order |
| **Normalization** | Scaling input values to a fixed range (0–1) for stable training |
| **Flatten layer** | Reshapes multi-dimensional input into a 1D vector |
| **Dense layer** | A fully connected layer where every neuron receives input from all neurons in the previous layer |
| **ReLU** | Activation function that outputs the input if positive, 0 otherwise |
| **Softmax** | Activation function that converts raw scores to a probability distribution summing to 1 |
| **Backpropagation** | Algorithm that computes gradients and propagates error backwards to update weights |
| **Loss function** | Measures how far the model's predictions are from the true labels |
| **Adam optimizer** | Adaptive learning rate optimizer that adjusts weight updates individually |
| **Epoch** | One complete pass through the entire training dataset |
| **Cross-entropy loss** | Loss function used for classification — penalizes incorrect or uncertain predictions |

---

*Source: Kie Codes — Neural Network with TensorFlow | Dataset: MNIST Handwritten Digits*