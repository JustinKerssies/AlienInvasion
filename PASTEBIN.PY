    def update(self):
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top < self.screen_rect.top:
            self.centery += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom > 0:
            self.centery -= self.ai_settings.ship_speed_factor


          ##########################################
    
    alien = Alien(ai_settings, screen)


            filename = os.path.join(ROOT_DIR, 'Documents', 'high_scores.txt')
        with open(filename) as file_object:
            contents = file_object.read()