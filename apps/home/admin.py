from django.contrib import admin
from .models import (
    AndInventory,
    AndProperties,
    AtlDump,
    AtlInventory,
    AtlProperties,
    BuyersSellers,
    ItemsDb,
    Itemsdb2,
    NycDump,
    NycInventory,
    NycProperties,
    PlayerLocations,
    PlayerProfiles,
    PlayerStats,
    TravelRoutes
)

@admin.register(AndInventory)
class AndInventoryAdmin(admin.ModelAdmin):
    pass

@admin.register(AndProperties)
class AndPropertiesAdmin(admin.ModelAdmin):
    pass

@admin.register(AtlDump)
class AtlDumpAdmin(admin.ModelAdmin):
    pass

@admin.register(AtlInventory)
class AtlInventoryAdmin(admin.ModelAdmin):
    pass

@admin.register(AtlProperties)
class AtlPropertiesAdmin(admin.ModelAdmin):
    pass

@admin.register(BuyersSellers)
class BuyersSellersAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemsDb)
class ItemsDbAdmin(admin.ModelAdmin):
    pass

@admin.register(Itemsdb2)
class Itemsdb2Admin(admin.ModelAdmin):
    pass

@admin.register(NycDump)
class NycDumpAdmin(admin.ModelAdmin):
    pass

@admin.register(NycInventory)
class NycInventoryAdmin(admin.ModelAdmin):
    pass

@admin.register(NycProperties)
class NycPropertiesAdmin(admin.ModelAdmin):
    pass

@admin.register(PlayerLocations)
class PlayerLocationsAdmin(admin.ModelAdmin):
    pass

@admin.register(PlayerProfiles)
class PlayerProfilesAdmin(admin.ModelAdmin):
    pass

@admin.register(PlayerStats)
class PlayerStatsAdmin(admin.ModelAdmin):
    pass

@admin.register(TravelRoutes)
class TravelRoutesAdmin(admin.ModelAdmin):
    pass
