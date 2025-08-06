from circleshape import *
from shot import *

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.PLAYER_ACCEL = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt, 5)
        if keys[pygame.K_s]:
            self.move(dt, -5)
        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                self.timer -= dt
            else:
                self.shoot()
    
    def move(self, dt, dv):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        self.PLAYER_ACCEL += dv

        if self.PLAYER_ACCEL > PLAYER_SPEED:
            self.PLAYER_ACCEL = PLAYER_SPEED

        if self.PLAYER_ACCEL < -PLAYER_SPEED:
            self.PLAYER_ACCEL = -PLAYER_SPEED

        self.position += forward * self.PLAYER_ACCEL * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

