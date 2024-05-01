#include "../../include/common.h"

void writeWTI(int index) {
	ExpandPauseMenu = index;
	int init_y = 0x198;
	InitialPauseHeight = init_y - (0x28 * index);
}

static short isles_maps[] = {
	MAP_ISLES,
	MAP_FAIRYISLAND,
	MAP_KLUMSY,
	MAP_ISLES_SNIDEROOM,
};

void handle_WTI(void) {
	if (isLobby(CurrentMap)) {
		// Lobbies
		writeWTI(1);
	} else if (levelIndexMapping[CurrentMap] < LEVEL_ISLES) {
		// Any Map explicitly in first 7 worlds
		writeWTI(1);
	} else if ((CurrentMap == MAP_HELM) && (checkFlag(FLAG_MODIFIER_HELMBOM, FLAGTYPE_PERMANENT))) {
		// Helm (Only if BoM is off)
		writeWTI(1);
	} else if (inShortList(CurrentMap, &isles_maps[0], sizeof(isles_maps) >> 1)) {
		// Isles, BFI, K. Lumsy, Snide Room
		writeWTI(1);
	} else if ((checkFlagDuplicate(FLAG_ESCAPE, FLAGTYPE_PERMANENT)) && ((CurrentMap == MAP_TRAININGGROUNDS) || (CurrentMap == MAP_TREEHOUSE))) {
		// TGrounds & Treehouse (Only if escaped from Isles)
		writeWTI(1);
	} else {
		writeWTI(0);
	}
}

void warpToIsles(void) {
	initiateTransition(Rando.starting_map, Rando.starting_exit);
	fixHelmTimerCorrection();
}