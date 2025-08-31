import tkinter as tk

positions = {
    0: (1, 0),  # top-left
    1: (0, 0),  # bottom-left
    2: (0, 1),  # top-right
    3: (1, 1)   # bottom-right
}

def on_change(var, index, mode, grid_num, row, col):
    value = grids_vars[grid_num][row][col].get()
    print(f"Grid {grid_num+1}, Row {row}, Col {col} changed to: {value}")

root = tk.Tk()
root.title("4 Grids of 3x4 Entries")

rows, cols = 3, 4
num_grids = 4
grids_vars = []  # Store StringVars for each grid

for g in range(0, num_grids):
    frame = tk.LabelFrame(root, text=f"Grid {g+1}", padx=10, pady=10)
    frame.grid(row=positions[g][0], column=positions[g][1], padx=10, pady=10)

    grid_vars = []
    for r in range(rows):
        row_vars = []
        for c in range(cols):
            sv = tk.StringVar()
            sv.trace_add("write", lambda var, idx, mode, g=g, r=r, c=c: on_change(var, idx, mode, g, r, c))
            entry = tk.Entry(frame, textvariable=sv, width=8)
            entry.grid(row=r, column=c, padx=5, pady=5)
            row_vars.append(sv)
        grid_vars.append(row_vars)
    grids_vars.append(grid_vars)

root.mainloop()
