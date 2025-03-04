'''
Write a program to find out the line number where python is present in a log file.

'''

x_content = '''The sun rises over the horizon, painting the sky with shades of orange and pink.
A cat stretches lazily on the windowsill, watching birds flutter between the trees.
The morning air feels crisp, carrying the scent of fresh grass and blooming flowers. Somewhere in the distance, a dog barks, breaking the silence.
Raindrops from last night’s storm still cling to the leaves, reflecting the golden sunlight.
A child laughs while chasing butterflies in the garden, their tiny feet crushing fallen petals.
A gentle breeze stirs the curtains, sending soft ripples across the glass of water on the table. A notebook lies open, its blank pages waiting to be filled with thoughts and ideas.
A radio hums a nostalgic tune, mixing with the rhythmic ticking of the clock on the wall.
The scent of toast drifts from the kitchen, mingling with the rich aroma of freshly brewed coffee.
A newspaper rustles as someone flips through the pages, scanning the headlines.
Outside, the city wakes up, with people rushing to catch buses, bicycles weaving through traffic, and vendors setting up stalls.
The world feels alive, each moment filled with movement, sound, and color.
Sunlight glimmers on the river’s surface as ripples spread from a passing boat.
Ducks paddle lazily, dipping their heads underwater in search of food.
A fisherman casts his line, waiting patiently for a bite.
The gentle lapping of waves against the shore creates a soothing rhythm.
Nearby, a painter sits with a canvas, capturing the scene in delicate brushstrokes.
A jogger passes by, music playing through their headphones, lost in thought.
The park is alive with the chatter of people enjoying the fresh air.
A little girl blows bubbles, watching them float and pop in the breeze.
A group of friends shares laughter over a picnic, sandwiches and fruit spread out on a checkered cloth.
Squirrels dart between the trees python, collecting acorns for the coming season.
The scent of pine needles lingers in the air, mixing with the earthy aroma of damp soil.
A train rumbles in the distance, its whistle cutting through the morning quiet.
A traveler waits on the platform, gripping a suitcase tightly.
The wind ruffles their coat, bringing the scent of the city with it.
Footsteps echo in the station as people hurry toward their destinations.
A vendor sells hot tea, steam rising from the paper cups.
A child tugs at their parent’s hand, excited for the journey ahead.
The train doors slide open, revealing rows of empty seats, waiting to be filled.
The sound of pages turning fills the quiet as a passenger loses themselves in a book.
Another stares out the window, watching fields and buildings blur into a moving painting.
The rhythmic clatter of the tracks creates a steady, almost hypnotic beat.
A thunderstorm brews in the distance, dark clouds rolling in with a sense of urgency.
The air thickens, heavy with the promise of rain.'''


def create_file():
    with open("log.txt", "w") as f:
        f.write(x_content)



def find_line_number_of_word(word_to_find):
    with open("log.txt", "r") as f:
        content = f.readlines()

    lineno = 1
    for line in content:
        if (word_to_find in line):
            print(f"Yes, the log file has '{word_to_find}' in line {lineno}")
            break

        lineno += 1

    else:
        print(f"No, the log file does not have '{word_to_find}' in it.")


create_file()
find_line_number_of_word("python")