"""Import functions within the UI folder to have them run on load of the UI."""

import ui.plando_settings
import js
from ui.rando_options import (
    disable_barrel_modal,
    disable_boss_rando,
    disable_colors,
    disable_enemy_modal,
    disable_excluded_songs_modal,
    disable_music_filtering_modal,
    disable_hard_mode_modal,
    disable_helm_hurry,
    disable_remove_barriers,
    disable_faster_checks,
    disable_move_shuffles,
    disable_music,
    enable_plandomizer,
    handle_progressive_hint_text,
    item_rando_list_changed,
    max_doorone_requirement,
    max_doortwo_requirement,
    max_music,
    max_music_proportion,
    max_randomized_blocker,
    max_randomized_fairies,
    max_randomized_pearls,
    max_randomized_medal_cb_req,
    max_randomized_medals,
    max_randomized_troff,
    max_sfx,
    max_starting_moves_count,
    set_preset_options,
    set_random_weights_options,
    toggle_b_locker_boxes,
    toggle_counts_boxes,
    toggle_item_rando,
    toggle_key_settings,
    toggle_medals_box,
    toggle_vanilla_door_rando,
    update_boss_required,
    updateDoorOneNumAccess,
    updateDoorTwoNumAccess,
)

js.check_seed_info_tab()

# Update Rando Options
set_random_weights_options()
set_preset_options()
toggle_counts_boxes(None)
toggle_b_locker_boxes(None)
update_boss_required(None)
disable_colors(None)
disable_music(None)
disable_move_shuffles(None)
max_randomized_blocker(None)
handle_progressive_hint_text(None)
max_randomized_troff(None)
max_music(None)
max_music_proportion(None)
max_sfx(None)
disable_barrel_modal(None)
disable_enemy_modal(None)
disable_excluded_songs_modal(None)
disable_music_filtering_modal(None)
disable_hard_mode_modal(None)
toggle_item_rando(None)
disable_boss_rando(None)
toggle_medals_box(None)
max_randomized_medals(None)
max_randomized_medal_cb_req(None)
max_randomized_fairies(None)
max_randomized_pearls(None)
max_starting_moves_count(None)
max_doorone_requirement(None)
max_doortwo_requirement(None)
updateDoorOneNumAccess(None)
updateDoorTwoNumAccess(None)
item_rando_list_changed(None)
toggle_key_settings(None)
disable_helm_hurry(None)
disable_remove_barriers(None)
disable_faster_checks(None)
toggle_vanilla_door_rando(None)
enable_plandomizer(None)
