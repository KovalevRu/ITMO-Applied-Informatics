import numpy as np
import matplotlib.pyplot as plt

# Данные из таблицы 4 (I=1мА, B=10мТл)
T = np.array([305, 310, 315, 320, 325, 330, 335])
U34p  = np.array([0.098, 0.100, 0.104, 0.102, 0.109, 0.111, 0.120])
U34pp = np.array([-0.091, -0.088, -0.087, -0.084, -0.078, -0.076, -0.070])
gain = 100

Ux_mV = (U34p - U34pp) / 2 / gain * 1e3

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(T, Ux_mV, 'ko-', markersize=6, linewidth=1.2, label='$U_x(T)$')

ax.set_xlabel('$T$, К', fontsize=13)
ax.set_ylabel('$U_x$, мВ', fontsize=13)
ax.set_title('Зависимость $U_x$ от $T$\n($I = 1$~мА, $B = 10$~мТл)', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_ylim(0.88, 1.02)

plt.tight_layout()
plt.savefig('plot4_ux_T.png', dpi=150)
plt.show()
print("Сохранено: plot4_ux_T.png")
print(f"\nUx(T): {Ux_mV}")
print(f"Среднее: {np.mean(Ux_mV):.4f} мВ, разброс: {Ux_mV.max()-Ux_mV.min():.4f} мВ")
