import numpy as np
import matplotlib.pyplot as plt

# Данные из таблицы 3 (T=300K, B=10мТл)
I_uA = np.array([990, 1047, 1165, 1268, 1384, 1476, 1593, 1687, 1784, 1870])  # мкА
U34p  = np.array([0.102, 0.107, 0.119, 0.131, 0.141, 0.153, 0.165, 0.175, 0.186, 0.194])
U34pp = np.array([-0.091, -0.093, -0.104, -0.112, -0.123, -0.130, -0.140, -0.149, -0.158, -0.166])
gain = 100

Ux_mV = (U34p - U34pp) / 2 / gain * 1e3

# МНК
coeffs = np.polyfit(I_uA, Ux_mV, 1)
x_fit = np.linspace(900, 1950, 100)
y_fit = np.polyval(coeffs, x_fit)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(I_uA, Ux_mV, 'ko', markersize=6, label='Экспериментальные точки')
ax.plot(x_fit, y_fit, 'b-', linewidth=1.5,
        label=f'МНК: наклон $= {coeffs[0]:.5f}$ мВ/мкА')

ax.set_xlabel('$I$, мкА', fontsize=13)
ax.set_ylabel('$U_x$, мВ', fontsize=13)
ax.set_title('Зависимость $U_x$ от $I$\n($T = 300$~К, $B = 10$~мТл)', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('plot3_ux_I.png', dpi=150)
plt.show()
print("Сохранено: plot3_ux_I.png")

# Rx из наклона
slope_V_A = coeffs[0] * 1e-3 / 1e-6   # В/А (мВ/мкА -> В/А)
b = 2e-3
B = 10e-3
Rx = slope_V_A * b / B
print(f"Наклон: {slope_V_A:.4f} В/А")
print(f"Rx = {Rx:.4f} м³/Кл")
