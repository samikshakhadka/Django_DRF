from rest_framework import serializers
from app.api.models import PoliticalParty, Place, MP , Sector


class PoliticalPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticalParty
        fields = ['id', 'name']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name']

class MPSerializer(serializers.ModelSerializer):
    party = serializers.PrimaryKeyRelatedField(queryset=PoliticalParty.objects.all())
    place = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all())

    class Meta:
        model = MP
        fields = ['id', 'name', 'party', 'place']
        read_only_fields = ['created']

    def create(self, validated_data):
        party_name = validated_data.pop('party').id
        
        place_name = validated_data.pop('place').id
        

        party = PoliticalParty.objects.get(id= party_name)
        place = Place.objects.get(id=place_name)

        mp = MP.objects.create(party=party, place=place, **validated_data)
        return mp
    

class SectorSerializer(serializers.ModelSerializer):
    mp = serializers.PrimaryKeyRelatedField(queryset=MP.objects.all(), many=True)

    class Meta:
        model = Sector
        fields = ['id', 'name', 'mp']

    def create(self, validated_data):
        mp_data = validated_data.pop('mp')
        sector = Sector.objects.create(**validated_data)
        
        sector.mp.set(mp_data)  
        return sector