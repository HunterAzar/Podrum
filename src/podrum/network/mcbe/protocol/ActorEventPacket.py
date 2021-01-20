from podrum.network.mcbe.protocol.DataPacket import DataPacket
from podrum.network.mcbe.protocol.Info import Info

class ActorEventPacket(DataPacket):
    networkId = Info.ACTOR_EVENT_PACKET
    entityRuntimeId = None
    event = None
    data = 0

    JUMP = 1
    HURT_ANIMATION = 2
    DEATH_ANIMATION = 3
    ARM_SWING = 4
    STOP_ATTACK = 5
    TAME_FAIL = 6
    TAME_SUCCESS =7
    SHAKE_WET = 8
    USE_ITEM = 9
    EAT_GRASS_ANIMATION = 10
    FISH_HOOK_BUBBLE = 11
    FISH_HOOK_POSITION = 12
    FISH_HOOK_HOOK = 13
    FISH_HOOK_TEASE = 14
    SQUID_INK_CLOUD = 15
    ZOMBIE_VILLAGER_CURE = 16
    RESPAWN = 18
    IRON_GOLEM_OFFER_FLOWER = 19
    IRON_GOLEM_WITHDRAW_FLOWER = 20
    LOVE_PARTICLES = 21
    VILLAGER_ANGRY = 22
    VILLAGER_HAPPY = 23
    WITCH_SPELL_PARTICLES = 24
    FIREWORK_PARTICLES = 25
    IN_LOVE_PARTICLES = 26
    SILVERFISH_SPAWN_ANIMATION = 27
    GUARDIAN_ATTACK = 28
    WITCH_DRINK_POTION = 29
    WITCH_THROW_POTION = 30
    MINECRAFT_TNT_PRIME_FUSE = 31
    CREEPER_PRIME_FUSE = 32
    AIR_SUPPLY_EXPIRED = 33
    PLAYER_ADD_XP_LEVELS = 34
    ELDER_GUARDIAN_CURSE = 35
    AGENT_ARM_SWING = 36
    ENDER_DRAGON_DEATH = 37
    DUST_PARTICLES = 38
    ARROW_SHAKE = 39
    EATING_ITEM = 57
    BABY_ANIMAL_FEED = 60
    DEATH_SMOKE_CLOUD = 61
    COMPLETE_TRADE = 62
    REMOVE_LEASH = 63
    CONSUME_TOTEM = 65
    PLAYER_CHECK_TREASURE_HUNTER_ACHIEVEMENT = 66
    ENTITY_SPAWN = 67
    DRAGON_PUKE = 68
    ITEM_ENTITY_MERGE = 69
    START_SWIM = 70
    BALLOON_POP = 71
    TREASURE_HUNT = 72
    AGENT_SUMMON = 73
    CHARGED_CROSSBOW = 74
    FALL = 75

    def decodePayload(self):
        self.entityRuntimeId = self.getUnsignedVarLong()
        self.event = self.getByte()
        self.data = self.getVarInt()

    def encodePayload(self):
        self.putUnsignedVarLong(self.entityRuntimeId)
        self.putByte(self.event)
        self.putVarInt(self.data)