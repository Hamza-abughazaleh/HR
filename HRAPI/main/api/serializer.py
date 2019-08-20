from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from main.models import Candidates
from main.utils import normalise_email


# Serializers define the API representation.
class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidates
        fields = ['email', 'first_name', 'last_name', 'password', 'department_id', 'years_of_experience',
                  'date_of_birth', 'resume']

    def validate(self, data):
        email = normalise_email(data["email"])
        if Candidates._default_manager.filter(email__iexact=email).exists():
            raise serializers.ValidationError(_("A user with that email address already exists"))
        return data

    def create(self, validated_data):
        user = super(CandidatesSerializer, self).create(validated_data)
        user.username = validated_data['email']
        user.set_password(validated_data['password'])
        user.save()
        return user


class CandidatesListSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField(source='get_full_name')
    candidates_details = serializers.HyperlinkedIdentityField(view_name='candidates-detail', lookup_field='pk')

    class Meta:
        model = Candidates
        fields = ['full_name', 'years_of_experience', 'date_of_birth', 'candidates_details']


class CandidatesDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField(source='get_full_name')

    class Meta:
        model = Candidates
        fields = ['full_name', 'email', 'department_id', 'years_of_experience', 'date_of_birth', 'resume']


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        try:
            normalise_email(attrs['email'])
        except:
            raise serializers.ValidationError(_('invalid username or password'))
        user = authenticate(username=attrs['email'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError(_('invalid login'))
        elif not user.is_active:
            raise serializers.ValidationError(
                _('Can not log in as inactive user'))
        self.instance = user
        return attrs
