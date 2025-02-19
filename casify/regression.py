from .function import function


class RegressionModel(function):
    def __init__(self, f_expr, model_fn, xdata, ydata):
        self.super().__init__(f_expr)
        self._model_fn = model_fn
        self._xdata = xdata
        self._ydata = ydata

    def __call__(self, x):
        return self._model_fn(x)

    def __repr__(self):
        import sympy

        return sympy.pretty(self._f_expr)


def make_model(
    model,
    xdata,
    ydata,
):
    import sympy
    from scipy.optimize import curve_fit

    f_expr = sympy.sympify(model)
    vars = f_expr.free_symbols
    vars = [str(var) for var in vars]
    vars = sorted(vars)
    vars.remove("x")
    params = vars[:]
    vars = ["x"] + vars
    model = sympy.lambdify(vars, f_expr)

    popt, _ = curve_fit(
        f=model,
        xdata=xdata,
        ydata=ydata,
    )

    f_expr = f_expr.subs({var: round(val, 2) for var, val in zip(params, popt)})
    f = lambda x: model(x, *popt)

    return RegressionModel(f_expr, f, xdata, ydata)
