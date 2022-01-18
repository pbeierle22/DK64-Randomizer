#include "vars.h"

extern void playSFX(short sfxIndex);
extern void setPermFlag(short flagIndex);
extern int convertIDToIndex(short obj_index);
extern void* findActorWithType(int search_actor_type);
extern int isRDRAM(void* address);
extern void customHideHUD(void);
extern void setWarpPosition(float x, float y, float z);
extern void initHack(void);

extern void level_order_rando_funcs(void);
extern void unlockKongs(void);
extern void unlockMoves(void);
extern void tagAnywhere(void);
extern void islesSpawn(void);
extern void applyFastStart(void);
extern void fixCastleAutowalk(void);
extern void openCrownDoor(void);
extern void openCoinDoor(void);
extern void qualityOfLife_fixes(void);
extern void qualityOfLife_shorteners(void);
extern void decouple_moves_fixes(void);
extern void price_rando(void);
extern void determine_krool_order(void);
extern void replace_zones(int init_flag);
extern void randomize_bosses(void);

extern void PatchCrankyCode(void);

extern int* drawTri(int* dl, short x1, short y1, short x2, short y2, short x3, short y3, int red, int green, int blue, int alpha);
extern int* drawImage(int* dl, int text_index, codecs codec_index, int img_width, int img_height, int x, int y, float xScale, float yScale, int opacity);
extern int* drawPixelText(int* dl, int x, int y, char* str, int red, int green, int blue, int alpha);
extern int* drawPixelTextContainer(int* dl, int x, int y, char* str, int red, int green, int blue, int alpha, int offset);
extern int* drawScreenRect(int* dl, int x1, int y1, int x2, int y2, int red, int green, int blue, int alpha);