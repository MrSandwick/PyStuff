# Perceptron — Code Documentation

**Language:** Python
**Dependencies:** NumPy, scikit-learn, Matplotlib
**File:** `perceptron.py`

---

## Table of Contents

1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [Helper Function — unit_step_func](#helper-function)
4. [Class — Perceptron](#class-perceptron)
   - [__init__](#__init__)
   - [fit](#fit)
   - [predict](#predict)
5. [Testing Block](#testing-block)
   - [accuracy](#accuracy-function)
   - [Dataset](#dataset)
   - [Training and Prediction](#training-and-prediction)
   - [Visualization](#visualization)
6. [Full Code Flow](#full-code-flow)
7. [Parameters Reference](#parameters-reference)

---

## Overview

This module implements a **Perceptron classifier from scratch** using Python and NumPy. The Perceptron is a binary classification algorithm that learns a linear decision boundary by iteratively adjusting weights and bias whenever it makes a wrong prediction.

The implementation follows the standard object-oriented pattern — a `Perceptron` class with `fit` and `predict` methods — and includes a testing block that generates a synthetic dataset, trains the model, evaluates accuracy, and plots the decision boundary.

---

## Dependencies

```python
import numpy as np
```

Required for all numerical operations — dot products, array initialization, and the step function.

```python
# Used only in the testing block
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets
```

| Library | Purpose |
|---|---|
| `numpy` | Core math and array operations |
| `matplotlib.pyplot` | Plotting the decision boundary |
| `sklearn.model_selection` | Splitting data into train/test sets |
| `sklearn.datasets` | Generating synthetic classification data |

---

## Helper Function

### `unit_step_func(x)`

```python
def unit_step_func(x):
    return np.where(x > 0, 1, 0)
```

**Description:**
The activation function used by the Perceptron. Applies the unit step function element-wise to an array.

**Logic:**
- Returns `1` where the input is greater than 0
- Returns `0` everywhere else

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `x` | `np.ndarray` or scalar | The linear output value(s) to threshold |

**Returns:** `np.ndarray` of `0`s and `1`s — the predicted class labels.

**Example:**
```python
unit_step_func(np.array([-2, 0, 3]))
# Output: array([0, 0, 1])
```

---

## Class — Perceptron

```python
class Perceptron:
```

A binary classifier that learns a linear decision boundary using the Perceptron update rule. Trained via the `fit` method and used for inference via `predict`.

---

### `__init__`

```python
def __init__(self, learning_rate=0.01, n_iters=1000):
    self.lr = learning_rate
    self.n_iters = n_iters
    self.activation_func = unit_step_func
    self.weights = None
    self.bias = None
```

**Description:**
Initializes the Perceptron with hyperparameters. Weights and bias are set to `None` and will be initialized during training in `fit`.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `learning_rate` | `float` | `0.01` | Step size for weight updates. Smaller values = slower but more stable learning |
| `n_iters` | `int` | `1000` | Number of full passes through the training dataset |

**Attributes set at init:**

| Attribute | Value | Description |
|---|---|---|
| `self.lr` | `learning_rate` | Stored learning rate |
| `self.n_iters` | `n_iters` | Number of training iterations |
| `self.activation_func` | `unit_step_func` | The activation function applied to linear output |
| `self.weights` | `None` | Initialized to None; set during `fit` |
| `self.bias` | `None` | Initialized to None; set during `fit` |

---

### `fit`

```python
def fit(self, X, y):
    n_samples, n_features = X.shape

    self.weights = np.zeros(n_features)
    self.bias = 0

    y_ = np.where(y > 0, 1, 0)

    for _ in range(self.n_iters):
        for idx, x_i in enumerate(X):
            linear_output = np.dot(x_i, self.weights) + self.bias
            y_predicted = self.activation_func(linear_output)

            update = self.lr * (y_[idx] - y_predicted)
            self.weights += update * x_i
            self.bias += update
```

**Description:**
Trains the Perceptron on labeled data. Iterates through the training set multiple times and updates weights and bias whenever a misclassification occurs.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `X` | `np.ndarray`, shape `(n_samples, n_features)` | Training feature matrix |
| `y` | `np.ndarray`, shape `(n_samples,)` | Training labels (any numeric values; binarized internally) |

**Step-by-step breakdown:**

1. **Extract dimensions** — `n_samples` and `n_features` are read from `X.shape`
2. **Initialize weights** — set to a zero vector of length `n_features`
3. **Initialize bias** — set to `0`
4. **Binarize labels** — `y_` converts any label > 0 to `1`, otherwise `0`
5. **Training loop** — for each iteration and each sample:
   - Compute **linear output**: `dot(x_i, weights) + bias`
   - Apply **activation function** to get prediction (`0` or `1`)
   - Compute **update**: `learning_rate x (actual - predicted)`
   - Adjust **weights**: `weights += update x x_i`
   - Adjust **bias**: `bias += update`

**Update rule:**

```
update = learning_rate x (y_actual - y_predicted)

weights = weights + update x x_i
bias    = bias + update
```

If the prediction is correct, `(y_actual - y_predicted) = 0` and nothing changes. If wrong, the weights shift in the direction that would have produced the correct output.

**Returns:** `None` — modifies `self.weights` and `self.bias` in place.

---

### `predict`

```python
def predict(self, X):
    linear_output = np.dot(X, self.weights) + self.bias
    y_predicted = self.activation_func(linear_output)
    return y_predicted
```

**Description:**
Generates class predictions for new input data using the weights and bias learned during training.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `X` | `np.ndarray`, shape `(n_samples, n_features)` | Input feature matrix to classify |

**Step-by-step breakdown:**

1. Compute **linear output** for all samples at once: `dot(X, weights) + bias`
2. Apply **unit step function** to threshold the output into class labels
3. Return the predicted labels array

**Returns:** `np.ndarray` of `0`s and `1`s — predicted class labels for each sample.

**Note:** `predict` must be called **after** `fit`. Calling it before training will raise an error because `self.weights` is `None`.

---

## Testing Block

The testing code runs only when the script is executed directly (`__name__ == "__main__"`).

---

### Accuracy Function

```python
def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy
```

**Description:**
Computes the fraction of correctly classified samples.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `y_true` | `np.ndarray` | Ground truth labels |
| `y_pred` | `np.ndarray` | Predicted labels from the model |

**Returns:** `float` between `0.0` and `1.0` representing classification accuracy.

---

### Dataset

```python
X, y = datasets.make_blobs(
    n_samples=150, n_features=2, centers=2, cluster_std=1.05, random_state=2
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123
)
```

**Description:**
Generates a synthetic binary classification dataset and splits it into training and test sets.

**Dataset parameters:**

| Parameter | Value | Description |
|---|---|---|
| `n_samples` | `150` | Total number of data points |
| `n_features` | `2` | Two features (x and y coordinates for easy plotting) |
| `centers` | `2` | Two cluster centers — one per class |
| `cluster_std` | `1.05` | Spread of each cluster |
| `random_state` | `2` | Seed for reproducibility |

**Train/test split:**

| Parameter | Value | Description |
|---|---|---|
| `test_size` | `0.2` | 20% of data held out for testing (30 samples) |
| `random_state` | `123` | Seed for reproducibility |

---

### Training and Prediction

```python
p = Perceptron(learning_rate=0.01, n_iters=1000)
p.fit(X_train, y_train)
predictions = p.predict(X_test)

print("Perceptron classification accuracy", accuracy(y_test, predictions))
```

Creates a Perceptron instance, trains it on the training set, predicts on the test set, and prints accuracy.

---

### Visualization

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.scatter(X_train[:, 0], X_train[:, 1], marker="o", c=y_train)

x0_1 = np.amin(X_train[:, 0])
x0_2 = np.amax(X_train[:, 0])

x1_1 = (-p.weights[0] * x0_1 - p.bias) / p.weights[1]
x1_2 = (-p.weights[0] * x0_2 - p.bias) / p.weights[1]

ax.plot([x0_1, x0_2], [x1_1, x1_2], "k")

ymin = np.amin(X_train[:, 1])
ymax = np.amax(X_train[:, 1])
ax.set_ylim([ymin - 3, ymax + 3])

plt.show()
```

**Description:**
Plots the training data and the learned decision boundary.

**How the decision boundary is computed:**

The Perceptron's decision boundary is the line where the linear output equals zero:

```
weights[0] * x0 + weights[1] * x1 + bias = 0
```

Solving for `x1`:

```
x1 = (-weights[0] * x0 - bias) / weights[1]
```

Two points on this line are calculated at `x0_min` and `x0_max` (the leftmost and rightmost training points), and a line is drawn between them.

---

## Full Code Flow

```
1. Define unit_step_func
2. Define Perceptron class (__init__, fit, predict)
3. Generate dataset with make_blobs
4. Split into train/test sets
5. Instantiate Perceptron(lr=0.01, n_iters=1000)
6. Call p.fit(X_train, y_train)
   - Initialize weights to zeros
   - Loop 1000 times over all training samples
   - Update weights on each misclassification
7. Call p.predict(X_test)
   - Compute linear output
   - Apply step function
   - Return class predictions
8. Compute and print accuracy
9. Plot training data and decision boundary
```

---

## Parameters Reference

| Parameter | Location | Default | Description |
|---|---|---|---|
| `learning_rate` | `Perceptron.__init__` | `0.01` | Weight update step size |
| `n_iters` | `Perceptron.__init__` | `1000` | Number of training iterations |
| `n_samples` | `make_blobs` | `150` | Number of data points |
| `n_features` | `make_blobs` | `2` | Number of input features |
| `centers` | `make_blobs` | `2` | Number of classes |
| `test_size` | `train_test_split` | `0.2` | Fraction of data used for testing |

---

*Documentation for: Perceptron from Scratch — Machine Learning from Scratch course*