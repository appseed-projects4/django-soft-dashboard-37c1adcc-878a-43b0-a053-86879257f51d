# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Sliberty_Gguajira(models.Model):

    #__Sliberty_Gguajira_FIELDS__
    sliberty_gguajira_sfunerario_ptradicional_prima = models.CharField(max_length=255, null=True, blank=True)

    #__Sliberty_Gguajira_FIELDS__END

    class Meta:
        verbose_name        = _("Sliberty_Gguajira")
        verbose_name_plural = _("Sliberty_Gguajira")


class Sliberty_Gcaribe(models.Model):

    #__Sliberty_Gcaribe_FIELDS__

    #__Sliberty_Gcaribe_FIELDS__END

    class Meta:
        verbose_name        = _("Sliberty_Gcaribe")
        verbose_name_plural = _("Sliberty_Gcaribe")


class Sliberty_Surtigas(models.Model):

    #__Sliberty_Surtigas_FIELDS__

    #__Sliberty_Surtigas_FIELDS__END

    class Meta:
        verbose_name        = _("Sliberty_Surtigas")
        verbose_name_plural = _("Sliberty_Surtigas")


class Sliberty_Efigas(models.Model):

    #__Sliberty_Efigas_FIELDS__

    #__Sliberty_Efigas_FIELDS__END

    class Meta:
        verbose_name        = _("Sliberty_Efigas")
        verbose_name_plural = _("Sliberty_Efigas")


class Sliberty_Goccidente(models.Model):

    #__Sliberty_Goccidente_FIELDS__
    sliberty_goccidente_sfunerario_tradicional_prima = models.CharField(max_length=255, null=True, blank=True)

    #__Sliberty_Goccidente_FIELDS__END

    class Meta:
        verbose_name        = _("Sliberty_Goccidente")
        verbose_name_plural = _("Sliberty_Goccidente")


class Sliberty_Ceo(models.Model):

    #__Sliberty_Ceo_FIELDS__

    #__Sliberty_Ceo_FIELDS__END

    class Meta:
        verbose_name        = _("Sliberty_Ceo")
        verbose_name_plural = _("Sliberty_Ceo")


class Salfa_Gcaribe(models.Model):

    #__Salfa_Gcaribe_FIELDS__

    #__Salfa_Gcaribe_FIELDS__END

    class Meta:
        verbose_name        = _("Salfa_Gcaribe")
        verbose_name_plural = _("Salfa_Gcaribe")


class Salfa_Gguajira(models.Model):

    #__Salfa_Gguajira_FIELDS__

    #__Salfa_Gguajira_FIELDS__END

    class Meta:
        verbose_name        = _("Salfa_Gguajira")
        verbose_name_plural = _("Salfa_Gguajira")


class Salfa_Surtigas(models.Model):

    #__Salfa_Surtigas_FIELDS__

    #__Salfa_Surtigas_FIELDS__END

    class Meta:
        verbose_name        = _("Salfa_Surtigas")
        verbose_name_plural = _("Salfa_Surtigas")


class Salfa_Efigas(models.Model):

    #__Salfa_Efigas_FIELDS__

    #__Salfa_Efigas_FIELDS__END

    class Meta:
        verbose_name        = _("Salfa_Efigas")
        verbose_name_plural = _("Salfa_Efigas")


class Salfa_Goccidente(models.Model):

    #__Salfa_Goccidente_FIELDS__
    salfa_goccidente_sfactura_tmk_indemnizacion = models.CharField(max_length=255, null=True, blank=True)

    #__Salfa_Goccidente_FIELDS__END

    class Meta:
        verbose_name        = _("Salfa_Goccidente")
        verbose_name_plural = _("Salfa_Goccidente")


class Salfa_Ceo(models.Model):

    #__Salfa_Ceo_FIELDS__

    #__Salfa_Ceo_FIELDS__END

    class Meta:
        verbose_name        = _("Salfa_Ceo")
        verbose_name_plural = _("Salfa_Ceo")


class Szuritch_Pcombovida(models.Model):

    #__Szuritch_Pcombovida_FIELDS__

    #__Szuritch_Pcombovida_FIELDS__END

    class Meta:
        verbose_name        = _("Szuritch_Pcombovida")
        verbose_name_plural = _("Szuritch_Pcombovida")


class Szuritch_Paccidentperasistencia(models.Model):

    #__Szuritch_Paccidentperasistencia_FIELDS__
    szuritch_pvidarentadiaxhosp_plan1_asistmedyodonto(s_n) = models.CharField(max_length=255, null=True, blank=True)
    szuritch_pvidarentadiaxhosp_plan2_asistmedyodonto(s_n) = models.CharField(max_length=255, null=True, blank=True)
    szuritch_pvidarentadiaxhosp_plan3_asistmedyodonto(s_n) = models.CharField(max_length=255, null=True, blank=True)
    szuritch_pvidarentadiaxhosp_plan4_asistmedyodonto(s_n) = models.CharField(max_length=255, null=True, blank=True)

    #__Szuritch_Paccidentperasistencia_FIELDS__END

    class Meta:
        verbose_name        = _("Szuritch_Paccidentperasistencia")
        verbose_name_plural = _("Szuritch_Paccidentperasistencia")


class Szuritch_Pvidaenfergraves(models.Model):

    #__Szuritch_Pvidaenfergraves_FIELDS__
    szuritch_pvidaenfergraves_plan3_vida = models.CharField(max_length=255, null=True, blank=True)

    #__Szuritch_Pvidaenfergraves_FIELDS__END

    class Meta:
        verbose_name        = _("Szuritch_Pvidaenfergraves")
        verbose_name_plural = _("Szuritch_Pvidaenfergraves")



#__MODELS__END
