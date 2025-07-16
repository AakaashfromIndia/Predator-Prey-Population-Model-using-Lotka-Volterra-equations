import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.widgets import Slider

def lotka_volterra(X, t, alpha, beta, delta, gamma):
    prey, predator = X
    dprey_dt = alpha * prey - beta * prey * predator
    dpredator_dt = delta * prey * predator - gamma * predator
    return [dprey_dt, dpredator_dt]

alpha0, beta0, delta0, gamma0 = 0.5, 0.02, 0.01, 0.4
prey0, predator0 = 40, 9
t = np.linspace(0, 200, 1000)
X0 = [prey0, predator0]

sol = odeint(lotka_volterra, X0, t, args=(alpha0, beta0, delta0, gamma0))
dt = t[1] - t[0]
dPop = np.gradient(sol, dt, axis=0)

fig = plt.figure(figsize=(16, 7))
gs = fig.add_gridspec(1, 2, width_ratios=[3, 1], wspace=0.25)
ax_main = fig.add_subplot(gs[0, 0])
gs_right = gs[0, 1].subgridspec(3, 1, hspace=0.8)
ax_phase = fig.add_subplot(gs_right[0])
ax_change = fig.add_subplot(gs_right[1])
ax_final = fig.add_subplot(gs_right[2])

l1, = ax_main.plot(t, sol[:, 0], label='Rabbits', color='tab:blue')
l2, = ax_main.plot(t, sol[:, 1], label='Foxes', color='tab:orange')
ax_main.set_xlabel('Time')
ax_main.set_ylabel('Population')
ax_main.set_title('Predator-Prey Population Dynamics')
ax_main.legend()
ax_main.grid(True)

l3, = ax_phase.plot(sol[:, 0], sol[:, 1], color='purple', lw=2)
ax_phase.set_xlabel('Rabbits')
ax_phase.set_ylabel('Foxes')
ax_phase.set_title('Phase')
ax_phase.grid(True)

l4, = ax_change.plot(t, dPop[:,0], label='dRabbits/dt', color='tab:blue', linestyle='dashed')
l5, = ax_change.plot(t, dPop[:,1], label='dFoxes/dt', color='tab:orange', linestyle='dashed')
ax_change.set_xlabel('Time')
ax_change.set_ylabel('dPopulation/dt')
ax_change.set_title('Population Change Rate')
ax_change.legend()
ax_change.grid(True)

bar_labels = ['Final', 'Max']
rabbit_vals = [sol[-1,0], np.max(sol[:,0])]
fox_vals = [sol[-1,1], np.max(sol[:,1])]
bar_width = 0.35
x = np.arange(len(bar_labels))
bars1 = ax_final.bar(x - bar_width/2, rabbit_vals, bar_width, label='Rabbits', color='tab:blue')
bars2 = ax_final.bar(x + bar_width/2, fox_vals, bar_width, label='Foxes', color='tab:orange')
ax_final.set_ylabel('Population')
ax_final.set_title('Final and Max Population')
ax_final.set_xticks(x)
ax_final.set_xticklabels(bar_labels)
ax_final.legend()

ax_alpha = plt.axes([0.12, 0.09, 0.25, 0.03])
ax_beta  = plt.axes([0.12, 0.05, 0.25, 0.03])
ax_delta = plt.axes([0.57, 0.09, 0.25, 0.03])
ax_gamma = plt.axes([0.57, 0.05, 0.25, 0.03])

s_alpha = Slider(ax_alpha, 'Rabbit Birth (alpha)', 0.01, 1.0, valinit=alpha0, valstep=0.01)
s_beta  = Slider(ax_beta,  'Predation (beta)',     0.001, 0.1, valinit=beta0, valstep=0.001)
s_delta = Slider(ax_delta, 'Fox Reprod. (delta)',  0.001, 0.1, valinit=delta0, valstep=0.001)
s_gamma = Slider(ax_gamma, 'Fox Death (gamma)',    0.01, 1.0, valinit=gamma0, valstep=0.01)

def update(val):
    a, b, d, g = s_alpha.val, s_beta.val, s_delta.val, s_gamma.val
    sol = odeint(lotka_volterra, X0, t, args=(a, b, d, g))
    dPop = np.gradient(sol, dt, axis=0)
    l1.set_ydata(sol[:, 0])
    l2.set_ydata(sol[:, 1])
    l3.set_data(sol[:, 0], sol[:, 1])
    l4.set_ydata(dPop[:,0])
    l5.set_ydata(dPop[:,1])
    prey_min, prey_max = np.min(sol[:, 0]), np.max(sol[:, 0])
    pred_min, pred_max = np.min(sol[:, 1]), np.max(sol[:, 1])
    pad_x = (prey_max - prey_min) * 0.1 if prey_max > prey_min else 1
    pad_y = (pred_max - pred_min) * 0.1 if pred_max > pred_min else 1
    ax_phase.set_xlim(prey_min - pad_x, prey_max + pad_x)
    ax_phase.set_ylim(pred_min - pad_y, pred_max + pad_y)
    ax_final.clear()
    rabbit_vals = [sol[-1,0], np.max(sol[:,0])]
    fox_vals = [sol[-1,1], np.max(sol[:,1])]
    ax_final.bar(x - bar_width/2, rabbit_vals, bar_width, label='Rabbits', color='tab:blue')
    ax_final.bar(x + bar_width/2, fox_vals, bar_width, label='Foxes', color='tab:orange')
    ax_final.set_ylabel('Population')
    ax_final.set_title('Final and Max Population')
    ax_final.set_xticks(x)
    ax_final.set_xticklabels(bar_labels)
    ax_final.legend()
    fig.canvas.draw_idle()

for slider in [s_alpha, s_beta, s_delta, s_gamma]:
    slider.on_changed(update)

plt.subplots_adjust(bottom=0.2)
plt.show()
