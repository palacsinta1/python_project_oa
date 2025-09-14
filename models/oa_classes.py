import random

class OAShape:
    def __init__(self, kind, x, y, size, color):
        self.kind = kind
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, canvas):
        s = self.size
        if self.kind == "oval":
            return canvas.create_oval(self.x - s, self.y - s, self.x + s, self.y + s, fill=self.color, outline="")
        if self.kind == "rect":
            return canvas.create_rectangle(self.x - s, self.y - s, self.x + s, self.y + s, fill=self.color, outline="")
        r = random.randint(0, 1)
        if r == 0:
            return canvas.create_oval(self.x - s, self.y - s, self.x + s, self.y + s, fill=self.color, outline="")
        return canvas.create_rectangle(self.x - s, self.y - s, self.x + s, self.y + s, fill=self.color, outline="")

    def to_dict(self, item_id):
        return {"kind": self.kind, "x": self.x, "y": self.y, "size": self.size, "color": self.color, "item_id": item_id}

    @classmethod
    def from_dict(cls, d):
        return cls(d["kind"], d["x"], d["y"], d["size"], d["color"])
