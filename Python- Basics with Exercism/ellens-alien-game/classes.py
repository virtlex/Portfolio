"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created= 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1
        

    def hit(self):
        self.health -= 1
    
    def is_alive(self):
        if self.health > 0:
            return True
        
    def teleport(self,cordinate1, cordinate2):
        self.x_coordinate += cordinate1
        self.y_coordinate += cordinate2
        return self.x_coordinate, self.y_coordinate

    def collision_detection(self, other):
        pass

#alien = Alien(0, 0)

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.


#alien_start_positions = [(4, 7), (-1, 0)]

def new_aliens_collection(positions):
    aliens = []
    
    for position in positions:  
        aliens.append(Alien(position[0],position[1])) 
    return aliens


#print(new_aliens_collection(alien_start_positions))
