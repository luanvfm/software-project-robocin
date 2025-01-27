from utils.ssl.Navigation import Navigation
from utils.ssl.base_agent import BaseAgent
from utils.Geometry import Geometry
from utils.Point import Point
class ExampleAgent(BaseAgent):
    
    def __init__(self, id=0, yellow=False):
        super().__init__(id, yellow)

    def decision(self):
        position = self.pos
        obstacles = [self.opponents]
        target = self.targets

        def is_collision_and_act(position, target, obstacles, clearance=100):
            for obstacle in obstacles:
                for obs in obstacle.values():
                    distance = Geometry.dist_to(position, Point(obs.x, obs.y))
                    if distance < clearance:
                            target_velocity, target_angle_velocity = Navigation.goToPoint(
                            self.robot, Point(obs.x+50, obs.y+40)
                        )
                            self.set_vel(target_velocity)
                            self.set_angle_vel(target_angle_velocity)
                            return True
                    else:
                            return False

        if len(self.targets) == 0:
            return
        if is_collision_and_act(position, target, obstacles):
            pass
        else:            
            target_velocity, target_angle_velocity = Navigation.goToPoint(self.robot, self.targets[0])
            self.set_vel(target_velocity)
            self.set_angle_vel(target_angle_velocity) 
             

    def post_decision(self):
        pass