"""List of maps with in-game index."""

from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING

from randomizer.Enums.Levels import Levels
from randomizer.LogicClasses import Regions, TransitionBack
from randomizer.Enums.Maps import Maps

if TYPE_CHECKING:
    from randomizer.Enums.Regions import Regions

RegionMapList = {
    # Isles
    Regions.Treehouse: Maps.Treehouse,
    Regions.TrainingGrounds: Maps.TrainingGrounds,
    Regions.IslesMain: Maps.Isles,
    Regions.OuterIsles: Maps.Isles,
    Regions.IslesMainUpper: Maps.Isles,
    Regions.IslesHill: Maps.Isles,
    Regions.IslesEar: Maps.Isles,
    Regions.KremIsle: Maps.Isles,
    Regions.KremIsleBeyondLift: Maps.Isles,
    Regions.KremIsleTopLevel: Maps.Isles,
    Regions.KremIsleMouth: Maps.Isles,
    Regions.Prison: Maps.KLumsy,
    Regions.IslesSnideRoom: Maps.IslesSnideRoom,
    Regions.CabinIsle: Maps.Isles,
    Regions.IslesAboveWaterfall: Maps.Isles,
    Regions.IslesAirspace: Maps.Isles,
    Regions.AztecLobbyRoof: Maps.Isles,
    Regions.BananaFairyRoom: Maps.BananaFairyRoom,
    Regions.RarewareGBRoom: Maps.BananaFairyRoom,
    Regions.JungleJapesLobby: Maps.JungleJapesLobby,
    Regions.AngryAztecLobby: Maps.AngryAztecLobby,
    Regions.FranticFactoryLobby: Maps.FranticFactoryLobby,
    Regions.GloomyGalleonLobby: Maps.GloomyGalleonLobby,
    Regions.GloomyGalleonLobbyEntrance: Maps.GloomyGalleonLobby,
    Regions.FungiForestLobby: Maps.FungiForestLobby,
    Regions.CrystalCavesLobby: Maps.CrystalCavesLobby,
    Regions.CreepyCastleLobby: Maps.CreepyCastleLobby,
    Regions.HideoutHelmLobby: Maps.HideoutHelmLobby,
    # Japes
    Regions.JungleJapesEntryHandler: Maps.JungleJapes,
    Regions.JungleJapesStart: Maps.JungleJapes,
    Regions.JungleJapesMain: Maps.JungleJapes,
    Regions.JapesTnSAlcove: Maps.JungleJapes,
    Regions.JapesBeyondCoconutGate1: Maps.JungleJapes,
    Regions.JapesBeyondCoconutGate2: Maps.JungleJapes,
    Regions.JapesBeyondPeanutGate: Maps.JungleJapes,
    Regions.JapesBeyondFeatherGate: Maps.JungleJapes,
    Regions.TinyHive: Maps.JapesTinyHive,
    Regions.BeyondRambiGate: Maps.JungleJapes,
    Regions.JapesLankyCave: Maps.JapesLankyCave,
    Regions.Mine: Maps.JapesMountain,
    Regions.JapesTopOfMountain: Maps.JungleJapes,
    Regions.JapesMinecarts: Maps.JapesMinecarts,
    Regions.JapesCatacomb: Maps.JapesUnderGround,
    Regions.JapesBaboonBlast: Maps.JapesBaboonBlast,
    Regions.JapesHill: Maps.JungleJapes,
    Regions.JapesHillTop: Maps.JungleJapes,
    Regions.JapesCannonPlatform: Maps.JungleJapes,
    # Aztec
    Regions.AngryAztecEntryHandler: Maps.AngryAztec,
    Regions.AngryAztecStart: Maps.AngryAztec,
    Regions.BetweenVinesByPortal: Maps.AngryAztec,
    Regions.AztecTunnelBeforeOasis: Maps.AngryAztec,
    Regions.AngryAztecOasis: Maps.AngryAztec,
    Regions.TempleStart: Maps.AztecTinyTemple,
    Regions.TempleUnderwater: Maps.AztecTinyTemple,
    Regions.AngryAztecConnectorTunnel: Maps.AngryAztec,
    Regions.AngryAztecMain: Maps.AngryAztec,
    Regions.AztecDonkeyQuicksandCave: Maps.AngryAztec,
    Regions.DonkeyTemple: Maps.AztecDonkey5DTemple,
    Regions.DiddyTemple: Maps.AztecDiddy5DTemple,
    Regions.LankyTemple: Maps.AztecLanky5DTemple,
    Regions.TinyTemple: Maps.AztecTiny5DTemple,
    Regions.ChunkyTemple: Maps.AztecChunky5DTemple,
    Regions.AztecTinyRace: Maps.AztecTinyRace,
    Regions.LlamaTemple: Maps.AztecLlamaTemple,
    Regions.LlamaTempleBack: Maps.AztecLlamaTemple,
    Regions.AztecBaboonBlast: Maps.AztecBaboonBlast,
    # Factory
    Regions.FranticFactoryEntryHandler: Maps.FranticFactory,
    Regions.FranticFactoryStart: Maps.FranticFactory,
    Regions.Testing: Maps.FranticFactory,
    Regions.RandD: Maps.FranticFactory,
    Regions.FactoryTinyRaceLobby: Maps.FranticFactory,
    Regions.FactoryTinyRace: Maps.FactoryTinyRace,
    Regions.ChunkyRoomPlatform: Maps.FranticFactory,
    Regions.PowerHut: Maps.FactoryPowerHut,
    Regions.BeyondHatch: Maps.FranticFactory,
    Regions.LowerCore: Maps.FranticFactory,
    Regions.InsideCore: Maps.FactoryCrusher,
    Regions.MiddleCore: Maps.FranticFactory,
    Regions.UpperCore: Maps.FranticFactory,
    Regions.FactoryBaboonBlast: Maps.FactoryBaboonBlast,
    Regions.FactoryArcadeTunnel: Maps.FranticFactory,
    Regions.RandDUpper: Maps.FranticFactory,
    # Galleon
    Regions.GloomyGalleonEntryHandler: Maps.GloomyGalleon,
    Regions.GloomyGalleonStart: Maps.GloomyGalleon,
    Regions.GalleonPastVines: Maps.GloomyGalleon,
    Regions.GalleonBeyondPineappleGate: Maps.GloomyGalleon,
    Regions.LighthouseSurface: Maps.GloomyGalleon,
    Regions.LighthousePlatform: Maps.GloomyGalleon,
    Regions.LighthouseUnderwater: Maps.GloomyGalleon,
    Regions.LighthouseSnideAlcove: Maps.GloomyGalleon,
    Regions.Lighthouse: Maps.GalleonLighthouse,
    Regions.MermaidRoom: Maps.GalleonMermaidRoom,
    Regions.SickBay: Maps.GalleonSickBay,
    Regions.Shipyard: Maps.GloomyGalleon,
    Regions.ShipyardUnderwater: Maps.GloomyGalleon,
    Regions.SealRace: Maps.GalleonSealRace,
    Regions.TreasureRoom: Maps.GloomyGalleon,
    Regions.TreasureRoomDiddyGoldTower: Maps.GloomyGalleon,
    Regions.TinyChest: Maps.GalleonTreasureChest,
    Regions.Submarine: Maps.GalleonSubmarine,
    Regions.Mechafish: Maps.GalleonMechafish,
    Regions.LankyShip: Maps.Galleon2DShip,
    Regions.TinyShip: Maps.Galleon2DShip,
    Regions.BongosShip: Maps.Galleon5DShipDKTiny,
    Regions.SaxophoneShip: Maps.Galleon5DShipDKTiny,
    Regions.GuitarShip: Maps.Galleon5DShipDiddyLankyChunky,
    Regions.TromboneShip: Maps.Galleon5DShipDiddyLankyChunky,
    Regions.TriangleShip: Maps.Galleon5DShipDiddyLankyChunky,
    Regions.GalleonBaboonBlast: Maps.GalleonBaboonBlast,
    # Fungi
    Regions.FungiForestEntryHandler: Maps.FungiForest,
    Regions.FungiForestStart: Maps.FungiForest,
    Regions.ForestMinecarts: Maps.ForestMinecarts,
    Regions.GiantMushroomArea: Maps.FungiForest,
    Regions.MushroomLower: Maps.ForestGiantMushroom,
    Regions.MushroomLowerMid: Maps.ForestGiantMushroom,
    Regions.MushroomMiddle: Maps.ForestGiantMushroom,
    Regions.MushroomUpperMid: Maps.ForestGiantMushroom,
    Regions.MushroomLowerExterior: Maps.FungiForest,
    Regions.MushroomUpper: Maps.ForestGiantMushroom,
    Regions.MushroomNightDoor: Maps.ForestGiantMushroom,
    Regions.MushroomNightExterior: Maps.FungiForest,
    Regions.MushroomUpperExterior: Maps.FungiForest,
    Regions.MushroomChunkyRoom: Maps.ForestChunkyFaceRoom,
    Regions.MushroomLankyMushroomsRoom: Maps.ForestLankyMushroomsRoom,
    Regions.MushroomLankyZingersRoom: Maps.ForestLankyZingersRoom,
    Regions.HollowTreeArea: Maps.FungiForest,
    Regions.Anthill: Maps.ForestAnthill,
    Regions.MillArea: Maps.FungiForest,
    Regions.MillChunkyTinyArea: Maps.ForestMillBack,
    Regions.SpiderRoom: Maps.ForestSpider,
    Regions.GrinderRoom: Maps.ForestMillFront,
    Regions.MillRafters: Maps.ForestRafters,
    Regions.WinchRoom: Maps.ForestWinchRoom,
    Regions.MillAttic: Maps.ForestMillAttic,
    Regions.ThornvineArea: Maps.FungiForest,
    Regions.ThornvineBarn: Maps.ForestThornvineBarn,
    Regions.WormArea: Maps.FungiForest,
    Regions.ForestBaboonBlast: Maps.ForestBaboonBlast,
    Regions.MushroomUpperMidExterior: Maps.FungiForest,
    Regions.ForestTopOfMill: Maps.FungiForest,
    Regions.ForestVeryTopOfMill: Maps.FungiForest,
    # Caves
    Regions.CrystalCavesEntryHandler: Maps.CrystalCaves,
    Regions.CrystalCavesMain: Maps.CrystalCaves,
    Regions.CavesSnideArea: Maps.CrystalCaves,
    Regions.CavesBlueprintCave: Maps.CrystalCaves,
    Regions.CavesBonusCave: Maps.CrystalCaves,
    Regions.CavesBlueprintPillar: Maps.CrystalCaves,
    Regions.CavesBananaportSpire: Maps.CrystalCaves,
    Regions.BoulderCave: Maps.CrystalCaves,
    Regions.CavesLankyRace: Maps.CavesLankyRace,
    Regions.FrozenCastle: Maps.CavesFrozenCastle,
    Regions.IglooArea: Maps.CrystalCaves,
    Regions.GiantKosha: Maps.CrystalCaves,
    Regions.DonkeyIgloo: Maps.CavesDonkeyIgloo,
    Regions.DiddyIgloo: Maps.CavesDiddyIgloo,
    Regions.LankyIgloo: Maps.CavesLankyIgloo,
    Regions.TinyIgloo: Maps.CavesTinyIgloo,
    Regions.ChunkyIgloo: Maps.CavesChunkyIgloo,
    Regions.CabinArea: Maps.CrystalCaves,
    Regions.RotatingCabin: Maps.CavesRotatingCabin,
    Regions.DonkeyCabin: Maps.CavesDonkeyCabin,
    Regions.DiddyLowerCabin: Maps.CavesDiddyLowerCabin,
    Regions.DiddyUpperCabin: Maps.CavesDiddyUpperCabin,
    Regions.LankyCabin: Maps.CavesLankyCabin,
    Regions.TinyCabin: Maps.CavesTinyCabin,
    Regions.ChunkyCabin: Maps.CavesChunkyCabin,
    Regions.CavesBaboonBlast: Maps.CavesBaboonBlast,
    # Castle
    Regions.CreepyCastleEntryHandler: Maps.CreepyCastle,
    Regions.CreepyCastleMain: Maps.CreepyCastle,
    Regions.CastleWaterfall: Maps.CreepyCastle,
    Regions.CastleTree: Maps.CastleTree,
    Regions.Library: Maps.CastleLibrary,
    Regions.LibraryPastSlam: Maps.CastleLibrary,
    Regions.LibraryPastBooks: Maps.CastleLibrary,
    Regions.Ballroom: Maps.CastleBallroom,
    Regions.MuseumBehindGlass: Maps.CastleMuseum,
    Regions.CastleTinyRace: Maps.CastleTinyRace,
    Regions.Tower: Maps.CastleTower,
    Regions.Greenhouse: Maps.CastleGreenhouse,
    Regions.TrashCan: Maps.CastleTrashCan,
    Regions.Shed: Maps.CastleShed,
    Regions.Museum: Maps.CastleMuseum,
    Regions.LowerCave: Maps.CastleLowerCave,
    Regions.Crypt: Maps.CastleCrypt,
    Regions.CastleMinecarts: Maps.CastleMinecarts,
    Regions.Mausoleum: Maps.CastleMausoleum,
    Regions.UpperCave: Maps.CastleUpperCave,
    Regions.Dungeon: Maps.CastleDungeon,
    Regions.CastleBaboonBlast: Maps.CastleBaboonBlast,
    # Helm
    Regions.HideoutHelmEntry: Maps.HideoutHelm,
    Regions.HideoutHelmStart: Maps.HideoutHelm,
    Regions.HideoutHelmSwitchRoom: Maps.HideoutHelm,
    Regions.HideoutHelmMiniRoom: Maps.HideoutHelm,
    Regions.HideoutHelmMain: Maps.HideoutHelm,
    Regions.HideoutHelmDonkeyRoom: Maps.HideoutHelm,
    Regions.HideoutHelmDiddyRoom: Maps.HideoutHelm,
    Regions.HideoutHelmLankyRoom: Maps.HideoutHelm,
    Regions.HideoutHelmTinyRoom: Maps.HideoutHelm,
    Regions.HideoutHelmChunkyRoom: Maps.HideoutHelm,
    Regions.HideoutHelmAfterBoM: Maps.HideoutHelm,
    Regions.HideoutHelmThroneRoom: Maps.HideoutHelm,
    Regions.HideoutHelmKeyRoom: Maps.HideoutHelm,
    Regions.HideoutHelmOOBChunky: Maps.HideoutHelm,
    Regions.HideoutHelmOOBLanky: Maps.HideoutHelm,
}

LevelMapTable = {
    Levels.JungleJapes: [Maps.JungleJapes, Maps.JapesTinyHive, Maps.JapesLankyCave, Maps.JapesMountain, Maps.JapesMinecarts, Maps.JapesUnderGround, Maps.JapesBaboonBlast],
    Levels.AngryAztec: [
        Maps.AngryAztec,
        Maps.AztecTinyTemple,
        Maps.AztecDonkey5DTemple,
        Maps.AztecDiddy5DTemple,
        Maps.AztecLanky5DTemple,
        Maps.AztecTiny5DTemple,
        Maps.AztecChunky5DTemple,
        Maps.AztecTinyRace,
        Maps.AztecLlamaTemple,
        Maps.AztecBaboonBlast,
    ],
    Levels.FranticFactory: [Maps.FranticFactory, Maps.FactoryTinyRace, Maps.FactoryPowerHut, Maps.FactoryCrusher, Maps.FactoryBaboonBlast],
    Levels.GloomyGalleon: [
        Maps.GloomyGalleon,
        Maps.GalleonLighthouse,
        Maps.GalleonMermaidRoom,
        Maps.GalleonSickBay,
        Maps.GalleonSealRace,
        Maps.GalleonTreasureChest,
        Maps.GalleonSubmarine,
        Maps.GalleonMechafish,
        Maps.Galleon5DShipDKTiny,
        Maps.Galleon5DShipDiddyLankyChunky,
        Maps.Galleon2DShip,
        Maps.GalleonBaboonBlast,
    ],
    Levels.FungiForest: [
        Maps.FungiForest,
        Maps.ForestMinecarts,
        Maps.ForestGiantMushroom,
        Maps.ForestChunkyFaceRoom,
        Maps.ForestLankyZingersRoom,
        Maps.ForestLankyMushroomsRoom,
        Maps.ForestAnthill,
        Maps.ForestMillFront,
        Maps.ForestMillBack,
        Maps.ForestSpider,
        Maps.ForestRafters,
        Maps.ForestWinchRoom,
        Maps.ForestMillAttic,
        Maps.ForestThornvineBarn,
        Maps.ForestBaboonBlast,
    ],
    Levels.CrystalCaves: [
        Maps.CrystalCaves,
        Maps.CavesLankyRace,
        Maps.CavesFrozenCastle,
        Maps.CavesDonkeyIgloo,
        Maps.CavesDiddyIgloo,
        Maps.CavesLankyIgloo,
        Maps.CavesTinyIgloo,
        Maps.CavesChunkyIgloo,
        Maps.CavesRotatingCabin,
        Maps.CavesDonkeyCabin,
        Maps.CavesDiddyLowerCabin,
        Maps.CavesDiddyUpperCabin,
        Maps.CavesLankyCabin,
        Maps.CavesTinyCabin,
        Maps.CavesChunkyCabin,
        Maps.CavesBaboonBlast,
    ],
    Levels.CreepyCastle: [
        Maps.CreepyCastle,
        Maps.CastleTree,
        Maps.CastleLibrary,
        Maps.CastleBallroom,
        Maps.CastleMuseum,
        Maps.CastleTinyRace,
        Maps.CastleTower,
        Maps.CastleGreenhouse,
        Maps.CastleTrashCan,
        Maps.CastleShed,
        Maps.CastleLowerCave,
        Maps.CastleCrypt,
        Maps.CastleMinecarts,
        Maps.CastleMausoleum,
        Maps.CastleUpperCave,
        Maps.CastleDungeon,
        Maps.CastleBaboonBlast,
    ],
    Levels.DKIsles: [
        Maps.Isles,
        Maps.BananaFairyRoom,
        Maps.JungleJapesLobby,
        Maps.AngryAztecLobby,
        Maps.IslesSnideRoom,
        Maps.FranticFactoryLobby,
        Maps.GloomyGalleonLobby,
        Maps.FungiForestLobby,
        Maps.CrystalCavesLobby,
        Maps.CreepyCastleLobby,
        Maps.HideoutHelmLobby,
        Maps.TrainingGrounds,
        Maps.Treehouse,
        Maps.KLumsy,
    ],
    Levels.HideoutHelm: [Maps.HideoutHelm],
}


def getLevelFromMap(map_enum):
    """Get level from map index referencing lookup table."""
    for level in LevelMapTable:
        if map_enum in LevelMapTable[level]:
            return level
    return None


MapExitTable = {
    Maps.TrainingGrounds: ["From DK Isles", "From Treehouse"],
    Maps.Treehouse: ["Test Cutscene", "From Training Grounds"],
    Maps.Isles: [
        "From Training Grounds",
        "From K-Lumsy",
        "From Japes Lobby",
        "From Aztec Lobby",
        "From Factory Lobby",
        "From Galleon Lobby",
        "From Fungi Lobby",
        "From Helm Lobby",
        "From Banana Fairy Isle",
        "From Snide's Room",
        "From Caves Lobby",
        "From Castle Lobby",
        "From K Rool",
        "From Training Grounds",
    ],
    Maps.JungleJapes: [
        "From Japes Lobby",
        "From Beehive",
        "From Mountain",
        "From Cranky",
        "From Funky",
        "From Painting Room",
        "From Snide's",
        "From BBlast",
        "From Underground",
        "From T&S (Diddy Cave)",
        "From T&S (Near Cannon)",
        "From ? (Other hill near SSSortie)",
        "From T&S (Near Pool Fairy)",
        "From ? (Near Pool Fairy)",
        "From Minecart",
        "From Japes Lobby",
        "From DK Rap (DKTV Demo)",
        "From Japes Lobby (Intro)",
    ],
    Maps.AngryAztec: [
        "From Aztec Lobby",
        "From Tiny Temple",
        "From Llama Temple",
        "From Tiny 5DTemple",
        "From Chunky 5DTemple",
        "From DK 5DTemple",
        "From Diddy 5DTemple",
        "From Lanky 5DTemple",
        "From Candy's",
        "From Snide's",
        "From Cranky's",
        "From BBlast",
        "From T&S (Candy's)",
        "From T&S (W5)",
        "From T&S (5DTemple)",
        "From T&S (Cranky's)",
        "From T&S (Funky's)",
        "From Beetle Race",
        "From Funky's",
        "From Aztec Lobby",
    ],
    Maps.FranticFactory: [
        "From Factory Lobby",
        "From Arcade Area (near Tiny BP)",
        "From Tiny BP Area (To Arcade Area)",
        "From Power Shed",
        "From R&D Area (To Storage Room)",
        "From Snide's",
        "From Funky's",
        "From Cranky's",
        "From Crusher Room",
        "From T&S (Block Tower)",
        "From T&S (Arcade)",
        "From T&S (R&D)",
        "From T&S (Production Room)",
        "From T&S (Storage Room)",
        "From ? (Near Bad Hit Detection Man)",
        "From BBlast",
        "From Car Race",
        "From Candy's",
        "From Factory Lobby",
    ],
    Maps.GloomyGalleon: [
        "From Galleon Lobby",
        "From Diddy 5DShip",
        "From Chunky 5DShip",
        "From Lanky 5DShip",
        "From Treasure Chest",
        "From Mermaid",
        "From Tiny 5DShip",
        "From Donkey 5DShip",
        "From Tiny 2DShip",
        "From Lanky 2DShip",
        "From Lighthouse",
        "From Seasick Ship",
        "From T&S (Cactus)",
        "From T&S (Near Cranky's)",
        "From T&S (2DShip)",
        "From T&S (Enguarde Door)",
        "From BBlast",
        "From Snide's",
        "From Candy's",
        "From Seal Race",
        "From T&S (Meme Hole)",
        "From Submarine",
        "From Cranky's",
        "From Funky's",
        "From Galleon Lobby",
    ],
    Maps.Galleon5DShipDiddyLankyChunky: ["From Galleon (Diddy Entrance)", "From Galleon (Chunky Entrance)", "From Galleon (Lanky Entrance)", "From Galleon (Diddy Entrance)"],
    Maps.Galleon5DShipDKTiny: ["From Galleon (DK Entrance)", "From Galleon (Tiny Entrance)", "From Galleon (DK Entrance)"],
    Maps.Galleon2DShip: ["From Galleon (Tiny Entrance)", "From Galleon (Lanky Entrance)", "From Galleon (Tiny Entrance)"],
    Maps.FungiForest: [
        "From Fungi Lobby",
        "From Mill Attic",
        "From Winch",
        "From Rafters",
        "From Thornvine Barn",
        "From Mill (PPunch Door)",
        "From Mill (Front)",
        "From Mill (Tiny Hole)",
        "From G. Mush (Low)",
        "From G. Mush (Low Middle)",
        "From G. Mush (Middle)",
        "From G. Mush (High Middle)",
        "From G. Mush (High)",
        "From Face Puzzle (Chunky)",
        "From Mushrooms Room (Lanky)",
        "From Zingers Room (Lanky)",
        "From Minecart",
        "From Cranky's",
        "From Funky's",
        "From Snide's",
        "From T&S (DK Barn)",
        "From T&S (Snide's)",
        "From T&S (Beanstalk)",
        "From Anthill",
        "From T&S (G. Mush)",
        "From T&S (Tree)",
        "From BBlast",
        "From Fungi Lobby (?)",
        "From Fungi Lobby",
    ],
    Maps.ForestMillFront: ["From Fungi (Front)", "From Mill (Rear)", "From Fungi (Front)"],
    Maps.ForestMillBack: ["From Fungi (PPunch Door)", "From Spider Boss", "From Mill (Front)", "From Fungi (Tiny Hole)", "From Fungi (PPunch Door)"],
    Maps.ForestGiantMushroom: ["From Fungi (Low)", "From Fungi (Middle)", "From Fungi (Low Middle)", "From Fungi (High Middle)", "From Fungi (High)", "From Fungi (Low)"],
    Maps.CrystalCaves: [
        "From Caves Lobby",
        "From Diddy 5DIgloo",
        "From DK 5DIgloo",
        "From Lanky 5DIgloo",
        "From Chunky 5DIgloo",
        "From Tiny 5DIgloo",
        "From Beetle Race",
        "From ? (Near Rotating Room)",
        "From ? (Near 1DC)",
        "From ? (Near 5DC)",
        "From ? (Near W3 Room)",
        "From ? (5DIgloo W3, Beta T&S)",
        "From Cranky's",
        "From Funky's",
        "From DK 5DCabin",
        "From Chunky 5DCabin",
        "From Tiny 5DCabin",
        "From Diddy Lower 5DCabin",
        "From Diddy Upper 5DCabin",
        "From Rotating Cabin",
        "From Lanky Cabin",
        "From Candy's",
        "From Snide's",
        "From T&S (Snide's)",
        "From T&S (Rotating Room)",
        "From T&S (1DC)",
        "From T&S (Giant Boulder)",
        "From ? (Behind W3 Room)",
        "From BBlast",
        "From ? (Giant Kosha Room)",
        "From Tile Flipping",
        "From DK Treehouse (Secret Exit)",
        "From Caves Lobby",
    ],
    Maps.CreepyCastle: [
        "From Castle Lobby",
        "From Tree (Drain)",
        "From Tunnel (Front)",
        "From T&S (W2)",
        "From Lower Cave",
        "From Tunnel (Rear)",
        "From T&S (Rear)",
        "From Museum",
        "From Greenhouse (Start)",
        "From Shed",
        "From T&S (W4)",
        "From Ballroom",
        "From Library (Start)",
        "From Library (End)",
        "From Tower",
        "From Tree (Entrance)",
        "From Trash Can",
        "From BBlast",
        "From Cranky's",
        "From Snide's",
        "From Greenhouse (End)",
        "From Castle Lobby (Intro)",
        "From Castle Lobby",
    ],
    Maps.CastleBallroom: ["From Castle Main", "From Museum (Monkeyport)", "From Castle Main"],
    Maps.CastleCrypt: ["From Lower Cave", "From Minecart", "From Lower Cave"],
    Maps.CastleMuseum: ["From Castle Main", "From Car Race", "From Ballroom (Monkeyport)", "From Castle Main"],
    Maps.CastleLibrary: ["From Castle Main (Start)", "From Castle Main (End)"],
    Maps.CastleUpperCave: ["From Castle (Front)", "From Candy's", "From Castle (Rear)", "From T&S", "From Dungeon", "From Castle (Front)"],
    Maps.CastleLowerCave: ["From Castle Main", "From Funky's", "From T&S", "From Crypt (DK/Diddy/Chunky)", "From Mausoleum (Lanky/Tiny)", "From Castle Main"],
    Maps.JungleJapesLobby: ["From DK Isles", "From Japes", "From DK Isles"],
    Maps.AngryAztecLobby: ["From DK Isles", "From Aztec", "From DK Isles"],
    Maps.GloomyGalleonLobby: ["From DK Isles", "From Galleon", "From DK Isles"],
    Maps.FranticFactoryLobby: ["From DK Isles", "From Factory", "From DK Isles"],
    Maps.FungiForestLobby: ["From DK Isles", "From Fungi", "From DK Isles"],
    Maps.CreepyCastleLobby: ["From DK Isles", "From Castle", "From DK Isles"],
    Maps.CrystalCavesLobby: ["From DK Isles", "From Caves", "From DK Isles"],
    Maps.HideoutHelmLobby: ["From DK Isles", "From Helm", "From DK Isles"],
}


def GetMapId(regionId) -> Maps:
    """Get the map id of a transition."""
    return RegionMapList[regionId]


def GetExitId(back: TransitionBack) -> int:
    """Get exit id of a transition."""
    mapId = GetMapId(back.regionId)
    if mapId in MapExitTable:
        return MapExitTable[mapId].index(back.name)
    else:
        # Default exit number should be zero for all maps that don't have multiple exits
        return 0
