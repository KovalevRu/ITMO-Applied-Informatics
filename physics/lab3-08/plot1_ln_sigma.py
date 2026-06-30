import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as P

# Данные из таблицы 1
T = np.array([300, 305, 310, 315, 320, 325, 330, 335])
U12 = np.array([1.900, 1.930, 2.040, 2.080, 2.140, 2.200, 2.260, 2.320])

I_const = 1e-3   # А
L12 = 10e-6      # м
b = 2e-3         # м
d = 2e-3         # м

sigma = (I_const * L12) / (U12 * b * d)
ln_sigma = np.log(sigma)
inv_T = 1.0 / T

# Линейная регрессия
coeffs = np.polyfit(inv_T, ln_sigma, 1)
x_fit = np.linspace(inv_T.min(), inv_T.max(), 100)
y_fit = np.polyval(coeffs, x_fit)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(inv_T, ln_sigma, 'ko', markersize=6, label='Экспериментальные точки')
ax.plot(x_fit, y_fit, 'b-', linewidth=1.5,
        label=f'МНК: $\\ln\\sigma = {coeffs[0]:.1f}/T + ({coeffs[1]:.2f})$')

ax.set_xlabel('$1/T$, К$^{-1}$', fontsize=13)
ax.set_ylabel('$\\ln\\sigma$', fontsize=13)
ax.set_title('Зависимость $\\ln\\sigma$ от $1/T$', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('plot1_ln_sigma.png', dpi=150)
plt.show()
print("Сохранено: plot1_ln_sigma.png")
