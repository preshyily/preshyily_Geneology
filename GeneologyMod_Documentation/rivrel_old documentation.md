
### Summary of `riv_rel.py`

- **Total Imports:** 27
- **Total Classes:** 3
- **Total Functions:** 96
- **Total Global Variables:** 29
- 
### Imports

Here are all the imports found in `riv_rel.py`:

1. **`from server_commands.argument_helpers import SimInfoParam`** - Importing `SimInfoParam` from argument_helpers.
2. **`from sims.sim_info import SimInfo`** - Importing `SimInfo` class from sim_info.
3. **`import services`** - Importing the `services` module.
4. **`import sims4.commands`** - Importing the `sims4.commands` module.
5. **`from relationships.relationship_bit import RelationshipBit`** - Importing `RelationshipBit` from relationship_bit.
6. **`from typing import List, Dict`** - Importing `List` and `Dict` from typing.
7. **`from functools import wraps`** - Importing `wraps` from functools.
8. **`import sims4.resources`** - Importing the `sims4.resources` module.
9. **`from sims4.resources import Types, get_resource_key`** - Importing `Types` and `get_resource_key` from sims4.resources.
10. **`from sims4.tuning.instance_manager import InstanceManager`** - Importing `InstanceManager` from instance_manager.
11. **`import random`** - Importing the `random` module.
12. **`from distributor.shared_messages import IconInfoData`** - Importing `IconInfoData` from shared_messages.
13. **`from sims4.localization import LocalizationHelperTuning`** - Importing `LocalizationHelperTuning` from sims4.localization.
14. **`from sims.sim_info_manager import SimInfoManager`** - Importing `SimInfoManager` from sim_info_manager.
15. **`from ui.ui_dialog_notification import UiDialogNotification`** - Importing `UiDialogNotification` from ui_dialog_notification.
16. **`import json`** - Importing the `json` module.
17. **`import os`** - Importing the `os` module.
18. **`from pathlib import Path`** - Importing `Path` from pathlib.
19. **`import configparser`** - Importing the `configparser` module.
20. **`from services.persistence_service import PersistenceService`** - Importing `PersistenceService` from persistence_service.
21. **`import sys`** - Importing the `sys` module.
22. **`import time`** - Importing the `time` module.
23. **`from interactions.utils.death import DeathTracker`** - Importing `DeathTracker` from interactions.utils.death.
24. **`from functools import lru_cache`** - Importing `lru_cache` from functools.
25. **`from zone import Zone`** - Importing `Zone` from zone.
26. **`from datetime import datetime`** - Importing `datetime` from datetime.
27. **`from scumbumbo import show_notif_texttitle`** - Importing `show_notif_texttitle` from scumbumbo.

### Classes in `riv_rel.py`

#### RivSim
1. **`__init__(self, sim_x)`**: Initializes a RivSim object either from a dictionary or a SimInfoParam object.
2. **`__str__(self)`**: Returns a string representation of the RivSim object.
3. **`__repr__(self)`**: Returns a string representation of the RivSim object (same as `__str__`).
4. **`to_dict(self)`**: Converts the RivSim object to a dictionary.
5. **`cull(self)`**: Marks a Sim as culled.
6. **`uncull(self)`**: Marks a Sim as unculled.
7. **`update_info(self, new_first_name, new_last_name, new_is_female, new_time)`**: Updates the information of a Sim if details have changed.

#### RivSimList
1. **`sims`**: A list to store RivSim objects.
2. **`__str__(self)`**: Returns a string representation of the RivSimList object.
3. **`__repr__(self)`**: Returns a string representation of the RivSimList object (same as `__str__`).
4. **`load_sims(self, file_name_extra: str)`**: Loads a list of Sims from a JSON file.
5. **`clear_sims(self)`**: Clears the list of Sims.

#### RivRelDict
1. **`rels`**: A dictionary to store relationships (sim_id: [parent_ids]).
2. **`__str__(self)`**: Returns a string representation of the RivRelDict object.
3. **`__repr__(self)`**: Returns a string representation of the RivRelDict object (same as `__str__`).
4. **`load_rels(self, file_name_extra: str)`**: Loads a dictionary of relationships from a JSON file.
5. **`clear_rels(self)`**: Clears the dictionary of relationships.

### Functions

1. **`get_slot`** - Retrieves the current save slot.
2. **`format_sim_date`** - Formats the current date in the Sim format.
3. **`riv_log`** - Logs messages for debugging purposes.
4. **`start_logging`** - Starts the logging process.
5. **`true_false`** - Converts values to boolean.
6. **`get_pairs_yield`** - Yields pairs of values.
7. **`get_pairs_return`** - Returns pairs of values.
8. **`console_show_relbits`** - Displays relationship bits via console.
9. **`get_rivsim_from_id`** - Retrieves a RivSim instance by its ID.
10. **`get_rivsim_from_sim`** - Retrieves a RivSim instance from a Sim instance.
11. **`get_sim_from_rivsim`** - Retrieves a Sim instance from a RivSim instance.
12. **`get_parents_ingame`** - Retrieves the parents of a Sim in-game.
13. **`get_parents`** - Retrieves the parents of a Sim.
14. **`console_get_parents`** - Displays the parents of a Sim via console.
15. **`get_children_ingame`** - Retrieves the children of a Sim in-game.
16. **`get_children`** - Retrieves the children of a Sim.
17. **`console_get_children`** - Displays the children of a Sim via console.
18. **`get_ancestors`** - Retrieves the ancestors of a Sim.
19. **`get_ancestors_ingame`** - Retrieves the ancestors of a Sim in-game.
20. **`rivsims_to_sims`** - Converts RivSim instances to Sim instances.
21. **`console_get_ancestors`** - Displays the ancestors of a Sim via console.
22. **`get_descendants`** - Retrieves the descendants of a Sim.
23. **`console_get_descendants`** - Displays the descendants of a Sim via console.
24. **`get_direct_rel`** - Retrieves direct relationships between Sims.
25. **`get_direct_relation`** - Checks if there is a direct relationship between two Sims.
26. **`format_direct_rel_gender`** - Formats direct relationships by gender.
27. **`format_direct_rel`** - Formats direct relationships.
28. **`console_get_direct_rel`** - Displays direct relationships via console.
29. **`get_sib_strength`** - Retrieves the sibling strength between Sims.
30. **`console_get_sib_strength`** - Displays sibling strength via console.
31. **`get_indirect_rel`** - Retrieves indirect relationships between Sims.
32. **`get_indirect_relation`** - Checks if there is an indirect relationship between two Sims.
33. **`format_indirect_rel_gender`** - Formats indirect relationships by gender.
34. **`format_indirect_rel`** - Formats indirect relationships.
35. **`console_get_indirect_rel`** - Displays indirect relationships via console.
36. **`get_spouses`** - Retrieves the spouses of a Sim.
37. **`get_inlaw_rel`** - Retrieves in-law relationships between Sims.
38. **`get_inlaw_relation`** - Checks if there is an in-law relationship between two Sims.
39. **`format_inlaw_rel`** - Formats in-law relationships.
40. **`get_step_rel`** - Retrieves step relationships between Sims.
41. **`get_step_relation`** - Checks if there is a step relationship between two Sims.
42. **`format_step_rel`** - Formats step relationships.
43. **`drel_percent`** - Retrieves the percentage of direct relationships.
44. **`irel_percent`** - Retrieves the percentage of indirect relationships.
45. **`consang`** - Calculates consanguinity between Sims.
46. **`console_get_consanguinity`** - Displays consanguinity via console.
47. **`inject`** - Injects a function.
48. **`inject_to`** - Injects a function into another function.
49. **`riv_rel_int_AddMixer_24508`** - Adds a relationship mixer interaction.
50. **`scumbumbo_show_notification`** - Shows a notification.
51. **`scumbumbo_show_notif_texttitle`** - Shows a notification with a text title.
52. **`get_str_list`** - Retrieves a list of strings.
53. **`num_to_tuple`** - Converts a number to a tuple.
54. **`combine_str_list`** - Combines lists of strings.
55. **`give_me_a_string`** - Retrieves a string.
56. **`riv_get_notif_generic`** - Retrieves a generic notification.
57. **`riv_get_notif`** - Retrieves a notification.
58. **`load_sims`** - Loads Sims data from a JSON file.
59. **`save_sims`** - Saves Sims data to a JSON file.
60. **`clean_sims`** - Cleans Sims data.
61. **`save_rels`** - Saves relationships data to a JSON file.
62. **`console_save_sims`** - Saves Sims data via console command.
63. **`console_load_sims`** - Loads Sims data via console command.
64. **`console_mem_sims`** - Displays the number of Sims in memory via console.
65. **`console_clean_sims`** - Cleans Sims data via console command.
66. **`console_clear_sims`** - Clears Sims data via console command.
67. **`console_update_sims`** - Updates Sims data via console command.
68. **`fix_cfg_settings`** - Fixes configuration settings.
69. **`load_cfg_settings`** - Loads configuration settings.
70. **`console_load_cfg_manually`** - Manually loads configuration settings via console command.
71. **`auto_json`** - Automatically updates JSON files.
72. **`console_auto_json`** - Sets up automatic JSON file updates via console command.
73. **`get_slot_olsaf`** - Injected function to get slot after loading screen animation finishes.
74. **`auto_json_oahasil`** - Injected function to automatically update JSON files on all households and Sims loaded.
75. **`is_eligible_couple`** - Checks if two Sims are eligible to be a couple.
76. **`riv_get_sims_for_spin_up_action`** - Injected function to pre-roll consanguinity calculations.
77. **`riv_load_zone`** - Injected function to handle zone loading.
78. **`auto_json_fam_asiinim`** - Injected function to update JSON files when a Sim info is added.
79. **`auto_json_fam_apr`** - Injected function to update JSON files when parent relations are added.
80. **`auto_json_fam_oatr`** - Injected function to update JSON files when a relationship bit is added.
81. **`auto_json_del_tmp_su`** - Injected function to update JSON files when the game is saved.
82. **`riv_getrelation_moreinfo`** - Gets detailed relationship info including step relations.
83. **`riv_getrandomrel`** - Checks a Sim's relation to a random Sim.
84. **`riv_getrandomrandomrel`** - Checks the relationship between two random Sims.
85. **`riv_getallrels`** - Checks a Sim's relationship to all Sims in the game.
86. **`riv_getallallrels`** - Checks all Sims' relationships to all other Sims.
87. **`console_help`** - Displays help information for the mod.
88. **`mean`** - Calculates the mean of a list.
89. **`generational_difference`** - Calculates the generational difference between two Sims.
90. **`riv_getgendiff`** - Gets the generational difference between two Sims.
91. **`riv_getsaveslotid`** - Retrieves the current save slot ID.
92. **`riv_clear_log`** - Clears the log except for errors and birth records.
93. **`console_is_eligible_couple`** - Checks if two Sims are an eligible couple.
94. **`console_get_suitors`** - Lists all eligible partners for a Sim.
95. **`riv_incest_prevention_test`** - Checks if a relationship is considered incest by the game.
96. **`riv_set_death_type`** - Logs when a Sim dies.

### Global Variables

1. **`addons`** - Configuration for addons.
2. **`cfg_default_vals`** - Default values for configuration settings.
3. **`consang_limit`** - Limit for consanguinity calculations.
4. **`drel_incest`** - Flag for direct relationship incest settings.
5. **`dt_string`** - Date and time string.
6. **`ex_file_name_extra`** - Extra file name for existing files.
7. **`ex_hex_slot_id`** - Hexadecimal slot ID for existing saves.
8. **`ex_mccc_autosaves_str`** - String representation of MCCC autosaves.
9. **`ex_opener`** - Opener string for notifications.
10. **`file_name_extra`** - Extra file name for new files.
11. **`global_include_step_rels`** - Flag for including step relationships globally.
12. **`hex_slot_id`** - Hexadecimal slot ID for current saves.
13. **`jsyk_ownfolder`** - Flag indicating if files are in their own folder.
14. **`log_level`** - Log level for logging.
15. **`mccc_autosave_enabled`** - Flag indicating if MCCC autosave is enabled.
16. **`mccc_autosaves`** - List of MCCC autosaves.
17. **`now`** - Current date and time.
18. **`num_reps`** - Number of repetitions for a process.
19. **`riv_allow_auto_json_simi`** - Flag allowing automatic JSON updates for a Sim.
20. **`riv_auto_enabled`** - Flag indicating if automatic JSON updates are enabled.
21. **`riv_auto_log`** - Flag indicating if logging is enabled.
22. **`riv_log_last_line`** - Last line logged.
23. **`riv_rel_dict`** - Dictionary for managing relationships.
24. **`riv_rel_int_24508_MixerId`** - Mixer ID for relationship interaction.
25. **`riv_rel_int_24508_SnippetId`** - Snippet ID for relationship interaction.
26. **`riv_sim_list`** - List for managing Sims.
27. **`rr_gen`** - Generation count for relationships.
28. **`show_consang`** - Flag indicating if consanguinity should be shown.
29. **`use_currentsession_files`** - Flag indicating if current session files should be used.

### Relationship Bits

#### DIRECT
- **0x2268**: `family_grandparent` – Indicates a grandparent relationship.
- **0x2269**: `family_parent` – Indicates a parent relationship.
- **0x2265**: `family_son_daughter` – Indicates a son or daughter relationship.
- **0x2267**: `family_grandchild` – Indicates a grandchild relationship.

#### VIA SIBLINGS
- **0x2262**: `family_brother_sister` – Indicates a sibling relationship.
- **0x227A**: `family_cousin` – Indicates a cousin relationship.
- **0x227D**: `family_aunt_uncle` – Indicates an aunt or uncle relationship.
- **0x2705**: `family_niece_nephew` – Indicates a niece or nephew relationship.

#### BY MARRIAGE
- **0x2278**: `family_stepsibling` – Indicates a stepsibling relationship.
- **0x5FAA**: `family_husband_wife` – Indicates a husband or wife relationship (not fully functional).
- **0x3DCE**: `romantic-Married` – Indicates a married relationship.

#### BY LOCALITY
- **0x1261E**: `neighbor` – Indicates a neighbor relationship.
- **0x1A36D**: `relationshipbit_CoWorkers` – Indicates a coworker relationship.

#### CLONES
- **0x1ABED**: `relationshipBit_IsClone` – Indicates a clone relationship (Get to Work pack).
- **0x34CCE**: `relationshipBit_Clone` – Indicates a clone relationship (Realm of Magic pack).

#### PARENTHOOD
- **0x0000000000027875**: `familyRelationshipBitsAcquired_Grandparent_HighRel` – Indicates a high relationship with a grandparent.
- **0x0000000000027876**: `familyRelationshipBitsAcquired_Grandchild_HighRel` – Indicates a high relationship with a grandchild.
- **0x0000000000027877**: `familyRelationshipBitsAcquired_Grandparent_NeutralRel` – Indicates a neutral relationship with a grandparent.
- **0x0000000000027882**: `familyRelationshipBitsAcquired_Grandchild_NeutralRel` – Indicates a neutral relationship with a grandchild.
- **0x0000000000027883**: `familyRelationshipBitsAcquired_Grandparent_PoorRel` – Indicates a poor relationship with a grandparent.
- **0x0000000000027884**: `familyRelationshipBitsAcquired_GrandChild_PoorRel` – Indicates a poor relationship with a grandchild.
- **0x000000000002788A**: `familyRelationshipBitsAcquired_Sibling_HighRel_LowRival` – Indicates a high relationship with a sibling with low rivalry.
- **0x000000000002788B**: `familyRelationshipBitsAcquired_Sibling_HighRel_HighRival` – Indicates a high relationship with a sibling with high rivalry.
- **0x000000000002788C**: `familyRelationshipBitsAcquired_Sibling_NeutralRel_HighRival` – Indicates a neutral relationship with a sibling with high rivalry.
- **0x000000000002788D**: `familyRelationshipBitsAcquired_Sibling_NeutralRel_LowRival` – Indicates a neutral relationship with a sibling with low rivalry.
- **0x000000000002788E**: `familyRelationshipBitsAcquired_Sibling_PoorRel_HighRival` – Indicates a poor relationship with a sibling with high rivalry.
- **0x000000000002788F**: `familyRelationshipBitsAcquired_Sibling_PoorRel_LowRival` – Indicates a poor relationship with a sibling with low rivalry.
- **0x00000000000278B0**: `familyRelationshipBitsAcquired_Parent_HighRel_HighAuth` – Indicates a high relationship with a parent with high authority.
- **0x00000000000278B1**: `familyRelationshipBitsAcquired_Child_HighRel_HighAuth` – Indicates a high relationship with a child with high authority.
- **0x00000000000278B2**: `familyRelationshipBitsAcquired_Parent_HighRel_LowAuth` – Indicates a high relationship with a parent with low authority.
- **0x00000000000278B3**: `familyRelationshipBitsAcquired_Child_HighRel_LowAuth` – Indicates a high relationship with a child with low authority.
- **0x00000000000278B4**: `familyRelationshipBitsAcquired_Parent_MaxRel_HighAuth` – Indicates a maximum relationship with a parent with high authority.
- **0x00000000000278B5**: `familyRelationshipBitsAcquired_Child_MaxRel_HighAuth` – Indicates a maximum relationship with a child with high authority.
- **0x00000000000278B6**: `familyRelationshipBitsAcquired_Parent_MaxRel_LowAuth` – Indicates a maximum relationship with a parent with low authority.
- **0x00000000000278B7**: `familyRelationshipBitsAcquired_Child_MaxRel_LowAuth` – Indicates a maximum relationship with a child with low authority.
- **0x00000000000278B8**: `familyRelationshipBitsAcquired_Parent_NeutralRel_HighAuth` – Indicates a neutral relationship with a parent with high authority.
- **0x00000000000278B9**: `familyRelationshipBitsAcquired_Child_NeutralRel_HighAuth` – Indicates a neutral relationship with a child with high authority.
- **0x00000000000278BA**: `familyRelationshipBitsAcquired_Parent_NeutralRel_LowAuth` – Indicates a neutral relationship with a parent with low authority.
- **0x00000000000278BB**: `familyRelationshipBitsAcquired_Child_NeutralRel_LowAuth` – Indicates a neutral relationship with a child with low authority.
- **0x00000000000278BC**: `familyRelationshipBitsAcquired_Parent_PoorRel_HighAuth` – Indicates a poor relationship with a parent with high authority.
- **0x00000000000278BD**: `familyRelationshipBitsAcquired_Child_PoorRel_HighAuth` – Indicates a poor relationship with a child with high authority.
- **0x00000000000278BE**: `familyRelationshipBitsAcquired_Parent_PoorRel_LowAuth` – Indicates a poor relationship with a parent with low authority.
- **0x00000000000278BF**: `familyRelationshipBitsAcquired_Child_PoorRel_LowAuth` – Indicates a poor relationship with a child with low authority.

#### FRIENDSHIP (positive)
- **0x3DB5**: `friendship-friend` – Indicates a friendship relationship.
- **0x3DB7**: `friendship-good_friends` – Indicates a good friends relationship.
- **0x3DB2**: `friendship-bff` – Indicates a best friends forever relationship.

#### FRIENDSHIP (negative)
- **0x0000000000003DB9**: `friendship-nemesis` – Indicates a nemesis relationship.
- **0x0000000000003DBA**: `friendship-disliked` – Indicates a disliked relationship.

#### ROMANCE (negative)
- **0x3DC3**: `romantic-Broken_Up` – Indicates a broken-up relationship.
- **0x3DC4**: `romantic-Broken_Up_Engaged` – Indicates a broken-up engagement.
- **0x3DC6**: `romantic-Despised_Ex` – Indicates a despised ex-relationship.
- **0x3DC7**: `romantic-Divorced` – Indicates a divorced relationship.
- **0x3DC9**: `romantic-Frustrated_Ex` – Indicates a frustrated ex-relationship.
- **0x3DCB**: `romantic-GotColdFeet` – Indicates a relationship where someone got cold feet.
- **0x3DCD**: `romantic-LeftAtTheAltar` – Indicates a relationship where someone was left at the altar.
- **0x99BC**: `romantic-LeaveAtTheAltar` – Indicates a relationship where someone left at the altar.
- **0x3DD2**: `RomanticCombo_AwkwardFriends` – Indicates an awkward friends relationship.
- **0x3DD3**: `RomanticCombo_AwkwardLovers` – Indicates an awkward lovers relationship.
- **0x3DD4**: `RomanticCombo_BadMatch` – Indicates a bad match relationship.
- **0x3DD6**: `RomanticCombo_EnemiesWithBenefits` – Indicates an enemies with benefits relationship.
- **0x3DE1**: `RomanticCombo_TerribleMatch` – Indicates a terrible match relationship.
- **0x3DE2**: `RomanticCombo_TotalOpposites` – Indicates a total opposites relationship.
- **0x3DE3**: `RomanticCombo_BadRomance` – Indicates a bad romance relationship.
- **0x905D**: `romantic-HasBeenUnfaithful` – Indicates an unfaithful relationship.
- **0x9191**: `romantic_CheatedWith` – Indicates a relationship involving cheating.
- **0x17C

34**: `ShortTerm_JustBrokeUpOrDivorced` – Indicates a short-term just broke up or divorced relationship.

#### ROMANCE (positive)
- **0x3DCA**: `romantic-GettingMarried` – Indicates a relationship where the couple is getting married.
- **0x3DD1**: `romantic-Significant_Other` – Indicates a significant other relationship.
- **0x3DD5**: `RomanticCombo_Lovebirds` – Indicates a lovebirds relationship.
- **0x3DDD**: `RomanticCombo_Lovers` – Indicates a lovers relationship.
- **0x3DDE**: `RomanticCombo_RomanticInterest` – Indicates a romantic interest relationship.
- **0x3DE0**: `RomanticCombo_Sweethearts` – Indicates a sweethearts relationship.
- **0x2DD3D**: `romance-Faithful` – Indicates a faithful romantic relationship.

#### ROMANCE (other)
- **0x18EC1**: `romantic-Widow` – Indicates a widow relationship.
- **0x191FF**: `romantic-Widower` – Indicates a widower relationship.
- **0x196E1**: `romantic_DeadSpouse` – Indicates a dead spouse relationship.

#### MISC
- **0x27AB2**: `CT_notParent_CareGiver` – Indicates a caregiver relationship (Parenthood pack).
- **0x27AB3**: `CT_notParent_CareDependent` – Indicates a care dependent relationship (Parenthood pack).
- **0x000000000000692B**: `relationshipBits_Mischief_PartnersInCrime` – Indicates a partners in crime relationship.
- **0x00000000000070EF**: `LoanRelationshipBits_Small` – Indicates a small loan relationship.
- **0x00000000000070F0**: `LoanRelationshipBits_Large` – Indicates a large loan relationship.

#### ???
- **0x3DD7**: `RomanticCombo_Frenemies` – Indicates a frenemies relationship.
- **0x3DD8**: `RomanticCombo_HotAndCold` – Indicates a hot and cold relationship.
- **0x0000000000003DB3**: `friendship-bff_Evil` – Indicates an evil best friends forever relationship.
- **0x0000000000003DB6**: `friendship-friend_Evil` – Indicates an evil friendship relationship.
- **0x0000000000003DB8**: `friendship-good_friends_Evil` – Indicates an evil good friends relationship.
- **0x0000000000003DC1**: `relationshipBits_Friendship_NeutralBit` – Indicates a neutral friendship relationship.
- **0x0000000000003DC2**: `relationshipBits_Romance_NeutralBit` – Indicates a neutral romance relationship.
- **0x000000000000692A**: `relationshipBits_Mischief_NeutralBit` – Indicates a neutral mischief relationship.
- **0x12F11**: `RomanticCombo_Acquaintances` – Indicates an acquaintances romantic relationship.
- **0x0000000000012F41**: `RomanticCombo_JustFriends` – Indicates a just friends relationship.
- **0x0000000000012F42**: `RomanticCombo_JustGoodFriends` – Indicates a just good friends relationship.
- **0x0000000000012F4F**: `RomanticCombo_Disliked` – Indicates a disliked romantic relationship.
- **0x0000000000012F50**: `RomanticCombo_Despised` – Indicates a despised romantic relationship.
- **0x1F90F**: `HasBeenFriends` – Indicates a has been friends relationship.

#### In packs not owned
- **0x0000000000035662**: `relationshipBit_Robot_Creation` – Indicates a robot creation relationship.
- **0x0000000000035663**: `relationshipBit_Robot_Creator` – Indicates a robot creator relationship.

#### Added to notifications
- **0x3DB0**: `friendship-acquaintances` – Indicates an acquaintances friendship relationship.
- **0x18961**: `relbit_Pregnancy_Birthparent` – Indicates a pregnancy birthparent relationship.
- **0x79EB**: `friendship-bff_BromanticPartner` – Indicates a bromantic partner relationship.
- **0x1A36D**: `relationshipbit_CoWorkers` – Indicates a coworkers relationship.
- **0x27A6**: `had first kiss` – Indicates a first kiss relationship.
- **0x12E3B**: `ShortTerm_RecentFirstKiss` – Indicates a recent first kiss relationship.
- **0x873B**: `romantic-HaveDoneWooHoo` – Indicates a woohoo relationship.
- **0x17B82**: `romantic-HaveDoneWooHoo_Recently` – Indicates a recent woohoo relationship.
- **0x3DB4**: `friendship-despised` – Indicates a despised friendship relationship.
- **0x181C4**: `HaveBeenRomantic` – Indicates a have been romantic relationship.
- **0x1F064**: `romantic-ExchangedNumbers` – Indicates an exchanged numbers relationship.
- **0x3DDF**: `RomanticCombo_Soulmates` – Indicates a soulmates relationship.
- **0x18465**: `romantic-Promised` – Indicates a promised relationship (engaged as teens).
- **0x3DC8**: `romantic-Engaged` – Indicates an engaged relationship.
- **0x3DCE**: `romantic-Married` – Indicates a married relationship.
- **0x34CCE**: `relationshipBit_Clone` – Indicates a clone relationship (Realm of Magic pack).

#### Extended relationships package by simsmodelsimmer
- **0x794**: `great-grandchild` – Indicates a great-grandchild relationship.
- **0x795**: `great-grandparent` – Indicates a great-grandparent relationship.
- **0x796**: `sibling-in-law` – Indicates a sibling-in-law relationship.
- **0x797**: `??` – Unknown.
- **0x798**: `??` – Unknown.
- **0x793**: `child-in-law` – Indicates a child-in-law relationship.
- **0x788**: `parent-in-law` – Indicates a parent-in-law relationship.

#### Test set instances
- **0x278D9**: `testSetInstance_FamilyRelBitAcquired_HasNoSiblingBit` – Test set instance for family relationship bit acquired with no sibling bit.
- **0x278EC**: `testSetInstance_FamilyRelBitAcquired_HasNoParentBit` – Test set instance for family relationship bit acquired with no parent bit.

This detailed breakdown covers all the components of the `riv_rel.py` file, providing a comprehensive overview of its structure and functionality.


## `riv_rel.py` file:

The first part of the `riv_rel.py` file includes several imports from the Sims 4 modding API and some Python standard libraries. Here's an overview of the imports and what they imply about the functionality of the mod:

```python
from server_commands.argument_helpers import SimInfoParam
# from relationships.relationship_service import RelationshipService
# from server_commands.genealogy_commands import get_family_relationship_bit
# from sims.sim_info import get_sim_instance, get_name_data
from sims.sim_info import SimInfo
import services
import sims4.commands  # , sims.sim_info_types, sims.sim_info_manager, server_commands.relationship_commands
# from relationships.relationship import Relationship
from relationships.relationship_bit import RelationshipBit
# from relationships.relationship_tracker import RelationshipTracker
from typing import List, Dict
from functools import wraps
import sims4.resources
from sims4.resources import Types, get_resource_key
from sims4.tuning.instance_manager import InstanceManager
import random
from distributor.shared_messages import IconInfoData
# from sims4.collections import make_immutable_slots_class
from sims4.localization import LocalizationHelperTuning  # , _create_localized_string
from sims.sim_info_manager import SimInfoManager

# for notifications
# from ui.ui_dialog import UiDialogResponse, ButtonType, CommandArgType
from ui.ui_dialog_notification import UiDialogNotification

# for finding file location
# https://discordapp.com/channels/605863047654801428/624442188335415320/760257300002504756
import json
# import date_and_time
import os
from pathlib import Path

# for config file (used for auto_json settings)
import configparser

# for getting save IDs and running on save
from services.persistence_service import PersistenceService

# for getting autosaves from MCCC (add IDs to mccc_autosaves = [])
# Mods/riv_rel/riv_rel.ts4script/riv_rel.pyc
import sys
import time

# for despawn (death) things
from interactions.utils.death import DeathTracker

# for cache (used for consang and is_eligible_couple)
from functools import lru_cache

# determining if zone is loading
from zone import Zone

# get irl datetime
from datetime import datetime
```
### Analysis of Imports

1. **SimInfoParam and SimInfo**:
   - These are used to interact with the Sim information, allowing access to Sim properties and methods.

2. **services**:
   - This module provides access to various game services, which are essential for implementing features that interact with the game world and Sim data.

3. **sims4.commands**:
   - This is used to define custom commands that can be executed from the game’s console. The commented out parts suggest that some commands related to relationships and genealogy were considered but not included in this specific implementation.

4. **RelationshipBit**:
   - This class is part of the relationship module, likely used to define specific types of relationships between Sims.

5. **List, Dict, wraps**:
   - These are standard Python modules and functions used for typing hints and function decoration.

6. **sims4.resources and InstanceManager**:
   - These modules are used for managing game resources and instances, which can include tuning files and other game data.

7. **random**:
   - The random module suggests that there might be some randomization in how relationships or interactions are determined or presented.

8. **IconInfoData and LocalizationHelperTuning**:
   - These are used for handling game icons and localization, respectively, indicating that the mod includes custom icons and localized text.

9. **SimInfoManager**:
   - Manages multiple SimInfo objects, likely used to handle interactions involving multiple Sims.

10. **UiDialogNotification**:
   - This class is used to create and manage notification dialogs within the game, essential for displaying relationship information to the player.

11. **json, os, Path**:
   - Standard libraries for handling JSON data, file operations, and path manipulations, which are used for saving and loading genealogical data.

12. **configparser**:
   - Used for reading and writing configuration files, allowing the mod to save settings and preferences.

13. **PersistenceService**:
   - Handles the persistence of data, crucial for maintaining genealogical information across game sessions.

14. **sys, time**:
   - Standard libraries for system-specific parameters and functions, and time-related functions.

15. **DeathTracker**:
   - Tracks the death state of Sims, possibly used to manage genealogical data when Sims die.

16. **lru_cache**:
   - A decorator to cache the results of expensive or I/O bound functions, used to optimize performance for functions like consanguinity checks.

17. **Zone**:
   - Likely used to determine the loading state of the game zone, which can be important for initializing or updating mod data.

18. **datetime**:
    - Used to get the current date and time, potentially for timestamping genealogical data or managing time-sensitive features.

Now that we have an understanding of the imports and setup, the next step is to look at the code defined in the file. This will help us understand how these imports are used in practice.


### Function Definitions

#### `get_slot()`
```python
def get_slot():
    # get save slot ID
    per = services.get_persistence_service()
    int_slot_id = int(per._save_game_data_proto.save_slot.slot_id)
    hex_slot_id_tmp = hex(int_slot_id)[2:]
    hex_slot_id = ('0' * (8 - len(hex_slot_id_tmp))) + hex_slot_id_tmp
    return hex_slot_id
```
- **Purpose**: Retrieves the current save slot ID and converts it to a hex string.
- **How It Works**: 
  1. It accesses the persistence service to get the save slot ID.
  2. Converts the integer slot ID to a hexadecimal string.
  3. Pads the hex string with leading zeros to ensure it is 8 characters long.
- **Why It’s Needed**: This function is likely used to uniquely identify and manage save files, which is crucial for maintaining genealogical data across different game saves.

#### `format_sim_date()`
```python
def format_sim_date():
    simNow = str(services.time_service().sim_now)
    listNow = simNow.split(' ')
    simWeek = listNow[2].split(':')
    simDay = listNow[1].split(':')
    simTime = listNow[0].split('.')
    if 0 <= int(simDay[1]):
        simWeekNumber = 1 + int(simWeek[1])
        simDayNumber = 1 + int(simDay[1])
        simTimeNow = 'week {} day {} {}'.format(simWeekNumber, simDayNumber, simTime[0])
        return simTimeNow
```
- **Purpose**: Formats the current in-game time into a human-readable string.
- **How It Works**: 
  1. Gets the current in-game time from the time service.
  2. Splits the time into components (week, day, and time).
  3. Adjusts the week and day numbers to be 1-based (instead of 0-based).
  4. Constructs a string in the format "week X day Y Z" where X is the week number, Y is the day number, and Z is the time.
- **Why It’s Needed**: This function is useful for logging and displaying in-game time in a way that is easy for players to understand.

#### Global Variables

```python
rr_gen = 7
```
- **Purpose**: Tracks the generation or version of the mod.
- **Why It’s Needed**: This helps in managing updates and ensuring compatibility with the current version of the game or the mod.

```python
riv_auto_enabled = False  # this can be set by the user for each save. KEEP this as default false!!!
file_name_extra = ''
hex_slot_id = '00000000'  # updated on game load
```
- **Purpose**: Manages the state of automatic saving and file naming.
- **Why It’s Needed**: Allows users to enable or disable auto-saving features and manage file names dynamically based on the game load.

```python
riv_rel_int_24508_SnippetId = 24508
riv_rel_int_24508_MixerId = (
    17552881007513514036,
    18078901824007092157
)
```
- **Purpose**: Stores identifiers for specific interactions related to the mod.
- **Why It’s Needed**: These IDs are used to link in-game interactions to the mod’s functionality, such as asking if Sims are related.

```python
jsyk_ownfolder = False  # KEEP FALSE
```
- **Purpose**: Indicates if the mod should give a heads up about its own folder.
- **Why It’s Needed**: This is likely a placeholder for a feature that alerts users about the mod’s folder structure.

```python
mccc_autosaves = []
mccc_autosave_enabled = False  # KEEP FALSE
```
- **Purpose**: Manages compatibility with MCCC (MC Command Center) autosave functionality.
- **Why It’s Needed**: Ensures that the mod does not interfere with MCCC’s autosave feature unless explicitly enabled by the user.

```python
addons = {'computer': False, 'traits': False, 'GT': False}  # KEEP FALSE
```
- **Purpose**: Tracks the existence and state of various addons.
- **Why It’s Needed**: Allows the mod to conditionally enable or disable features based on the presence of specific addons.

```python
use_currentsession_files = False  # KEEP FALSE
```
- **Purpose**: Indicates whether to use files specific to the current game session.
- **Why It’s Needed**: This can help in managing performance by limiting file operations to the current session.

```python
global_include_step_rels = False  # KEEP FALSE TODO: until they work
```
- **Purpose**: Controls whether step relationships are included in relationship checks.
- **Why It’s Needed**: This feature is marked as a TODO, indicating that step relationships may not be fully implemented or reliable yet.

```python
# default cfg values
# search_if_updating_settings
cfg_default_vals = dict(
    # gen 4
    file_name_extra='default'
```
- **Purpose**: Stores default configuration values for the mod.
- **Why It’s Needed**: Provides a baseline for settings that can be customized by the user.

```python
cfg_default_vals = dict(
    file_name_extra='default_asdfghjkl',
    auto_update_json='False',  # stays false to prevent multiple writes to default_asdfghjkl
    advanced_use_currentsession_files='False',
    # include_step_rels='False',
)
```
- **Purpose**: Contains default values for various configuration settings.
- **Why It’s Needed**: Provides default settings that can be adjusted by the user, ensuring the mod operates correctly out of the box.

```python
# whether to allow auto_json for one sim (false during loading screen)
riv_allow_auto_json_simi = False

# previous notif text
ex_opener = ''
ex_mccc_autosaves_str = ''
ex_hex_slot_id = ''
ex_file_name_extra = ''
```
- **Purpose**: Tracks the state of various features and previous notification texts.
- **Why It’s Needed**: These variables help manage the state of the mod during gameplay, such as preventing actions during the loading screen and storing previous state information.

```python
# logging stuff for testing (true <=> riv_rel.log is in the folder)
riv_auto_log = os.path.isfile(os.path.join(Path(__file__).resolve().parent.parent, 'riv_rel.log'))
riv_log_last_line = ''
num_reps = 1
# log level (3 for showing extra, 2 for normal, 1 for errors only, 0 for none)
log_level = 2
```
- **Purpose**: Manages logging for debugging and testing purposes.
- **Why It’s Needed**: Provides a way to log the mod’s activities and errors, which is crucial for debugging and ensuring the mod runs smoothly.

#### `riv_log` Function

```python
def riv_log(string, level=2):
    # make absolutely sure it's a string lol
    string = str(string)
    global riv_auto_log
    global log_level
    if riv_auto_log and level <= log_level:
        file_dir = Path(__file__).resolve().parent.parent
        file_name = 'riv_rel.log'
        file_path = os.path.join(file_dir, file_name)
        global riv_log_last_line
        global num_reps
        try:
            if string == riv_log_last_line:
                num_reps += 1
            else:
                if 'error' in string:
                    log_level = 1
                with open(file_path, 'a') as file:
                    if num_reps > 1:
                        file.write(f'    (repeated {num_reps} times)\n')
                    file.write(string + '\n')
                    riv_log_last_line = string
                    num_reps = 1
        except Exception as e:
            riv_log(str(e))
    else:
        pass
```
- **Purpose**: Enhances the logging functionality to handle repeated messages and errors.
- **How It Works**:
  1. Sets up the file path for the log file.
  2. Checks if the current message is the same as the last logged message to count repetitions.
  3. Logs messages to the file, including repetition counts if necessary.
  4. Catches and logs any exceptions that occur during logging.
- **Why It’s Needed**: This ensures that the log file remains concise by consolidating repeated messages and handling errors gracefully.

### Initialization Logging

```python
# new line before session
riv_log(f'[game loaded at {format(dt_string)}]', 1)
riv_log('', 1)
```
- **Purpose**: Logs the game load event with a timestamp.
- **Why It’s Needed**: Marks the start of a new game session in the log file, helping to differentiate between different play sessions.

### Importing Strings

```python
# get strings
try:
    import strings.riv_rel_strings as rrs  # TODO: get individual ones

    p = rrs.p
    riv_log(f'riv_rel successfully imported riv_rel_strings for language {rrs.lang}')
except Exception as e:
    riv_log('error - riv_rel failed to import riv_rel_strings because ' + str(e))
```
- **Purpose**: Logs the successful import of string resources and handles exceptions.
- **Why It’s Needed**: Ensures that any issues with importing string resources are logged for debugging purposes.

### Update Configuration Files

```python
# gen 4 -> gen 5 update: rename .cfg
for file in os.scandir(Path(__file__).resolve().parent.parent):
    if file.name.startswith('riv_rel_autojson') and file.name.endswith('.cfg'):
        os.rename(os.path.join(Path(__file__).resolve().parent.parent, file),
                  os.path.join(Path(__file__).resolve().parent.parent, 'riv_rel - individual save settings.cfg'))
```
- **Purpose**: Renames configuration files from the old naming convention to the new one.
- **Why It’s Needed**: Ensures compatibility with updates to the mod’s configuration file structure.

### Default Settings

```python
# search_if_updating_settings
consang_limit = 2 ** -5  # second cousin
drel_incest = True  # whether direct rels always count as incestuous
show_consang = False  # whether consanguinity is shown in notifications
```
- **Purpose**: Sets default values for consanguinity limit, direct relationship incest rules, and consanguinity display.
- **Why It’s Needed**: Provides default settings that can be customized by the user.

### Logging Initialization Function

```python
# find addons and MCCC; now in a function so it can be called again

# made into a function so it can be called
def start_logging():
    global riv_auto_log
    if not riv_auto_log:
        riv_log(f'[started logging at {format(dt_string)}]', 1)
        riv_log('', 1)
        try:
            riv_log(f'using riv_rel_strings for language {rrs.lang}')
        except Exception as e0:
            riv_log('error - riv_rel failed to detect language because ' + str(e0))
```
- **Purpose**: Enhances the `start_logging` function to log the language setting and handle errors.
- **How It Works**:
  1. Attempts to log the language used by the string resources.
  2. Catches and logs any exceptions related to detecting the language.
- **Why It’s Needed**: Provides additional context in the log file regarding the language settings, which can be useful for debugging and user support.

#### Mod Folder Access and Path Setup

```python
    extra_files_tic = time.perf_counter()

    # access the mods folder
    mods_path = Path(__file__).resolve()
    appendage = '/'
    # https://stackoverflow.com/questions/33372054/get-folder-name-of-the-file-in-python
    while not os.path.basename(mods_path) == 'Mods':
        mods_path = mods_path.parent
        appendage = '.' + appendage
    sys.path.append(appendage)  # will go up to Mods/ folder
```
- **Purpose**: Determines the path to the Mods folder and sets up the system path accordingly.
- **How It Works**:
  1. Resolves the current file path.
  2. Traverses up the directory tree until it finds the Mods folder.
  3. Appends the appropriate path to the system path to ensure the mod can access necessary resources.
- **Why It’s Needed**: Ensures that the mod can locate and access the required files and folders within the Mods directory, which is essential for its operation.

#### MCCC Autosave Detection

```python
    global mccc_autosave_enabled
    global mccc_autosave_hexslotnumber
    global mccc_autosave_maxsavenumber
    try:
        mccc_cfg_path = None
        # search folders and subfolders
        # https://stackoverflow.com/questions/5817209/browse-files-and-subfolders-in-python
        for root, dirs, files in os.walk(mods_path):
            for name in files:
                if name.startswith('mc_settings') and name.endswith('cfg'):
                    mccc_cfg_path = root + os.sep + name
                elif name.startswith('riv_rel_addon_computer') and name.endswith('package'):
                    riv_log('detected computer addon', 2)
                    addons['computer'] = True
                elif (not addons['traits']) and name.startswith('riv_rel_addon_traits') \
                        and (name.endswith('package') or name.endswith('ts4script')):
                    riv_log('detected traits addon', 2)
                    addons['traits'] = True
                elif name.startswith('riv_rel_addon_GT') and name.endswith('ts4script'):
                    riv_log('detected GT addon', 2)
                    addons['GT'] = True
                if addons['computer'] and addons['traits'] and addons['GT'] and (mccc_cfg_path is not None):
                    # all settings confirmed
                    break
        # find file and grab it as dict
            if mccc_cfg_path is not None:
                with open(mccc_cfg_path, 'r') as mccc_cfg:
                    mccc_cfg_dict = json.load(mccc_cfg)
            else:
                riv_log('did not find mc_settings.cfg', 1)
            # get vars
            mccc_autosave_enabled = mccc_cfg_dict['Autosave_Enabled']
            mccc_autosave_hexslotnumber = mccc_cfg_dict['Autosave_HexSlotNumber']
            mccc_autosave_maxsavenumber = mccc_cfg_dict['Autosave_MaxSaveNumber']
            # kill dict
            del mccc_cfg_dict
        except Exception as ex:
            riv_log(f'mc_settings not grabbed from .cfg: {ex}', 1)
            mccc_autosave_enabled = False
            mccc_autosave_hexslotnumber = ''
            mccc_autosave_maxsavenumber = 0
```
- **Purpose**: Detects the presence of MCCC settings and various addons in the Mods folder.
- **How It Works**:
  1. Traverses the Mods directory and its subdirectories to find specific files.
  2. Checks for MCCC settings files and sets the `mccc_cfg_path` if found.
  3. Logs and updates the `addons` dictionary based on the presence of addon files (`computer`, `traits`, `GT`).
  4. Breaks out of the loop once all required settings and addons are confirmed.
- **Why It’s Needed**: Ensures that the mod can detect and utilize additional functionalities provided by MCCC and other addons, enhancing compatibility and user experience.


#### Autosave Slots Handling

```python
    if mccc_autosave_enabled:
        # turn smallest save ID into an int: '1111' -> '0x1111' -> 4369
        smallest_save = int('0x' + str(mccc_autosave_hexslotnumber), 16)
        for i in range(0, mccc_autosave_maxsavenumber):
            # int_slot_id = 4369 + i
            int_slot_id = smallest_save + i
            # hex_slot_id_tmp = 1111
            hex_slot_id_tmp = hex(int_slot_id)[2:]
            # hex_slot_id = 00001111
            hex_slot_id = ('0' * (8 - len(hex_slot_id_tmp))) + hex_slot_id_tmp
            mccc_autosaves.append(hex_slot_id)
        riv_log(f'autosave slots = {mccc_autosaves}')
```
- **Purpose**: Manages the list of autosave slots based on MCCC settings.
- **How It Works**:
  1. Converts the smallest save ID from hex to an integer.
  2. Iterates over the range of maximum save numbers to generate slot IDs.
  3. Converts each slot ID back to a padded hex string and appends it to the `mccc_autosaves` list.
  4. Logs the autosave slots.
- **Why It’s Needed**: Ensures that the mod can correctly identify and manage autosave slots provided by MCCC, enhancing compatibility and functionality.

#### Performance Logging

```python
    extra_files_toc = time.perf_counter()
    riv_log(f'time taken to find extra files (riv_rel addons and mc_settings.cfg): {extra_files_toc - extra_files_tic}')
```
- **Purpose**: Logs the time taken to find extra files such as addons and MCCC settings.
- **Why It’s Needed**: Helps in performance monitoring and optimization.

#### Configuration File Handling

```python
    # add to or make overall cfg file
    try:
        # config stuff
        config_dir = Path(__file__).resolve().parent.parent
        config_name = 'riv_rel - overall settings.cfg'
        file_path = os.path.join(config_dir, config_name)
        config = configparser.ConfigParser()

        # try to get cfg file
        try:
            config.read_file(open(file_path, 'r'))
        except:
            riv_log('no .cfg file found. creating one...')
```
- **Purpose**: Reads or creates the overall configuration file for the mod.
- **How It Works**:
  1. Defines the path and name for the configuration file.
  2. Attempts to read the configuration file.
  3. If the file does not exist, logs a message and prepares to create a new one.
- **Why It’s Needed**: Ensures that the mod has a persistent configuration file to store settings and preferences.

#### Default Settings Handling

```python
        # default settings if needed
        if not (os.path.isfile(file_path) and 'main_mod' in config.sections()):
            config['main_mod'] = {}
            with open(file_path, 'w') as cfg_file:
                config.write(cfg_file)
                riv_log('created main_mod section in overall cfg')
```
- **Purpose**: Ensures that the configuration file has a `main_mod` section.
- **How It Works**:
  1. Checks if the configuration file exists and contains a `main_mod` section.
  2. If not, creates the `main_mod` section and writes it to the file.
  3. Logs the creation of the `main_mod` section.
- **Why It’s Needed**: Provides a dedicated section for the mod’s main settings, ensuring a structured and organized configuration file.

#### Loading Configuration Settings

```python
        # now cfg will exist; load in settings
        config.read_file(open(file_path, 'r'))
        keys = []
        for (key, val) in config.items('main_mod'):
            if key not in keys:
                keys.append(key)
        # search_if_updating_settings
```
- **Purpose**: Loads the settings from the configuration file.
- **How It Works**:
  1. Reads the configuration file.
  2. Iterates through the items in the `main_mod` section and collects the keys.
- **Why It’s Needed**: Ensures that the mod loads its settings from the configuration file at startup.

#### Consanguinity Limit Handling

```python
        # consanguinity
        global consang_limit
        try:
            consang_limit = config.getfloat('main_mod', 'consanguinity_limit')
            riv_log(f'grabbed main_mod consanguinity limit as {consang_limit}')
        except Exception as e:
            config['main_mod']['consanguinity_limit'] = str(consang_limit)
            with open(file_path, 'w') as cfg_file:
                config.write(cfg_file)
            riv_log(f'set up main_mod consanguinity limit as default {consang_limit}')
```
- **Purpose**: Retrieves the consanguinity limit from the configuration file or sets a default value if not present.
- **How It Works**:
  1. Attempts to get the `consanguinity_limit` value from the `main_mod` section.
  2. If successful, logs the retrieved value.
  3. If an error occurs (e.g., the key doesn’t exist), sets the default value and writes it to the configuration file.
- **Why It’s Needed**: Ensures that the consanguinity limit is properly configured, providing a key setting for managing in-game relationships.

#### Show Consanguinity in Notifications

```python
        # show consanguinity in notifications
        global show_consang
        try:
            show_consang = config.getboolean('main_mod', 'show_consanguinity_in_notifs')
            riv_log(f'grabbed main_mod show_consanguinity_in_notifs as {show_consang}')
        except Exception as e:
            config['main_mod']['show_consanguinity_in_notifs'] = str(show_consang)
            with open(file_path, 'w') as cfg_file:
                config.write(cfg_file)
            riv_log(f'set up main_mod show_consanguinity_in_notifs as {show_consang}')
```
- **Purpose**: Retrieves the setting for showing consanguinity in notifications from the configuration file or sets a default value if not present.
- **How It Works**:
  1. Attempts to get the `show_consanguinity_in_notifs` value from the `main_mod` section.
  2. If successful, logs the retrieved value.
  3. If an error occurs (e.g., the key doesn’t exist), sets the default value and writes it to the configuration file.
- **Why It’s Needed**: Ensures that the setting for showing consanguinity in notifications is properly configured, providing a key feature for user interaction.

#### Direct Relationships as Incestuous

```python
        # direct rels are incest
        global drel_incest
        try:
            drel_incest = config.getboolean('main_mod', 'direct_rels_are_incestuous')
            riv_log(f'grabbed main_mod direct rel is always incest as {drel_incest}')
        except Exception as e:
            config['main_mod']['direct_rels_are_incestuous'] = str(drel_incest)
            with open(file_path, 'w') as cfg_file:
                config.write(cfg_file)
            riv_log(f'set up main_mod direct rel is always incest as {drel_incest}')

            riv_log('loaded in cfg settings')
            except Exception as e2:
            riv_log('error - something went wrong with the cfg: ' + str(e2))
            riv_log('using riv\'s default settings')
```
- **Purpose**: Retrieves the setting for treating direct relationships as incestuous from the configuration file or sets a default value if not present. Finalizes the configuration settings by writing any defaults if necessary and logging the loaded settings.
- **How It Works**:
  1. Attempts to get the `direct_rels_are_incestuous` value from the `main_mod` section.
  2. If successful, logs the retrieved value.
  3. If an error occurs (e.g., the key doesn’t exist), sets the default value and writes it to the configuration file.
  4. Writes any default settings to the configuration file if they were not previously present.
  5. Logs the successful loading of configuration settings.
  6. Catches and logs any exceptions that occur during the process, and falls back to default settings if necessary.
- **Why It’s Needed**: Ensures that the setting for treating direct relationships as incestuous is properly configured, providing a key feature for managing in-game relationships.Ensures that the configuration settings are properly loaded and any missing settings are initialized to default values

### Initial Function Call

```python
# call it (function name might be misleading, it doesn't always log lol)
start_logging()
```
- **Purpose**: Initializes logging by calling the `start_logging` function.
- **Why It’s Needed**: Ensures that logging is set up at the start of the script execution, providing immediate logging capabilities.

### Helper Function for Boolean Values

```python
# true and false
def true_false(x):
    if x in [True, 'True', 'true', 'TRUE', 1]:
        return True
    elif x in [False, 'False', 'false', 'FALSE', 0]:
        return False
    else:
        return None
```
- **Purpose**: Converts various representations of boolean values to Python `True` or `False`.
- **How It Works**:
  1. Checks if the input value matches common representations of `True` and returns `True`.
  2. Checks if the input value matches common representations of `False` and returns `False`.
  3. Returns `None` if the input value does not match any known boolean representations.
- **Why It’s Needed**: Provides a utility function to handle boolean values that might be represented in different formats, ensuring consistent boolean handling.

### Comments and Additional Functionality

```python
# services, sims4.commands:
#   @sims4.commands.Command
#   command_type=sims4.commands.CommandType.Live
#   output = sims4.commands.CheatOutput(_connection)
# sims.sim_info_manager:
#   get_sim_info_by_name
# find out what specifically we need from sims.sim_info

# commands break if sim has spaces in their first/last names (e.g. Rhona Pine I)
# overcome with Rhona
```
- **Purpose**: Provides comments and notes on services, commands, and handling Sim names with spaces.
- **Why It’s Needed**: Offers context and reminders for handling specific aspects of the mod, such as command definitions and name handling.

### Comments and Additional Context

```python
# returns the player's locale (for translation stuff)
# @sims4.commands.Command('riv_get_locale', command_type=sims4.commands.CommandType.Live)
# def riv_get_locale(_connection=None):
#    output = sims4.commands.CheatOutput(_connection)
#    output(services.get_locale())

# riv_sim_list and riv_rel_dict will be used if riv_sim_list is not empty!
# for now, sim_x and sim_y in commands MUST be sims that exist in the game

# range(a,b)   = [a, b) \cap ZZ
# range(a,b+1) = [a, b] \cap ZZ
```
- **Purpose**: Provides additional comments and context for functionality related to locale retrieval and Sim existence requirements.
- **Why It’s Needed**: Offers useful reminders and context for developers or users who might be modifying or extending the mod.


### Introduction to Classes

The next part of the file introduces a class `RivSim`, which seems to be used for managing individual Sim data.

### `RivSim` Class

#### Initialization

```python
class RivSim:
    def __init__(self, sim_x):  # will only be created in game, so current time will be readily available
        # creates RivSim from Dict (in json)
        # this code assumes that the keys exist, so make sure you're importing the right thing!
        if isinstance(sim_x, Dict):
            self.sim_id = str(sim_x['sim_id'])  # should be a string anyway
            self.first_name = sim_x['first_name']
            self.last_name = sim_x['last_name']
            self.is_female = true_false(sim_x['is_female'])
            self.is_culled = true_false(sim_x['is_culled'])
            self.time = int(sim_x['time'])
        # creates RivSim from SimInfoParam (in game)
        else:  # elif isinstance(sim_x, SimInfoParam):
            self.sim_id = str(sim_x.sim_id)  # bc json keys need to be strings
            self.first_name = sim_x.first_name
            self.last_name = sim_x.last_name
            self.is_female = sim_x.is_female
            self.is_culled = False
            self.time = services.time_service().sim_now.absolute_ticks()
```
- **Purpose**: Handles the initialization of `RivSim` objects from both dictionaries (imported from JSON) and `SimInfoParam` objects (in-game).
- **How It Works**:
  1. If `sim_x` is a dictionary, initializes attributes from the dictionary values.
  2. Converts boolean values using the `true_false` helper function.
  3. If `sim_x` is a `SimInfoParam` object, initializes attributes directly from the `SimInfoParam` properties.
  4. Sets the `is_culled` attribute to `False` for in-game Sims.
  5. Sets the `time` attribute to the current in-game time.
- **Why It’s Needed**: Provides flexibility in creating `RivSim` objects from different data sources, ensuring compatibility with both saved data and in-game data.

#### String Representations

```python
    def __str__(self):
        return f'<RivSim {self.first_name} {self.last_name} {self.sim_id}>'

    def __repr__(self):
        return str(self)
```
- **Purpose**: Provides string representations for `RivSim` objects.
- **How It Works**:
  1. `__str__` returns a formatted string with the Sim's first name, last name, and ID.
  2. `__repr__` calls `__str__` to provide a representation suitable for debugging.
- **Why It’s Needed**: Improves readability and debugging by providing clear and informative string representations of `RivSim` objects.

#### Conversion to Dictionary

```python
    def to_dict(self):
        return {
            'sim_id': self.sim_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_female': self.is_female,
            'is_culled': self.is_culled,
            'time': self.time
        }
```
- **Purpose**: Converts a `RivSim` object to a dictionary.
- **How It Works**: Returns a dictionary with the Sim's attributes as key-value pairs.
- **Why It’s Needed**: Facilitates the serialization of `RivSim` objects, making it easy to save and load Sim data.


#### Cull Method

```python
    # for marking a sim as culled; do this if the sim cannot be found
    # also removes their marriages
    # TODO: work out why every already culled sim gets culled AGAIN
    def cull(self):
        if not self.is_culled:
            # riv_log(f'marked {self.first_name} {self.last_name} as culled')
            self.is_culled = True
```
- **Purpose**: Marks a Sim as culled (removed or no longer in the game).
- **How It Works**: Sets the `is_culled` attribute to `True` if it is not already set.
- **Why It’s Needed**: Provides a way to mark Sims as culled, which can be used to manage the Sim's status and relationships within the mod.

#### Uncull Method

```python
    # for marking a sim as unculled; for cleaning
    def uncull(self):
        if self.is_culled:
            self.is_culled = False
            riv_log(f'marked {self.first_name} {self.last_name} as unculled')
```
- **Purpose**: Marks a Sim as unculled (restored or back in the game).
- **How It Works**: Sets the `is_culled` attribute to `False` if it is currently set to `True`, and logs the action.
- **Why It’s Needed**: Provides a way to restore Sims who were previously marked as culled, ensuring accurate tracking of Sim status.

#### Update Info Method

```python
    # for updating a sim in the file if that sim exists with different details
    def update_info(self, new_first_name, new_last_name, new_is_female, new_time):
        something_changed = False
        if self.first_name != new_first_name:
            riv_log('updated first name ' + self.first_name + ' to ' + new_first_name)
            self.first_name = new_first_name
            something_changed = True
        if self.last_name != new_last_name:
            riv_log('updated last name ' + self.last_name + ' to ' + new_last_name)
            self.last_name = new_last_name
            something_changed = True
        if self.is_female != new_is_female:
            riv_log('updated gender for ' + self.first_name + ' ' + self.last_name)
            self.is_female = new_is_female
            something_changed = True
        if self.time != new_time:
            self.time = new_time
            something_changed = True
        return something_changed
```
- **Purpose**: Updates a Sim's information if there are changes.
- **How It Works**:
  1. Checks each attribute (`first_name`, `last_name`, `is_female`, `time`) for changes.
  2. Updates the attribute if it has changed and logs the update.
  3. Returns `True` if any changes were made, otherwise returns `False`.
- **Why It’s Needed**: Ensures that Sim information is kept up-to-date, allowing the mod to accurately reflect any changes to Sim details.

### Introduction to `RivSimList` Class

The `RivSimList` class is introduced to manage a list of `RivSim` objects.

#### `RivSimList` Class

```python
class RivSimList:
    sims = []

    def __str__(self):
        return f'<RivSimList - len {len(self.sims)}>'

    def __repr__(self):
        return str(self)
```
- **Purpose**: Represents a list of `RivSim` objects.
- **How It Works**:
  1. Defines a class attribute `sims` to store the list of `RivSim` objects.
  2. Implements `__str__` and `__repr__` methods to provide string representations of the list.
- **Why It’s Needed**: Provides a structured way to manage multiple Sims within the mod.

#### Load Sims Method

```python
    # loads in list of sims from .json
    def load_sims(self, file_name_extra: str):
        file_dir = Path(__file__).resolve().parent.parent
        file_name = f'riv_rel_{file_name_extra}.json'  # e.g. riv_rel_pine.json
        file_name2 = f'riv_currentsession_tmp_{file_name_extra}.json'
        file_path = os.path.join(file_dir, file_name)
        file_path2 = os.path.join(file_dir, file_name2)

        # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
        if os.path.isfile(file_path2):  # if tmp file is already being used
            with open(file_path2, 'r') as json_file:  # read from this
                temp_sims = json.load(json_file)
            self.sims = [RivSim(sim) for sim in temp_sims]
        elif os.path.isfile(file_path):  # tmp file hasn't been created but perm file has
            with open(file_path, 'r') as json_file:  # read from perm file
                temp_sims = json.load(json_file)
            if use_currentsession_files:
                riv_log('creating temporary file in .load_sims for ' + file_name_extra)
                with open(file_path2, 'w') as json_file2:  # create tmp file
                    json.dump(temp_sims, json_file2)
            self.sims = [RivSim(sim) for sim in temp_sims]
        return self.sims
```
- **Purpose**: Converts the loaded Sims from JSON to `RivSim` objects and returns the list.
- **How It Works**:
  1. Checks if the temporary file exists and loads Sims from it if available.
  2. If the temporary file does not exist but the permanent file does, it loads Sims from the permanent file.
  3. Optionally creates a temporary file if the `use_currentsession_files` flag is set.
- **Why It’s Needed**: Ensures flexibility in loading Sim data from different sources, supporting both persistent and session-specific data.the final step in loading Sims, ensuring the `RivSimList` is populated and ready for use.

#### Clear Sims Method

```python
    def clear_sims(self):
        self.sims = []
```
- **Purpose**: Clears the list of Sims.
- **Why It’s Needed**: Provides a way to reset the list, useful for managing the state of the `RivSimList`.


### Introduction to `RivRelDict` Class

The `RivRelDict` class is introduced to manage relationships between Sims.

#### `RivRelDict` Class

```python
class RivRelDict:
    rels = {}  # sim_id: [parent_ids]

    def __str__(self):
        return f'<RivRelDict - len {len(list(self.rels.keys()))}>'

    def __repr__(self):
        return str(self)
```
- **Purpose**: Represents a dictionary of relationships between Sims, mapping each Sim ID to a list of parent IDs.
- **How It Works**:
  1. Defines a class attribute `rels` to store relationships.
  2. Implements `__str__` and `__repr__` methods to provide string representations of the dictionary.
- **Why It’s Needed**: Provides a structured way to manage and represent relationships within the mod.

#### Load Relationships Method

```python
    # loads in dict of rels from .json
    def load_rels(self, file_name_extra: str):
        file_dir = Path(__file__).resolve().parent.parent
        file_name = f'riv_relparents_{file_name_extra}.json'  # e.g. riv_rel_pine.json
        file_name2 = f'riv_currentsession_tmpparents_{file_name_extra}.json'  # e.g. riv_currentsession_tmp_pine.json
        file_path = os.path.join(file_dir, file_name)
        file_path2 = os.path.join(file_dir, file_name2)

        # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
        if os.path.isfile(file_path2):  # if tmp file is already being used
            with open(file_path2, 'r') as json_file:
                self.rels = json.load(json_file)
            elif os.path.isfile(file_path):  # tmp file hasn't been created but perm file has
                # perm file exists
                with open(file_path, 'r') as json_file:
                    self.rels = json.load(json_file)
                if use_currentsession_files:
                    riv_log('creating temporary file in .load_rels for ' + file_name_extra)
                    with open(file_path2, 'w') as json_file2:
                        json.dump(self.rels, json_file2)
            return self.rels
```
- **Purpose**: Loads relationships from JSON file.
- **How It Works**:
  1. Defines the directory and file names for loading relationships.
  2. Attempts to read the primary and secondary JSON files and parse them into the `rels` dictionary.
  3. If the temporary file exists, loads relationships from it.
  4. If the temporary file does not exist but the permanent file does, loads relationships from the permanent file and optionally creates a temporary file.
  5. Returns the loaded relationships.
- **Why It’s Needed**: Ensures that the mod can load and manage relationships from saved data, supporting persistent and session-specific data. Provides flexibility in loading relationship data from different sources, supporting both persistent and session-specific data.

#### Clear Relationships Method

```python
    def clear_rels(self):
        self.rels = {}
```
- **Purpose**: Clears the relationships dictionary.
- **Why It’s Needed**: Provides a way to reset the relationships, useful for managing the state of the `RivRelDict`.

### Comments and Context

```python
# this is within class Zone in simulation/zone.py
#
#     def on_households_and_sim_infos_loaded(self):
#         self._set_zone_state(zone_types.ZoneState.HOUSEHOLDS_AND_SIM_INFOS_LOADED)
#         object_preference_tracker = services.object_preference_tracker()
#         if object_preference_tracker is not None:
#             object_preference_tracker.convert_existing_preferences()
#
# maybe use for replacing code to run on zone spin up as
```
- **Purpose**: Provides comments and context for potential integration points within the Sims 4 game engine.
- **Why It’s Needed**: Offers useful reminders and context for developers or users who might be modifying or extending the mod.

### Global Instances and Helper Functions

#### Creating Empty Lists

```python
# creates empty lists
# this will store sims as RivSims and rels as a dict with sim_id: [parent_id1, parent_id2]
riv_sim_list = RivSimList()
riv_rel_dict = RivRelDict()
```
- **Purpose**: Initializes global instances of `RivSimList` and `RivRelDict`.
- **Why It’s Needed**: Provides a centralized place to manage all Sims and their relationships within the mod.

#### Helper Functions for Pairing Lists

```python
# get list of pairs in lists
def get_pairs_yield(a: List, b: List):
    for x in a:
        for y in b:
            yield x, y

def get_pairs_return(a: List, b: List):
    ab = []
    for x in a:
        for y in b:
            ab.append((x, y))
    return ab
```
- **Purpose**: Provides functions to generate pairs of elements from two lists.
- **How It Works**:
  1. `get_pairs_yield`: Uses a generator to yield pairs of elements from lists `a` and `b`.
  2. `get_pairs_return`: Creates and returns a list of pairs of elements from lists `a` and `b`.
- **Why It’s Needed**: Useful for operations that require pairwise comparisons or combinations of elements from two lists.

### Console Commands

#### Show Relationship Bits Command

```python
# input: two sims. output: list of relbits
@sims4.commands.Command('riv_show_relbits', command_type=sims4.commands.CommandType.Live)
def console_show_relbits(sim_x: SimInfoParam, sim_y: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    relbits = services.relationship_service().get_all_bits(sim_x.sim_id, sim_y.sim_id)
    output(str(relbits))
```
- **Purpose**: Console command to show the relationship bits between two Sims.
- **How It Works**:
  1. Takes two Sims as input.
  2. Retrieves and displays all relationship bits between the two Sims.
- **Why It’s Needed**: Provides a way for players or developers to inspect the relationship bits between two Sims for debugging or informational purposes.

#### Get RivSim by Sim ID

```python
# input: a sim ID as Int or String. output: the corresponding RivSim in mem
def get_riv_sim_by_id(sim_id):
    for sim in riv_sim_list.sims:
        if sim.sim_id == str(sim_id):
            return sim
    return None
```
- **Purpose**: Retrieves a `RivSim` object by its Sim ID.
- **How It Works**:
  1. Iterates through the list of `RivSim` objects.
  2. Returns the `RivSim` object that matches the given Sim ID.
- **Why It’s Needed**: Provides a utility function to fetch `RivSim` objects based on their Sim ID, facilitating various operations within the mod.

### Helper Functions for Retrieving `RivSim` Objects

#### Get `RivSim` by Sim ID (Extended)

```python
def get_rivsim_from_id(sim_id):
    if isinstance(sim_id, int):  # if the ID is an integer
        return get_rivsim_from_id(str(sim_id))  # calls the function again but with sim_id as string
    else:
        for rivsim in riv_sim_list.sims:  # for all rivsims
            if rivsim.sim_id == sim_id:  # if it has the same ID
                return rivsim  # then this is the rivsim we want

        # has not found that rivsim, so we make it
        rivsim = RivSim(services.sim_info_manager().get(int(sim_id)).sim_info)
        riv_sim_list.sims.append(rivsim)
        return rivsim
```
- **Purpose**: Retrieves a `RivSim` object by its Sim ID, creating a new one if it doesn't exist.
- **How It Works**:
  1. Converts integer Sim IDs to strings and calls itself recursively.
  2. Searches the list of `RivSim` objects for a matching Sim ID.
  3. If no matching `RivSim` is found, creates a new `RivSim` from the Sim information and adds it to the list.
- **Why It’s Needed**: Provides a robust way to fetch or create `RivSim` objects, ensuring that the mod can always access the necessary Sim data.

#### Get `RivSim` by Sim Object

```python
# input: a sim as SimInfoParam or RivSim. output: the corresponding RivSim in mem
# updates the name if needed, adds rivsim if needed
def get_rivsim_from_sim(sim_z):
    try:
        if isinstance(sim_z, RivSim):  # if this is a rivsim
            return sim_z  # then just return the rivsim
        else:  # this will be a SimInfoParam
            rivsim_z = get_rivsim_from_id(str(sim_z.sim_id))
            sim_time = services.time_service().sim_now.absolute_ticks()

            if rivsim_z is None:
                rivsim_z = RivSim(sim_z)
                riv_sim_list.sims.append(rivsim_z)
                riv_log(f'get_rivsim_from_sim created a rivsim for {sim_z.first_name} {sim_z.last_name}')
                # fill in parent list
                riv_rel_dict.rels[str(rivsim_z.sim_id)] = [parent.sim_id for parent in get_parents_ingame(sim_z)]
            else:
                rivsim_z.update_info(sim_z.first_name, sim_z.last_name, sim_z.is_female, sim_time)

            return rivsim_z  # so we get rivsim from the id
    except Exception as e:
        riv_log(f'get_rivsim_from_sim error: {e}')
        return None
```
- **Purpose**: Handles cases where the `RivSim` object does not exist, creating a new one if necessary.
- **How It Works**:
  1. If no `RivSim` is found, creates a new one from the Sim object and adds it to the list.
  2. Logs the creation of the new `RivSim`.
  3. Fills in the parent list for the new `RivSim`.
  4. If a `RivSim` is found, updates its information.
  5. Returns the `RivSim`.
- **Why It’s Needed**: Ensures that all Sims are represented as `RivSim` objects and that their relationships are accurately tracked.

### Additional Helper Functions

#### Get Sim Object from `RivSim`

```python
# input: a rivsim or sim. output: the corresponding sim info if it exists, else None
def get_sim_from_rivsim(rivsim_z):
    try:
        sim_z = services.sim_info_manager().get(int(rivsim_z.sim_id))
        if sim_z is not None:
            return sim_z.sim_info
        else:
            return None
    except Exception as e:
        riv_log(f'get_sim_from_rivsim error: {e}')
        return None
```
- **Purpose**: Retrieves the corresponding Sim object from a `RivSim` object if it exists.
- **How It Works**:
  1. Uses the Sim ID to get the Sim object from the Sim info manager.
  2. Returns the Sim info if it exists, otherwise returns `None`.
  3. Logs any errors encountered.
- **Why It’s Needed**: Provides a way to fetch the in-game Sim object corresponding to a `RivSim`, facilitating further operations that require access to the Sim’s full information.

#### Get Parents In-Game

```python
# gets parents, but only the sim infos in the game, going via parent relbits
def get_parents_ingame(sim_x):
    sim_parents = []
    sim_x = get_sim_from_rivsim(sim_x)

    if sim_x is None:
        return sim_parents

    manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
    parent_relbit = manager.get(0x2269)
    for sim_y in services.sim_info_manager().get_all():
        if sim_x.relationship_tracker.has_bit(sim_y.sim_id, parent_relbit):
            sim_parents.append(sim_y)

    # remove list elements that are NOT sim infos (bc apparently this happens???)
    for parent in sim_parents:
        if not isinstance(parent, SimInfo):
            sim_parents.remove(parent)

    return sim_parents
```
- **Purpose**: Retrieves the in-game parents of a given Sim by checking relationship bits.
- **How It Works**:
  1. Converts the input to a Sim object.
  2. Uses the relationship tracker to find Sims that have a parent relationship bit with the given Sim.
  3. Removes any non-SimInfo objects from the parent list.
- **Why It’s Needed**: Provides a way to find a Sim's parents based on in-game data, ensuring the mod can accurately track relationships.

#### Get Parents

```python
# input: a sim. output: list of their parents
def get_parents(sim_x):
    # try ingame ones first
    ingame_parents = get_parents_ingame(sim_x)

    # sort out sim_x as a rivsim
    rivsim_x = get_rivsim_from_sim(sim_x)  # rivsim_x is the entry for sim_x in riv_sim_list.sims
    if rivsim_x is None:  # TODO: remove this section
        rivsim_x = RivSim(sim_x)
        riv_sim_list.sims.append(RivSim(sim_x))
        riv_log(f'get_parents added sim {sim_x.first_name} {sim_x.last_name} to riv_sim_list.sims')
        # not a rivsim => won't have a rel => need to set up
        riv_rel_dict.rels[str(rivsim_x.sim_id)] = [int(parent.sim_id) for parent in ingame_parents]
    x_id = rivsim_x.sim_id  # and this is the ID as a string

    # now we build this list as rivsims
    sim_parents = []
    # sort out parents sim_y as rivsims, grabbing them from the dict entry
    for y_id in riv_rel_dict.rels.get(x_id):  # for each y_id in the list of sim_x's parents
        # {x_id: [y_id,...]}
        rivsim_y = get_rivsim_from_id(y_id)  # get rivsim_y as a rivsim
        # if there is no rivsim for this sim, create one
        if rivsim_y is None:
            sim_y = services.sim_info_manager().get(y_id).sim_info
            rivsim_y = RivSim(sim_y)
            riv_sim_list.sims.append(rivsim_y)
        sim_parents.append(rivsim_y)
    return sim_parents
```
- **Purpose**: Retrieves the parents of a given Sim, ensuring both in-game and mod-specific data are considered.
- **How It Works**:
  1. Ensures the input is converted to a `RivSim` object.
  2. Checks if the `RivSim` object exists and creates one if necessary, adding it to the `riv_sim_list`.
  3. Initializes the parent list using in-game parents and converts them to `RivSim` objects.
  4. Builds the parent list from the dictionary entry of relationships, converting parent IDs to `RivSim` objects.
  5. Returns the list of parent `RivSim` objects.
- **Why It’s Needed**: Combines in-game data with the mod's data structures to provide a comprehensive view of a Sim's parents, ensuring accurate relationship tracking.

#### Console Command for Getting Parents

```python
# the above as a console command
@sims4.commands.Command('riv_get_parents', command_type=sims4.commands.CommandType.Live)
def console_get_parents(sim_x: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    sim_parents = get_parents(sim_x)
    if not sim_parents:
        output(p(rrs.get_parents_0).format(x_firstname=sim_x.first_name))
    else:
        for sim_y in sim_parents:
            output(p(rrs.get_parents_1, sim_y.is_female)
                   .format(y_firstname=sim_y.first_name, y_lastname=sim_y.last_name, x_firstname=sim_x.first_name))
```
- **Purpose**: Provides a console command to get the parents of a given Sim.
- **How It Works**:
  1. Retrieves the parents using the `get_parents` function.
  2. Outputs a message if no parents are found.
  3. If parents are found, outputs their names.
- **Why It’s Needed**: Provides an easy way for players or developers to check a Sim's parents using the in-game console, facilitating debugging and gameplay.

#### Get Children In-Game

```python
# gets children, but only the sim infos in the game, going via child relbits
def get_children_ingame(sim_x):
    sim_children = []
    sim_x = get_sim_from_rivsim(sim_x)

    if sim_x is None:
        return sim_children

    manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
    parent_relbit = manager.get(0x2269)
    for sim_y in services.sim_info_manager().get_all():
        if sim_y.relationship_tracker.has_bit(sim_x.sim_id, parent_relbit):
            sim_children.append(sim_y)

    # remove list elements that are NOT sim infos (bc apparently this happens???)
    for child in sim_children:
        if not isinstance(child, SimInfo):
            sim_children.remove(child)

    return sim_children
```
- **Purpose**: Retrieves the in-game children of a given Sim by checking relationship bits.
- **How It Works**:
  1. Converts the input to a Sim object.
  2. Uses the relationship tracker to find Sims that have a child relationship bit with the given Sim.
  3. Removes any non-SimInfo objects from the children list.
- **Why It’s Needed**: Provides a way to find a Sim's children based on in-game data, ensuring the mod can accurately track relationships.

#### Get Children

```python
# also adds all sims concerned as rivsims if needed
def get_children(sim_x):
    # try ingame ones first
    ingame_children = get_children_ingame(sim_x)

    # sort out sim_x as a rivsim
    rivsim_x = get_rivsim_from_sim(sim_x)  # rivsim_x is the entry for sim_x in riv_sim_list.sims
    if rivsim_x is None:  # TODO: remove this section
        rivsim_x = RivSim(sim_x)
        riv_sim_list.sims.append(RivSim(sim_x))
        riv_log('get_children added sim {} {} to riv_sim_list.sims'.format(sim_x.first_name, sim_x.last_name))
    x_id = rivsim_x.sim_id  # and this is the ID as a string

    # now we build this list as rivsims
    # grab ingame kids
    sim_children = []
    for y_id in [str(child.sim_id) for child in ingame_children]:  # for each y_id in the list of sim_x's children
        rivsim_y = get_rivsim_from_id(y_id)  # get rivsim_y as a rivsim
        # if there is no rivsim for this sim, create one
        if rivsim_y is None:
            sim_y = services.sim_info_manager().get(y_id).sim_info
            rivsim_y = RivSim(sim_y)
            riv_sim_list.sims.append(rivsim_y)
            riv_log('get_children added sim {} {} to riv_sim_list.sims'.format(sim_y.first_name, sim_y.last_name))
            riv_rel_dict.rels[str(rivsim_y.sim_id)] = [int(parent.sim_id) for parent in get_parents(rivsim_y)]
        sim_children.append(rivsim_y)  # then add rivsim_y to the list

    # grab ones in rel dict
    for rivsim_y in riv_sim_list.sims:  # for every known rivsim
        y_id = rivsim_y.sim_id  # get their ID as a string
        y_parents = riv_rel_dict.rels.get(y_id)  # and this is a list of parent simIDs as ints
        if y_parents is not None:
            for z_id in y_parents:  # for each z_id
                if int(z_id) == int(x_id) and rivsim_y not in sim_children:  # same id, and this child has been counter
                    sim_children.append(rivsim_y)

    return sim_children
```
- **Purpose**: Retrieves the children of a given Sim, ensuring both in-game and mod-specific data are considered.
- **How It Works**:
  1. Attempts to get the in-game children first.
  2. Ensures the input is converted to a `RivSim` object.
  3. Checks if the `RivSim` object exists and creates one if necessary, adding it to the `riv_sim_list`.
  4. Initializes the children list using in-game children and converts them to `RivSim` objects.
  5. Builds the children list from the dictionary entry of relationships, converting child IDs to `RivSim` objects.
  6. Iterates through the list of `RivSim` objects.
  7. Checks if each `RivSim` object is a child of the given Sim by comparing parent IDs.
  8. Adds the `RivSim` object to the children list if it matches and isn't already in the list.
  9. Returns the list of child `RivSim` objects.
- **Why It’s Needed**: Combines in-game data with the mod's data structures to provide a comprehensive view of a Sim's children, ensuring accurate relationship tracking.

#### Console Command for Getting Children

```python
# the above as a console command
@sims4.commands.Command('riv_get_children', command_type=sims4.commands.CommandType.Live)
def console_get_children(sim_x: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    sim_children = get_children(sim_x)
    if not sim_children:
        output(p(rrs.get_children_0).format(x_firstname=sim_x.first_name))
    else:
        for sim_y in sim_children:
            output(p(rrs.get_children_1, sim_y.is_female)
                   .format(y_firstname=sim_y.first_name, y_lastname=sim_y.last_name, x_firstname=sim_x.first_name))
```
- **Purpose**: Provides a console command to get the children of a given Sim.
- **How It Works**:
  1. Retrieves the children using the `get_children` function.
  2. Outputs a message if no children are found.
  3. If children are found, outputs their names.
- **Why It’s Needed**: Provides an easy way for players or developers to check a Sim's children using the in-game console, facilitating debugging and gameplay.

#### Get Ancestors

```python
# input: a sim. output: dictionary of their ancestors sim_z with values (gens back, via child of sim_z)
# note the values are lists!!
# look into defaultdict later to rework adding items to the list
def get_ancestors(sim_x):
    ancestors = {}  # stores ancestors as {sim_z: [(n, sim_zx), (n, sim_zx)]} where
    # sim_z is n generations back from sim_x
    # sim_zx child of sim_z and ancestor of sim_x
    queue = []  # stores sims to check

    if riv_sim_list.sims:  # using list in mem
        sim_x = get_rivsim_from_sim(sim_x)  # rivsim_x is the entry for sim_x in riv_sim_list.sims

    for sim_z in get_parents(sim_x):
        queue.append((sim_z, 1, sim_x))
    while queue:
        tuple_znzx = queue[0]  # gets first (sim_z, n, sim_zx)
        sim_z = tuple_znzx[0]
        n = tuple_znzx[1]
        sim_zx = tuple_znzx[2]
        queue.pop(0)  # removes first item (tuple_znzx) from the queue
        for parent in get_parents(sim_z):
            queue.append((parent, n + 1, sim_z))  # adds parents of sim_z to the queue
        if sim_z in ancestors.keys():
            temp_list = ancestors[sim_z]
            temp_list.append((n, sim_zx))
            ancestors[sim_z] = temp_list.copy()
        else:
            ancestors[sim_z] = [(n, sim_zx)]  # adds sim_z: [(n, sim_zx)] to the dictionary
    return ancestors  # dictionary of sim_z: (n, sim_zx) for sim_z ancestor, n gens back, via sim_zx
```
- **Purpose**: Retrieves the ancestors of a given Sim.
- **How It Works**:
  1. Initializes an empty dictionary to store ancestors.
  2. Uses a queue to manage Sims to check for ancestors.
  3. Iteratively retrieves parents and adds them to the queue with generation information.
  4. Updates the ancestors dictionary with new ancestor data.
  5. Returns the complete ancestors dictionary.
- **Why It’s Needed**: Provides a comprehensive view of a Sim's ancestry, ensuring the mod can accurately track and display genealogical data.

#### Get Ancestors In-Game

```python
# input: a sim. output: dictionary of their ancestors sim_z with values (gens back, via child of sim_z)
# note the values are lists!!
# look into defaultdict later to rework adding items to the list
def get_ancestors_ingame(sim_x):
    ancestors = {}  # stores ancestors as {sim_z: [(n, sim_zx), (n, sim_zx)]} where
    # sim_z is n generations back from sim_x
    # sim_zx child of sim_z and ancestor of sim_x
    queue = []  # stores sims to check

    if isinstance(sim_x, RivSim):
        sim_x = get_sim_from_rivsim(sim_x)
    if sim_x is None:
        return {}

    try:
        for sim_z in get_parents_ingame(sim_x):
            queue.append((sim_z, 1, sim_x))
        while queue:
            tuple_znzx = queue[0]  # gets first (sim_z, n, sim_zx)
            sim_z = tuple_znzx[0]
            n = tuple_znzx[1]
            sim_zx = tuple_znzx[2]
            queue.pop(0)  # removes first item (tuple_znzx) from the queue
            for parent in get_parents_ingame(sim_z):
                queue.append((parent, n + 1, sim_z))  # adds parents of sim_z to the queue
            if sim_z in ancestors.keys():
                temp_list = ancestors[sim_z]
                temp_list.append((n, sim_zx))
                ancestors[sim_z] = temp_list.copy()
            else:
                ancestors[sim_z] = [(n, sim_zx)]  # adds sim_z: [(n, sim_zx)] to the dictionary
    except Exception as e:
        riv_log(f'get_ancestors error: {e}')
    return ancestors  # dictionary of sim_z: (n, sim_zx) for sim_z ancestor, n gens back, via sim_zx
```
- **Purpose**: Retrieves the in-game ancestors of a given Sim.
- **How It Works**:
  1. Similar to `get_ancestors` but focuses on in-game data.
  2. Uses a queue to manage Sims to check for ancestors.
  3. Iteratively retrieves parents and adds them to the queue with generation information.
  4. Populates the ancestors dictionary with new ancestor data.
  5. Catches and logs any exceptions encountered.
  6. Returns the complete ancestors dictionary.
- **Why It’s Needed**: Provides a way to find a Sim's ancestors based on in-game data, ensuring the mod can accurately track and display genealogical data.

#### Convert `RivSim` Objects to Sim Objects

```python
# get list of sims/rivsims, turn into list of sims
def rivsims_to_sims(rivsims):
    return [get_sim_from_rivsim(rivsim) for rivsim in rivsims if not (isinstance(rivsim, RivSim) and rivsim.is_culled)]
```
- **Purpose**: Converts a list of `RivSim` objects to a list of Sim objects.
- **How It Works**:
  1. Iterates through the list of `RivSim` objects.
  2. Converts each `RivSim` object to a Sim object using `get_sim_from_rivsim`.
  3. Excludes any `RivSim` objects that are culled.
- **Why It’s Needed**: Provides a utility to convert `RivSim` objects back to their corresponding Sim objects, facilitating further operations that require access to the full Sim data.

#### Console Command for Getting Ancestors

```python
# the above as a console command. redundant except for debugging
@sims4.commands.Command('riv_get_ancestors', command_type=sims4.commands.CommandType.Live)
def console_get_ancestors(sim_x: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    x_ancestors = get_ancestors(sim_x)
    if not x_ancestors:
        output(p(rrs.get_ancestors_0).format(x_firstname=sim_x.first_name))
    else:
        for sim_y in x_ancestors.keys():
            for sim_z in x_ancestors[sim_y]:
                if sim_z[0] == 1:
                    output(p(rrs.get_ancestors_1, sim_z[1].is_female)
                           .format(y_firstname=sim_y.first_name, y_lastname=sim_y.last_name,
                                   z_firstname=sim_z[1].first_name, z_lastname=sim_z[1].last_name,
                                   x_firstname=sim_x.first_name))
                else:
                    output(p(rrs.get_ancestors_2, sim_z[1].is_female)
                           .format(y_firstname=sim_y.first_name, y_lastname=sim_y.last_name,
                                   z_firstname=sim_z[1].first_name, z_lastname=sim_z[1].last_name,
                                   x_firstname=sim_x.first_name, n=sim_z[0]))
```
- **Purpose**: Provides a console command to get the ancestors of a given Sim.
- **How It Works**:
  1. Retrieves the ancestors using the `get_ancestors` function.
  2. Outputs a message if no ancestors are found.
  3. If ancestors are found, outputs their names and generation information.
- **Why It’s Needed**: Provides an easy way for players or developers to check a Sim's ancestors using the in-game console, facilitating debugging and gameplay.

#### Get Descendants

```python
# input: a sim. output: dictionary of their descendants sim_z with values (gens back, via child of sim_z)
# note the values are lists!!
# look into defaultdict later to rework adding items to the list
def get_descendants(sim_x):
    descendants = {}  # stores descendants as {sim_z: [(n, sim_zx), (n, sim_zx)]} where
    # sim_z is n generations back from sim_x
    # sim_zx child of sim_z and descendant of sim_x
    queue = []  # stores sims to check

    if riv_sim_list.sims:  # using list in mem
        sim_x = get_rivsim_from_sim(sim_x)  # rivsim_x is the entry for sim_x in riv_sim_list.sims

    for sim_z in get_children(sim_x):
        queue.append((sim_z, 1, sim_x))
    while queue:
        tuple_znzx = queue[0]  # gets first (sim_z, n, sim_zx)
        sim_z = tuple_znzx[0]
        n = tuple_znzx[1]
        sim_zx = tuple_znzx[2]
        queue.pop(0)  # removes first item (tuple_znzx) from the queue
        for child in get_children(sim_z):
            queue.append((child, n + 1, sim_z))  # adds children of sim_z to the queue
        if sim_z in descendants.keys():
            temp_list = descendants[sim_z]
            temp_list.append((n, sim_zx))
            descendants[sim_z] = temp_list.copy()
        else:
            descendants[sim_z] = [(n, sim_zx)]

    return descendants
```
- **Purpose**: Retrieves the descendants of a given Sim.
- **How It Works**:
  1. Initializes an empty dictionary to store descendants.
  2. Uses a queue to manage Sims to check for descendants.
  3. Iteratively retrieves children and adds them to the queue with generation information.
  4. Populates the descendants dictionary with generation information.
- **Why It’s Needed**: Provides a comprehensive view of a Sim's descendants, ensuring the mod can accurately track and display genealogical data.

#### Console Command for Getting Descendants

```python
# the above as a console command. redundant except for debugging
@sims4.commands.Command('riv_get_descendants', command_type=sims4.commands.CommandType.Live)
def console_get_descendants(sim_x: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    x_descendants = get_descendants(sim_x)
    if not x_descendants:
        output(p(rrs.get_descendants_0).format(x_firstname=sim_x.first_name))
    else:
        for sim_y in x_descendants.keys():
            for sim_z in x_descendants[sim_y]:
                if sim_z[0] == 1:
                    output(p(rrs.get_descendants_1, sim_y.is_female)
                           .format(y_firstname=sim_y.first_name, y_lastname=sim_y.last_name,
                                   x_firstname=sim_x.first_name, x_lastname=sim_x.last_name, n=sim_z[0]))
                else:
                    output(p(rrs.get_descendants_2, sim_y.is_female)
                           .format(y_firstname=sim_y.first_name, y_lastname=sim_y.last_name,
                                   x_firstname=sim_x.first_name, x_lastname=sim_x.last_name, n=sim_z[0]))

```
- **Purpose**: Provides a console command to get the descendants of a given Sim.
- **How It Works**:
  1. Retrieves the descendants using the `get_descendants` function.
  2. Outputs a message if no descendants are found.
  3. If descendants are found, outputs their names and generation information.
  4. Updates the descendants dictionary with new descendant data.
  5. Catches and logs any exceptions encountered.
  6. Returns the complete descendants dictionary.
- **Why It’s Needed**: Provides an easy way for players or developers to check a Sim's descendants using the in-game console, facilitating debugging and gameplay.

#### Get Direct Relationship

```python
# input: two sims and ancestors. output: [] if there is no direct relation, generational difference if there is
def get_direct_rel(sim_x, sim_y, x_ancestors, y_ancestors):
    xy_direct_rels = []

    if riv_sim_list.sims:
        sim_x = get_rivsim_from_sim(sim_x)
        sim_y = get_rivsim_from_sim(sim_y)

    if not (sim_x is None or sim_y is None):
        if sim_x.sim_id == sim_y.sim_id:  # same sim
            riv_log(sim_x.sim_id + ' ' + sim_y.sim_id)
            xy_direct_rels.append(0)
        if sim_y in x_ancestors.keys():  # sim_y is a direct ancestor of sim_x
            for sim_z in x_ancestors[sim_y]:
                xy_direct_rels.append(sim_z[0])  # gets each n from {sim_y: [sim_z = (n, sim_yx), (n, sim_yx), ...]}
        if sim_x in y_ancestors.keys():  # sim_x is a direct ancestor of sim_y
            for sim_z in y_ancestors[sim_x]:
                xy_direct_rels.append(-sim_z[0])  # gets each -n from {sim_x: [sim_z = (n, sim_xy), (n, sim_xy), ...]}

        riv_log(f'[get direct rel {sim_x.first_name} {sim_y.first_name}] {xy_direct_rels}', 3)

    # order the rels by magnitude
    xy_direct_rels.sort(key=abs)

    return xy_direct_rels

```
- **Purpose**: Determines the direct relationship between two Sims, including generational differences.
- **How It Works**:
  1. Converts the inputs to `RivSim` objects if necessary.
  2. Checks if the two Sims are the same.
  3. Checks if one Sim is a direct ancestor of the other and records the generational difference with a negative sign.
  4. Logs the relationship details.
  5. Sorts the relationships by their absolute magnitude.
  6. Returns the sorted list of generational differences.
- **Why It’s Needed**: Provides a way to determine direct relationships between two Sims, which is important for tracking genealogy.

#### Get Direct Relation Wrapper

```python
# ... -1 => sim_x child of sim_y, 0 => sim_x is sim_y, 1 => sim_x parent of sim_y, ...

# input: two sims. output: [] if there is no direct relation, generational difference if there is
def get_direct_relation(sim_x: SimInfoParam, sim_y: SimInfoParam):
    return get_direct_rel(sim_x, sim_y, get_ancestors(sim_x), get_ancestors(sim_y))
```
- **Purpose**: Provides a wrapper function for `get_direct_rel` to directly retrieve the relationship between two Sims.
- **How It Works**:
  1. Calls `get_direct_rel` with the ancestors of both Sims.
  2. Returns the result.
- **Why It’s Needed**: Simplifies the process of retrieving direct relationships between two Sims by encapsulating the ancestor retrieval process.

### Format Direct Relationship with Gender

```python
# input: a number and sim_x's gender. output: sim_x's relation to sim_y
# gens = xy_direct_rels
# gender bit is for compatibility with inlaw rels
def format_direct_rel_gender(gens: List, gender: int):
    gens_str = rrs.direct(gens, gender)
    riv_log(f'formatted direct rel: {gens_str}', 3)
    return gens_str
```
- **Purpose**: Formats the direct relationship between two Sims, considering gender.
- **How It Works**:
  1. Uses the `rrs.direct` function to format the generational differences with gender considerations.
  2. Logs the formatted relationship.
  3. Returns the formatted relationship string.
- **Why It’s Needed**: Provides a way to present direct relationships between Sims in a gender-aware manner, enhancing the clarity and accuracy of relationship descriptions.

#### Format Direct Relationship

```python
def format_direct_rel(gens: List, sim_x: SimInfoParam):
    return format_direct_rel_gender(gens, sim_x.is_female)
```
- **Purpose**: Formats the direct relationship between two Sims based on generational differences and the gender of `sim_x`.
- **How It Works**:
  1. Calls `format_direct_rel_gender` with the generational differences and the gender of `sim_x`.
  2. Returns the formatted relationship string.
- **Why It’s Needed**: Provides a utility to format direct relationships, simplifying the process of generating relationship descriptions.

### Console Command for Direct Relationship

```python
# direct relation as a console command
@sims4.commands.Command('riv_get_direct_rel', command_type=sims4.commands.CommandType.Live)
def console_get_direct_rel(sim_x: SimInfoParam, sim_y: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    if sim_x is not None:
        if sim_y is not None:
            xy_direct_rels = get_direct_relation(sim_x, sim_y)
            if not xy_direct_rels:  # there is no direct relation, list is empty
                output(p(rrs.get_direct_rel_0)
                       .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name))
            else:
                xy_direct_rel_str = format_direct_rel(xy_direct_rels, sim_x)
                for xy_rel in xy_direct_rel_str:
                    output(p(rrs.get_direct_rel_1, sim_x.is_female)
                           .format(y_firstname=sim_y.first_name, y_lastname=sim_y.last_name,
                                   x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                                   direct_rel=xy_rel))
```
- **Purpose**: Provides a console command to get the direct relationship between two Sims.
- **How It Works**:
  1. Retrieves the direct relationship using the `get_direct_relation` function.
  2. Outputs a message if no direct relationship is found.
  3. If a direct relationship is found, formats and outputs the relationship description.
- **Why It’s Needed**: Allows players or developers to easily check the direct relationship between two Sims using the in-game console, facilitating debugging and gameplay.

#### Get Sibling Strength

```python
# input: two sims. output: the strength of their siblinghood
# 0 if not sibs, 0.5 if half-sibs, 1 if full sibs (or undetermined bc parents don't exist)
def get_sib_strength(sim_x: SimInfoParam, sim_y: SimInfoParam):
    x_parents = get_parents(sim_x)
    y_parents = get_parents(sim_y)
    z_parents = [value for value in x_parents if value in y_parents]  # intersection of list
    if riv_sim_list.sims:  # if using riv_sim_list
        if len(z_parents) == 2:  # two shared parents
            return 1  # if x and y share two parents, they are full siblings.
        elif len(z_parents) == 1:  # one shared parent
            if len(x_parents) == 1 and len(y_parents) == 1:
                return 1  # if x and y only have one parent and it is the same sim, ASSUME they are full siblings
            return 0.5  # if x has one parent and y has two parents, sharing one, they are half siblings
            # if x and y each have two parents and only share one, they are half siblings
        else:  # no shared parents
            if len(x_parents) == 0 and len(y_parents) == 0:
                return 1  # if they have the sibling rel bit and neither has parents, ASSUME they are full siblings
            return 0.5  # x or y may or may not have parents, x and y have sibling rel bit
    else:
        manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
        sibling_relbit = manager.get(0x2262)
        if sim_x.relationship_tracker.has_bit(sim_y.sim_id, sibling_relbit):
            if len(z_parents) == 2:  # two shared parents
                return 1  # if x and y share two parents, they are full siblings.
            elif len(z_parents) == 1:  # one shared parent
                if len(x_parents) == 1 and len(y_parents) == 1:
                    return 1  # if x and y only have one parent and it is the same sim, ASSUME they are full siblings
                return 0.5  # if x has one parent and y has two parents, sharing one, they are half siblings
                # if x and y each have two parents and only share one, they are half siblings
            else:  # no shared parents
                if len(x_parents) == 0 and len(y_parents) == 0:
                    return 1  # if they have the sibling rel bit and neither has parents, ASSUME they are full siblings
                return 0.5  # x or y may or may not have parents, x and y have sibling rel bit
        return 0

```
- **Purpose**: Determines the strength of siblinghood between two Sims.
- **How It Works**:
  1. Retrieves the parents of both Sims.
  2. Checks the intersection of the parents lists to find common parents.
  3. Returns 1 if they share two parents (full siblings), 0.5 if they share one parent (half-siblings), and 0 if they share no parents (not siblings).
- **Why It’s Needed**: Provides a way to determine the sibling relationship between two Sims, which is important for tracking family relationships.

### Console Command for Sibling Strength

```python
# the above as a console command
@sims4.commands.Command('riv_get_sib_strength', command_type=sims4.commands.CommandType.Live)
def console_get_sib_strength(sim_x: SimInfoParam, sim_y: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    sib_strength = get_sib_strength(sim_x, sim_y)
    if sim_x == sim_y:
        output(p(rrs.get_sib_strength_self)
               .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name))
    elif sib_strength == 1:
        output(p(rrs.get_sib_strength_full, sim_x.is_female and sim_y.is_female)
               .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name))
    elif sib_strength == 0.5:
        output(p(rrs.get_sib_strength_half, sim_x.is_female and sim_y.is_female)
               .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name))
    elif sib_strength == 0:
        output(p(rrs.get_sib_strength_none, sim_x.is_female and sim_y.is_female)
               .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name))
    else:
        output(p(rrs.get_sib_strength_error).format(num=sib_strength))

```
- **Purpose**: Provides a console command to get the strength of siblinghood between two Sims.
- **How It Works**:
  1. Retrieves the sibling strength using the `get_sib_strength` function.
  2. Returns appropriate sibling strength based on the relationship bits and shared parents.
- **Why It’s Needed**: Allows players or developers to easily check the sibling relationship between two Sims using the in-game console, facilitating debugging and gameplay.

#### Get Indirect Relationship

```python
# input: two sims and ancestors. output: None if there is no indirect relation, list if there is
def get_indirect_rel(sim_x: SimInfoParam, sim_y: SimInfoParam, x_ancestors: Dict, y_ancestors: Dict):
    xy_indirect_rels = []  # will be the output

    if riv_sim_list.sims:
        sim_x = get_rivsim_from_sim(sim_x)
        sim_y = get_rivsim_from_sim(sim_y)

    if not (sim_x is None or sim_y is None):
        # list is empty if it's the same sim
        if sim_x == sim_y:
            return []

        xy_ancestors = [get_rivsim_from_sim(value) for value in x_ancestors.keys() if
                        value in y_ancestors.keys()]  # intersection of list

        # get list of shared ancestors [(sim_z, nx, ny, sim_zx, sim_zy)]
        # where sim_zx =/= sim_zy are siblings, children of sim_z, ancestors of x,y resp; nx, ny gens back
        xy_rels = []  # dumps all shared ancestors with needed info
        for sim_z in xy_ancestors:  # {sim_z: [(n, sim_zx),...],...}
            for sim_xz in x_ancestors[sim_z]:  # x_ancestors[sim_z] = [sim_xz,...], sim_xz = (n, sim_zx)
                for sim_yz in y_ancestors[sim_z]:
                    nx = sim_xz[0]
                    ny = sim_yz[0]
                    sim_zx = sim_xz[1]
                    sim_zy = sim_yz[1]
                    if not sim_zx == sim_zy:
                        xy_rels.append((sim_z, nx, ny, sim_zx, sim_zy))

        # case handling siblings where both parents exist
        to_remove = []  # to be removed from xy_rels
        for rel_one in xy_rels:
            for rel_two in xy_rels:
                if not rel_one[0] == rel_two[0]:
                    if rel_one[1:] == rel_two[1:]:  # i.e. (nx, ny, sim_zx, sim_zy) is the same
                        # this indicates these are the parents
                        if rel_one[0].sim_id < rel_two[0].sim_id:
                            # ensures we don't have (sim1, sim2,...), (sim2, sim1,...) for parents
                            to_add = (rel_one[0], rel_two[0], rel_one[1], rel_one[2], 1)
                            if to_add not in xy_indirect_rels:  # removes duplicates
                                xy_indirect_rels.append(to_add)
                                if rel_one not in to_remove:
                                    to_remove.append(rel_one)
                                if rel_two not in to_remove:
                                    to_remove.append(rel_two)

        # remove rels handled above
        for rel in to_remove:
            if rel in xy_rels:
                xy_rels.remove(rel)

        # case handling the ones that are from one shared parent
        for rel in xy_rels:
            to_add = (rel[0], rel[0], rel[1], rel[2], get_sib_strength(rel[3], rel[4]))
            if to_add not in xy_indirect_rels:
                xy_indirect_rels.append(to_add)

        # case handling filled gaps by indirect relations
        # i.e. there exists a close indirect relation between sim_xx and sim_yy where
        # sim_xx is an ancestor of only sim_x
        # sim_yy is an ancestor of only sim_y
        # sim_xx has no parent who is an ancestor of sim_x and sim_y

        xx = []  # list of sims who are x or ancestors of x and not y
        yy = []  # list of sims who are y or ancestors of y and not x
        x_ancestors[sim_x] = [(0, sim_x)]  # here it helps to have the sim's self
        y_ancestors[sim_y] = [(0, sim_y)]  # trust me it'll be useful later
        for sim_xx in x_ancestors.keys():
            if sim_xx not in y_ancestors.keys():
                xx.append(get_sim_from_rivsim(sim_xx))
        for sim_yy in y_ancestors.keys():
            if sim_yy not in x_ancestors.keys():
                yy.append(get_sim_from_rivsim(sim_yy))

        # remove nones
        # ancestors of only x, as sims
        xx = [sim for sim in xx if sim is not None]
        # ancestors of only y, as sims
        yy = [sim for sim in yy if sim is not None]

        # x (has an ancestor who) is a close indirect relative of y('s ancestor), but these share no ancestor who is an
        # ancestor of x AND y changed from elifs bc some rels are gross af

        #   sim_x.relationship_tracker.has_bit(sim_y.sim_id, relname_relbit) <=> sim_y is the relname of sim_x

        manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
        sibling_relbit = manager.get(0x2262)
        cousin_relbit = manager.get(0x227A)
        pibling_relbit = manager.get(0x227D)
        nibling_relbit = manager.get(0x2705)
        for sim_xx in xx:
            for sim_yy in yy:
                try:
                    # sim_xx and sim_yy siblings, with no parent who is an ancestor of x and y
                    if sim_xx.relationship_tracker.has_bit(int(sim_yy.sim_id), sibling_relbit):
                        # get parents of sim_xx or sim_yy that are ancestors of x and y
                        xx_parents = [p for p in get_parents(sim_xx) if p in xy_ancestors]
                        yy_parents = [p for p in get_parents(sim_yy) if p in xy_ancestors]

                        # riv_log(f'relation stitching for siblings {sim_x.first_name} and {sim_y.first_name}:', 3)
                        # riv_log(xx_parents, 3)
                        # riv_log(yy_parents, 3)
                        # riv_log([p for p in xx_parents if p in yy_parents], 3)

                        # get parents of sim_xx AND sim_yy that are ancestors of x and y
                        if not [p for p in xx_parents if p in yy_parents]:
                            # convert back to rivsims
                            rivsim_xx = get_rivsim_from_sim(sim_xx)
                            rivsim_yy = get_rivsim_from_sim(sim_yy)
                            # sim_xx and sim_yy have no parents that are ancestors of sim_x and sim_y
                            #   => rels via xx and yy have not been added yet
                            for sim_xz in x_ancestors[rivsim_xx]:
                                # x_ancestors[sim_xx] = [sim_xz,...], sim_xz = (n, sim)
                                # where sim_xx is n gens back from sim_x via sim
                                for sim_yz in y_ancestors[rivsim_yy]:
                                    # y_ancestors[sim_yy] = [sim_yz,...], sim_yz = (n, sim)
                                    # where sim_yy is n gens back from sim_x via sim
                                    nx = sim_xz[0]
                                    ny = sim_yz[0]
                                    to_add = (rivsim_xx, rivsim_yy, nx + 1, ny + 1, get_sib_strength(sim_xx, sim_yy))
                                    # connections are sibs (sharing parents), so gen + 1
                                    if to_add not in xy_indirect_rels:
                                        xy_indirect_rels.append(to_add)
                except Exception as e:
                    riv_log('error with siblings ' + sim_xx.first_name + ' and ' + sim_yy.first_name + ': ' + str(e))

                try:
                    # sim_yy pibling of sim_xx, and there are no siblings to check
                    if sim_xx.relationship_tracker.has_bit(int(sim_yy.sim_id), pibling_relbit):
                        for sim_xxx in get_parents(sim_xx):
                            sim_xxx = get_sim_from_rivsim(sim_xxx)
                            if sim_xxx is not None:
                                if sim_xxx.relationship_tracker.has_bit(int(sim_yy.sim_id), sibling_relbit):
                                    # this case will already by covered by sib case, using yy's parent = xx's sib
                                    break
                        else:
                            # convert back to rivsims
                            rivsim_xx = get_rivsim_from_sim(sim_xx)
                            rivsim_yy = get_rivsim_from_sim(sim_yy)
                            for sim_xz in x_ancestors[rivsim_xx]:
                                # x_ancestors[sim_xx] = [sim_xz,...], sim_xz = (n, sim)
                                # where sim_xx is n gens back from sim_x via sim
                                for sim_yz in y_ancestors[rivsim_yy]:
                                    # y_ancestors[sim_yy] = [sim_yz,...], sim_yz = (n, sim)
                                    # where sim_yy is n gens back from sim_x via sim
                                    nx = sim_xz[0]
                                    ny = sim_yz[0]
                                    to_add = (rivsim_xx, rivsim_yy, nx + 2, ny + 1, 1)
                                    # connections are nibling + pibling, so an extra 2, 1 to joining point.
                                    # assume missing parent of xx is yy's full sib
                                    if to_add not in xy_indirect_rels:
                                        xy_indirect_rels.append(to_add)
                except Exception as e:
                    riv_log(
                        'error with pibling/nibling ' + sim_xx.first_name + ' and ' + sim_yy.first_name + ': ' + str(e))

                try:
                    # sim_yy nibling of sim_xx, and there are no siblings to check
                    if sim_xx.relationship_tracker.has_bit(int(sim_yy.sim_id), nibling_relbit):
                        for sim_yyy in get_parents(sim_yy):
                            sim_yyy = get_sim_from_rivsim(sim_yyy)
                            if sim_yyy is not None:
                                if sim_yyy.relationship_tracker.has_bit(int(sim_xx.sim_id), sibling_relbit):
                                    # this case will already by covered by sib case, using xx's parent = yy's sib
                                    break
                        else:
                            # convert back to rivsims
                            rivsim_xx = get_rivsim_from_sim(sim_xx)
                            rivsim_yy = get_rivsim_from_sim(sim_yy)
                            for sim_xz in x_ancestors[rivsim_xx]:
                                # x_ancestors[sim_xx] = [sim_xz,...], sim_xz = (n, sim)
                                # where sim_xx is n gens back from sim_x via sim
                                for sim_yz in y_ancestors[rivsim_yy]:
                                    # y_ancestors[sim_yy] = [sim_yz,...], sim_yz = (n, sim)
                                    # where sim_yy is n gens back from sim_x via sim
                                    nx = sim_xz[0]
                                    ny = sim_yz[0]
                                    to_add = (rivsim_xx, rivsim_yy, nx + 1, ny + 2, 1)
                                    # connections are pibling + nibling, so an extra 1, 2 to joining point.
                                    # assume missing parent of yy is xx's full sib
                                    if to_add not in xy_indirect_rels:
                                        xy_indirect_rels.append(to_add)
                except Exception as e:
                    riv_log(
                        'error with nibling/pibling ' + sim_xx.first_name + ' and ' + sim_yy.first_name + ': ' + str(e))

                try:
                    # sim_xx and sim_yy first cousins, and there are no siblings to check
                    # (between sim_xx+parents AND sim_yy+parents)
                    # spaghet bc i don't fkn remember which way round the pnibling rel goes, two of these are unneeded
                    if sim_xx.relationship_tracker.has_bit(int(sim_yy.sim_id), cousin_relbit):
                        xx_parents = get_parents(sim_xx)
                        yy_parents = get_parents(sim_yy)
                        for sim_xxx, sim_yyy in get_pairs_yield(xx_parents, yy_parents):
                            sim_xxx = get_sim_from_rivsim(sim_xxx)
                            sim_yyy = get_sim_from_rivsim(sim_yyy)
                            if sim_xxx is not None and sim_yyy is not None:
                                if sim_xxx.relationship_tracker.has_bit(sim_yyy.sim_id, sibling_relbit):
                                    # handled by sibling case
                                    break
                                if sim_xxx.relationship_tracker.has_bit(sim_yy.sim_id, nibling_relbit):
                                    # handled by pnibling case
                                    break
                                if sim_xx.relationship_tracker.has_bit(sim_yyy.sim_id, nibling_relbit):
                                    # handled by pnibling case
                                    break
                                if sim_yyy.relationship_tracker.has_bit(sim_xx.sim_id, nibling_relbit):
                                    # handled by pnibling case
                                    break
                                if sim_yy.relationship_tracker.has_bit(sim_xxx.sim_id, nibling_relbit):
                                    # handled by pnibling case
                                    break
                        else:  # sim_xx and sim_yy are first cousins, but have no parents who are siblings
                            # convert back to rivsims
                            rivsim_xx = get_rivsim_from_sim(sim_xx)
                            rivsim_yy = get_rivsim_from_sim(sim_yy)
                            for sim_xz in x_ancestors[rivsim_xx]:
                                # x_ancestors[sim_xx] = [sim_xz,...], sim_xz = (n, sim)
                                # where sim_xx is n gens back from sim_x via sim
                                for sim_yz in y_ancestors[rivsim_yy]:
                                    # y_ancestors[sim_yy] = [sim_yz,...], sim_yz = (n, sim)
                                    # where sim_yy is n gens back from sim_x via sim
                                    nx = sim_xz[0]
                                    ny = sim_yz[0]
                                    to_add = (rivsim_xx, rivsim_yy, nx + 2, ny + 2, 1)
                                    # connections are cousins (sharing grandparents), so gen + 2.
                                    # assume missing parents would be full sibs
                                    if to_add not in xy_indirect_rels:
                                        xy_indirect_rels.append(to_add)
                except Exception as e:
                    riv_log(
                        'error with first cousins ' + sim_xx.first_name + ' and ' + sim_yy.first_name + ': ' + str(e))

        riv_log(f'[get indirect rel {sim_x.first_name} {sim_y.first_name}] {xy_indirect_rels}', 3)

    # order the rels by magnitude
    xy_indirect_rels.sort(key=lambda irel: -irel[4] * -(2 ** (irel[2] + irel[3])))  # - to ensure ascending

    return xy_indirect_rels  # [(sim_z, sim_w, nx, ny, sib_strength)]
    # where sim_z and sim_w are parents/sibs/relations to link, sim_z = sim_w if half-
    # sim_x and sim_y are connected nx and ny gens back respectively, via sim_z and sim_w

```
- **Purpose**: Determines the indirect relationship between two Sims.
- **How It Works**:
  1. Initializes an empty list to store the indirect relationships.
  2. Converts the inputs to `RivSim` objects if necessary.
  3. Finds common ancestors of the two Sims.
  4. Iterates through shared ancestors to gather information about generational differences and sibling relationships.
  5. Populates the list of indirect relationships with generational differences and related Sims.
- **Why It’s Needed**: Ensures that indirect relationships are accurately tracked and included in the output, providing comprehensive genealogical data.

#### Get Indirect Relationship Wrapper

```python
def get_indirect_relation(sim_x: SimInfoParam, sim_y: SimInfoParam):
    return get_indirect_rel(sim_x, sim_y, get_ancestors(sim_x), get_ancestors(sim_y))
```
- **Purpose**: Provides a wrapper function for `get_indirect_rel` to directly retrieve the indirect relationship between two Sims.
- **How It Works**:
  1. Calls `get_indirect_rel` with the ancestors of both Sims.
  2. Returns the result.
- **Why It’s Needed**: Simplifies the process of retrieving indirect relationships between two Sims by encapsulating the ancestor retrieval process.

#### Format Indirect Relationship with Gender

```python
def format_indirect_rel_gender(xy_indirect_rels: List, gender: int):
    rels_via = rrs.indirect(xy_indirect_rels, gender)
    riv_log(f'[format indirect rel] {rels_via}', 3)
    return rels_via  # [(str, sim_z, sim_w)]
```
- **Purpose**: Formats the indirect relationship between two Sims, considering gender.
- **How It Works**:
  1. Uses the `rrs.indirect` function to format the relationships.
  2. Logs the formatted relationships.
  3. Returns the formatted relationships as a list of tuples.
- **Why It’s Needed**: Provides a way to present indirect relationships between Sims in a gender-aware manner, enhancing the clarity and accuracy of relationship descriptions.

#### Format Indirect Relationship

```python
def format_indirect_rel(xy_indirect_rels: List, sim_x: SimInfoParam):
    return format_indirect_rel_gender(xy_indirect_rels, sim_x.is_female)
```
- **Purpose**: Formats the indirect relationship between two Sims using the gender of `sim_x`.
- **How It Works**:
  1. Calls `format_indirect_rel_gender` with the indirect relationships and the gender of `sim_x`.
  2. Returns the formatted relationship string.
- **Why It’s Needed**: Simplifies the process of generating relationship descriptions by encapsulating the gender-specific formatting.

### Console Command for Indirect Relationship

```python
@sims4.commands.Command('riv_get_indirect_rel', command_type=sims4.commands.CommandType.Live)
def console_get_indirect_rel(sim_x: SimInfoParam, sim_y: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    rels_via = format_indirect_rel(get_indirect_relation(sim_x, sim_y), sim_x)
    # we now have a list (relation, via this person)
    if sim_x is not None:
        if sim_y is not None:
            if rels_via:
                for rel_via in rels_via:
                    if rel_via[1] == rel_via[2]:  # via one sim
                        output(p(rrs.get_indirect_rel_1, sim_x.is_female)
                               .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                                       y_firstname=sim_y.first_name, y_lastname=sim_y.last_name, rel=rel_via[0],
                                       z_firstname=rel_via[1].first_name, z_lastname=rel_via[1].last_name))
                    else:
                        sim_z = rel_via[1]
                        sim_w = rel_via[2]  # via two sims
                        output(p(rrs.get_indirect_rel_2, sim_x.is_female)
                               .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                                       y_firstname=sim_y.first_name, y_lastname=sim_y.last_name, rel=rel_via[0],
                                       z_firstname=sim_z.first_name, z_lastname=sim_z.last_name,
                                       w_firstname=sim_w.first_name, w_lastname=sim_w.last_name))
            else:
                output(p(rrs.get_indirect_rel_0)
                       .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name))
```
- **Purpose**: Provides a console command to get the indirect relationship between two Sims.
- **How It Works**:
  1. Retrieves the indirect relationship using the `get_indirect_relation` function.
  2. Formats the relationship description.
  3. Outputs the relationship description based on the formatted result.
- **Why It’s Needed**: Allows players or developers to easily check the indirect relationship between two Sims using the in-game console, facilitating debugging and gameplay.

#### Get Spouses

```python
def get_spouses(sim_x: SimInfoParam):
    sim_x = get_sim_from_rivsim(sim_x)
    if sim_x is None:
        return []

    manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
    spouse_relbit = manager.get(0x3DCE)
    sim_spouses = []
    for sim_y in services.sim_info_manager().get_all():
        if sim_x.relationship_tracker.has_bit(sim_y.sim_id, spouse_relbit):
            sim_spouses.append(sim_y)

    return sim_spouses
```
- **Purpose**: Retrieves the spouses of a given Sim.
- **How It Works**:
  1. Converts the input to a `Sim` object if necessary.
  2. Retrieves the relationship bit for spouses.
  3. Checks all Sims in the game for the spouse relationship bit.
  4. Returns a list of Sims who are spouses of the given Sim.
- **Why It’s Needed**: Provides a way to retrieve the spouses of a Sim, which is important for tracking in-law relationships.

### Get In-Law Relationship

```python
def get_inlaw_rel(sim_x, sim_y, x_ancestors, y_ancestors):
    x_spouse = []
    y_spouse = []
    xy_inlaw_rels = []
    # gets list of spouses for each of sim_x and sim_y
    try:
        if riv_sim_list.sims:  # if using RivSims
            # uses actual sim for spouse if needed and doable
            ssim_x_tmp = get_sim_from_rivsim(sim_x)
            ssim_y_tmp = get_sim_from_rivsim(sim_y)
            if ssim_x_tmp is not None:
                x_culled = False
            else:
                x_culled = True
            if ssim_y_tmp is not None:
                y_culled = False
            else:
                y_culled = True
        else:  # these will defo be non-culled sims
            x_culled = False
            y_culled = False

        # we now have sims in game where possible, and whether the sim has been culled
        # if the sim is culled then we just assume they have no spouse

        if not x_culled:
            x_spouse = get_spouses(sim_x)
        if not y_culled:
            y_spouse = get_spouses(sim_y)

    except Exception as e:
        riv_log(f'error in getting spouse lists ({e})')
    # check if sim_x is married to sim_y
    try:
        if sim_x in y_spouse:
            if sim_y in x_spouse:  # just checks nothing is weird
                xy_inlaw_rels.append((0,))  # the comma is needed to make this a tuple
    except Exception as e:
        riv_log(f'error in checking if sims are married ({e})')

    # http://www.genetic-genealogy.co.uk/supp/NonGenetictRelationships.html
    # check if sim_x is related to sim_y's spouse
    try:
        # x is related to y's spouse (type a on site above)
        for sim_s in y_spouse:
            s_ancestors = get_ancestors(sim_s)
            # direct rel is a list of integers with generational difference
            temp_rels = get_direct_rel(sim_x, sim_s, x_ancestors, s_ancestors)
            if temp_rels:
                for rel in temp_rels:
                    if rel < 0:  # if x is y's spouse's ancestor (e.g. mother-in-law)
                        xy_inlaw_rels.append((1, rel, sim_x, sim_s))
            # indirect rel is a list of (sim_z, sim_w, nx, ny, sib_strength)
            temp_rels = get_indirect_rel(sim_x, sim_s, x_ancestors, s_ancestors)
            if temp_rels:
                for rel in temp_rels:
                    xy_inlaw_rels.append((2, rel, sim_x, sim_s))
    except Exception as e:
        riv_log(f'error in checking if sim_x is related to sim_y\'s spouse ({e})')
    # check if sim_y is related to sim_x's spouse
    try:
        # x is the spouse of y's relative / y is related to x's spouse (type b on site above)
        for sim_s in x_spouse:
            s_ancestors = get_ancestors(sim_s)
            # direct rel is a list of integers with generational difference
            temp_rels = get_direct_rel(sim_s, sim_y, s_ancestors, y_ancestors)
            if temp_rels:
                for rel in temp_rels:
                    if rel > 0:  # if x is the spouse of y's descendant (e.g. son-in-law)
                        xy_inlaw_rels.append((1, rel, sim_y, sim_s))
            # indirect rel is a list of (sim_z, sim_w, nx, ny, sib_strength)
            temp_rels = get_indirect_rel(sim_s, sim_y, s_ancestors, y_ancestors)
            if temp_rels:
                for rel in temp_rels:
                    xy_inlaw_rels.append((2, rel, sim_y, sim_s))
    except Exception as e:
        riv_log(f'error in checking if sim_y is related to sim_x\'s spouse ({e})')

    riv_log(f'[get inlaw rel {sim_x.first_name} {sim_y.first_name}] {xy_inlaw_rels}', 3)

    return xy_inlaw_rels
    # list [(0), (1, drel, sim_t, sim_s), (2, irel, sim_t, sim_s)] where
    # sim_s is the spouse of sim_t = sim_x or sim_y
    # drel = n describing the direct-in-law relationship between sim_x and sim_y
    # irel = (sim_z, sim_w, nx, ny, sib_strength) describing the indirect-in-law relationship
```
- **Purpose**: Determines the in-law relationship between two Sims.
- **How It Works**:
  1. Retrieves the spouses of both Sims.
  2. Checks if the Sims are married to each other.
  3. Checks if one Sim is related to the other Sim's spouse and vice versa.
  4. Gathers direct and indirect relationships involving spouses.
  5. Returns a list of in-law relationships.
- **Why It’s Needed**: Provides a comprehensive way to track in-law relationships, which is important for maintaining accurate genealogical data.

#### Get In-Law Relationship Wrapper

```python
def get_inlaw_relation(sim_x: SimInfoParam, sim_y: SimInfoParam):
    return get_inlaw_rel(sim_x, sim_y, get_ancestors(sim_x), get_ancestors(sim_y))
```
- **Purpose**: Provides a wrapper function for `get_inlaw_rel` to directly retrieve the in-law relationship between two Sims.
- **How It Works**:
  1. Calls `get_inlaw_rel` with the ancestors of both Sims.
  2. Returns the result.
- **Why It’s Needed**: Simplifies the process of retrieving in-law relationships between two Sims by encapsulating the ancestor retrieval process.

### Format In-Law Relationship

```python
def format_inlaw_rel(xy_inlaw_rels: List, sim_x: SimInfoParam):
    inlaw_rels = rrs.inlaw(xy_inlaw_rels, sim_x)  # this will have the strings and via
    riv_log(f'[format inlaw rel] {inlaw_rels}', 3)
    return inlaw_rels  # [(string, sim)] where sim is the spouse related to sim_x or sim_y, or is 0 if spouse
```
- **Purpose**: Formats the in-law relationship between two Sims.
- **How It Works**:
  1. Uses the `rrs.inlaw` function to format the in-law relationships.
  2. Logs the formatted relationships.
  3. Returns the formatted relationships as a list of tuples.
- **Why It’s Needed**: Provides a way to present in-law relationships between Sims in a clear and organized manner.

#### Get Step Relationship

```python
def get_step_rel(sim_x, sim_y, x_ancestors_tmp, y_ancestors_tmp):
    get_step_rel_tic = time.perf_counter()
    riv_log(f'finding step rels between {sim_x.first_name} and {sim_y.first_name}...')

    manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)

    x_ancestors = {}
    x_list_ingame = rivsims_to_sims(x_ancestors_tmp.keys())
    riv_log(f'number of ingame ancestors of {sim_x.first_name}: {len(x_list_ingame)}')
    for rivsim_z in x_ancestors.keys():
        sim_z = get_sim_from_rivsim(rivsim_z)
        if sim_z in x_list_ingame:
            x_ancestors[sim_z] = x_ancestors_tmp[rivsim_z]
    del x_list_ingame
    sim_x = get_sim_from_rivsim(sim_x)

    y_ancestors = {}
    y_list_ingame = rivsims_to_sims(y_ancestors_tmp.keys())
    riv_log(f'number of ingame ancestors of {sim_y.first_name}: {len(y_list_ingame)}')
    for rivsim_z in y_ancestors.keys():
        sim_z = get_sim_from_rivsim(rivsim_z)
        if sim_z in y_list_ingame:
            y_ancestors[sim_z] = y_ancestors_tmp[rivsim_z]
    del y_list_ingame
    sim_y = get_sim_from_rivsim(sim_y)

    x_step_y = []

    # check step-parent / step-child
    try:
        for sim_z in get_spouses(sim_x):
            if sim_z in get_parents_ingame(sim_y):
                if sim_x not in get_parents_ingame(sim_y):
                    x_step_y.append({'sim_xz': sim_z, 'sim_zy': sim_z, 'xzy': [((0,), 1)]})
                    riv_log('{} is the step-parent of {}'.format(sim_x.first_name, sim_y.first_name))
    except Exception as e:
        riv_log(f'error in checking if {sim_x.first_name} is the step-parent of {sim_y.first_name}: {e}')
    try:
        for sim_z in get_parents_ingame(sim_x):
            if sim_z in get_spouses(sim_y):
                if sim_x not in get_children_ingame(sim_y):
                    x_step_y.append({'sim_xz': sim_z, 'sim_zy': sim_z, 'xzy': [(-1, (0,))]})
                    riv_log(f'{sim_x.first_name} is the step-child of {sim_y.first_name}')
    except Exception as e:
        riv_log(f'error in checking if {sim_x.first_name} is the step-child of {sim_y.first_name}: {e}')

    # get all married relatives of sim_x and sim_y
    x_rels = {}
    num_xz = 0
    y_rels = {}
    num_zy = 0
    for sim_z in services.sim_info_manager().get_all():
        try:
            if sim_z.spouse_sim_id is not None and sim_z not in [sim_x, sim_y]:
                z_ancestors = get_ancestors_ingame(sim_z)
                xz = get_direct_rel(sim_x, sim_z, x_ancestors, z_ancestors) + \
                     get_indirect_rel(sim_x, sim_z, x_ancestors, z_ancestors) + \
                     get_inlaw_rel(sim_x, sim_z, x_ancestors, z_ancestors)
                zy = get_direct_rel(sim_z, sim_y, z_ancestors, y_ancestors) + \
                     get_indirect_rel(sim_z, sim_y, z_ancestors, y_ancestors) + \
                     get_inlaw_rel(sim_z, sim_y, z_ancestors, y_ancestors)
                if xz:
                    x_rels[sim_z] = xz
                    num_xz += len(xz)
                if zy:
                    y_rels[sim_z] = zy
                    num_zy += len(zy)
        except Exception as e:
            riv_log(f'error in getting relatives of sim_x and sim_y: {e}')
    riv_log(f'number of married rels found for {sim_x.first_name}: {num_xz}')
    riv_log(f'number of married rels found for {sim_y.first_name}: {num_zy}')

    if num_xz == 0 and num_zy == 0:
        get_step_rel_toc = time.perf_counter()
        riv_log(f'time taken to find step rels between {sim_x.first_name} and {sim_y.first_name} = '
                f'{get_step_rel_toc - get_step_rel_tic}')
        return []

    # check if any are married to each other
    try:
        for sim_xz in x_rels.keys():
            for sim_zy in y_rels.keys():
                if sim_xz.relationship_tracker.has_bit(sim_zy.sim_id, manager.get(0x3DCE)):
                    x_step_y.append({'sim_xz': sim_xz, 'sim_zy': sim_zy,
                                     'xzy': [(a, b) for a in x_rels[sim_xz] for b in y_rels[sim_zy]]})
                    riv_log(f'found a marriage between {sim_xz.first_name} and {sim_zy.first_name}!')
        riv_log('marriages found: ' + str(len(x_step_y)))
    except Exception as e:
        riv_log(f'error in checking if any relatives are married: {e}')

    xy_step_rels = []
    for d in x_step_y:
        try:
            sim_xz = d['sim_xz']
            sim_zy = d['sim_zy']
            xzy_rels = []
            for rel_tuple in d['xzy']:
                rel_xz = rel_tuple[0]
                rel_zy = rel_tuple[1]
                if isinstance(rel_xz, int):
                    if isinstance(rel_zy, int):
                        if (rel_xz * rel_zy) > 0:
                            xzy_rels.append(rel_xz + rel_zy)
                        elif rel_xz < 0 and rel_zy > 0:
                            xzy_rels.append((sim_xz, sim_zy, abs(rel_xz), abs(rel_zy), 1))
                    elif isinstance(rel_zy, tuple):
                        if isinstance(rel_zy[0], int):
                            continue
                        elif rel_xz < 0:
                            xzy_rels.append((rel_zy[0], rel_zy[1], rel_zy[2] - rel_xz, rel_zy[3], rel_zy[4]))
                elif isinstance(rel_xz, tuple):
                    if isinstance(rel_xz[0], int):
                        continue
                    else:
                        if isinstance(rel_zy, int):
                            if rel_zy > 0:
                                xzy_rels.append((rel_xz[0], rel_xz[1], rel_xz[2], rel_xz[3] + rel_zy, rel_xz[4]))
                        else:
                            continue
            xy_step_rels.append((sim_xz, sim_zy, xzy_rels))
            riv_log('found rels: ' + str(xzy_rels))
        except Exception as e:
            riv_log(f'error in trying to create step-relation: {e}')

    get_step_rel_toc = time.perf_counter()
    riv_log(f'time taken to find step rels between {sim_x.first_name} and {sim_y.first_name} = '
            f'get_step_rel_toc - get_step_rel_tic')

    riv_log(f'[get step rel {sim_x.first_name} {sim_y.first_name}] {xy_step_rels}', 3)

    return xy_step_rels  # [(sim_xz, sim_zy, [rels if sim_xz = sim_zy])]
```
- **Purpose**: Determines the step relationship between two Sims.
- **How It Works**:
  1. Initializes performance tracking and logs the start of the process.
  2. Retrieves and converts ancestors to their in-game representations.
  3. Checks for step-parent and step-child relationships.
  4. Retrieves all married relatives and their relationships.
  5. Checks if any relatives are married to each other.
  6. Combines the relationships and returns the step relationships.
- **Why It’s Needed**: Provides a comprehensive way to track step relationships, which is important for maintaining accurate genealogical data.

#### Get Step Relationship Wrapper

```python
def get_step_relation(sim_x: SimInfoParam, sim_y: SimInfoParam):
    return get_step_rel(sim_x, sim_y, get_ancestors_ingame(sim_x), get_ancestors_ingame(sim_y))
```
- **Purpose**: Provides a wrapper function for `get_step_rel` to directly retrieve the step relationship between two Sims.
- **How It Works**:
  1. Calls `get_step_rel` with the ancestors of both Sims.
  2. Returns the result.
- **Why It’s Needed**: Simplifies the process of retrieving step relationships between two Sims by encapsulating the ancestor retrieval process.

#### Format Step Relationship

```python
def format_step_rel(xy_step_rels: List, sim_x: SimInfoParam):
    step_rels = rrs.step(xy_step_rels, sim_x

)  # this will have the strings and via
    riv_log(f'[format step rel] {step_rels}', 3)
    return step_rels  # [(string, sim_xz, sim_zy)]
```
- **Purpose**: Formats the step relationship between two Sims.
- **How It Works**:
  1. Uses the `rrs.step` function to format the step relationships.
  2. Logs the formatted relationships.
  3. Returns the formatted relationships as a list of tuples.
- **Why It’s Needed**: Provides a way to present step relationships between Sims in a clear and organized manner.

#### Direct Relationship Percentage

```python
@lru_cache(maxsize=None)
def drel_percent(x_id, y_id):
    if int(y_id) < int(x_id):
        return drel_percent(y_id, x_id)

    drels = get_direct_relation(get_rivsim_from_id(x_id), get_rivsim_from_id(y_id))
    drel_ps = [0.5 ** abs(gen) for gen in drels]
    riv_log(drel_ps, 3)
    return sum(drel_ps)
```
- **Purpose**: Calculates the percentage of direct relationships between two Sims.
- **How It Works**:
  1. Retrieves the direct relationships between two Sims.
  2. Calculates the percentage based on generational differences.
  3. Logs the percentages and returns the sum.
- **Why It’s Needed**: Provides a quantitative measure of direct relationships, which is useful for consanguinity calculations.

#### Indirect Relationship Percentage

```python
@lru_cache(maxsize=None)
def irel_percent(x_id, y_id):
    if int(y_id) < int(x_id):
        return irel_percent(y_id, x_id)

    irels = get_indirect_relation(get_rivsim_from_id(x_id), get_rivsim_from_id(y_id))
    irel_ps = [2 * irel[4] * (0.5 ** (irel[2] + irel[3])) for irel in irels]
    riv_log(irel_ps, 3)
    return sum(irel_ps)
```
- **Purpose**: Calculates the percentage of indirect relationships between two Sims.
- **How It Works**:
  1. Retrieves the indirect relationships between two Sims.
  2. Calculates the percentage based on generational differences and sibling strength.
  3. Logs the percentages and returns the sum.
- **Why It’s Needed**: Provides a quantitative measure of indirect relationships, which is useful for consanguinity calculations.

#### Consanguinity Calculation

```python
@lru_cache(maxsize=None)
def consang(sim_x: RivSim, sim_y: RivSim):
    if sim_x == sim_y:
        return 1.0
    return drel_percent(sim_x.sim_id, sim_y.sim_id) + irel_percent(sim_x.sim_id, sim_y.sim_id)
```
- **Purpose**: Calculates the consanguinity (degree of relatedness) between two Sims.
- **How It Works**:
  1. Checks if the Sims are the same, returning 100% if they are.
  2. Sums the direct and indirect relationship percentages.
  3. Returns the consanguinity percentage.
- **Why It’s Needed**: Provides a comprehensive measure of relatedness, useful for preventing incest and displaying genealogical information.

### Console Command for Consanguinity

```python
@sims4.commands.Command('riv_consang', command_type=sims4.commands.CommandType.Live)
def console_get_consanguinity(sim_x: SimInfoParam, sim_y: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    xy_consang = consang(sim_x, sim_y)
    output(p(rrs.consang_1)
           .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name, num=round(100 * xy_consang, 5)))
```
- **Purpose**: Provides a console command to get the consanguinity between two Sims.
- **How It Works**:
  1. Retrieves the consanguinity using the `consang` function.
  2. Outputs the consanguinity percentage to the console.
- **Why It’s Needed**: Allows players or developers to easily check the degree of relatedness between two Sims using the in-game console, facilitating debugging and gameplay.

#### Inject Wrapper

```python
def inject(target_function, new_function):
    @wraps(target_function)
    def _inject(*args, **kwargs):
        return new_function(target_function, *args, **kwargs)

    return _inject
```
- **Purpose**: Creates a wrapper for injecting custom behavior into existing functions.
- **How It Works**:
  1. Defines a new function that calls the target function with the new behavior.
  2. Returns the new function.
- **Why It’s Needed**: Allows for modifying the behavior of existing functions without directly changing their code.

#### Inject to Target Object

```python
def inject_to(target_object, target_function_name):
    def _inject_to(new_function):
        target_function = getattr(target_object, target_function_name)
        setattr(target_object, target_function_name, inject(target_function, new_function))
        return new_function

    return _inject_to
```
- **Purpose**: Injects custom behavior into a specific function of a target object.
- **How It Works**:
  1. Retrieves the target function from the target object.
  2. Replaces the target function with the injected function.
  3. Returns the new function.
- **Why It’s Needed**: Provides a flexible way to modify the behavior of specific functions in the game.

#### Show Notification

```python
def scumbumbo_show_notification(sim_x: SimInfoParam, sim_y: SimInfoParam, text: str):
    client = services.client_manager().get_first_client()
    localized_title = lambda **_: LocalizationHelperTuning.get_raw_text(sim_x.first_name + ' to ' + sim_y.first_name)
    localized_text = lambda **_: LocalizationHelperTuning.get_raw_text(text)
    primary_icon = lambda _: IconInfoData(obj_instance=sim_x)

    urgency = UiDialogNotification.UiDialogNotificationUrgency.DEFAULT
    information_level = UiDialogNotification.UiDialogNotificationLevel.PLAYER
    visual_type = UiDialogNotification.UiDialogNotificationVisualType.INFORMATION

    notification = UiDialogNotification.TunableFactory().default(client.active_sim, text=localized_text,
                                                                 title=localized_title, icon=primary_icon,
                                                                 urgency=urgency, information_level=information_level,
                                                                 visual_type=visual_type)
    notification.show_dialog()
```
- **Purpose**: Displays a notification with information about the relationship between two Sims.
- **How It Works**:
  1. Retrieves the client and creates localized strings for the title and text.
  2. Sets the primary icon to the first Sim.
  3. Configures the visual styles for the notification.
  4. Creates and shows the notification.
- **Why It’s Needed**: Provides a way to inform players about the relationship status between Sims in an immersive and interactive manner.

#### Show Notification with Text and Title

```python
def scumbumbo_show_notif_texttitle(text: str, title: str):
    # We need the client to get the active sim for the icon
    client = services.client_manager().get_first_client()
    localized_title = lambda **_: LocalizationHelperTuning.get_raw_text(title)
    localized_text = lambda **_: LocalizationHelperTuning.get_raw_text(text)

    sprout_plant_icon_key = get_resource_key(0x9993999E26D6CB56, Types.PNG)
    primary_icon = lambda _: IconInfoData(icon_resource=sprout_plant_icon_key)

    urgency = UiDialogNotification.UiDialogNotificationUrgency.DEFAULT
    information_level = UiDialogNotification.UiDialogNotificationLevel.PLAYER
    visual_type = UiDialogNotification.UiDialogNotificationVisualType.INFORMATION

    notification = UiDialogNotification.TunableFactory().default(client.active_sim, text=localized_text,
                                                                 title=localized_title, icon=primary_icon,
                                                                 urgency=urgency, information_level=information_level,
                                                                 visual_type=visual_type)
    notification.show_dialog()
```
- **Purpose**: Displays a notification with custom text and title.
- **How It Works**:
  1. Retrieves the client and creates localized strings for the title and text.
  2. Sets a custom icon for the notification.
  3. Configures the visual styles for the notification.
  4. Creates and shows the notification.
- **Why It’s Needed**: Provides a way to show detailed notifications with specific titles and texts.

#### Get String List of Relationships

```python
def get_str_list(sim_x, sim_y, x_ancestors, y_ancestors, include_step_rels=global_include_step_rels):
    bio_rels_output = []
    inlaw_rels_output = []
    step_rels_output = []

    direct_rels = get_direct_rel(sim_x, sim_y, x_ancestors, y_ancestors)
    for rel in format_direct_rel(direct_rels, sim_x):
        try:
            bio_rels_output.append(rel)
        except Exception as e:
            bio_rels_output.append(f'[direct rel error {e}]')
            riv_log(f'get_str_list; direct rel error {e}')
    indirect_rels = get_indirect_rel(sim_x, sim_y, x_ancestors, y_ancestors)
    for rel in format_indirect_rel(indirect_rels, sim_x):
        try:
            bio_rels_output.append(rel[0])
        except Exception as e:
            bio_rels_output.append(f'[indirect rel error {e}]')
            riv_log(f'get_str_list; indirect rel error {e}')
    inlaw_rels = get_inlaw_rel(sim_x, sim_y, x_ancestors, y_ancestors)
    for rel in format_inlaw_rel(inlaw_rels, sim_x):
        try:
            inlaw_rels_output.append(rel[0])
        except Exception as e:
            inlaw_rels_output.append(f'[inlaw rel error {e}]')
            riv_log(f'get_str_list; inlaw rel error {e}')
    if include_step_rels or global_include_step_rels:
        step_rels = get_step_rel(sim_x, sim_y, x_ancestors, y_ancestors)
        for rel in format_step_rel(step_rels, sim_x):
            try:
                step_rels_output.append(rel[0])
                riv_log(f'found this step rel: {rel[0]}', 3)
            except Exception as e:
                step_rels_output.append(f'[step rel error {e}]')
                riv_log(f'get_str_list; step rel error {e}')

    riv_log(f'[get str list {sim_x.first_name} {sim_y.first_name}] '
            f'{(bio_rels_output, inlaw_rels_output, step_rels_output)}', 3)

    return (bio_rels_output, inlaw_rels_output, step_rels_output)
```
- **Purpose**: Retrieves and formats lists of relationship strings between two Sims.
- **How It Works**:
  1. Gets direct, indirect, and in-law relationships.
  2. Formats and logs each type of relationship.
  3. Optionally includes step relationships.
  4. Returns the formatted lists.
- **Why It’s Needed**: Provides a comprehensive list of relationships between two Sims, useful for displaying relationship data.

#### Format Relationship Multiplicity

```python
def num_to_tuple(n: int, show_single: int):
    return rrs.tup(n, show_single)
```
- **Purpose**: Formats the multiplicity of relationships as a string.
- **How It Works**:
  1. Uses a predefined function `rrs.tup` to format the multiplicity.
  2. Returns the formatted string.
- **Why It’s Needed**: Ensures consistent formatting for relationship multiplicity.

#### Combine Relationship Strings

```python
def combine_str_list(bio_rels: List, inlaw_rels: List, step_rels: List):
    br_count_dict = {}
    ir_count_dict = {}
    sr_count_dict = {}

    for rel in bio_rels:
        try:
            br_count_dict[rel] += 1
        except:
            br_count_dict[rel] = 1

    for rel in inlaw_rels:
        try:
            ir_count_dict[rel] += 1
        except:
            ir_count_dict[rel] = 1

    for rel in step_rels:
        try:
            sr_count_dict[rel] += 1
        except:
            sr_count_dict[rel] = 1

    bio_rels_fixed = []
    inlaw_rels_fixed = []
    step_rels_fixed = []

    for rel in br_count_dict.keys():
        prefix = num_to_tuple(br_count_dict[rel], 0)
        bio_rels_fixed.append(prefix + rel)

    for rel in ir_count_dict.keys():
        prefix = num_to_tuple(ir_count_dict[rel], 0)
        inlaw_rels_fixed.append(prefix + rel)

    for rel in sr_count_dict.keys():
        prefix = num_to_tuple(sr_count_dict[rel], 0)
        step_rels_fixed.append(prefix + rel)

    return (bio_rels_fixed, inlaw_rels_fixed, step_rels_fixed)
```
- **Purpose**: Combines relationship strings, including multiplicity.
- **How It Works**:
  1. Counts occurrences of each relationship string.
  2. Formats each string with its multiplicity.
  3. Returns the formatted lists.
- **Why It’s Needed**: Provides clear and concise representation of relationships with their multiplicity.

#### Generate Notification Text

```python
def give_me_a_string(string_type):
    strings_dict = rrs.strings_dict
    string_list = strings_dict[string_type]
    string_output = random.choice(string_list)
    return string_output + ' '
```
- **Purpose**: Generates a notification string based on the relationship type.
- **How It Works**:
  1. Retrieves a list of strings for the specified type.
  2. Selects a random string from the list.
  3. Returns the selected string with a trailing space.
- **Why It’s Needed**: Adds variety and context-specific text to notifications.

#### Handle Notifications for Relationships

```python
def riv_get_notif_generic(x_id: int, y_id: int, x_person: int, y_person: int, _connection=None):
    sim_x = services.sim_info_manager().get(x_id).sim_info
    sim_y = services.sim_info_manager().get(y_id).sim_info
    try:
        x_ancestors = get_ancestors(sim_x)
        y_ancestors = get_ancestors(sim_y)
    except Exception as e:
        scumbumbo_show_notification(sim_x, sim_y, '[failed to get ancestors: ' + str(e) + ']')
        return

    rel_lists = get_str_list(sim_x, sim_y, x_ancestors, y_ancestors, global_include_step_rels)
    bio_rels = rel_lists[0]
    inlaw_rels = rel_lists[1]
    step_rels = rel_lists[2]

    rel_lists = combine_str_list(bio_rels, inlaw_rels, step_rels)
    bio_rels = rel_lists[0]
    inlaw_rels = rel_lists[1]
    step_rels = rel_lists[2]

    rel_code = 0
    if inlaw_rels:
        rel_code += 1
    if bio_rels:
        rel_code += 2
    if step_rels:
        rel_code += 4

    if x_person == 1 and y_person == 2:
        notif_text = give_me_a_string(rel_code)
    elif x_person == 1 and y_person == 3:
        notif_text = rrs.othersim_string.format(yname=sim_y.first_name)
        if rel_code == 0:
            notif_text = notif_text + ' ' + give_me_a_string(rel_code)
    else:
        notif_text = ''

    if bio_rels:
        notif_text += rrs.x_is_ys[f'{x_person}.{y_person}'] + bio_rels[0]
        if len(bio_rels) == 2:
            notif_text += rrs.and__ + bio_rels[1]
        elif len(bio_rels) > 2:
            for i in range(1, len(bio_rels)

 - 1):
                notif_text += ', ' + bio_rels[i]
            notif_text += ',' + rrs.and__ + bio_rels[len(bio_rels) - 1]
        notif_text += '. '
        if inlaw_rels + step_rels:
            non_bio_rels = inlaw_rels + step_rels
            notif_text += rrs.x_is_ys[f'{x_person}..{y_person}'] + non_bio_rels[0]
            if len(non_bio_rels) == 2:
                notif_text += rrs.and__ + non_bio_rels[1]
            elif len(non_bio_rels) > 2:
                for i in range(1, len(non_bio_rels) - 1):
                    notif_text += ', ' + non_bio_rels[i]
                notif_text += ',' + rrs.and__ + non_bio_rels[len(non_bio_rels) - 1]
            notif_text += '. '
    else:
        if inlaw_rels:
            notif_text += rrs.x_is_ys[f'{x_person}.{y_person}'] + inlaw_rels[0]
            if len(inlaw_rels) == 2:
                notif_text += rrs.and__ + inlaw_rels[1]
            elif len(inlaw_rels) > 2:
                for i in range(1, len(inlaw_rels) - 1):
                    notif_text += ', ' + inlaw_rels[i]
                notif_text += ',' + rrs.and__ + inlaw_rels[len(inlaw_rels) - 1]
            notif_text += '. '
            if step_rels:
                notif_text += rrs.x_is_ys[f'{x_person}..{y_person}'] + step_rels[0]
                if len(step_rels) == 2:
                    notif_text += rrs.and__ + step_rels[1]
                elif len(step_rels) > 2:
                    for i in range(1, len(step_rels) - 1):
                        notif_text += ', ' + step_rels[i]
                    notif_text += ',' + rrs.and__ + step_rels[len(step_rels) - 1]
                notif_text += '. '
        else:
            if step_rels:
                notif_text += rrs.x_is_ys[f'{x_person}.{y_person}'] + step_rels[0]
                if len(step_rels) == 2:
                    notif_text += rrs.and__ + step_rels[1]
                elif len(step_rels) > 2:
                    for i in range(1, len(step_rels) - 1):
                        notif_text += ', ' + step_rels[i]
                    notif_text += ',' + rrs.and__ + step_rels[len(step_rels) - 1]
                notif_text += '. '

    if x_person == 1 and y_person == 2:
        try:
            manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
            if sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x3DB4)):
                if rel_code == 0:
                    notif_text = 'I\'m so glad we aren\'t related.'
                    scumbumbo_show_notification(sim_x, sim_y, notif_text)
                    return
                else:
                    notif_text = notif_text + ' Doesn\'t mean I want anything to do with you.'
            if sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x79EB)):
                notif_text = 'Bro... ' + notif_text
            if sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x18961)):
                notif_text = 'What? I gave birth to you! ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x3DDF)):
                if rel_code < 2:
                    notif_text = 'You\'re my soulmate! ' + notif_text
                elif rel_code < 8:
                    notif_text = notif_text + ' I can\'t help being deeply in love with you, though.'
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x18465)):
                notif_text = 'I\'ve already promised myself to you, so it\'s a bit late to ask... ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x3DC8)):
                notif_text = notif_text + ' ...we\'re still on for the wedding, right?'
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x3DCE)):
                notif_text = 'Ah yes, the right time to double check is after we get married. ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x17B82)):
                notif_text = 'We JUST woohooed! ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x873B)):
                notif_text = 'We\'ve woohooed, and now you\'re asking? ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x27A6)):
                notif_text = 'We literally just had our first kiss. ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x27A6)):
                notif_text = 'Maybe you should\'ve asked before we kissed? ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x1F064)):
                notif_text = 'Checking to see if you should keep my number? ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x3DD9)):
                notif_text = 'Things are already weird. ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x3DDA)):
                notif_text = 'This relationship is already complicated. ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x3DDB)):
                notif_text = 'Everything\'s already really weird... ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x3DDC)):
                notif_text = 'This relationship is already SUPER complicated! ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x181C4)):
                notif_text = 'We\'ve already been flirting... it\'s a little late to ask. ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x1A36D)):
                notif_text = 'We work together. ' + notif_text
            elif sim_x.relationship_tracker.has_bit(sim_y.sim_id, manager.get(0x3DB0)):
                notif_text = 'Oh, right, you barely know me. ' + notif_text
        except Exception as e:
            riv_log('error: failed to add flavour to notif because ' + str(e))

    if show_consang:
        notif_text = notif_text + '\n\n[consanguinity: {num}%]'.format(num=round(100 * consang(sim_x, sim_y), 5))

    scumbumbo_show_notification(sim_x, sim_y, notif_text)
```
- **Purpose**: Generates and displays a notification for relationships between Sims.
- **How It Works**:
  1. Retrieves Sims and their ancestors.
  2. Gets lists of relationship strings and combines them.
  3. Formats the notification text based on relationship types.
  4. Displays the notification.
- **Why It’s Needed**: Provides a detailed and formatted notification about relationships between Sims.

#### Main Interaction Notification

```python
@sims4.commands.Command('riv_get_notif', command_type=sims4.commands.CommandType.Live)
def riv_get_notif(x_id: int, y_id: int, _connection=None):
    riv_get_notif_generic(x_id, y_id, 1, 2, _connection)
```
- **Purpose**: Provides a console command to get relationship notifications for the main interaction.
- **How It Works**:
  1. Calls the generic notification function with specific parameters.
- **Why It’s Needed**: Allows players or developers to trigger relationship notifications through the console.

#### Other Sim Interaction Notification

```python
@sims4.commands.Command('riv_get_notif_othersim', command_type=sims4.commands.CommandType.Live)
def riv_get_notif_othersim(x_id: int, y_id: int, _connection=None):
    riv_get_notif_generic(x_id, y_id, 1, 3, _connection)
```
- **Purpose**: Provides a console command to get relationship notifications for the "ask about other Sim" interaction.
- **How It Works**:
  1. Calls the generic notification function with specific parameters.
- **Why It’s Needed**: Allows players or developers to trigger relationship notifications through the console.

#### Load Sims from JSON

```python
def load_sims(file_name_extra: str):
    file_dir = Path(__file__).resolve().parent.parent
    file_name = f'riv_rel_{file_name_extra}.json'
    file_name2 = f'riv_currentsession_tmp_{file_name_extra}.json'
    file_path = os.path.join(file_dir, file_name)
    file_path2 = os.path.join(file_dir, file_name2)



    if os.path.isfile(file_path2):
        with open(file_path2, 'r') as json_file:
            sims = json.load(json_file)
    elif os.path.isfile(file_path):
        with open(file_path, 'r') as json_file:
            sims = json.load(json_file)
        if use_currentsession_files:
            riv_log('creating temporary file in load_sims for ' + file_name_extra)
            with open(file_path2, 'w') as json_file2:
                json.dump(sims, json_file2)
    else:
        sims = {}
    return sims
```
- **Purpose**: Loads Sims data from JSON files.
- **How It Works**:
  1. Checks for a temporary session file and reads from it if available.
  2. If not, reads from a permanent file and optionally creates a temporary session file.
  3. Returns the loaded Sims data.
- **Why It’s Needed**: Provides persistent storage and retrieval of Sims data between sessions.









### Function: Save Sims to JSON

```python
def save_sims(sims_input: List, file_name_extra: str):
    sim_time = services.time_service().sim_now.absolute_ticks()
    file_dir = Path(__file__).resolve().parent.parent
    file_name = f'riv_rel_{file_name_extra}.json'
    file_name2 = f'riv_currentsession_tmp_{file_name_extra}.json'
    file_path = os.path.join(file_dir, file_name)
    file_path2 = os.path.join(file_dir, file_name2)
    sims = []

    if os.path.isfile(file_path2) or not use_currentsession_files:
        game_sims = []
        for sim in sims_input:
            if isinstance(sim, RivSim):
                game_sims.append(sim)
            else:
                game_sims.append(RivSim(sim))
        riv_log('number of sims in game = ' + str(len(game_sims)))

        if (use_currentsession_files or not riv_sim_list.sims) and os.path.isfile(file_path):
            file_sims = [RivSim(sim) for sim in load_sims(file_name_extra)]
        else:
            file_sims = [RivSim(sim) for sim in riv_sim_list.sims]

        new_sims = []
        for sim_g in game_sims:
            sim_fg = None
            for sim_f in file_sims:
                if str(sim_g.sim_id) == str(sim_f.sim_id):
                    sim_fg = sim_f
                    break
            if sim_fg is None:
                new_sims.append(sim_g)
                riv_log(f'new sim: {sim_g.first_name} {sim_g.last_name} spawned {format_sim_date()}')
                if not use_currentsession_files:
                    riv_sim_list.sims.append(RivSim(sim_g))

        for sim_f in file_sims:
            sim_g = get_sim_from_rivsim(sim_f)
            if sim_f.time <= sim_time:
                if sim_g is None:
                    if not sim_f.is_culled:
                        sim_f.cull()
                else:
                    sim_f.update_info(sim_g.first_name, sim_g.last_name, sim_g.is_female, sim_time)
            sims.append(sim_f.to_dict())

        for sim_n in new_sims:
            sims.append(sim_n.to_dict())

        riv_log(f'number of new sims = {len(new_sims)}')
        riv_log(f'number of sims in file = {len(sims)}')

    else:
        if os.path.isfile(file_path):
            with open(file_path, 'r') as json_file:
                temp_sims = json.load(json_file)
            riv_log('creating temporary file in save_sims for ' + file_name_extra)
            with open(file_path2, 'w') as json_file2:
                json.dump(temp_sims, json_file2)
            return save_sims(sims_input, file_name_extra)
        else:
            game_sims = []
            for sim in sims_input:
                if isinstance(sim, RivSim):
                    game_sims.append(sim)
                else:
                    game_sims.append(RivSim(sim))
            riv_log(f'number of sims in game = {len(game_sims)}')
            sims = [sim_g.to_dict() for sim_g in game_sims]

    if use_currentsession_files:
        with open(file_path2, 'w') as json_file2:
            json.dump(sims, json_file2)

    if not os.path.isfile(file_path) or not use_currentsession_files:
        with open(file_path, 'w') as json_file:
            json.dump(sims, json_file)
        riv_log('created/updated perm file for sims ' + file_name_extra)

    riv_log('saved json files to ' + file_name_extra)
    riv_sim_list.sims = [RivSim(sim) for sim in sims]
```

#### Purpose

The `save_sims` function saves the current state of Sims to a JSON file. It updates both temporary and permanent files as needed.

#### How It Works

1. **Setup**: Define file paths and initialize the `sims` list.
2. **Check for Temporary File**: If a temporary file exists or the `use_currentsession_files` flag is not set, proceed with updating existing files.
3. **Load Sims from Game**: Convert the input Sims into `RivSim` objects and count them.
4. **Load Sims from File**: If necessary, load Sims from a permanent file into `file_sims`.
5. **Find New Sims**: Compare game Sims against file Sims and find new ones not already in the file.
6. **Update Sims Information**: Update information for Sims already in the file, handle culling if needed, and add new Sims to the list.
7. **Write Temporary File**: If `use_currentsession_files` is set, write the Sims to a temporary file.
8. **Write Permanent File**: Ensure the permanent file is created or updated with the latest Sims data.
9. **Update In-Memory List**: Update the global list of Sims in memory.

#### Why It’s Needed

This function ensures that the state of Sims is saved persistently across game sessions, allowing for data recovery and consistent game behavior.

### Function: Clean Sims

```python
def clean_sims(file_name_extra: str):
    dict_sims = load_sims(file_name_extra)

    sims = []
    for i in range(0, len(dict_sims)):
        if dict_sims[i] not in dict_sims[i + 1:]:
            sims.append(RivSim(dict_sims[i]))

    to_remove = []
    for sim_x in sims:
        for sim_y in sims:
            if sim_x.sim_id == sim_y.sim_id:
                if sim_x.time < sim_y.time:
                    if not sim_x in to_remove:
                        to_remove.append(sim_x)

    for sim in to_remove:
        sims.remove(sim)

    sim_time = services.time_service().sim_now.absolute_ticks()
    for rivsim in sims:
        sim = get_sim_from_rivsim(rivsim)
        if sim is not None:
            if rivsim.is_culled:
                if not sim_time < rivsim.time:
                    rivsim.uncull()

    output_sims = []
    for sim in sims:
        output_sims.append(sim.to_dict())

    file_dir = Path(__file__).resolve().parent.parent
    file_name = f'riv_rel_{file_name_extra}.json'
    file_name2 = f'riv_currentsession_tmp_{file_name_extra}.json'
    file_path = os.path.join(file_dir, file_name)
    file_path2 = os.path.join(file_dir, file_name2)

    if os.path.isfile(file_path2):
        with open(file_path2, 'w') as json_file2:
            json.dump(output_sims, json_file2)
```

#### Purpose

The `clean_sims` function removes duplicate Sims from the JSON file, ensuring only the most recent version of each Sim is kept.

#### How It Works

1. **Load Sims**: Load Sims from the JSON file.
2. **Remove Exact Duplicates**: Create a list of unique Sims by removing exact duplicates.
3. **Identify Older Versions**: Find older versions of Sims with the same ID.
4. **Remove Older Versions**: Remove these older versions from the list.
5. **Un-Cull Sims**: Mark Sims as active if they are present in the game and not culled.
6. **Save Cleaned List**: Write the cleaned list back to the temporary JSON file.

#### Why It’s Needed

This function ensures data integrity by removing outdated or duplicate entries, which can prevent data corruption and improve performance.

### Function: Save Relationships

```python
def save_rels(game_sims: List, file_name_extra: str):
    file_dir = Path(__file__).resolve().parent.parent
    file_name = f'riv_relparents_{file_name_extra}.json'
    file_name2 = f'riv_currentsession_tmpparents_{file_name_extra}.json'
    file_path = os.path.join(file_dir, file_name)
    file_path2 = os.path.join(file_dir, file_name2)
    rels = {}
    new_rels = {}

    for sim_x in game_sims:
        parents = get_parents_ingame(sim_x)
        parents_id = [parent.sim_id for parent in parents]
        new_rels[str(sim_x.sim_id)] = parents_id

    if os.path.isfile(file_path2) or not use_currentsession_files:
        if (use_currentsession_files or not riv_rel_dict.rels) and os.path.isfile(file_path):
            json_rels = riv_rel_dict.load_rels(file_name_extra)
        else:
            json_rels = riv_rel_dict.rels
        for sim in list(set(new_rels.keys()) | set(json_rels.keys())):
            rels[sim] = list(set(json_rels.get(sim, [])) | set(new_rels.get(sim, [])))
    else:
        if os.path.isfile(file_path):
            riv_log('creating temporary file in save_rels for ' + file_name_extra)
            with open(file_path, 'r') as json_file:
                temp_rels = json.load(json_file)
            with open(file_path2, 'w') as json_file2:
                json.dump(temp_rels, json_file2)
            return save_rels(game_sims, file_name_extra)
        else:
            rels = new_rels

    if not os.path.isfile(file_path) or not use_currentsession_files:
        with open(file_path, 'w') as json_file:
            json.dump(re

ls, json_file)
        riv_log('created/updated perm file for rels ' + file_name_extra)

    if use_currentsession_files:
        with open(file_path2, 'w') as json_file2:
            json.dump(rels, json_file2)
```

#### Purpose

The `save_rels` function saves the relationships between Sims, particularly parent-child relationships, to a JSON file.

#### How It Works

1. **Setup**: Define file paths and initialize dictionaries for relationships.
2. **Extract Parent Relationships**: For each Sim, extract parent relationships and store them in `new_rels`.
3. **Merge with Existing Data**: Merge `new_rels` with existing relationship data from the JSON file or memory.
4. **Write Temporary File**: If `use_currentsession_files` is set, write the relationships to a temporary file.
5. **Write Permanent File**: Ensure the permanent file is created or updated with the latest relationship data.

#### Why It’s Needed

This function maintains accurate and up-to-date relationship data, which is essential for gameplay mechanics that depend on family connections.

### Function: Console Commands

```python
@sims4.commands.Command('riv_save', command_type=sims4.commands.CommandType.Live)
def console_save_sims(file_name_extra: str, _connection=None):
    output = sims4.commands.CheatOutput(_connection)

    sim_time = services.time_service().sim_now
    abs_tick = sim_time.absolute_ticks()
    output(p(rrs.save_time).format(num=sim_time, datetime=format_sim_date()))
    output(p(rrs.save_abs_tick) + f'abs_tick = {abs_tick}')

    save_sims(services.sim_info_manager().get_all(), file_name_extra)
    output(p(rrs.save_sims_done))
    save_rels(services.sim_info_manager().get_all(), file_name_extra)
    output(p(rrs.save_rels_done))
    output(p(rrs.save_cmd) + f'riv_load {file_name_extra}\n[riv_save: {p(rrs.all_done)}]')
```

#### Purpose

The `console_save_sims` function is a console command for saving the current state of Sims and their relationships.

#### How It Works

1. **Output Save Time**: Display the current simulation time and absolute ticks.
2. **Save Sims**: Call `save_sims` to save the current state of Sims.
3. **Save Relationships**: Call `save_rels` to save the relationships between Sims.
4. **Output Completion**: Display messages indicating the completion of the save process.

#### Why It’s Needed

This function provides a convenient way to manually trigger the save process via the console, ensuring that data is saved at appropriate times during gameplay.

### Function: Load Sims from JSON

```python
@sims4.commands.Command('riv_load', command_type=sims4.commands.CommandType.Live)
def console_load_sims(file_name_extra: str, _connection=None):
    output = sims4.commands.CheatOutput(_connection)

    try:
        riv_sim_list.load_sims(file_name_extra)
        riv_rel_dict.load_rels(file_name_extra)
        output(p(rrs.load_done).format(num=len(riv_sim_list.sims)) + '\n' + p(rrs.load_random))
        randsim = random.choice(riv_sim_list.sims)
        output(str(randsim.to_dict()))
        randparents = riv_rel_dict.rels.get(randsim.sim_id, [])
        output(str(randparents))
        for parent in randparents:
            for sim in riv_sim_list.sims:
                if str(parent) == sim.sim_id:
                    output(sim.first_name + ' ' + sim.last_name)
                    break
    except Exception as e:
        output(rrs.load_error_0 + ': ' + str(e))
        output(rrs.load_error_1)
        output(f'riv_rel_{file_name_extra}.json and riv_relparents_{file_name_extra}.json')
        output(rrs.load_error_2)

    output(f'[riv_load: {rrs.all_done}]')
```

#### Purpose

The `console_load_sims` function loads Sims and their relationships from JSON files into memory.

#### How It Works

1. **Initialize Output**: Prepare the console output.
2. **Load Sims and Relationships**: Load Sims and their relationships from the specified JSON files.
3. **Display Loaded Sims**: Output information about the loaded Sims and their relationships.
4. **Error Handling**: Handle and display errors if loading fails.

#### Why It’s Needed

This function ensures that the game can load previously saved Sims and their relationships, maintaining continuity across game sessions.

### Function: Show Sims in Memory

```python
@sims4.commands.Command('riv_mem', command_type=sims4.commands.CommandType.Live)
def console_mem_sims(_connection=None):
    output = sims4.commands.CheatOutput(_connection)

    output(f'riv_sim_list = {riv_sim_list}')
    sims = riv_sim_list.sims
    if sims:
        output(rrs.mem_randsim)
        randsim = random.choice(sims)
        output(str(randsim))
        output(str(randsim.to_dict()))
    else:
        output(rrs.mem_load)

    output(f'riv_rel_dict = {riv_rel_dict}')
    rels = riv_rel_dict.rels
    if rels:
        output(rrs.mem_randrel)
        randsim = random.choice(sims)
        output(str(randsim))
        output(str(riv_rel_dict.rels[randsim.sim_id]))
    else:
        output(rrs.mem_load)

    output(f'[riv_mem: {rrs.all_done}]')
```

#### Purpose

The `console_mem_sims` function displays the Sims and their relationships currently loaded in memory.

#### How It Works

1. **Initialize Output**: Prepare the console output.
2. **Display Sims**: Output information about the Sims currently in memory.
3. **Display Relationships**: Output information about the relationships currently in memory.

#### Why It’s Needed

This function helps to debug and verify that the correct Sims and relationships are loaded in memory during gameplay.

### Function: Clean Sims Data

```python
@sims4.commands.Command('riv_clean', command_type=sims4.commands.CommandType.Live)
def console_clean_sims(file_name_extra: str, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    sims = load_sims(file_name_extra)
    old_n = len(sims)
    old_c = len([rsim for rsim in sims if rsim['is_culled']])
    output(rrs.clean_start.format(n=old_n, c=old_c))
    clean_sims(file_name_extra)
    sims = load_sims(file_name_extra)
    new_n = len(sims)
    new_c = len([rsim for rsim in sims if rsim['is_culled']])
    output(rrs.clean_end.format(n=new_n))
    if old_c > new_c:
        output(rrs.clean_uncull.format(m=old_c - new_c))
    if old_n < new_n:
        output(rrs.clean_update + ' ' + file_name_extra)
    output(f'[riv_clean: {rrs.all_done}]')
```

#### Purpose

The `console_clean_sims` function cleans the Sims data, removing duplicates and updating the status of Sims.

#### How It Works

1. **Initialize Output**: Prepare the console output.
2. **Load and Clean Sims**: Load Sims from the specified file, clean the data, and reload the cleaned Sims.
3. **Display Results**: Output information about the cleaning process and the new state of the Sims.

#### Why It’s Needed

This function ensures data integrity by removing outdated or duplicate entries and updating the status of Sims, which is crucial for maintaining a consistent and error-free gameplay experience.

### Function: Clear Sims Data

```python
@sims4.commands.Command('riv_clear', command_type=sims4.commands.CommandType.Live)
def console_clear_sims(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    riv_sim_list.clear_sims()
    riv_rel_dict.clear_rels()

    file_dir = Path(__file__).resolve().parent.parent
    for file in os.scandir(file_dir):
        if file.name.startswith('riv_currentsession_tmp') and file.name.endswith('.json'):
            os.remove(os.path.join(file_dir, file))
            riv_log('deleted ' + file.name)
            output(rrs.clear_0 + ' ' + file.name)

    output(f'[riv_clear: {rrs.all_done}]')
```

#### Purpose

The `console_clear_sims` function clears all Sims and their relationships from memory and deletes temporary files.

#### How It Works

1. **Initialize Output**: Prepare the console output.
2. **Clear Memory**: Clear all Sims and relationships from memory.
3. **Delete Temporary Files**: Delete temporary files related to Sims data.
4. **Display Results**: Output information about the clearing process.

#### Why It’s Needed

This function helps to reset the game's data state, which can be useful for debugging, testing, or starting a new game session without residual data.

### Function: Update Sims Data

```python
@sims4.commands.Command('riv_update', command_type=sims4.commands.CommandType.Live)
def console_update_sims(file_name_extra: str, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    file_dir = Path(__file__).resolve().parent.parent
    file_name = f'riv_rel_{file_name_extra}.json'
    file_path = os.path.join(file_dir, file_name)
    if os.path.isfile(file_path):
        output(rrs.update_exists)
        console_load_sims(file_name_extra, _connection)
    output(rrs.update_desc)
    console_save_sims(file_name_extra, _connection)
    console_clear_sims(_connection)
    console_load_sims(file_name_extra, _connection)
    output(f'[riv_update: {rrs.all_done}]')
```

#### Purpose

The `console_update_sims` function updates the Sims data in JSON files.

#### How It Works

1. **Initialize Output**: Prepare the console output.
2. **Check Existing File**: Check if the specified file exists and load Sims from it if it does.
3. **Save, Clear, and Reload Sims**: Save the current state of Sims, clear the memory, and reload Sims from the updated file.
4. **Display Results**: Output information about the update process.

#### Why It’s Needed

This function ensures that the latest state of Sims is saved and reloaded, providing a mechanism to update the Sims data during gameplay.

### Function: Fix Configuration Settings

```python
def fix_cfg_settings():
    config_dir = Path(__file__).resolve().parent.parent
    config_name = 'riv_rel - individual save settings.cfg'
    file_path = os.path.join(config_dir, config_name)
    config = configparser.ConfigParser()
    if os.path.isfile(file_path):
        config.read_file(open(file_path, 'r'))

    for slot_id in config.sections():
        keys = []
        for (key, val) in config.items(slot_id):
            if key not in keys:
                keys.append(key)
        for key in list(cfg_default_vals.keys()) + keys:
            if key not in keys:
                val = cfg_default_vals[key]
                config[slot_id][key] = val
                riv_log(f'set {key} for save {slot_id} to default value {val}')
            elif key not in cfg_default_vals.keys():
                del config[slot_id][key]
                riv_log(f'removed invalid key {key} from settings for save {slot_id}')

    with open(file_path, 'w') as cfg_file:
        config.write(cfg_file)
```

#### Purpose

The `fix_cfg_settings` function ensures that the configuration settings for the mod are correct and complete, adding default values where necessary and removing invalid keys.

#### How It Works

1. **Load Configuration**: Load the configuration file if it exists.
2. **Check and Fix Keys**: For each save slot, ensure all necessary keys are present with default values and remove any invalid keys.
3. **Save Configuration**: Write the updated configuration back to the file.

#### Why It’s Needed

This function ensures that the configuration settings are valid and up-to-date, preventing potential issues caused by missing or incorrect settings.

### Function: Load Configuration Settings

```python
def load_cfg_settings(attempt_number=1):
    global hex_slot_id
    global file_name_extra
    global riv_auto_enabled
    global global_include_step_rels
    global use_currentsession_files

    config_dir = Path(__file__).resolve().parent.parent
    config_name = 'riv_rel - individual save settings.cfg'
    file_path = os.path.join(config_dir, config_name)
    config = configparser.ConfigParser()

    if os.path.isfile(file_path):
        config.read_file(open(file_path, 'r'))
        if hex_slot_id in config.sections():
            try:
                file_name_extra = config.get(hex_slot_id, 'file_name_extra')
                riv_log(f'loading in cfg settings: {hex_slot_id} {file_name_extra}')

                riv_auto_enabled = config.getboolean(hex_slot_id, 'auto_update_json')
                riv_log(f'auto_update_json set to {riv_auto_enabled}')
                if riv_auto_enabled:
                    riv_log('json updates enabled')
                else:
                    riv_log('json updates disabled')

                try:
                    global_include_step_rels = config.getboolean(hex_slot_id, 'include_step_rels')
                    if global_include_step_rels:
                        riv_log('including step rels')
                    else:
                        riv_log('excluding step rels')
                except:
                    pass

                use_currentsession_files = config.getboolean(hex_slot_id, 'advanced_use_currentsession_files')
                if use_currentsession_files:
                    riv_log('using currentsession files')
                else:
                    riv_log('not using currentsession files')

            except Exception as e1:
                if attempt_number == 1:
                    try:
                        riv_log('some keys were missing in the cfg. fixing file...')
                        fix_cfg_settings()
                    except Exception as e2:
                        riv_log('error in fixing cfg settings: ' + str(e2))
                    return load_cfg_settings(2)
                else:
                    riv_log('error in loading cfg settings: ' + str(e1))
        else:
            riv_log(f'no cfg settings for save {hex_slot_id}')
            file_name_extra = ''
            riv_auto_enabled = False
            riv_log('json updates disabled')

            try:
                global_include_step_rels = true_false(cfg_default_vals['include_step_rels'])
            except:
                global_include_step_rels = False

            if global_include_step_rels:
                riv_log('including step rels')
            else:
                riv_log('excluding step rels')

            use_currentsession_files = true_false(cfg_default_vals['advanced_use_currentsession_files'])
            if use_currentsession_files:
                riv_log('using currentsession files')
            else:
                riv_log('not using currentsession files')
```

#### Purpose

The `load_cfg_settings` function loads the configuration settings for the current game save from a configuration file.

#### How It Works

1. **Initialize Globals**: Prepare the global variables to be updated.
2. **Load Configuration File**: Check if the configuration file exists and load it.
3. **Load Settings**: Retrieve settings for the current save slot. If settings are missing, fix the configuration file and reload.
4. **Error Handling**: Handle errors and log relevant information.

#### Why It’s Needed

This function ensures that the game loads the correct settings for the current save slot, enabling or disabling automatic updates and other features based on the configuration.

### Function: Manual Configuration Loading Command

```python
@sims4.commands.Command('riv_load_cfg_manually', command_type=sims4.commands.CommandType.Live)
def console_load_cfg_manually(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    try:
        hsi = get_slot()
        if hsi not in ['00000000'] + mccc_autosaves:
            global hex_slot_id
            hex_slot_id = hsi
            load_cfg_settings()
            output(rrs.load_cfg_save.format(slot_id=hex_slot_id))
        else:
            output(rrs.load_cfg_save0)
            output(f'[riv_load_cfg_manually: {rrs.all_done}]')
            return
    except Exception as e:
        output(rrs.load_cfg_error)
        output(str(e))
        return
    if not file_name_extra == '':
        output(rrs.load_cfg_update.format(keyword=file_name_extra))
        console_update_sims(file_name_extra, _connection)
    else:
        output(rrs.load_cfg_nexists)
    output(f'[riv_load_cfg_manually: {rrs.all_done}]')
```

#### Purpose

The `console_load_cfg_manually` function allows users to manually load the configuration settings for the current save slot via a console command.

#### How It Works

1. **Initialize Output**: Prepare the console output.
2. **Get Save Slot**: Retrieve the current save slot.
3. **Load Settings**: Load the configuration settings for the save slot.
4. **Update Sims**: If a configuration is loaded, update the Sims data.
5. **Error Handling**: Handle and display errors if loading fails.

#### Why It’s Needed

This function provides a manual way to load and apply configuration settings, which is useful for debugging and ensuring the correct settings are applied during gameplay.

### Function: Automatic JSON Updates

```python
def auto_json(new_sim=None):
    if riv_auto_enabled and not file_name_extra == '':
        sim_time = services.time_service().sim_now.absolute_ticks()

        if use_currentsession_files:
            riv_log('running auto_json with currentsession files...')
            save_sims(services.sim_info_manager().get_all(), file_name_extra)
            save_rels(services.sim_info_manager().get_all(), file_name_extra)
            riv_sim_list.load_sims(file_name_extra)
            riv_rel_dict.load_rels(file_name_extra)

        else:
            if not riv_sim_list.sims or not riv_rel_dict.rels:
                riv_log('auto_json is loading in sims and rels...')
                riv_sim_list.load_sims(file_name_extra)
                riv_rel_dict.load_rels(file_name_extra)

            if new_sim is None:
                riv_log('running auto_json without currentsession files...')
                game_sims = [RivSim(sim) for sim in services.sim_info_manager().get_all()]
                riv_log(f'number of sims in game = {len(game_sims)}')
                file_sims = [RivSim(sim) for sim in riv_sim_list.sims]
                new_sims = []
                sims = []
                for sim_g in game_sims:
                    sim_fg = None
                    for sim_f in file_sims:
                        if str(sim_g.sim_id) == str(sim_f.sim_id):
                            sim_fg = sim_f
                            break
                    if sim_fg is None:
                        new_sims.append(sim_g)
                        riv_log(f'new sim: {sim_g.first_name} {sim_g.last_name} spawned {format_sim_date()}')
                for sim_f in file_sims:
                    sim_g = get_sim_from_rivsim(sim_f)
                    if sim_f.time <= sim_time:
                        if sim_g is None:
                            if not sim_f.is_culled:
                                sim_f.cull()
                        else:
                            sim_f.update_info(sim_g.first_name, sim_g.last_name, sim_g.is_female, sim_time)
                    sims.append(sim_f)
                new_rels = {}
                for sim_x in game_sims:
                    parents = get_parents_ingame(sim_x)
                    parents_id = [parent.sim_id for parent in parents]
                    new_rels[str(sim_x.sim_id)] = parents_id

            else:
                riv_log(f'running auto_json for just {new_sim.first_name} {new_sim.last_name}...')
                sims = riv_sim_list.sims
                file_sim = get_rivsim_from_sim(new_sim)
                new_rels = {}
                new_sims = []
                if file_sim is None:
                    riv_log(f'auto_json created rivsim for {new_sim.first_name} {new_sim.last_name}')
                    new_sims.append(RivSim(new_sim))
                if str(new_sim.sim_id) not in riv_rel_dict.rels.keys():
                    new_parents = []
                    for new_parent in get_parents_ingame(file_sim):
                        file_parent = get_rivsim_from_sim(new_parent)
                        if file_parent is None:
                            riv_log(f'calling auto_json for parent {new_parent.first_name} {new_parent.last_name}...')
                            auto_json(new_parent)
                            new_parents.append(get_rivsim_from_sim(new_parent))
                        else:
                            new_parents.append(file_parent)
                    new_rels[str(new_sim.sim_id)] = [int(p.sim_id) for p in new_parents]

            for sim_n in new_sims:
                sims.append(sim_n)
            riv_sim_list.sims = sims.copy()

            if new_rels:
                for sim_id in list(set(new_rels.keys()) | set(riv_rel_dict.rels.keys())):
                    riv_rel_dict.rels[sim_id] = list(
                        set(riv_rel_dict.rels.get(sim_id, [])) | set(new_rels.get(sim_id, [])))

            if new_sim is not None:
                if new_sims:
                    riv_log('number of new sims = ' + str(len(new_sims)))
                    riv_log('len(sims) = ' + str(len(sims)))
                    riv_log('updated sim list in mem')

        riv_log('ran auto_json')
    else:
        riv_sim_list.sims = [RivSim(sim) for sim in services.sim_info_manager().get_all()]
        riv_log('set up riv sim list without json file')
        for riv_sim in riv_sim_list.sims:
            parents = get_parents_ingame(r

iv_sim)
            riv_rel_dict.rels[riv_sim.sim_id] = [parent.sim_id for parent in parents]
        riv_log('set up riv rel dict without json file')
```

#### Purpose

The `auto_json` function automatically updates the JSON files containing Sims data and their relationships, either incrementally or entirely, depending on whether the current session files are used.

#### How It Works

1. **Check Configuration**: Ensure automatic updates are enabled and a file name is provided.
2. **Save and Load Sims Data**: Save current Sims data to JSON files and load existing data.
3. **Update Sims Data**: Add new Sims, update existing ones, and manage relationships.
4. **Handle New Sim**: If a new Sim is provided, process only that Sim and its parents.

#### Why It’s Needed

This function automates the process of saving and updating Sims data, ensuring that the game state is consistently saved and updated, which is crucial for maintaining game integrity and avoiding data loss.

### Function: Console Command to Set Up Automatic JSON Updates

```python
@sims4.commands.Command('riv_auto', command_type=sims4.commands.CommandType.Live)
def console_auto_json(file_name_extra: str, _connection=None):
    output = sims4.commands.CheatOutput(_connection)

    global hex_slot_id
    hex_slot_id = get_slot()

    if hex_slot_id not in mccc_autosaves:
        file_dir = Path(__file__).resolve().parent.parent
        config_name = 'riv_rel - individual save settings.cfg'
        file_path = os.path.join(file_dir, config_name)
        config = configparser.ConfigParser()

        try:
            config.read_file(open(file_path, 'r'))
        except:
            output(rrs.auto_makecfg)

        if hex_slot_id in config.sections():
            output(rrs.auto_update.format(num=hex_slot_id))
        else:
            output(rrs.auto_add.format(num=hex_slot_id))
            config[hex_slot_id] = {}

        config[hex_slot_id]['file_name_extra'] = file_name_extra
        config[hex_slot_id]['auto_update_json'] = 'True'

        with open(file_path, 'w') as cfg_file:
            config.write(cfg_file)
            riv_log(f'added/updated cfg settings: slot {hex_slot_id} with word {file_name_extra}')

        output(rrs.auto_load_cfg)
        load_cfg_settings()

        sims_file_name = f'riv_rel_{file_name_extra}.json'
        sims_file_path = os.path.join(file_dir, sims_file_name)
        if os.path.isfile(sims_file_path):
            output(rrs.auto_load_sim)
            riv_sim_list.load_sims(file_name_extra)

        rels_file_name = f'riv_relparents_{file_name_extra}.json'
        rels_file_path = os.path.join(file_dir, rels_file_name)
        if os.path.isfile(rels_file_path):
            output(rrs.auto_load_rel)
            riv_rel_dict.load_rels(file_name_extra)

        output(rrs.auto_sccl)
        console_save_sims(file_name_extra, _connection)
        console_clear_sims(_connection)
        console_clean_sims(file_name_extra, _connection)
        console_load_sims(file_name_extra, _connection)

        output(f'[riv_auto: {rrs.all_done}]')
    else:
        output(rrs.auto_blocked0)
        output(rrs.auto_blocked1)
        output(rrs.auto_blocked2)
```

#### Purpose

The `console_auto_json` function allows users to set up automatic JSON updates for the current save slot via a console command.

#### How It Works

1. **Set Current Slot**: Retrieve and set the current save slot.
2. **Check Slot Type**: Ensure the slot is not an autosave slot.
3. **Update Configuration**: Load or create the configuration file and update settings.
4. **Load and Save Sims Data**: Load existing Sims data, save new data, and update relationships.
5. **Output Results**: Provide feedback to the user via the console output.

#### Why It’s Needed

This function automates the setup process for saving and updating Sims data, making it easier for users to maintain game state and avoid data loss.

### Function: Inject to SimInfoManager for Loading Screen Animation Finished

```python
@inject_to(SimInfoManager, 'on_loading_screen_animation_finished')
def get_slot_olsaf(original, self, *args, **kwargs):
    result = original(self, *args, **kwargs)

    try:
        global riv_allow_auto_json_simi
        riv_allow_auto_json_simi = True
        riv_log(f'riv_allow_auto_json_simi = True', 3)
    except Exception as e:
        riv_log(f'error in setting auto_json for one sim info in on_loading_screen_animation_finished: {e}')

    try:
        hsi = get_slot()
        if hsi not in ['00000000'] + mccc_autosaves:
            global hex_slot_id
            hex_slot_id = hsi
        else:
            riv_log(f'didn\'t change save ID in get_slot_olsaf to {hsi}')
    except Exception as e:
        riv_log(f'error in get_slot_olsaf in on_loading_screen_animation_finished: {e}')
        raise Exception(f'(riv) error in get_slot_olsaf in on_loading_screen_animation_finished: {e}')
    return result
```

#### Purpose

The `get_slot_olsaf` function is injected into the `SimInfoManager` to be executed when the loading screen animation finishes. It sets up automatic JSON updates for a single Sim and retrieves the current save slot.

#### How It Works

1. **Call Original Function**: Execute the original function logic.
2. **Set Auto JSON for Single Sim**: Enable auto JSON updates for a single Sim.
3. **Get Slot**: Retrieve the current save slot and update the global slot ID.
4. **Error Handling**: Log and handle any errors that occur during execution.

#### Why It’s Needed

This function ensures that automatic JSON updates are correctly set up when the loading screen finishes, maintaining game state consistency and enabling seamless updates.

### Function: Inject to SimInfoManager for All Households and Sim Infos Loaded

```python
@inject_to(SimInfoManager, 'on_all_households_and_sim_infos_loaded')
def auto_json_oahasil(original, self, client):
    result = original(self, client)

    try:
        global jsyk_ownfolder
        global hex_slot_id
        old_hsi = hex_slot_id
        hsi = get_slot()
        if hsi not in ['00000000'] + mccc_autosaves:
            hex_slot_id = hsi
            riv_log(f'save ID replaced by {hex_slot_id}')
        else:
            riv_log(f'save ID not loaded in, as it was {hsi}')
            if (not riv_sim_list.sims) and riv_auto_enabled:
                scumbumbo_show_notif_texttitle(
                    'failed to load in sims for this save ID: this usually happens when you\'ve just left CAS, you quit'
                    ' a different save without saving and then loaded this one, or you moved/deleted the .json files. '
                    '\nif you have not (or aren\'t about to) set up auto .json file updates for this save ID please '
                    'ignore this notification. \notherwise, please save your game and then enter the following into '
                    'the command line (CTRL+SHIFT+C): \n\nriv_load_cfg_manually',
                    'riv_rel issue')
        if old_hsi != hex_slot_id:
            if old_hsi not in ['00000000'] + mccc_autosaves:
                riv_sim_list.clear_sims()
                riv_rel_dict.clear_rels()
                riv_log('cleared sims and rels')
            else:
                if old_hsi == '00000000':
                    file_dir = Path(__file__).resolve().parent.parent
                    for file in os.scandir(file_dir):
                        if not file.name.startswith('riv'):
                            jsyk_ownfolder = True
                        if file.name.startswith('riv_currentsession_tmp') and file.name.endswith('.json'):
                            os.remove(os.path.join(file_dir, file))
                            riv_log('deleted ' + file.name)

    except Exception as e:
        riv_log(f'error in getting the slot ID in on_all_households_and_sim_infos_loaded: {e}')
        raise Exception(f'(riv) error in getting the slot ID in on_all_households_and_sim_infos_loaded: {e}')

    try:
        load_cfg_settings()
    except Exception as e:
        riv_log(f'error in load_cfg_settings in on_all_households_and_sim_infos_loaded: {e}')
        raise Exception(f'(riv) error in load_cfg_settings in on_all_households_and_sim_infos_loaded: {e}')

    try:
        auto_json()
        riv_log('ran auto_json_oahasil')

        global ex_opener
        global ex_mccc_autosaves_str
        global ex_hex_slot_id
        global ex_file_name_extra

        if riv_auto_enabled and hex_slot_id not in mccc_autosaves:
            riv_log('   with riv_auto_enabled = true, slot ID is not an autosave')
            opener = 'loaded in settings from riv_rel - individual save settings.cfg for save ID {save_id} and keyword {keyword}.\n\nsim mini-infos: ' \
                .format(save_id=hex_slot_id, keyword=file_name_extra)
        elif riv_auto_enabled and hex_slot_id in mccc_autosaves:
            riv_log('   with riv_auto_enabled = true, slot ID is an autosave (ERROR)')
            opener = ''
            scumbumbo_show_notif_texttitle(
                'you\'ve created settings for an MCCC autosave - this won\'t work properly!\n\nplease save your game to another slot and set up riv_auto again.',
                'riv_rel: auto json issue')
        elif hex_slot_id in mccc_autosaves:
            riv_log('   with riv_auto_enabled = false, slot ID is an autosave')
            opener = 'you\'ve loaded up an autosave slot! to use riv_auto backups, please save the game to another slot first (if you don\'t want to use riv_auto, you don\'t need to do this)\n\nnumber of sims: '
        else:
            riv_log('   with riv_auto_enabled = false, slot ID is not an autosave')
            opener = 'no sim/rel backups were found for this save - if you\'re expecting to see json file backups or want to set them up, enter riv_auto xyz into the

 cheat console for a keyword xyz!\n\nnumber of sims: '

        if jsyk_ownfolder:
            ownfolder_warning = 'you have other files in the same folder as my mod - i would recommend putting all files starting riv_rel in their own subfolder (i.e. in Mods/riv_rel/) if you encounter any additional lag on save/load. '
        else:
            ownfolder_warning = ''
        if mccc_autosaves and riv_auto_enabled:
            mccc_autosaves_str = '\n\nfound MCCC autosave slots (my mod will continue to see the save slot as {slot_id} if the actual save slot changes to one of these): {autosave_list}' \
                .format(slot_id=hex_slot_id, autosave_list=mccc_autosaves)
        else:
            mccc_autosaves_str = ''
        if addons['computer']:
            computer_str = '\n\nyou can see more information and help in the "Research on riv_rel.sim" menu on the computer'
        else:
            computer_str = ''
        if addons['GT'] and not addons['traits']:
            ownfolder_warning += '\n\nyou\'ve downloaded the GT addon without the traits addon - please either download riv_rel_addon_traits or remove riv_rel_addon_GT or you may face glitches with clubs being unable to find my family traits!'

        if opener:
            num_sims = str(len(riv_sim_list.sims))
        else:
            num_sims = ''

        if [ex_opener, ex_mccc_autosaves_str, ex_hex_slot_id, ex_file_name_extra] != \
                [opener, mccc_autosaves_str, hex_slot_id, file_name_extra]:
            ex_opener = opener
            ex_mccc_autosaves_str = mccc_autosaves_str
            ex_hex_slot_id = hex_slot_id
            ex_file_name_extra = file_name_extra

            scumbumbo_show_notif_texttitle(
                f'{opener}{num_sims} {mccc_autosaves_str}\n\nif this is the wrong file, run riv_clear, save your game, and run riv_load_cfg_manually.{ownfolder_warning}{computer_str}\n\nthank you for using my mod! '
                , f'riv_rel gen {rr_gen}')

    except Exception as e:
        riv_log(f'error in auto_json in on_all_households_and_sim_infos_loaded: {e}')
        raise Exception(f'(riv) error in auto_json in on_all_households_and_sim_infos_loaded: {e}')

    return result
```

#### Purpose

The `auto_json_oahasil` function is injected into the `SimInfoManager` to be executed when all households and Sim infos are loaded. It sets the slot ID, loads configuration settings, and triggers automatic JSON updates.

#### How It Works

1. **Call Original Function**: Execute the original function logic.
2. **Set Slot ID**: Retrieve and update the global slot ID.
3. **Clear Data if Slot Changes**: Clear Sims and relationships data if the slot ID changes.
4. **Load Configuration**: Load configuration settings for the current slot.
5. **Run Auto JSON**: Trigger automatic JSON updates.
6. **Show Notifications**: Display relevant notifications to the user.
7. **Error Handling**: Log and handle any errors that occur during execution.

#### Why It’s Needed

This function ensures that configuration settings and Sims data are correctly managed and updated when the game loads all households and Sim infos, maintaining consistency and integrity of the game state.

### Function: Check if Two Sims are an Eligible Couple

```python
@lru_cache(maxsize=None)
def is_eligible_couple(x_id, y_id):
    if x_id == y_id:
        return False, 'mate, that\'s just being single with extra steps'

    sim_x = get_rivsim_from_id(x_id)
    sim_y = get_rivsim_from_id(y_id)

    if drel_incest and get_direct_relation(sim_x, sim_y):
        return False, '{x_firstname} and {y_firstname} are not an eligible couple: they are directly related' \
            .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name)

    xy_consang = consang(sim_x, sim_y)
    if xy_consang >= consang_limit:
        return False, '{x_firstname} and {y_firstname} are not an eligible couple: over the consanguinity limit' \
            .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name)

    return True, '{x_firstname} and {y_firstname} are an eligible couple with your settings!' \
        .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name)
```

#### Purpose

The `is_eligible_couple` function checks if two Sims are an eligible couple based on direct relationships and consanguinity limits.

#### How It Works

1. **Self-Relationship Check**: Ensures that a Sim is not considered an eligible couple with themselves.
2. **Retrieve Sims**: Converts Sim IDs to RivSim objects.
3. **Direct Relationship Check**: Verifies if the Sims are directly related.
4. **Consanguinity Check**: Checks if the consanguinity (genetic relatedness) between the Sims is within the allowed limit.
5. **Eligibility Result**: Returns whether the Sims are an eligible couple along with a corresponding message.

#### Why It’s Needed

This function ensures that relationships between Sims adhere to defined rules, preventing inappropriate relationships and maintaining the integrity of the family tree.

### Function: Inject to SimInfoManager for Spin Up Action

```python
@inject_to(SimInfoManager, 'get_sims_for_spin_up_action')
def riv_get_sims_for_spin_up_action(original, self, action):
    result = original(self, action)
    try:
        preroll_consang_tic = time.perf_counter()
        instanced_sims = list(services.sim_info_manager().instanced_sims_gen())
        riv_log(f'number of instanced sims found: {len(instanced_sims)}')
        for sim_x in instanced_sims:
            for sim_y in instanced_sims:
                if sim_x.sim_id < sim_y.sim_id:
                    is_eligible_couple(sim_x.sim_id, sim_y.sim_id)
        preroll_consang_toc = time.perf_counter()
        riv_log(f'pre-rolled consanguinities of instanced sims - it took {preroll_consang_toc - preroll_consang_tic}s')
    except Exception as e:
        riv_log(f'error in pre-rolling consanguinities in get_sims_for_spin_up_action: {e}')

    return result
```

#### Purpose

The `riv_get_sims_for_spin_up_action` function is injected into the `SimInfoManager` to perform pre-roll consanguinity checks when the spin-up action is initiated.

#### How It Works

1. **Call Original Function**: Executes the original spin-up action logic.
2. **Pre-Roll Consanguinity Checks**: Iterates over all instanced Sims to pre-calculate consanguinity values.
3. **Logging**: Logs the number of instanced Sims and the time taken for pre-rolling consanguinities.
4. **Error Handling**: Logs any errors encountered during execution.

#### Why It’s Needed

Pre-rolling consanguinities ensures that relationship checks are more efficient during gameplay, reducing the computational load when determining eligible couples.

### Function: Inject to Zone for Zone Load

```python
@inject_to(Zone, 'load_zone')
def riv_load_zone(original, self):
    result = original(self)
    try:
        global riv_allow_auto_json_simi
        riv_allow_auto_json_simi = False
        riv_log(f'riv_allow_auto_json_simi = False', 3)
    except Exception as e:
        riv_log(f'error in riv_load_zone: {e}')

    return result
```

#### Purpose

The `riv_load_zone` function is injected into the `Zone` class to reset the `riv_allow_auto_json_simi` flag when a zone is loaded.

#### How It Works

1. **Call Original Function**: Executes the original zone load logic.
2. **Reset Flag**: Sets the `riv_allow_auto_json_simi` flag to `False`.
3. **Logging**: Logs the reset action.
4. **Error Handling**: Logs any errors encountered during execution.

#### Why It’s Needed

Resetting the `riv_allow_auto_json_simi` flag ensures that automatic JSON updates for a single Sim are disabled when a new zone is loaded, preventing unintended updates.

### Function: Inject to SimInfoManager for Adding Sim Info

```python
@inject_to(SimInfoManager, 'add_sim_info_if_not_in_manager')
def auto_json_fam_asiinim(original, self, sim_info):
    result = original(self, sim_info)
    try:
        if riv_allow_auto_json_simi:
            auto_json(sim_info)
            riv_log('ran auto_json_asiinim')
            if sim_info is None:
                riv_log(f'  NoneSim WithLeftBeef')
    except Exception as e:
        riv_log(f'error in auto_json in add_sim_info_if_not_in_manager: {e}')
        raise Exception(f'(riv) error in auto_json in add_sim_info_if_not_in_manager: {e}')
    return result
```

#### Purpose

The `auto_json_fam_asiinim` function is injected into the `SimInfoManager` to perform automatic JSON updates when a new Sim is added to the manager.

#### How It Works

1. **Call Original Function**: Executes the original logic for adding Sim info.
2. **Automatic JSON Update**: Triggers the `auto_json` function if the `riv_allow_auto_json_simi` flag is set.
3. **Logging**: Logs the automatic JSON update action.
4. **Error Handling**: Logs and raises any errors encountered during execution.

#### Why It’s Needed

This function ensures that the game's Sim information is consistently updated in the JSON files whenever new Sims are added, maintaining accurate and up-to-date records.

### Function: Inject to SimInfo for Adding Parent Relations

```python
@inject_to(SimInfo, 'add_parent_relations')
def auto_json_fam_apr(original, self, parent_a, parent_b):
    result = original(self, parent_a, parent_b)
    try:
        auto_json(self)

        new_parents = [parent_a.sim_id, parent_b.sim_id]
        sim_id = str(self.sim_id)
        if new_parents:
            riv_rel_dict.rels[sim_id] = list(set(riv_rel_dict.rels.get(sim_id, [])) | set(new_parents))

        riv_log(f'ran auto_json_apr with sim {self.first_name} and parents {parent_a.first_name} and {parent_b.first_name}')
    except Exception as e:
        riv_log(f'error in auto_json in add_parent_relations: {e}')
        raise Exception(f'(riv) error in auto_json in add_parent_relations: {e}')
    return result
```

#### Purpose

The `auto_json_fam_apr` function is injected into the `SimInfo` class to perform automatic JSON updates when parent relations are added.

#### How It Works

1. **Call Original Function**: Executes the original logic for adding parent relations.
2. **Automatic JSON Update**: Triggers the `auto_json` function for the Sim.
3. **Update Parent List**: Updates the parent list in the relationship dictionary.
4. **Logging**: Logs the automatic JSON update action.
5. **Error Handling**: Logs and raises any errors encountered during execution.

#### Why It’s Needed

This function ensures that family relationships are accurately reflected in the JSON files when parent relations are added, maintaining the integrity of the family tree.

### Function: Inject to RelationshipBit for Adding to Relationship

```python
@inject_to(RelationshipBit, 'on_add_to_relationship')
def auto_json_fam_oatr(original, self, sim, target_sim_info, relationship, from_load):
    result = original(self, sim, target_sim_info, relationship, from_load)
    try:
        manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
        parent_relbit = manager.get(0x2269)
        if self.matches_bit(parent_relbit):
            riv_log('a parent relbit was identified in on_add_to_relationship')
            auto_json(sim)
            auto_json(target_sim_info)
    except Exception as e:
        riv_log(f'error in auto_json in on_add_to_relationship: {e}')
        raise Exception(f'(riv) error in auto_json in on_add_to_relationship: {e}')
    return result
```

#### Purpose

The `auto_json_fam_oatr` function is injected into the `RelationshipBit` class to perform automatic JSON updates when a parent relationship bit is added.

#### How It Works

1. **Call Original Function**: Executes the original logic for adding to a relationship.
2. **Check for Parent Relationship**: Identifies

 if the relationship bit added is a parent relationship.
3. **Automatic JSON Update**: Triggers the `auto_json` function for both Sims involved in the relationship.
4. **Logging**: Logs the identification and automatic JSON update actions.
5. **Error Handling**: Logs and raises any errors encountered during execution.

#### Why It’s Needed

This function ensures that parent-child relationships are accurately reflected in the JSON files whenever a parent relationship bit is added, maintaining accurate family relationships.

### Function: Automatic Update of Permanent JSON on Save

```python
@inject_to(PersistenceService, 'save_using')
def auto_json_del_tmp_su(original, self, *args, **kwargs):
    result = original(self, *args, **kwargs)
    try:
        if riv_auto_enabled:
            auto_json()
        if not file_name_extra == '':
            file_dir = Path(__file__).resolve().parent.parent
            if use_currentsession_files:
                for file in os.scandir(file_dir):
                    if file.name.startswith('riv_currentsession_tmp') and file.name.endswith('.json'):
                        temp_file_name = file.name
                        perm_file_name = temp_file_name.replace('currentsession_tmp', 'rel')
                        with open(os.path.join(file_dir, temp_file_name), 'r') as json_file:
                            temp_contents = json.load(json_file)
                        with open(os.path.join(file_dir, perm_file_name), 'w') as json_file:
                            json.dump(temp_contents, json_file)
                        riv_log('written to ' + perm_file_name)
                        os.remove(os.path.join(file_dir, temp_file_name))
                        riv_log('removed file ' + temp_file_name)
            else:
                save_sims(services.sim_info_manager().get_all(), file_name_extra)
                save_rels(services.sim_info_manager().get_all(), file_name_extra)
    except Exception as e:
        riv_log(f'error in auto_json_del_tmp_su in save_using: {e}')
        raise Exception(f'(riv) error in auto_json_del_tmp_su in save_using: {e}')
    finally:
        riv_log('')
    return result
```

#### Purpose

This function ensures that the JSON files containing Sim data are automatically updated when the game is saved.

#### How It Works

1. **Call Original Function**: Executes the original save logic.
2. **Automatic JSON Update**: If `riv_auto_enabled` is set, calls `auto_json()` to update the in-memory Sim data.
3. **File Operations**:
   - If `use_currentsession_files` is enabled, temporary JSON files are copied to permanent JSON files.
   - If `use_currentsession_files` is not enabled, directly saves the Sim data to the permanent JSON files.
4. **Logging**: Logs the operations performed.
5. **Error Handling**: Logs and raises any errors encountered during execution.

#### Why It’s Needed

This function ensures that the Sim data is always saved and updated in the JSON files, maintaining data consistency across game sessions.

### Function: Get Relationship Between Sims

```python
@sims4.commands.Command('riv_rel', command_type=sims4.commands.CommandType.Live)
def riv_getrelation(sim_x: SimInfoParam, sim_y: SimInfoParam, show_if_not_related=True,
                    include_step_rels=global_include_step_rels,
                    xx_ancestors=None, yy_ancestors=None, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    if sim_x is not None and sim_y is not None:
        if sim_x == sim_y:
            main_text = '{x_firstname} {x_lastname} is {y_firstname} {y_lastname}' \
                .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                        y_firstname=sim_y.first_name, y_lastname=sim_y.last_name)
            output(main_text)
            riv_log(main_text, 3)
            return False
        else:
            if xx_ancestors is None:
                x_ancestors = get_ancestors(sim_x)
            else:
                x_ancestors = xx_ancestors
            if yy_ancestors is None:
                y_ancestors = get_ancestors(sim_y)
            else:
                y_ancestors = yy_ancestors

            rrel_lists = get_str_list(sim_x, sim_y, x_ancestors, y_ancestors,
                                      include_step_rels or global_include_step_rels)
            rel_lists = combine_str_list(rrel_lists[0], rrel_lists[1], rrel_lists[2])
            rel_list = rel_lists[0] + rel_lists[1] + rel_lists[2]
            if len(rel_list) > 0:
                main_text = '{x_firstname} is {y_firstname}\'s {rel}' \
                    .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name, rel=rel_list[0])
                if len(rel_list) == 2:
                    main_text += ' and ' + rel_list[1]
                elif len(rel_list) > 2:
                    for i in range(1, len(rel_list) - 1):
                        main_text += ', ' + rel_list[i]
                    main_text += ', and ' + rel_list[len(rel_list) - 1]
                main_text += '.'
                output(main_text)
                riv_log(main_text, 3)
            else:
                main_text = '{x_firstname} and {y_firstname} are not related.' \
                    .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name)
                if show_if_not_related:
                    output(main_text)
                riv_log(main_text, 3)
            return len(rel_list) > 0
```

#### Purpose

The `riv_getrelation` function checks and displays the relationship between two Sims.

#### How It Works

1. **Command Registration**: Registers the command `riv_rel` with the command type `Live`.
2. **Self-Relationship Check**: If the Sims are the same, logs and outputs that the Sim is themselves.
3. **Retrieve Ancestors**: Gets the ancestors for both Sims.
4. **Get Relationships**: Calls `get_str_list` to get biological, in-law, and step relationships.
5. **Combine Relationships**: Combines and formats the relationship strings.
6. **Output Result**: Outputs the relationship result or a message indicating no relation.
7. **Logging**: Logs the relationship result.
8. **Return Value**: Returns whether any relationship was found.

#### Why It’s Needed

This function allows players to easily check the relationships between Sims, including complex familial ties like step-relations and in-laws. It enhances gameplay by providing detailed relationship information through a simple command.

### Functions: Relationship and Generational Difference Commands

#### `riv_getrelation_moreinfo`

```python
@sims4.commands.Command('riv_rel_more_info', command_type=sims4.commands.CommandType.Live)
def riv_getrelation_moreinfo(sim_x: SimInfoParam, sim_y: SimInfoParam, include_step_rels=True, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    if sim_x is not None and sim_y is not None:
        if sim_x == sim_y:
            output('{x_firstname} {x_lastname} is {y_firstname} {y_lastname}'
                   .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                           y_firstname=sim_y.first_name, y_lastname=sim_y.last_name))
            output('consanguinity: 100%')
        else:
            x_ancestors = get_ancestors(sim_x)
            y_ancestors = get_ancestors(sim_y)

            sim_x = get_rivsim_from_sim(sim_x)
            sim_y = get_rivsim_from_sim(sim_y)

            xy_direct_rels = get_direct_rel(sim_x, sim_y, x_ancestors, y_ancestors)
            if xy_direct_rels:
                xy_direct_rel_str = format_direct_rel(xy_direct_rels, sim_x)
                for xy_rel in xy_direct_rel_str:
                    try:
                        output('{x_firstname} {x_lastname} is {y_firstname} {y_lastname}\'s {rel}'
                               .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                                       y_firstname=sim_y.first_name, y_lastname=sim_y.last_name, rel=xy_rel))
                    except Exception as e:
                        output('error in riv_rel, direct rel section: ' + str(e))

            xy_indirect_rels = get_indirect_rel(sim_x, sim_y, x_ancestors, y_ancestors)
            rels_via = format_indirect_rel(xy_indirect_rels, sim_x)
            if rels_via:
                for rel_via in rels_via:
                    try:
                        if rel_via[1] == rel_via[2]:
                            output(
                                '{x_firstname} {x_lastname} is {y_firstname} {y_lastname}\'s {rel} (relation found via {z_firstname} {z_lastname})'
                                    .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                                            y_firstname=sim_y.first_name, y_lastname=sim_y.last_name, rel=rel_via[0],
                                            z_firstname=rel_via[1].first_name, z_lastname=rel_via[1].last_name))
                        else:
                            sim_z = rel_via[1]
                            sim_w = rel_via[2]
                            output(
                                '{x_firstname} {x_lastname} is {y_firstname} {y_lastname}\'s {rel} (relation found via {z_firstname} {z_lastname} and {w_firstname} {w_lastname})'
                                    .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                                            y_firstname=sim_y.first_name, y_lastname=sim_y.last_name, rel=rel_via[0],
                                            z_firstname=sim_z.first_name, z_lastname=sim_z.last_name,
                                            w_firstname=sim_w.first_name, w_lastname=sim_w.last_name))
                    except Exception as e:
                        output('error in riv_rel, indirect rel section: ' + str(e))

            xy_consang = consang(sim_x, sim_y)
            output(f'consanguinity: {round(100 * xy_consang, 5)}%')

            sim_x = get_sim_from_rivsim(sim_x)
            sim_y = get_sim_from_rivsim(sim_y)

            if sim_x is not None and sim_y is not None:
                xy_inlaw_rels = get_inlaw_rel(sim_x, sim_y, x_ancestors, y_ancestors)
                if xy_inlaw_rels:
                    inlaw_str = format_inlaw_rel(xy_inlaw_rels, sim_x)
                    for rel in inlaw_str:
                        try:
                            if rel[1] == 0:
                                output('{x_firstname} {x_lastname} is {y_firstname} {y_lastname}\'s {rel}'
                                       .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                                               y_firstname=sim_y.first_name, y_lastname=sim_y.last_name, rel=rel[0]))
                            elif rel[1] == 1:
                                output(rel[0])
                            else:
                                output(
                                    '{x_firstname} {x_lastname} is {y_firstname} {y_lastname}\'s {rel} (relation found via {z_firstname} {z_lastname})'
                                        .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                                                y_firstname=sim_y.first_name, y_lastname=sim_y.last_name, rel=rel[0],
                                                z_firstname=rel[1].first_name, z_lastname=rel[1].last_name))
                        except Exception as e:
                            output('error in riv_rel, inlaw section: ' + str(e))

                if include_step_rels:
                    xy_step_rels = get_step_rel(sim_x, sim_y, x_ancestors, y_ancestors)
                    if xy_step_rels:
                        step_str = format_step_rel(xy_inlaw_rels, sim_x)
                        for rel in step_str:
                            try:
                                output(
                                    '{x_firstname} {x_lastname} is {y_firstname} {y_lastname}\'s {rel} (relation found via {z_firstname} {z_lastname} and {w_firstname} {w_lastname})'
                                        .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                                                y_firstname=sim_y.first_name, y_lastname=sim_y.last_name, rel=rel[0],
                                                z_firstname=rel[1].first_name, z_lastname=rel[1].last_name,
                                                w_firstname=rel[2].first_name, w_lastname=rel[2].last_name))
                            except Exception as e:
                                output('error in riv_rel, step section: ' + str(e))
```

#### Purpose

This function provides detailed relationship information between two Sims, including direct, indirect, in-law, and step relationships, as well as consanguinity percentages.

#### How It Works

1. **Command Registration**: Registers the command `riv_rel_more_info` with the command type `Live`.
2. **Self-Relationship Check**: Checks if the Sims are the same and outputs their relationship to themselves.
3. **Retrieve Ancestors**: Gets the ancestors for both Sims.
4. **Convert to RivSim**: Converts the Sims to `RivSim` objects.
5. **Direct Relationships**: Retrieves and formats direct relationships.
6. **Indirect Relationships**: Retrieves and formats indirect relationships, including the Sims through whom the relationship is found.
7. **Consanguinity**: Calculates and outputs the consanguinity percentage.
8. **In-Law Relationships**: Retrieves and formats in-law relationships.
9. **Step Relationships**: Retrieves and formats step relationships if `include_step_rels` is enabled.
10. **Error Handling**: Logs and outputs any errors encountered during execution.

#### Why It’s Needed

This function enhances the game's relationship management by providing a comprehensive view of all types of relationships between Sims, including complex family ties and consanguinity percentages.

---

#### `riv_getrandomrel`

```python
@sims4.commands.Command('riv_rel_rand', command_type=sims4.commands.CommandType.Live)
def riv_getrandomrel(sim_x: SimInfoParam, include_step_rels=global_include_step_rels, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    sim_y = random.choice(list(services.sim_info_manager()._objects.values()))
    output('relation with: {y_firstname} {y_lastname}'.format(y_firstname=sim_y.first_name, y_lastname=sim_y.last_name))
    riv_getrelation(sim_x, sim_y, True, global_include_step_rels or include_step_rels, None, None, _connection)
```

#### Purpose

This function checks the relationship between a specified Sim and a randomly chosen Sim from the game.

#### How It Works

1. **Command Registration**: Registers the command `riv_rel_rand` with the command type `Live`.
2. **Random Sim Selection**: Randomly selects a Sim from the game.
3. **Relationship Check**: Calls `riv_getrelation` to check and display the relationship between the specified Sim and the randomly chosen Sim.

#### Why It’s Needed

This function provides a quick way to check relationships between a specified Sim and a random Sim, which can be useful for gameplay dynamics and storytelling.

---

#### `riv_getrandomrandomrel`

```python
@sims4.commands.Command('riv_rel_rand_rand', command_type=sims4.commands.CommandType.Live)
def riv_getrandomrandomrel(include_step_rels=global_include_step_rels, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    sim_x = random.choice(list(services.sim_info_manager()._objects.values()))
    sim_y = random.choice(list(services.sim_info_manager()._objects.values()))


    output('sims: {x_firstname} {x_lastname} and {y_firstname} {y_lastname}'
           .format(x_firstname=sim_x.first_name, x_lastname=sim_x.last_name,
                   y_firstname=sim_y.first_name, y_lastname=sim_y.last_name))
    riv_getrelation(sim_x, sim_y, True, global_include_step_rels or include_step_rels, None, None, _connection)
```

#### Purpose

This function checks the relationship between two randomly chosen Sims from the game.

#### How It Works

1. **Command Registration**: Registers the command `riv_rel_rand_rand` with the command type `Live`.
2. **Random Sim Selection**: Randomly selects two Sims from the game.
3. **Relationship Check**: Calls `riv_getrelation` to check and display the relationship between the two randomly chosen Sims.

#### Why It’s Needed

This function provides a quick way to explore relationships between random Sims, adding an element of surprise and variety to gameplay.

---

#### `riv_getallrels`

```python
@sims4.commands.Command('riv_rel_all', command_type=sims4.commands.CommandType.Live)
def riv_getallrels(sim_y: SimInfoParam, include_step_rels=global_include_step_rels, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    yy_ancestors = get_ancestors(sim_y)
    relatives_found = 0
    for sim_x in services.sim_info_manager().get_all():
        x_y_related = riv_getrelation(sim_x, sim_y, False, False, None, yy_ancestors, _connection)
        if x_y_related:
            relatives_found += 1
    output('relatives found for {y_firstname}: {num_rels}'
           .format(y_firstname=sim_y.first_name, num_rels=str(relatives_found)))
```

#### Purpose

This function checks the relationship between a specified Sim and all other Sims in the game.

#### How It Works

1. **Command Registration**: Registers the command `riv_rel_all` with the command type `Live`.
2. **Retrieve Ancestors**: Gets the ancestors for the specified Sim.
3. **Relationship Check**: Iterates through all Sims in the game and calls `riv_getrelation` to check the relationship between each Sim and the specified Sim.
4. **Output Result**: Outputs the number of relatives found for the specified Sim.

#### Why It’s Needed

This function provides a comprehensive view of all relationships for a specified Sim, making it easier to understand their family and social connections within the game.

---

#### `riv_getallallrels`

```python
@sims4.commands.Command('riv_rel_all_all', command_type=sims4.commands.CommandType.Live)
def riv_getallallrels(include_step_rels=global_include_step_rels, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    for sim_x in services.sim_info_manager().get_all():
        riv_getallrels(sim_x, False, _connection)
        output('')
```

#### Purpose

This function checks the relationships between all Sims in the game against all other Sims.

#### How It Works

1. **Command Registration**: Registers the command `riv_rel_all_all` with the command type `Live`.
2. **Relationship Check**: Iterates through all Sims in the game and calls `riv_getallrels` to check the relationships for each Sim against all other Sims.
3. **Output Result**: Outputs the relationship results for each Sim.

#### Why It’s Needed

This function provides a complete map of all relationships in the game, useful for detailed analysis and understanding of the social structure within the game.

---

#### `console_help`

```python
@sims4.commands.Command('riv_help', command_type=sims4.commands.CommandType.Live)
def console_help(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    if addons['GT']:
        addon_GT_text = ' (fam and inc can be used as club requirements)'
    else:
        addon_GT_text = ''
    output(
        f'riv_rel gen {rr_gen} - biological, in-law, and (optional) step relations, console commands, social interaction, auto .json files, optional computer help menu, optional traits'
        f'{addon_GT_text}, consanguinity')
    output('all settings can be edited by opening the .cfg files (in the same folder as riv_rel) in notepad++')
    output(
        'sims can be typed as firstname lastname (use "" if there is a space in the first/last name, e.g. J "Huntington III") or as the sim ID')
    output(
        'if you find an error, please send me (rivforthesesh / riv#4381) the error text and any relevant rels/files!')

    output('')

    output(
        'commands taking two sims: riv_rel, riv_rel_more_info, riv_get_sib_strength, riv_get_direct_rel, riv_get_indirect_rel, riv_show_relbits, riv_gen_diff, riv_consang, riv_is_eligible_couple')
    output(
        'commands taking one sim: riv_get_parents, riv_get_children, riv_get_ancestors, riv_get_descendants, riv_rel_all, riv_rel_rand')

    output('')

    output(
        'using .json files [replace xyz by whatever you want to create/use the files riv_rel_xyz.json and riv_relparents_xyz.json]:')
    output('riv_auto xyz (sets up save to run riv_update xyz on every zone load or sim birth or save)')
    output(
        '.json files debug commands: riv_save xyz (save sim info to .json files), riv_load xyz (load sim info from .json files), riv_clean xyz (removes duplicates from .json file), riv_mem (shows no. mini sim-infos in memory), riv_clear (clears memory), riv_update xyz (runs save, clear, then load), riv_save_slot_id (shows current save ID)')
    if addons['traits']:
        output('')

        output(
            'trait commands taking one sim, and a letter from A to H: riv_include_in_family, riv_add_to_family, riv_exclude_from_family, riv_make_heir, riv_add_founder')
        output('trait commands taking one sim: riv_traits_by_name, riv_clear_fam_sim (removes fam traits)')
        output('trait commands taking a letter from A to H: riv_traits_by_fam, riv_clear_fam, riv_show_family')
        output('trait commands taking no arguments: riv_traits, riv_clear_fam_all')
    if addons['computer']:
        output('')

        output('check the computer for a menu called "Research on riv_rel.sim..." for explanations and help.')

    output('')
    output('the help menu is a little long, please scroll up!')
```

#### Purpose

This function provides a comprehensive help menu for all available commands and features in the mod.

#### How It Works

1. **Command Registration**: Registers the command `riv_help` with the command type `Live`.
2. **Add-on Check**: Checks for specific add-ons and adjusts the help text accordingly.
3. **Output Help Text**: Outputs detailed information about the commands and features available in the mod, including how to use JSON files, debug commands, and trait commands.
4. **Output Additional Information**: Provides additional instructions for using commands and seeking help for errors.

#### Why It’s Needed

This function serves as a quick reference guide for users, making it easier to understand and use the various features and commands provided by the mod. It ensures that users have all the necessary information to fully utilize the mod's capabilities.

#### `mean`

```python
def mean(list_boi: List):
    if len(list_boi) == 0:
        return None
    else:
        return sum(list_boi) / len(list_boi)
```

#### Purpose

Calculates the mean (average) of a list of numbers.

#### How It Works

1. **Check List Length**: If the list is empty, return `None`.
2. **Calculate Mean**: If the list is not empty, sum the numbers and divide by the length of the list to get the mean.

#### Why It’s Needed

This function is a utility to compute the average value of a list, which can be used in various calculations within the mod.

---

#### `generational_difference`

```python
def generational_difference(sim_x: SimInfoParam, sim_y: SimInfoParam):
    x_ancestors = get_ancestors(sim_x)
    y_ancestors = get_ancestors(sim_y)
    direct_gen_diff = get_direct_rel(sim_x, sim_y, x_ancestors, y_ancestors)
    indirect_rels = get_indirect_rel(sim_x, sim_y, x_ancestors, y_ancestors)
    indirect_gen_diff = []
    for ituple in indirect_rels:
        nx = ituple[2]
        ny = ituple[3]
        indirect_gen_diff.append(nx - ny)
    gen_diff_list = direct_gen_diff + indirect_gen_diff
    mean_gd = mean(gen_diff_list)
    if mean_gd is not None:
        gen_diff = round(mean_gd, 3)
    else:
        gen_diff = None
    return (gen_diff, gen_diff_list)
```

#### Purpose

Calculates the generational difference between two Sims based on their family tree.

#### How It Works

1. **Retrieve Ancestors**: Gets the ancestors for both Sims.
2. **Direct Relationship Difference**: Calculates the generational difference for direct relationships.
3. **Indirect Relationship Difference**: Calculates the generational difference for indirect relationships.
4. **Combine Differences**: Combines direct and indirect generational differences into a list.
5. **Calculate Mean Difference**: Calculates the mean generational difference and rounds it to three decimal places.
6. **Return Results**: Returns the mean generational difference and the list of generational differences.

#### Why It’s Needed

This function helps to understand the generational gap between two Sims, which can be useful for managing family trees and relationships in the game.

---

#### `riv_getgendiff`

```python
@sims4.commands.Command('riv_gen_diff', command_type=sims4.commands.CommandType.Live)
def riv_getgendiff(sim_x: SimInfoParam, sim_y: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    gen_diff_tuple = generational_difference(sim_x, sim_y)
    gen_diff = gen_diff_tuple[0]
    gen_diff_list = gen_diff_tuple[1]
    output('as a list: ' + str(gen_diff_list))
    output('the average generational difference is ' + str(gen_diff))
    output('(negative means sim_x is higher up in the family tree than sim_y)')
```

#### Purpose

Displays the generational difference between two Sims in the game.

#### How It Works

1. **Command Registration**: Registers the command `riv_gen_diff` with the command type `Live`.
2. **Calculate Generational Difference**: Calls `generational_difference` to get the generational difference and the list of differences.
3. **Output Results**: Outputs the list of generational differences and the average generational difference.

#### Why It’s Needed

This command provides a quick way for players to see the generational gap between two Sims, adding depth to the game's relationship dynamics.

---

#### `riv_getsaveslotid`

```python
@sims4.commands.Command('riv_save_slot_id', command_type=sims4.commands.CommandType.Live)
def riv_getsaveslotid(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    try:
        per = services.get_persistence_service()
    except Exception as e:
        output('failed to get persistence service because ' + str(e))
        return
    output('str(per._save_game_data_proto.save_slot.slot_id) = ' + str(per._save_game_data_proto.save_slot.slot_id))
    output('riv_rel is currently using save slot id ' + hex_slot_id)
```

#### Purpose

Displays the current save slot ID being used by the game.

#### How It Works

1. **Command Registration**: Registers the command `riv_save_slot_id` with the command type `Live`.
2. **Retrieve Persistence Service**: Attempts to get the persistence service.
3. **Output Save Slot ID**: Outputs the save slot ID from the persistence service and the mod's current save slot ID.

#### Why It’s Needed

This command helps players identify the current save slot ID, which can be useful for debugging and managing save files.

---

#### `riv_clear_log`

```python
@sims4.commands.Command('riv_rel_start_log', command_type=sims4.commands.CommandType.Live)
def riv_clear_log(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    global riv_auto_log
    riv_auto_log = True
    start_logging()
    output('created the logging file (riv_rel.log) - if you\'re trying to debug something, '
           'redo whatever caused the issue and send it to me (rivforthesesh / riv#4381)')
    output('to stop logging, just delete this file after you\'ve closed the game')
```

#### Purpose

Starts the logging process for debugging purposes.

#### How It Works

1. **Command Registration**: Registers the command `riv_rel_start_log` with the command type `Live`.
2. **Enable Logging**: Sets `riv_auto_log` to `True` and starts logging.
3. **Output Instructions**: Outputs instructions for players on how to use the logging file and send it for debugging.

#### Why It’s Needed

This command enables detailed logging for debugging issues within the mod, helping developers and players identify and fix problems.

---

#### `riv_clear_log`

```python
@sims4.commands.Command('riv_rel_log_clear', command_type=sims4.commands.CommandType.Live)
def riv_clear_log(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output('clearing non-error/birth record lines from riv_rel.log...')
    file_dir = Path(__file__).resolve().parent.parent
    file_name = 'riv_rel.log'
    file_path = os.path.join(file_dir, file_name)

    if not os.path.isfile(file_path):
        output('nothing to clear')
        return

    with open(file_path, 'r') as log_file:
        old_file = log_file.read()
    old_text = old_file.split('\n')
    old_line_num = len(old_text)

    with open(file_path, 'w') as log_file:
        log_file.write('')

    new_line_num = 0
    while old_text:
        line = old_text.pop(0)
        if 'error' in line or 'spawned' in line or 'game loaded' in line:
            new_line_num += 1
            with open(file_path, 'a') as log_file:
                log_file.write(line + '\n')

    with open(file_path, 'a') as log_file:
        log_file.write('\n')

    output(f'done: gone from {old_line_num} lines to {new_line_num}.')
```

#### Purpose

Clears non-error and non-birth record lines from the logging file to reduce clutter and focus on important logs.

#### How It Works

1. **Command Registration**: Registers the command `riv_rel_log_clear` with the command type `Live`.
2. **Check Log File**: Checks if the log file exists.
3. **Read and Filter Log Lines**: Reads the log file, filters out non-error and non-birth record lines, and rewrites the log file with the filtered content.
4. **Output Results**: Outputs the number of lines before and after clearing.

#### Why It’s Needed

This command helps manage the log file by removing unnecessary lines, making it easier to identify and focus on important log entries.

---

#### `console_is_eligible_couple`

```python
@sims4.commands.Command('riv_is_eligible_couple', command_type=sims4.commands.CommandType.Live)
def console_is_eligible_couple(sim_x: SimInfoParam, sim_y: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    eligibility = is_eligible_couple(sim_x.sim_id, sim_y.sim_id)
    if sim_x.is_teen_or_older and sim_y.is_teen_or_older:
        output(eligibility[1])
    else:
        output('{x_firstname} and {y_firstname} are not an eligible couple: '
               .format(x_firstname=sim_x.first_name, y_firstname=sim_y.first_name) +
               'at least one is too young for romance')
    try:
        eligibility2 = sim_x.incest_prevention_test(sim_y)
        if eligibility2:
            output('the game considers this as incest')
        else:
            output('the game does not consider this as incest')
    except Exception as e:
        riv_log(f'riv_is_eligible_couple couldn\'t check if this is ingame incest because {e}', 1)
```

#### Purpose

Checks if two Sims are an eligible couple based on age, relationship, and consanguinity.

#### How It Works

1. **Command Registration**: Registers the command

 `riv_is_eligible_couple` with the command type `Live`.
2. **Eligibility Check**: Calls `is_eligible_couple` to check if the two Sims can be a couple.
3. **Age Check**: Checks if both Sims are teens or older.
4. **Output Eligibility**: Outputs the eligibility result.
5. **Incest Check**: Checks if the relationship is considered incestuous by the game.

#### Why It’s Needed

This command provides a way to verify if two Sims can be a romantic couple, considering both the mod's and the game's rules for relationships.

---

#### `console_get_suitors`

```python
@sims4.commands.Command('riv_get_suitors', command_type=sims4.commands.CommandType.Live)
def console_get_suitors(sim_x: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    incest_rules = f'consanguinity under {round(100 * consang_limit, 5)}%'
    if drel_incest:
        incest_rules = incest_rules + ', not directly related'
    output(f'all eligible partners for {sim_x.first_name}, i.e. different sims, same age, alive, '
           f'and their relationship wouldn\'t be incestuous ({incest_rules})')
    for sim_y in services.sim_info_manager().get_all():
        eligibility = is_eligible_couple(sim_x.sim_id, sim_y.sim_id)
        try:
            eligibility2 = sim_x.incest_prevention_test(sim_y)
        except Exception as e:
            riv_log(f'error: riv_get_suitors couldn\'t check if this is ingame incest because {e}', 1)
            eligibility2 = True  # x and True = x
        if eligibility[0] and eligibility2:  # this couple is eligible
            if sim_x.age == sim_y.age:  # this couple is the same age
                if not sim_y.is_ghost():  # sim_y isn't dead
                    output(f'{sim_y.first_name} {sim_y.last_name}, with '
                           f'consanguinity {round(100 * consang(sim_x, sim_y), 5)}%')
```

#### Purpose

Lists all eligible romantic partners for a specified Sim based on age, relationship, and consanguinity.

#### How It Works

1. **Command Registration**: Registers the command `riv_get_suitors` with the command type `Live`.
2. **Incest Rules Check**: Checks and formats the incest rules based on the mod's settings.
3. **Iterate Through Sims**: Iterates through all Sims in the game.
4. **Eligibility Check**: Checks if each Sim is an eligible partner based on consanguinity and age.
5. **Output Eligible Partners**: Outputs the list of eligible partners along with their consanguinity percentage.

#### Why It’s Needed

This command provides a comprehensive list of potential romantic partners for a specified Sim, helping players manage relationships more effectively.

---

#### `riv_incest_prevention_test`

```python
@inject_to(SimInfo, 'incest_prevention_test')
def riv_incest_prevention_test(original, self, sim_info_b):
    incest_prevention_tic = time.perf_counter()
    result = original(self, sim_info_b)

    if not result:
        return result

    riv_result = True
    try:
        riv_result = is_eligible_couple(self.sim_id, sim_info_b.sim_id)[0]
        riv_log(f'incest test between {self.first_name} and {sim_info_b.first_name}: '
                f'original result is {result}, my mod says {riv_result}. __name__ = {__name__}', 3)
    except Exception as e:
        riv_log(f'error: didn\'t manage to influence incest settings because {e}')

    incest_prevention_toc = time.perf_counter()
    iptime = incest_prevention_toc - incest_prevention_tic

    if iptime > 1:
        ip_loglevel = 2
    else:
        ip_loglevel = 3

    riv_log(f'incest test between {self.first_name} and {sim_info_b.first_name} took {iptime}s', ip_loglevel)
    return riv_result
```

#### Purpose

Overrides the game's incest prevention test to include the mod's consanguinity check.

#### How It Works

1. **Inject into `incest_prevention_test`**: Injects custom logic into the game's `incest_prevention_test` method.
2. **Original Result Check**: Checks the original result of the game's incest prevention test.
3. **Custom Consanguinity Check**: Adds a custom check for consanguinity using the mod's `is_eligible_couple` function.
4. **Log Results**: Logs the results and the time taken for the incest prevention test.
5. **Return Result**: Returns the final result, combining the game's and the mod's checks.

#### Why It’s Needed

This injection ensures that the mod's consanguinity rules are considered in addition to the game's default incest prevention rules, providing a more comprehensive check for relationships.

#### `riv_set_death_type`

```python
@inject_to(DeathTracker, 'set_death_type')
def riv_set_death_type(original, self, *args, **kwargs):
    result = original(self, *args, **kwargs)
    try:
        riv_log(f'dead sim: {self._sim_info.first_name} {self._sim_info.last_name} despawned {format_sim_date()}')
    except Exception as e:
        riv_log(f'error in riv_set_death_type: {e}')
    return result
```

#### Purpose

Logs the death of a Sim by injecting into the `set_death_type` method of the `DeathTracker` class.

#### How It Works

1. **Inject into `set_death_type`**: This function uses an injection to add custom behavior to the existing `set_death_type` method.
2. **Call Original Method**: Calls the original `set_death_type` method to ensure the standard behavior is retained.
3. **Log Sim Death**: Logs the first name, last name, and the formatted date of the Sim who has died.
4. **Error Handling**: If an error occurs during logging, it is caught and logged.

#### Why It’s Needed

This function is necessary to keep track of Sim deaths within the game, providing additional context for debugging and gameplay purposes. It ensures that each death is recorded with relevant information, aiding in both development and player awareness.

