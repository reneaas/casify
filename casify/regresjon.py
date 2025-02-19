from .regression import make_model


def lag_modell(
    modell,
    xdata,
    ydata,
):
    return make_model(modell, xdata, ydata)
