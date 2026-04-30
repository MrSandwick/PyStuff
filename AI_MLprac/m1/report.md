# Lecture Notes: Implementing the Perceptron from Scratch

**Course:** Machine Learning from Scratch
**Topic:** Perceptron Algorithm — Theory and Python Implementation
**Tools:** Python, NumPy, scikit-learn

---

## Overview

This lesson covers the Perceptron algorithm — the simplest form of a neural network. The lecture is divided into three parts: theoretical foundations, coding implementation, and testing with results. The goal is to build a fully functional Perceptron from scratch without relying on high-level machine learning libraries.

---

## Part 1 — Theoretical Foundations (0:15 - 5:07)

### What Is a Perceptron?

The Perceptron is a **single-layer neural network** used for **binary classification**. It is one of the oldest and most fundamental models in machine learning, and serves as the building block for more complex neural networks.

The model is inspired by biological neurons. In the brain, a neuron receives input signals and "fires" an output only when the cumulative signal crosses a certain threshold. The Perceptron replicates this behavior mathematically.

**Use case:** Answering binary questions — spam or not spam, class A or class B, positive or negative.

### The Linear Model

The Perceptron computes a weighted sum of inputs plus a bias term:

```
f(x) = (weights × inputs) + bias
```

This result is then passed through an **activation function** — the **unit step function** — which converts the output into a class prediction:

- Output **> 0** — predicted class = **1**
- Output **<= 0** — predicted class = **0**

### The Update Rule (2:44 - 5:07)

The Perceptron learns by correcting itself on misclassified examples. After each wrong prediction, the weights and bias are updated using the following formulas:

```
delta weight = learning_rate x (actual - predicted) x input
delta bias   = learning_rate x (actual - predicted)
```

**Behavior:**
- Predicted **0**, actual **1** — weights increase
- Predicted **1**, actual **0** — weights decrease
- Prediction correct — no change

Over repeated iterations, these incremental corrections move the model toward the correct **decision boundary** — the line or hyperplane that separates the two classes.

---

## Part 2 — Coding Implementation (6:00 - 12:05)

The Perceptron is implemented as a Python class using only NumPy. The class contains three components:

### `__init__` — Initialization (6:00 - 7:40)

Sets up the model parameters:

- **learning_rate** — controls the size of each weight update step
- **n_iterations** — number of full passes through the training dataset
- Weights and bias are initialized to zero

### `fit` — Training (7:41 - 11:32)

Trains the model on labeled data. For each training sample, the method:

1. Computes the **linear output** — weights dot-product input, plus bias
2. Applies the **unit step function** to produce a predicted label (0 or 1)
3. Compares the prediction to the **actual label**
4. Updates weights and bias if the prediction was incorrect

This process repeats for the specified number of iterations. With each pass, the model gradually converges on the optimal decision boundary.

### `predict` — Inference (11:35 - 12:05)

Used after training to classify new, unseen data. The method:

1. Computes the linear output using the learned weights and bias
2. Applies the step function
3. Returns the **predicted class labels**

---

## Part 3 — Testing and Results (12:10 - 13:46)

### Dataset

The model is tested on a synthetic dataset generated using **scikit-learn's `make_blobs`** function, which produces two clearly separated clusters of data points — a standard setup for testing binary classifiers.

### Results

- The Perceptron correctly identified the **decision boundary** between the two clusters
- The model achieved **100% accuracy** on the test set
- A plot was generated showing the classified data points and the learned separating line

### Key Limitation

The Perceptron **only converges on linearly separable data** — datasets where a straight line (or hyperplane) can cleanly separate the two classes. If the data is not linearly separable, the update rule will never stabilize and the model will fail to converge. This limitation directly motivated the development of multi-layer neural networks.

---

## Summary

| Component | Description |
|---|---|
| **Model type** | Single-layer neural network for binary classification |
| **Activation function** | Unit step function (threshold at 0) |
| **Learning method** | Iterative weight updates on misclassified samples |
| **Implementation** | Python class with `fit` and `predict` methods |
| **Limitation** | Only works on linearly separable data |

---

## Core Concept

Machine learning, at its most basic level, is a loop — make a prediction, measure the error, adjust the parameters, repeat. The Perceptron is the clearest illustration of this process, and understanding it provides the conceptual foundation for every neural network that follows.

---

*Source: Machine Learning from Scratch — Video Lecture*