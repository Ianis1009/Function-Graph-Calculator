# Mini GeoGebra PRO — Interactive Mathematical Analysis Tool

## Overview

This project is an interactive web-based mathematical analysis system inspired by tools such as GeoGebra and lightweight symbolic computation engines.

It combines:

- Symbolic computation (derivatives, expressions)
- Numerical analysis (integration, monotonicity)
- Interactive visualization (Plotly)
- Web interface (Flask + HTML/CSS/JavaScript)
- Optional C-based numerical extensions

The goal is to provide a compact environment for studying and visualizing mathematical functions in real time.

---

# 1. Mathematical Theory

## 1.1 Derivative

The derivative of a function is defined as:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

Interpretation:
- Slope of the tangent line
- Instantaneous rate of change
- Growth behavior of a function

In this project:
- The derivative is computed symbolically using SymPy.

---

## 1.2 Critical Points

Critical points are values of x such that:

$$
f'(x) = 0
$$

Classification:
- Local maximum: derivative changes from positive to negative
- Local minimum: derivative changes from negative to positive

Detection method:
- Sign change analysis of the derivative on a discrete grid

---

## 1.3 Monotonicity

A function is:

- Increasing if $$f'(x) > 0$$
- Decreasing if $$f'(x) < 0$$

Implementation:
- The sign of $$f'(x)$$ is evaluated on sampled intervals
- Intervals are grouped based on sign changes

---

## 1.4 Definite Integral (Numerical Approximation)

The definite integral is approximated using the trapezoidal rule:

$$
\int_a^b f(x)\,dx \approx \sum \frac{f(x_i) + f(x_{i+1})}{2} \cdot \Delta x
$$

Implementation:
- `numpy.trapz` is used for numerical integration

---

## 1.5 Tangent Line

The equation of the tangent line at $$x_0$$ is:

$$
y = f(x_0) + f'(x_0)(x - x_0)
$$

This is used for interactive point-based tangent visualization.

---

# 2. System Architecture
project/
│
├── app.py # Flask backend
├── compute.c # optional numerical module (C)
├── templates/
│ └── index.html # frontend interface
├── static/
│ └── grafic.png # exported plot image
└── README.md


---

# 3. Backend (Python / Flask)

## Technologies

- Flask (web server)
- SymPy (symbolic computation)
- NumPy (numerical processing)
- Matplotlib (static plot export)

## Responsibilities

The backend:

- Receives function input from the user
- Computes:
  - function values $$f(x)$$
  - derivative $$f'(x)$$
  - critical points
  - monotonicity intervals
  - numerical integral
- Returns structured JSON data to the frontend

---

# 4. Optional C Module

The C component is designed for performance-oriented numerical computation.

Possible uses:

- Numerical derivative approximation
- Riemann or trapezoidal integration
- Function evaluation optimization

Example (finite difference derivative):

$$
f'(x) \approx \frac{f(x+h) - f(x)}{h}
$$

This module can be integrated via Python bindings or system calls.

---

# 5. Frontend (HTML / JavaScript)

## Technologies

- HTML / CSS (UI layout)
- JavaScript (interaction logic)
- Plotly (interactive graphs)
- MathJax (mathematical rendering)

## Features

- Function input system
- Interval and step configuration
- Dynamic graph rendering
- Real-time updates via Flask API
- Display of:
  - $$f(x)$$
  - $$f'(x)$$
  - critical points
  - monotonicity
  - integral approximation

---

# 6. Visualization Features

The graph includes:

- Function curve $$f(x)$$
- Derivative curve $$f'(x)$$
- Local maxima (red markers)
- Local minima (blue markers)
- Filled area under $$f(x)$$

Interactive capabilities:

- Zoom and pan
- Hover tooltips
- Click events for tangent visualization