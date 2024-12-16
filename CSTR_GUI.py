import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Ensure Tkinter backend
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import RangeSlider

# Profit function
def profit_function(V, C_A_in, k, F, P_B, C_C, C_O, m, n, P_A):
    tau = V / F
    conversion_factor = (k * tau) / (1 + k * tau)
    revenue = F * C_A_in * conversion_factor * P_B
    cap_op_cost = C_C * (F*tau)**m + C_O * (F*tau)**n
    cost_A = P_A * F * C_A_in
    return revenue - cap_op_cost - cost_A

# Run simulation
def run_simulation(*args):
    C_A_in = float(entry_C_A_in.get())
    k = float(entry_k.get())
    F = float(entry_F.get())
    V_max = float(entry_V_max.get())

    num_points = int(V_max * 200)
    if num_points < 200:
        num_points = 200

    P_A = P_A_var.get()
    P_B = P_B_var.get()
    C_C = C_C_var.get()
    C_O = C_O_var.get()
    m = m_var.get()
    n = n_var.get()

    V_values = np.linspace(0, V_max, num_points)

    profit_values = [profit_function(V, C_A_in, k, F, P_B, C_C, C_O, m, n, P_A) for V in V_values] #This takes all the volume values I generated and calculates the corresponding profit. then it saves it as a new list

    max_profit = max(profit_values)
    opt_V = V_values[profit_values.index(max_profit)] #Find the index of the maximal profit value so I can draw the red line where the profit is maximal. I avoid using derivatives

    result_label.config(text=f"Optimal Reactor Volume: **{opt_V:.2f} m³**\nMaximum Profit: **{max_profit:.2f} €/s**", justify="center")

    ax.clear()
    ax.plot(V_values, profit_values, color='blue', linewidth=2, label='Profit(V)')
    ax.axvline(opt_V, color='red', linestyle='--', label=f'Optimal V = {opt_V:.2f} m^3\nMax Profit = {max_profit:.2f} €/s')
    ax.set_xlabel('Volume (m^3)')
    ax.set_ylabel('Profit (€/s)')
    ax.set_title('Profit as a Function of Reactor Volume')
    ax.grid(True)
    ax.legend()

    # Update sliders for axes limits
    ax.set_xlim(xlim_slider.val)
    ax.set_ylim(ylim_slider.val)
    canvas.draw()

# Update plot dynamically
def update_plot(_):
    ax.set_xlim(xlim_slider.val)
    ax.set_ylim(ylim_slider.val)
    canvas.draw_idle()

# Update slider labels for adjustable variables dynamically
def update_label(val, var, label):
    label.config(text=f"{float(val):.2f}")
    run_simulation()

# GUI setup
root = tk.Tk()
root.title("CSTR Profit vs. Volume Simulation")
root.geometry("1500x850")

font_style = ("Helvetica", 12)

# Layout configuration
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=0)

# Fixed parameters frame
fixed_frame = tk.LabelFrame(root, text="Fixed Parameters", font=font_style)
plot_frame = tk.Frame(root)
slider_frame = tk.LabelFrame(root, text="Adjustable Parameters", font=font_style)

fixed_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
plot_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
slider_frame.grid(row=0, column=2, padx=20, pady=20, sticky="ns")

# Label to display results above the plot
result_label = tk.Label(plot_frame, text="testing testing", font=("Helvetica", 14, "bold"), fg="black")
result_label.pack(side="top", pady=10)

# Fixed parameters
fixed_params = [
    ("C_A_in (mol/m^3)", "1000"),
    ("k (1/s)", "0.01"),
    ("F (m^3/s)", "0.001"),
    ("V_max (m^3)", "6"),
]

entries = []
for i, (label_txt, default_val) in enumerate(fixed_params):
    lbl = tk.Label(fixed_frame, text=label_txt, font=font_style)
    lbl.grid(row=i, column=0, padx=5, pady=5, sticky='e')
    entry = tk.Entry(fixed_frame, font=font_style, width=10)
    entry.insert(0, default_val)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
    entries.append(entry)

(entry_C_A_in, entry_k, entry_F, entry_V_max) = entries

run_button = ttk.Button(fixed_frame, text="Run Simulation", command=run_simulation)
run_button.grid(row=len(fixed_params), column=0, columnspan=2, pady=15)

# Slider variables
P_A_var = tk.DoubleVar(value=10.0)
P_B_var = tk.DoubleVar(value=50.0)
C_C_var = tk.DoubleVar(value=0.5)
C_O_var = tk.DoubleVar(value=0.2)
m_var = tk.DoubleVar(value=1.0)
n_var = tk.DoubleVar(value=1.0)

slider_specs = [
    ("P_A (€/mol)", P_A_var, 0, 50),
    ("P_B (€/mol)", P_B_var, 0, 100),
    ("C_C (coeff)", C_C_var, 0, 2),
    ("C_O (coeff)", C_O_var, 0, 2),
    ("m (exp)", m_var, 0.5, 2),
    ("n (exp)", n_var, 0.5, 2),
]

# Create sliders with dynamic labels
for i, (label_txt, var, vmin, vmax) in enumerate(slider_specs):
    lbl = tk.Label(slider_frame, text=label_txt, font=font_style)
    lbl.grid(row=i, column=0, padx=5, pady=5, sticky='w')

    scale = ttk.Scale(slider_frame, orient='vertical', length=200,
                      from_=vmax, to=vmin, variable=var,
                      command=lambda val, v=var, l=None: None)  # Placeholder for now
    scale.grid(row=i, column=1, padx=5, pady=5, sticky='w')

    # Create a value label next to the slider
    value_lbl = tk.Label(slider_frame, text=f"{var.get():.2f}", font=font_style)
    value_lbl.grid(row=i, column=2, padx=5, pady=5, sticky='w')

    # Correct the command to update the label dynamically
    scale.config(command=lambda val, v=var, l=value_lbl: update_label(val, v, l))


# Plot and RangeSliders
fig, ax = plt.subplots(figsize=(9, 6))
fig.subplots_adjust(bottom=0.3)  # Allocate space at the bottom for sliders

canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(fill='both', expand=True)

# Slider axes below the plot
axcolor = 'lightgoldenrodyellow'
slider_xlim_ax = plt.axes([0.15, 0.16, 0.7, 0.03], facecolor=axcolor)
slider_ylim_ax = plt.axes([0.15, 0.10, 0.7, 0.03], facecolor=axcolor)

xlim_slider = RangeSlider(slider_xlim_ax, 'Xlim', 0, 20, valinit=(0, 3))
ylim_slider = RangeSlider(slider_ylim_ax, 'Ylim', 0, 50, valinit=(0, 50))

xlim_slider.on_changed(update_plot)
ylim_slider.on_changed(update_plot)

if __name__ == '__main__':
    run_simulation()
    root.mainloop()
