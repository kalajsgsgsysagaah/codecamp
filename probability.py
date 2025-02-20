import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    
    for _ in range(num_experiments):
        copied_hat = Hat(**{ball: hat.contents.count(ball) for ball in set(hat.contents)})
        drawn_balls = copied_hat.draw(num_balls_drawn)
        drawn_counts = {ball: drawn_balls.count(ball) for ball in set(drawn_balls)}
        
        if all(drawn_counts.get(ball, 0) >= count for ball, count in expected_balls.items()):
            success_count += 1
    
    return success_count / num_experiments
