from scipy.integrate import ode
from tqdm import tqdm

%pylab inline
import numpy as np

def solve(f, Xs, Y0, with_h = 1., max_iter = 1e5):
    X0, XF = Xs
    r = ode(f)
    r.set_integrator('dopri5')
    r.set_initial_value(Y0, X0)

    dt = with_h
    Xs = []
    Ys = []

    length = min((XF - X0)/dt, max_iter)
    for i in tqdm(range(int(length))):
        if not r.successful():
            break

        r.integrate(r.t + dt)
        Xs.append(r.t)
        Ys.append(r.y)
    return Xs, Ys

sigma = 10.
r = 99.96
b = 8/3
def f(t, Y):
    x, y, z = Y
    ẋ = sigma * (y - x)
    ẏ = -x*z + r*x - y
    ż = x*y - b*z
    return [ẋ, ẏ, ż]

Xs = (0, 100)
Y0 = [0, 0.5, 1]

X_d, Y_d = solve(f, Xs, Y0, with_h = 1e-2)
Y_np = np.array(Y_d)
plot(Y_np[:, 0], Y_np[:, 1])
