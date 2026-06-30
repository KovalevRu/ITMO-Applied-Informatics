import numpy as np
import matplotlib.pyplot as plt

# Данные из таблицы 2 (T=300K, I=1mA)
B_mT = np.array([0, 2, 4, 6, 8, 10, 12])   # мТл
U34p  = np.array([0.010, 0.020, 0.050, 0.060, 0.080, 0.100, 0.120])
U34pp = np.array([-0.010, -0.010, -0.030, -0.050, -0.070, -0.090, -0.110])
gain = 100

# Реальная ЭДС Холла (мВ)
Ux_mV = (U34p - U34pp) / 2 / gain * 1e3

# МНК по точкам с B > 0
mask = B_mT > 0
coeffs = np.polyfit(B_mT[mask], Ux_mV[mask], 1)
x_fit = np.linspace(0, 13, 100)
y_fit = np.polyval(coeffs, x_fit)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(B_mT, Ux_mV, 'ko', markersize=6, label='Экспериментальные точки')
ax.plot(x_fit, y_fit, 'b-', linewidth=1.5,
        label=f'МНК: $U_x = {coeffs[0]:.4f}\\cdot B + {coeffs[1]:.4f}$, мВ/мТл')

ax.set_xlabel('$B$, мТл', fontsize=13)
ax.set_ylabel('$U_x$, мВ', fontsize=13)
ax.set_title('Зависимость $U_x$ от $B$\n($T = 300$~К, $I = 1$~мА)', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(-0.5, 13)
ax.set_ylim(-0.1, 1.4)

plt.tight_layout()
plt.savefig('plot2_ux_B.png', dpi=150)
plt.show()
print("Сохранено: plot2_ux_B.png")

# Rx из наклона
slope_V_T = coeffs[0] * 1e-3 / 1e-3   # В/Тл (перевод мВ/мТл -> В/Тл)
b = 2e-3
I = 1e-3
Rx = slope_V_T * b / I
print(f"Наклон: {slope_V_T:.4f} В/Тл")
print(f"Rx = {Rx:.4f} м³/Кл")
