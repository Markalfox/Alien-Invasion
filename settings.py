class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.caption = 'Alien Invasion'

        self.ship_speed = 5

        self.bullet_speed = 2
        self.bullet_size = (3, 15)  # (width, height)
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
