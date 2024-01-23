import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tools import P



x = np.arange(-10, 11)
y = x ** 2

plt.figure(figsize=(12, 6))
plt.title('My Nice Plot 1')
plt.plot(x, y)
plt.plot(x, -y)
plt.xlabel('x')
plt.ylabel('x^2')
plt.savefig('./plots/matplotlib_dv1.png')

plt.figure(figsize=(12, 6))
plt.title('My Nice Plot 2')

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.plot(x, -y)
plt.plot([0, 0, 0], [-10, 0, 100])
plt.legend(['X^2', 'Vertical Line'])
plt.xlabel('x')
plt.ylabel('x^2')

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.plot(x, -y)
plt.plot([-10, 0, 10], [-50, -50, -50])
plt.legend(['-X^2', 'Horizontal Line'])
plt.xlabel('x')
plt.ylabel('x^2')

plt.savefig('./plots/matplotlib_dv2.png')

# OOP Interface
fig, axes = plt.subplots(figsize=(12, 6))
axes.plot(x, (x ** 2), color='red', linewidth=3, marker='o', markersize=8, label='X^2')
axes.plot(x, -1 * (x ** 2), 'b--', label='-X^2')
axes.set_xlabel('X')
axes.set_ylabel('X Squared')
axes.set_title("My Nice Plot")
axes.legend()

plt.savefig('./plots/matplotlib_dv3.png')

# List of available line styles
fig, axes = plt.subplots(figsize=(12, 6))

axes.plot(x, x + 0, linestyle='solid')
axes.plot(x, x + 1, linestyle='dashed')
axes.plot(x, x + 2, linestyle='dashdot')
axes.plot(x, x + 3, linestyle='dotted');

axes.set_title("My Nice Plot")

plt.savefig('./plots/matplotlib_dv4.png')


# List of available line styles
fig, axes = plt.subplots(figsize=(12, 6))

axes.plot(x, x + 0, '-og', label="solid green")
axes.plot(x, x + 1, '--c', label="dashed cyan")
axes.plot(x, x + 2, '-.b', label="dashdot blue")
axes.plot(x, x + 3, ':r', label="dotted red")

axes.set_title("My Nice Plot")
axes.legend()

plt.savefig('./plots/matplotlib_dv5.png')


