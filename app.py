from flask import Flask, render_template, request, jsonify
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

app = Flask(__name__)

x_sym = sp.symbols('x')

current_x = None
current_f = None
current_df = None


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/compute", methods=["POST"])
def compute():
    global current_x, current_f, current_df

    data = request.json

    func_str = data["function"]
    a = float(data["a"])
    b = float(data["b"])
    step = float(data["step"])
    try:
        f_expr = sp.sympify(func_str)
        df_expr = sp.diff(f_expr, x_sym)

        f = sp.lambdify(x_sym, f_expr, "numpy")
        df = sp.lambdify(x_sym, df_expr, "numpy")

        xs = np.arange(a, b, step)
        ys = f(xs)
        dys = df(xs)
    except Exception as err:
        return jsonify({
            "error" : True, 
            "message" : f"Functia introdusa nu este valida!\nExemplu corect: x*x*x + sin(x) + exp(cos(x)) +x**2"
        }), 400

    current_x = xs
    current_f = ys
    current_df = dys

    max_pts = []
    min_pts = []

    for i in range(1, len(xs) - 1):
        if dys[i - 1] > 0 and dys[i] < 0:
            max_pts.append((xs[i], ys[i]))
        if dys[i - 1] < 0 and dys[i] > 0:
            min_pts.append((xs[i], ys[i]))

    intervals = []
    start = xs[0]
    prev = sign(dys[0])

    for i in range(1, len(xs)):
        curr = sign(dys[i])
        if curr != prev:
            intervals.append((start, xs[i], prev))
            start = xs[i]
            prev = curr

    intervals.append((start, xs[-1], prev))

    monotony = []
    for a1, b1, s in intervals: 
        if s > 0:
            monotony.append(f"↗ crescătoare pe [{a1:.2f}, {b1:.2f}]")
        elif s < 0:
            monotony.append(f"↘ descrescătoare pe [{a1:.2f}, {b1:.2f}]")

    integral = float(np.trapz(ys, xs))

    return jsonify({
        "x": xs.tolist(),
        "f": ys.tolist(),
        "df": dys.tolist(),

        "func": str(f_expr),
        "deriv": str(df_expr),

        "max_points": max_pts,
        "min_points": min_pts,
        "monotonie": monotony,

        "integral": integral
    })


@app.route("/tangent", methods=["POST"])
def tangent():
    data = request.json
    x0 = float(data["x"])

    idx = (np.abs(current_x - x0)).argmin()

    y0 = current_f[idx]
    slope = current_df[idx]

    tangent = slope * (current_x - x0) + y0 # ec tangentei la grafic intr-un punct (x0, y0)

    return jsonify({
        "x": current_x.tolist(),
        "tangent": tangent.tolist(),
        "x0": x0,
        "y0": y0
    })


@app.route("/save", methods=["POST"])
def save():
    plt.figure(figsize=(10, 6))

    plt.plot(current_x, current_f, color="green", label="f(x)")
    plt.plot(current_x, current_df, color="red", label="f'(x)")

    plt.grid(True)
    plt.legend()

    plt.savefig("static/grafic.png", dpi=300)
    plt.close()

    return jsonify({"status": "saved"})


if __name__ == "__main__":
    app.run(debug=True)