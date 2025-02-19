import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

def monte_carlo_integration(f, a, b, num_samples=10000):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, f(b), num_samples)
    under_curve = y_random <= f(x_random)
    area = (b - a) * f(b) * np.sum(under_curve) / num_samples
    return area

if __name__ == "__main__":
    a, b = 0, 2  
    monte_carlo_result = monte_carlo_integration(f, a, b)
    quad_result, error = spi.quad(f, a, b)
    
    print(f"Monte Carlo Integration Result: {monte_carlo_result}")
    print(f"Quad Integration Result: {quad_result}, Error: {error}")
    
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Integration graph f(x) = x^2 від {a} до {b}')
    plt.grid()
    plt.show()

