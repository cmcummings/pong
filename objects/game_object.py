# game_object.py


class GameObject:
    """Base class for a game object."""

    def __init__(self, obj_id, x, y):
        self.id = obj_id
        self.x = x
        self.y = y

    def tick(self, screen):
        self.logic()
        self.draw(screen)

    def logic(self):
        pass

    def draw(self, screen):
        pass

