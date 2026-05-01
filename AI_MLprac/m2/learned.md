# What I Learned: Building a Neural Network with TensorFlow

**Course:** Kie Codes — Neural Network Tutorial
**Task:** Classify handwritten digits from the MNIST dataset
**Tools:** Python, TensorFlow, NumPy, Matplotlib, Jupyter Notebook

---

## The Big Picture

This tutorial showed me how to build a real neural network using TensorFlow that can look at a handwritten digit — just a 28x28 grayscale image — and correctly identify which number (0 through 9) it represents. By the end, the model hits 97.93% accuracy on 10,000 test images it has never seen before.

More importantly, I now understand what is actually happening at each step — from raw pixel data all the way to a confident prediction.

---

## What I Learned — Section by Section

---

### 1. Setting Up the Environment

Before writing any model code, I learned how to set up a proper working environment:

- Use a **virtual environment** to keep project dependencies isolated
- Install the core libraries: **TensorFlow**, **NumPy**, and **Matplotlib**
- Work inside a **Jupyter Notebook** for interactive development and visualization

This is standard practice for ML projects and keeps the workspace clean and reproducible.

---

### 2. Understanding the MNIST Dataset

The MNIST dataset is the go-to benchmark for image classification. Here is what I learned about it:

- It contains **60,000 training images** and **10,000 test images**
- Each image is **28x28 pixels**, grayscale
- Each pixel holds a value between **0 and 255** (0 = black, 255 = white)
- Each image is labeled with the correct digit it represents (0–9)

**Why normalize?**
Raw pixel values (0–255) are too large for efficient training. Dividing every pixel by 255 scales all values to a range of **0 to 1**. This helps the model train faster and more stably — without normalization, large input values cause the weights to update erratically.

```python
x_train, x_test = x_train / 255.0, x_test / 255.0
```

---

### 3. Building the Neural Network

I learned how to construct a **feed-forward neural network** using TensorFlow's `Sequential` class — a clean way to stack layers in order.

The network has four layers:

#### Flatten Layer (Input)
```python
tf.keras.layers.Flatten(input_shape=(28, 28))
```
Converts the 28x28 pixel grid into a **flat vector of 784 values**. The network cannot process a 2D image directly — it needs a 1D input.

#### Hidden Layer 1
```python
tf.keras.layers.Dense(128, activation='relu')
```
128 neurons, each connected to all 784 inputs. Uses the **ReLU activation function**, which outputs the input directly if positive, and 0 if negative. This introduces non-linearity, allowing the network to learn complex patterns.

#### Hidden Layer 2
```python
tf.keras.layers.Dense(64, activation='relu')
```
A smaller layer of 64 neurons. Continues refining the learned features from the previous layer.

#### Output Layer
```python
tf.keras.layers.Dense(10, activation='softmax')
```
10 neurons — one for each digit (0–9). Uses the **Softmax activation function**, which converts raw scores into **probabilities that sum to 1**. The digit with the highest probability is the model's prediction.

---

### 4. Training the Model

This section taught me what "training" actually means at a deeper level.

#### Backpropagation
The model learns through **backpropagation** — a process where:
1. The model makes a prediction
2. The **loss function** measures how wrong the prediction was
3. The error is propagated backwards through the network
4. **Weights are adjusted** slightly to reduce the error

This loop repeats for every training sample, over multiple passes through the data.

#### Loss Function — Sparse Categorical Cross-Entropy
Used when the task is multi-class classification with integer labels. It measures the difference between the predicted probability distribution and the correct label.

#### Optimizer — Adam
Adam is an adaptive learning rate optimizer. It adjusts the step size for each weight individually, making training faster and more reliable than standard gradient descent.

#### Epochs
The model was trained for **5 epochs** — meaning it passed through all 60,000 training images 5 full times. With each epoch, the model's weights improve and accuracy increases.

---

### 5. Evaluating and Testing

After training, I learned how to properly evaluate a model:

- **Visualize predictions** — display a test image alongside the model's predicted probability for each digit (0–9)
- **Evaluate on the full test set** — run all 10,000 unseen test images through the trained model and measure overall accuracy

**Result: 97.93% accuracy**

This means the model correctly identified 9,793 out of 10,000 handwritten digits it had never seen during training.

---

## Key Concepts I Now Understand

| Concept | What It Means |
|---|---|
| **Normalization** | Scaling inputs to 0–1 for stable training |
| **Flatten layer** | Converts 2D image to 1D vector |
| **Dense layer** | Fully connected layer where every neuron connects to all inputs |
| **ReLU** | Activation that removes negative values, adds non-linearity |
| **Softmax** | Converts output scores to probabilities (sum = 1) |
| **Backpropagation** | Algorithm that adjusts weights based on prediction errors |
| **Loss function** | Measures how wrong the model's predictions are |
| **Adam optimizer** | Adaptive method for efficiently updating weights |
| **Epoch** | One full pass through the entire training dataset |

---

## Key Takeaway

Building this model taught me that a neural network is really just a chain of mathematical transformations — flatten the input, pass it through weighted layers, apply activation functions, and compare the output to the truth. Training is nothing more than repeating this process thousands of times while gradually adjusting the weights to reduce errors. TensorFlow handles the heavy lifting, but now I understand what it is actually doing under the hood.

---

*Source: Kie Codes — Neural Network with TensorFlow Tutorial | Dataset: MNIST*