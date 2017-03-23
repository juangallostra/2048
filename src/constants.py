############################
### CONSTANTS DEFINITION ###
############################


### DRAWING ###

# Sizes
PADDING = 10
TILE_SIZE = 125

# Colors
BACKGROUND_COLOR = "#92877d"
BACKGROUND_COLOR_EMPTY_TILE = "#9e948a"
BACKGROUND_TILE_COLORS = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
                          32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
                          512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
TILE_COLORS = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
               32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
               512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
# Fonts
FONT = ("Verdana", 40)


### GAME LOGIC CONSTANTS ###

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

