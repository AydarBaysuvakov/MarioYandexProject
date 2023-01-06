WIDTH, HEIGHT = 500, 500
class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT * 3 // 4)

class Zoom:
    def __init__(self):
        self.zoom = 1

    def change_zoom(self, d):
        self.zoom += d / 10

    def update(self, target):
        target.image