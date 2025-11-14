from libevdev import EV_KEY

# Increase the activation rectangle so the numpad can be activated
# from the top-right corner down to the "NUMLK" label area on the pad.
# These values define how far from the right edge (width) and how
# far down from the top edge (height) the activation rectangle extends.
# Previously: width=200, height=250. Enlarged to better match touchpad labeling.
top_right_icon_width = 600
top_right_icon_height = 700

top_left_icon_width = 200
top_left_icon_height = 200

top_offset = 80
right_offset = 40
left_offset = 40
bottom_offset = 80

keys = [
    ["7", "8", "9", "slash", "BackSpace"],
    ["4", "5", "6", "asterisk", "BackSpace"],
    ["1", "2", "3", "minus", "Return"],
    ["0", "0", "period", "plus", "Return"]
]