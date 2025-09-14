import json
import random
import tkinter as tk
from models.oa_classes import OAShape
from oa_utils import oa_scale

root = tk.Tk()
root.title("app")
root.geometry("900x600")

state = {"shapes": []}

canvas = tk.Canvas(root, width=700, height=500, bg="#1e1e1e", highlightthickness=0)
canvas.pack(padx=10, pady=10, fill="both", expand=True)

panel = tk.Frame(root)
panel.pack(fill="x")

shape_var = tk.StringVar(value="oval")
size_var = tk.IntVar(value=60)

def add_shape(x=None, y=None):
    t = shape_var.get()
    s = size_var.get()
    s = int(oa_scale(s, 1 + random.random() * 0.2))
    if x is None or y is None:
        x = random.randint(60, max(120, canvas.winfo_width() - 60))
        y = random.randint(60, max(120, canvas.winfo_height() - 60))
    color = random.choice(["#e11d48", "#22c55e", "#3b82f6", "#f59e0b", "#a855f7", "#10b981"])
    shape = OAShape(t, x, y, s, color)
    item_id = shape.draw(canvas)
    state["shapes"].append(shape.to_dict(item_id))
    return item_id

def clear_shapes():
    canvas.delete("all")
    state["shapes"].clear()

def save_json():
    data = {"shapes": state["shapes"]}
    with open("data/shapes.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_json():
    try:
        with open("data/shapes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        clear_shapes()
        for d in data.get("shapes", []):
            shape = OAShape.from_dict(d)
            item_id = shape.draw(canvas)
            state["shapes"].append(shape.to_dict(item_id))
    except FileNotFoundError:
        pass

def on_click(e):
    add_shape(e.x, e.y)

def on_key(e):
    if e.char == "c":
        clear_shapes()
    elif e.char == "s":
        save_json()
    elif e.char == "l":
        load_json()
    elif e.char == "a":
        for _ in range(5):
            add_shape()

canvas.bind("<Button-1>", on_click)
root.bind("<Key>", on_key)

add_btn = tk.Button(panel, text="Hozzáadás", command=lambda: add_shape())
add_btn.pack(side="left", padx=6, pady=6)

clear_btn = tk.Button(panel, text="Törlés", command=clear_shapes)
clear_btn.pack(side="left", padx=6, pady=6)

save_btn = tk.Button(panel, text="Mentés", command=save_json)
save_btn.pack(side="left", padx=6, pady=6)

load_btn = tk.Button(panel, text="Betöltés", command=load_json)
load_btn.pack(side="left", padx=6, pady=6)

opt1 = tk.Radiobutton(panel, text="Kör/ovál", variable=shape_var, value="oval")
opt1.pack(side="left", padx=6)

opt2 = tk.Radiobutton(panel, text="Négyzet", variable=shape_var, value="rect")
opt2.pack(side="left", padx=6)

size_scale = tk.Scale(panel, from_=20, to=200, orient="horizontal", variable=size_var)
size_scale.pack(side="right", padx=6)

root.mainloop()