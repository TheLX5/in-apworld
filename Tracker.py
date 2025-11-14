from typing import Any, TYPE_CHECKING
from .Variables import *

if TYPE_CHECKING:
    from . import TWorld

def setup_options_from_slot_data(world: "TWorld") -> None:
    if hasattr(world.multiworld, "generation_is_fake"):
        if hasattr(world.multiworld, "re_gen_passthrough"):
            if DISPLAY_NAME in world.multiworld.re_gen_passthrough:
                world.using_ut = True
                slot_data = world.multiworld.re_gen_passthrough[DISPLAY_NAME]
                world.options.characters.value = slot_data["characters"]
                world.options.exclude_lunatic.value = slot_data["exclude_lunatic"]
                world.options.stage_unlock.value = slot_data["stage_unlock"]
                world.options.spell_cards_teams.value = slot_data["spell_cards_teams"]
                world.options.number_life_mid.value = slot_data["number_life_mid"]
                world.options.number_bomb_mid.value = slot_data["number_bomb_mid"]
                world.options.difficulty_mid.value = slot_data["difficulty_mid"]
                world.options.number_life_end.value = slot_data["number_life_end"]
                world.options.number_bomb_end.value = slot_data["number_bomb_end"]
                world.options.difficulty_end.value = slot_data["difficulty_end"]
                world.options.number_life_extra.value = slot_data["number_life_extra"]
                world.options.number_bomb_extra.value = slot_data["number_bomb_extra"]
                world.options.extra_stage.value = slot_data["extra_stage"]
                world.options.difficulty_check.value = slot_data["difficulty_check"]
                world.options.time_check.value = slot_data["time_check"]
                world.options.time.value = slot_data["time"]
                world.options.both_stage_4.value = slot_data["both_stage_4"]
                world.options.goal.value = slot_data["goal"]
                world.options.ending_required.value = slot_data["ending_required"]
                world.options.treasure_location.value = slot_data["treasure_location"]
                world.options.treasure_final_spell_card.value = slot_data["treasure_final_spell_card"]
                world.treasure_final_spell_card = slot_data["treasure_final_spell_card"]
                world.options.capture_spell_cards_stage.value = slot_data["capture_spell_cards_stage"]
                world.spell_cards_teams = slot_data["spell_cards_teams"]
                world.characters_list = slot_data["characters_list"]
                world.spell_cards = slot_data["spell_cards"]
                world.capture_spell_cards_list = slot_data["capture_spell_cards_list"]
                world.capture_spell_cards_count = slot_data["capture_spell_cards_count"]
                world.nb_treasure_not_placed = slot_data["nb_treasure_not_placed"]
                world.treasures_locations = slot_data["treasures_locations"]
        else:
            world.using_ut = False
    else:
        world.using_ut = False