"""Import functions within the UI folder to have them run on load of the UI."""
from ui.generate_buttons import update_seed_text
from ui.rando_options import (
    set_preset_options,
    toggle_b_locker_boxes,
    toggle_counts_boxes,
    update_boss_required,
    disable_colors,
    disable_music,
    disable_prices,
    max_randomized_blocker,
    max_randomized_troff,
    disable_barrel_modal,
    disable_boss_rando,
    hide_rgb,
    toggle_medals_box,
    max_randomized_medals,
    disable_rw,
)

# Call the generate_buttons function just to force loading of the file
update_seed_text(None)

# Update Rando Options
set_preset_options()
toggle_counts_boxes(None)
toggle_b_locker_boxes(None)
update_boss_required(None)
disable_colors(None)
disable_music(None)
disable_prices(None)
max_randomized_blocker(None)
max_randomized_troff(None)
disable_barrel_modal(None)
disable_boss_rando(None)
hide_rgb(None)
toggle_medals_box(None)
max_randomized_medals(None)
disable_rw(None)
