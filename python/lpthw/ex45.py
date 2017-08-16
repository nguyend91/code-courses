#!/usr/bin/env python2
from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()


class Death(Scene):
    quips = [
        "[Col Campbell] What's wrong!? Snake. SNAAAKEE",
        "[Col Campbell] Snake, what happened!? Snake. SNAAAKEE",
        "[Col Campbell] Snake, are you okay!? Snake. SNAAAKEE",
        "[Col Campbell] Snake, answer me! Snake. SNAAAKEE"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips) - 1)]
        exit(1)


class Introduction(Scene):
    def enter(self):
        print """
-------------------------------------------------------------------------------

T  A  C  T  I  C  A  L      E  S  P  I  O  N  A  G  E      A  C  T  T  I  O  N
 _    _  ___ _____  _    _    ___   ___    _    ____    __    __   _   _  ___
| \  / ||  _|_   _|/ \  | |  / _ \ |  _|  / \  |  _ \  /  \  /  \ | | | ||   \\
|  \/  || |   | | / _ \ | | | / \_|| |   / A \ | | | || |\_|| /\ || | | || |\ |
| \  / || |_  | || |_| || | | | __ | |_ | /_\ || |_| | \ \  | || || | | || || |
| |\/| ||  _| | ||  _  || | | ||_ ||  _||  _  ||  _ <   \ \ | || || | | || || |
| |  | || |   | || | | || | | | | || |  | | | || | | | _ \ \| || || | | || || |
| |  | || |_  | || | | || |_| \_/ || |_ | | | || | | || \| || \/ || |_| || |/ |
|_|  |_||___| |_||_| |_||___|\__,_||___||_| |_||_| \_\ \__/  \__/ |___|_||___/

-------------------------------------------------------------------------------
"""
        return 'central_corridor'

class CentralCorridor(Scene):
    def enter(self):
        print "[Col Campbell] We need you to infiltrate the island and neutralize the theat."
        print "[Snake] Got it."
        print "|"
        print "|"
        print "|"
        print "|"
        print "|"
        print """
You've made it on the island codenamed "Shadow Moses", but most of your gear is
at the bottom of the ocean. The only thing you're armed with is an M9 and your
codec. "Col Roy Campbell" is in charge of this mission, and you (Solid Snake) are
responsible for taking down what's left FOXHOUND. Let's do this.
"""
        print "|"
        print "|"
        print "|"
        print "|"
        print "|"
        print """
Shortly after arriving, you manage to locate ArmsTech president Kenneth Baker.
Unfortunately you were unable to get any real information about the Metal Gear
FOXHOUND has in their possession before you were confronted by FOXHOUND member
"Revolver Ocelot". You can go toe-to-toe with Ocelot, but from what you know
about him, he's one of the best shooters in the business. One of his biggest
downfall is his cockiness, see if you can use that to your advatange...
"""
        print "|"
        print "|"

        print "1. Get in a shootout with Ocelot.."
        print "2. Try your best to find a way out.."
        print "3. Challenge him to a duel.."

        action = raw_input("> ")

        if action == "1":
            print "|"
            print "|"
            print "|"
            print """
You manage to hold Ocelot back for a bit, but his quick reload speed plus his
deadly accuracy make it impossible to get a good shot on him. He eventually
gets cocky enough, and starts ricocheting the bullets in your direction when
you finally get hit in the stomach and slowly bleed out. The last thing you see
is his stupid smile.
"""
            return 'death'

        elif action == "2":
            print "|"
            print "|"
            print "|"
            print """
Ocelot has a bit of trouble finding your exact location since you've decided not
to return any fire. He begins ricocheting the bullets off the walls making
every direction unsafe. You manage to see a slight opening through a cracked door
into a narrow hallway. When you've mustered enough courage, you take the
opportunity to run towards the door as fast as you can. You can hear Ocelot
laughing. Then suddenly everything goes black.
"""
            return 'death'

        elif action == "3":
            print "|"
            print "|"
            print "|"
            print """
You pop around the corner with your hands up making sure Ocelot sees that you
currently have your weapon holstered. He laughs and says, "Oh, you're giving
up quite easily I see. Well I don't take any prisoners Snake." You tell him
you want to quick draw duel him. He's becomes very intrigued and agrees to the
duel. Both of you guys square up waiting for each others move when suddenly, a
figure wearing a full metal suit wielding a katana bounces around the room.
You're unable to get a clean shot while also avoiding his attacks. You quickly
escape the room when you notice that the ninja was focused on Ocelot.
"""
            print "|"
            print "|"
            print "|"
            print "|"
            print "|"
            print "\"AAAAAAHH MY ARMMM\" was the last thing you heard."
            return 'library'

        else:
            print "That's not an option."
            return 'death'


class Library(Scene):
    def enter(self):
        print "|"
        print "|"
        print "|"
        print "|"
        print "|"
        print """
You have been door to door, inside almost every room trying to look for
"Meryl Silverburgh" (The Colonel's Daughter), when you noticed double doors
that you haven't noticed before. They have a weird shimmer to them and you can't
help but go in. In your mind you're trying to resist going towards the doors,
but you're body moves towards it until you finally open them. Inside the room
you don't see anything at first until suddenly a figure appears out of thin air
floating in the center. It's "Psycho Mantis"; a member of FOXHOUND who's abilities
are difficult to put into terms. He has invited you to play a game with him.
He's thinking of a number between 1 and 10 but leaves no clue as to what it
could be. He's offered to give you 3 attempts to guess the number, but with
every incorrect answer he'll drain your body of "all that keeps you alive".
"""
        print "|"
        print "|"
        print "|"
        print "|"

        number = "%d" % (randint(1, 10))
        guess = raw_input("> ")
        guesses = 0

        while guess != number and guesses < 2:
            print "Mantis: \"INCORRECT\" You can feel your vision blurring."
            guesses += 1
            guess = raw_input("> ")

        if guess == number:
            print "|"
            print """
Mantis: "WHAT!!!"
As Psycho Mantis screams you begin to feel more and more normal. It's like
whatever was holding your body captive is slowly moving away...
Mantis: "THIS WAS NEVER SUPPOSED TO HAPPEN!!! YOU WERE SUPPOSED TO DIE BEFORE
YOU EVEN GOT A SINGLE GUESS OFF!!!"
His body begins to slowly crumble inward into nothingness. It was as if he were
never there.
"""
            return 'airbase'
        else:
            print """
Your vision begins to blur very badly making it impossible to stay focused.
The last thing you see is Psycho Mantis with his mask off.
"""
            return 'death'


class Airbase(Scene):

    def enter(self):
        print "|"
        print "|"
        print "|"
        print "|"
        print "|"
        print """
You smoke a couple of cigarettes and find yourself feeling a little bit better
after the run in with Psycho Mantis. You've made your way to the airbase where
you're expected to find Meryl, but instead run into a machine standing about
100ft tall and walking on its hind legs. It's Metal Gear REX, and the person
piloting it is a member of FOXHOUND, Liquid Snake. Before any dialogue could take
place the first shots were fired by the Metal Gear. After finding cover, you
find yourself trying to devise a plan to take down this weapon. You can try
shooting rockets at him, but the chances of surviving that exchange is about
50%. Otherwise, you can figure out another clever way to take the Metal Gear
down.
"""
        print "|"
        print "|"
        print "1. Attack the Metal Gear with rockets.."
        print "2. Try and see if Vulcan Raven's tank is still operable.."
        print "3. Sit still and wait on the slightest mistake Liquid could make.."

        unumber = "%d" % (randint(0, 1))
        guess = raw_input("> ")

        if guess == unumber:
            print "You managed to hit the Metal Gear in the weakest area with your second rocket"
            print "sending Liquid Snake and the Metal Gear up in flames. You must hurry out of"
            print "the airbase before everything begins to collapse."
            return 'extraction'

        if guess == 2:
            print """
You decided to go check to see if Vulcan Raven's tank is still operable, but
forgot that earlier in the mission you blew the tank up with him in it. Liquid
finds this astonishing, and fires 4 missles at your and instantly kill you.
"""
            return 'death'

        if guess == 3:
            print """
You sit still observing every single move the Metal Gear makes. You then run
from cover to cover when Liquid decides to fire missles your way. You can't
seem to figure out a pattern on the Metal Gear when suddenly a familiar man
in a metal suit with a katana blade (Cyborg Ninja AKA Gray Fox) comes in and
takes out a lot of the Metal Gear's motory functions. You find it the perfect
opportunity to fire a rocket at the cockpit of the Metal Gear as Liquid was
trying to vacate. The Metal Gear, Liquid, and Cyborg Ninja are all destroyed
as the machine causes a massive explosion. You must hurry out of the airbase
before everything begins to collapse.
"""
            return 'extraction'


class Extraction(Scene):
    def enter(self):
        print "|"
        print "|"
        print "|"
        print "|"
        print "|"
        print """
You have reached the extraction point and see Otacon out in the distance flying
in with Meryl, apparently she was evacuated way before the run in with Mantis.
They come flying in a helicopter take fire from all over. You reach up and grab
a hand, it was neither Otacon's or Meryl's. You get up and see the Colonol.
You couldn't help but give him a salute out of habit, and in the midst of a
crazy extraction, why not?
"""
        return 'finished'


class Finished(Scene):
    def enter(self):
        print "Col Campbell: Good work."
        return 'finished'


class Map(object):

    scenes = {
        'introduction': Introduction(),
        'central_corridor': CentralCorridor(),
        'library': Library(),
        'airbase': Airbase(),
        'extraction': Extraction(),
        'death': Death(),
        'finished': Finished(),
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('introduction')
a_game = Engine(a_map)
a_game.play()
