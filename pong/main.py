from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongGame(Widget):
    
    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))

    def update(self,dt):
        # call ball and move stuff

        self.ball.move()

        # bounce off top and bottom
        if (self.ball.y == 0) or (self.ball.top >= self.height):
            self.ball.velocity *= -1

        # bounce off left and right
        if (self.ball.x == 0) or (self.ball.right > self.width):
            self.ball.velocity *= -1

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

class PongBall(Widget):

    # Velocity of the ball on the X and Y axes
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # Referencelist property so we can use velocity
    # as a shorthand just like w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ''move'' will animate the ball one step. This will be called
    # in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

if __name__ == "__main__":
    PongApp().run()