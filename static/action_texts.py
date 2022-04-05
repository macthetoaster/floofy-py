actions = {
    "boop": {
        "self": "{user} boops themselves!",
        "emoji": "<:meow_boop:960689660001124352>",
        "with_receivers": [
            "{user} sneakily walks towards {receivers} and boops them on the snoot!",
            "{user} boops {receivers} softly",
            "{user} runs towards {receivers} and boops them!",
            "{user} gently boops {receivers} on their snoot",
            "{user} boops {receivers} on the snoot!",
            "{user} approaches {receivers} and gives them a big boop!"
            "{user} walks towards {receivers}, waits a sec, and boops them!"
        ]
    },
    "pat": {
        "self": "{user} reaches over and pets themselves!",
        "emoji": "<:meow_pat:960689659904663573>",
        "with_receivers": [
            "{user} inches closer to {receivers} and pets them!",
            "{user} softly pets {receivers}",
            "{user} approaches {receivers} and gives them some pets!",
            "{user} gives a couple of quick pets to {receivers}",
            "{user} pets {receivers}!",
            "{user} walks towards {receivers} and gives them some pets!",
            "{user} approaches {receivers} and pets them!"
        ]
    },
    "hug": {
        "self": "{user} hugs a warm, soft pillow!",
        "emoji": "<:meow_hug:960689660043067392>",
        "with_receivers": [
            "{user} hugs {receivers}!",
            "{user} jumps on {receivers} and hugs them!",
            "{user} warms up to {receivers} and gives them a big hug",
            "{user} spreads their arms and locks {receivers} in a cozy hug!",
            "{user} embraces {receivers} in a warm, cozy hug!",
            "{user} walks towards {receivers} and hugs them!"
        ]
    },
    "nuzzle": {
        "self": "{user} nuzzles a soft plushie!",
        "emoji": "<:meow_happy:960689660005351484>",
        "with_receivers": [
            "{user} gets up close to {receivers} and nuzzles them!",
            "{user} nuzzles {receivers}",
            "{user} sneakily nuzzles {receivers}",
            "{user} gets their nose up close to {receivers} and nuzzles them!",
            "{user} goes towards {receivers} and gives them a big nuzzle!",
            "{user} shyly nuzzles {receivers}! Awwww~"
        ]
    },
    "kiss": {
        "self": "{user} kisses them- wait a minute! That's impossible!",
        "emoji": "<:meow_kissheart:960689659921449021>",
        "with_receivers": [
            "{user} jumps on {receivers} and smooches them!",
            "{user} kisses {receivers}",
            "{user} smooches {receivers}",
            "{user} gives multiple kisses to {receivers}!",
            "{user} shyly walks towards {receivers} and kisses them!",
            "{user} taps {receivers} on the shoulder and kisses them!"
        ]
    },
    "food": {
        "self": "{user} eats all the delicious food themselves! Oh no!",
        "emoji": "<:meow_fishnom:960689659904663572>",
        "with_receivers": [
            "{user} gives {receivers} a perfectly cooked :hamburger:! Yum!",
            "{user} gives {receivers} a delicious bowl of :salad:! Nom~",
            "{user} gives {receivers} a :burrito:! So good!",
            "{user} gives {receivers} a steaming hot bowl of :ramen:! Tasty!",
            "{user} gives {receivers} a big :sandwich:! Mmmmmm~",
            "{user} bakes some :cupcake: for {receivers}!",
            "{user} bakes a big :cake: for {receivers}!",
            "{user} shares some :cookie: with {receivers}! So generous!",
            "{user} cooks some fine :cut_of_meat: for {receivers}! What a chef~"
        ]
    },
    "bonk": {
        "self": "{user} bonks themselves! Such a klutz~",
        "emoji": "<:meow_baka:960689659904671815>",
        "with_receivers": [
            "{user} bonks {receivers}! Ow!",
            "{user} gives {receivers} a big bonk on the head!",
            "{user} walks up to {receivers} and bonks them!",
            "{user} sneakily bonks {receivers}! Ouchies!"
        ]
    },
    "slap": {
        "self": "{user} slaps themselves across the face! Ouchies!",
        "emoji": "<:meow_angryintensifies:960689339828936745>",
        "with_receivers": [
            "{user} slaps {receivers}!",
            "{user} smacks {receivers} across the face!",
            "{user} slapped {receivers}! Oh no!",
            "{user} beats some sense into {receivers}!",
            "{user} whacks {receivers} on the face! Ouchies!",
            "{user} slaps {receivers} leaving a big red mark! Ow!",
            "{user} gives {receivers} a real good slappin'!"
        ]
    }
}


# Aliases
actions["pet"] = actions["pat"]
actions["feed"] = actions["food"]
