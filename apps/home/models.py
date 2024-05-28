# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AndInventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.TextField(blank=True, null=True)  # This field type is a guess.
    cash = models.TextField(blank=True, null=True)  # This field type is a guess.
    diamonds = models.TextField(blank=True, null=True)  # This field type is a guess.
    gold = models.TextField(blank=True, null=True)  # This field type is a guess.
    item1 = models.TextField(db_column='Item1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item1qty = models.TextField(db_column='Item1Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item2 = models.TextField(db_column='Item2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item2qty = models.TextField(db_column='Item2Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item3 = models.TextField(db_column='Item3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item3qty = models.TextField(db_column='Item3Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item4 = models.TextField(db_column='Item4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item4qty = models.TextField(db_column='Item4Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item5 = models.TextField(db_column='Item5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item5qty = models.TextField(db_column='Item5Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item6 = models.TextField(db_column='Item6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item6qty = models.TextField(db_column='Item6Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'and_inventory'


class AndProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop8 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'and_properties'


class AtlDump(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    dropped_by_username = models.TextField(blank=True, null=True)
    item_code = models.TextField(blank=True, null=True)
    item_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'atl_dump'


class AtlInventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    username = models.TextField(blank=True, null=True)  # This field type is a guess.
    cash = models.TextField(blank=True, null=True)  # This field type is a guess.
    diamonds = models.TextField(blank=True, null=True)  # This field type is a guess.
    gold = models.TextField(blank=True, null=True)  # This field type is a guess.
    item1 = models.TextField(db_column='Item1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item1qty = models.TextField(db_column='Item1Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item2 = models.TextField(db_column='Item2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item2qty = models.TextField(db_column='Item2Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item3 = models.TextField(db_column='Item3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item3qty = models.TextField(db_column='Item3Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item4 = models.TextField(db_column='Item4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item4qty = models.TextField(db_column='Item4Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item5 = models.TextField(db_column='Item5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item5qty = models.TextField(db_column='Item5Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item6 = models.TextField(db_column='Item6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item6qty = models.TextField(db_column='Item6Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'atl_inventory'


class AtlProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    username = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop8 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'atl_properties'


class BuyersSellers(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    buyer_or_seller = models.TextField(db_column='Buyer_or_seller', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    neighborhood = models.TextField(db_column='Neighborhood', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    ec_rep_required = models.IntegerField(blank=True, null=True)
    wc_rep_required = models.IntegerField(blank=True, null=True)
    mx_rep_required = models.IntegerField(blank=True, null=True)
    max_heat = models.IntegerField(blank=True, null=True)
    itemcode_sold = models.TextField(blank=True, null=True)
    dealer_level = models.TextField(blank=True, null=True)
    quantityavailable = models.TextField(blank=True, null=True)
    informant = models.TextField(blank=True, null=True)
    undercover = models.TextField(blank=True, null=True)
    rep_increase_100k = models.IntegerField(blank=True, null=True)
    rep_increase_10k = models.FloatField(blank=True, null=True)
    itemcode_buy = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    purity = models.TextField(blank=True, null=True)
    offer_price = models.IntegerField(blank=True, null=True)
    price_multiplier = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'buyers_sellers'


class ItemsDb(models.Model):
    id = models.BigAutoField(primary_key=True)
    picture_code = models.IntegerField(db_column='Picture_code', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    qty_unit = models.IntegerField(db_column='Qty_unit', blank=True, null=True)  # Field name made lowercase.
    item_code = models.IntegerField(db_column='Item_code', blank=True, null=True)  # Field name made lowercase.
    source_code = models.IntegerField(db_column='Source_code', blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    carried = models.IntegerField(db_column='Carried', blank=True, null=True)  # Field name made lowercase.
    public_plane = models.IntegerField(db_column='Public_plane', blank=True, null=True)  # Field name made lowercase.
    private_plane = models.IntegerField(db_column='Private_plane', blank=True, null=True)  # Field name made lowercase.
    networth = models.IntegerField(db_column='Networth', blank=True, null=True)  # Field name made lowercase.
    purity = models.IntegerField(db_column='Purity', blank=True, null=True)  # Field name made lowercase.
    breakdown_item_code = models.IntegerField(db_column='Breakdown_item_code', blank=True, null=True)  # Field name made lowercase.
    breakdown_x = models.IntegerField(db_column='Breakdown_x', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    street_price = models.IntegerField(db_column='Street_price', blank=True, null=True)  # Field name made lowercase.
    bulk_price = models.IntegerField(db_column='Bulk_price', blank=True, null=True)  # Field name made lowercase.
    distributor_price = models.IntegerField(db_column='Distributor_price', blank=True, null=True)  # Field name made lowercase.
    farm_price = models.IntegerField(db_column='Farm_price', blank=True, null=True)  # Field name made lowercase.
    solo_mission_take = models.IntegerField(db_column='Solo_mission_take', blank=True, null=True)  # Field name made lowercase.
    attack_take = models.IntegerField(db_column='Attack_take', blank=True, null=True)  # Field name made lowercase.
    police_take = models.IntegerField(db_column='Police_take', blank=True, null=True)  # Field name made lowercase.
    mission_1 = models.IntegerField(db_column='Mission_1', blank=True, null=True)  # Field name made lowercase.
    mission_2 = models.IntegerField(db_column='Mission_2', blank=True, null=True)  # Field name made lowercase.
    mission_3 = models.IntegerField(db_column='Mission_3', blank=True, null=True)  # Field name made lowercase.
    mission_4 = models.IntegerField(db_column='Mission_4', blank=True, null=True)  # Field name made lowercase.
    attack_stat = models.IntegerField(db_column='Attack_stat', blank=True, null=True)  # Field name made lowercase.
    destroys_veh = models.IntegerField(db_column='Destroys_Veh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'items_db'


class Itemsdb2(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    picture_code = models.TextField(db_column='Picture_code', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    qty_unit = models.TextField(db_column='Qty_unit', blank=True, null=True)  # Field name made lowercase.
    item_code = models.TextField(db_column='Item_code', blank=True, null=True)  # Field name made lowercase.
    source_code = models.TextField(db_column='Source_code', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    carried = models.TextField(db_column='Carried', blank=True, null=True)  # Field name made lowercase.
    public_plane = models.TextField(db_column='Public_plane', blank=True, null=True)  # Field name made lowercase.
    private_plane = models.TextField(db_column='Private_plane', blank=True, null=True)  # Field name made lowercase.
    networth = models.TextField(db_column='Networth', blank=True, null=True)  # Field name made lowercase.
    purity = models.TextField(db_column='Purity', blank=True, null=True)  # Field name made lowercase.
    breakdown_item_code = models.TextField(db_column='Breakdown_item_code', blank=True, null=True)  # Field name made lowercase.
    breakdown_x = models.TextField(db_column='Breakdown_x', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    street_price = models.IntegerField(db_column='Street_price', blank=True, null=True)  # Field name made lowercase.
    bulk_price = models.IntegerField(db_column='Bulk_price', blank=True, null=True)  # Field name made lowercase.
    distributor_price = models.IntegerField(db_column='Distributor_price', blank=True, null=True)  # Field name made lowercase.
    farm_price = models.IntegerField(db_column='Farm_price', blank=True, null=True)  # Field name made lowercase.
    solo_mission_take = models.TextField(db_column='Solo_mission_take', blank=True, null=True)  # Field name made lowercase.
    attack_take = models.TextField(db_column='Attack_take', blank=True, null=True)  # Field name made lowercase.
    police_take = models.TextField(db_column='Police_take', blank=True, null=True)  # Field name made lowercase.
    mission1 = models.TextField(blank=True, null=True)
    mission2 = models.TextField(blank=True, null=True)
    mission3 = models.TextField(blank=True, null=True)
    mission4 = models.TextField(blank=True, null=True)
    attack_stat = models.IntegerField(db_column='Attack_stat', blank=True, null=True)  # Field name made lowercase.
    destroys_veh = models.TextField(db_column='Destroys_Veh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'itemsdb2'


class NycDump(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    dropped_by_username = models.TextField(blank=True, null=True)
    item_code = models.TextField(blank=True, null=True)
    item_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'nyc_dump'


class NycInventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    username = models.TextField(blank=True, null=True)  # This field type is a guess.
    cash = models.TextField(blank=True, null=True)  # This field type is a guess.
    diamonds = models.TextField(blank=True, null=True)  # This field type is a guess.
    gold = models.TextField(blank=True, null=True)  # This field type is a guess.
    item1 = models.TextField(db_column='Item1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item1qty = models.TextField(db_column='Item1Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item2 = models.TextField(db_column='Item2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item2qty = models.TextField(db_column='Item2Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item3 = models.TextField(db_column='Item3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item3qty = models.TextField(db_column='Item3Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item4 = models.TextField(db_column='Item4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item4qty = models.TextField(db_column='Item4Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item5 = models.TextField(db_column='Item5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item5qty = models.TextField(db_column='Item5Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item6 = models.TextField(db_column='Item6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item6qty = models.TextField(db_column='Item6Qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'nyc_inventory'


class NycProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    username = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    prop8 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'nyc_properties'


class PlayerLocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    username = models.TextField()
    city = models.TextField()
    travel_route = models.TextField(blank=True, null=True)
    travel_time_remaining = models.IntegerField(blank=True, null=True)
    jail = models.IntegerField(blank=True, null=True)
    jail_time = models.IntegerField(blank=True, null=True)
    hospital = models.IntegerField(blank=True, null=True)
    hospital_time = models.IntegerField(blank=True, null=True)
    untouchable_jail = models.IntegerField(blank=True, null=True)
    untouchable_hospital = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'player_locations'


class PlayerProfiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    username = models.TextField(blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)
    wc_rep = models.IntegerField(blank=True, null=True)
    ec_rep = models.IntegerField(blank=True, null=True)
    mx_rep = models.IntegerField(blank=True, null=True)
    heat = models.IntegerField(blank=True, null=True)
    us_banking = models.IntegerField(blank=True, null=True)
    mx_banking = models.IntegerField(blank=True, null=True)
    networth = models.IntegerField()
    account_age = models.IntegerField()
    email_address = models.IntegerField(blank=True, null=True)
    country = models.TextField()
    app_language = models.TextField()
    has_spent_money = models.TextField()

    class Meta:
        db_table = 'player_profiles'


class PlayerStats(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    username = models.IntegerField(blank=True, null=True)
    jail_visits = models.IntegerField(blank=True, null=True)
    hospital_visits = models.IntegerField(blank=True, null=True)
    peak_networth = models.IntegerField(blank=True, null=True)
    kg_cocaine = models.IntegerField(blank=True, null=True)
    kg_meth = models.IntegerField(blank=True, null=True)
    kg_weed = models.IntegerField(blank=True, null=True)
    total_cash_made = models.IntegerField(blank=True, null=True)
    total_cash_spent = models.IntegerField(blank=True, null=True)
    total_attacks = models.IntegerField(blank=True, null=True)
    total_been_attacked = models.IntegerField(blank=True, null=True)
    total_missions = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'player_stats'


class TravelRoutes(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    route_code = models.TextField(blank=True, null=True)
    starting_city = models.TextField(blank=True, null=True)
    destination_city = models.TextField(blank=True, null=True)
    mode = models.TextField(blank=True, null=True)
    heat = models.IntegerField(blank=True, null=True)
    time_minutes = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'travel_routes'
