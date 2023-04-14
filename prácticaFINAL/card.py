class Card:
    def __init__(self, front, back, tags=None, priority=1):
        self.front = front
        self.back = back
        self.tags = tags if tags else []
        self.priority = priority

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def get_tags(self):
        return self.tags

    def set_front(self, new_front):
        self.front = new_front

    def set_back(self, new_back):
        self.back = new_back

    def set_tags(self, new_tags):
        self.tags = new_tags
