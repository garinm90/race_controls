import subprocess
import time
import os

class Game:


    def __init__(self, target=12, race_animation=[], winner=16, not_winner=17, prepare=4, animation_selector=0):
        self.target = target
#        self.start = start
        self.race_animation = race_animation
        self.winner = winner
        self.not_winner = not_winner
        self.prepare = prepare
        self.animation_selector = animation_selector

#    def get_start(self):
#        return self.start
    def get_switches(self):
        return [self.target, self.winner, self.not_winner, self.prepare]

    def get_target(self):
        return self.target

    def get_winner(self):
        return self.winner

    def get_not_winner(self):
        return self.not_winner
    
    def get_prepare(self):
        return self.prepare


    def fill(self, channel):
        model = 'Matrix'
        command = ['/opt/fpp/src/fppmm', '-m', 'a' , '-o', 'off']
        counter = 1
        if counter <  24:
            command[2] = model + str(counter)
            subprocess.run(command)
            counter += 1

    def play_winner(self, channel):
        command = ['fpp', '-P', 'winner']
        subprocess.run(command)

    def play_not_winner(self, channel):
        command = ['fpp', '-P', 'nowinner']
        subprocess.run(command)

    def play_prepare(self, channel):
        play_animation = ['/opt/fpp/src/fpp', '-p',]
        if self.animation_selector < 4:
            play_animation.append(self.race_animation[self.animation_selector])
            subprocess.run(play_animation)
            self.animation_selector += 1
        elif self.animation_selector >= 4:
            self.animation_selector = 0
            play_animation.append(self.race_animation[self.animation_selector])
            subprocess.run(play_animation)
            self.animation_selector += 1

        model = 'Matrix'
        command = ['/opt/fpp/src/fppmm', '-m', 'a' , '-o', 'on']
        counter = 1
        if counter < 24:
            command[2] = model + str(counter)
            subprocess.run(command)
            counter += 1
