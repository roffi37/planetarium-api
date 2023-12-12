from django.contrib import admin

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)


@admin.register(ShowSession)
class ShowSession(admin.ModelAdmin):
    list_display = ("astronomy_show", "planetarium_dome", "show_time", )
    list_filter = ("show_time", )
    search_fields = ("astronomy_show", )


@admin.register(ShowTheme)
class ShowTheme(admin.ModelAdmin):
    list_display = ("name", )
    list_filter = ("name", )
    search_fields = ("name", )


@admin.register(AstronomyShow)
class AstronomyShow(admin.ModelAdmin):
    list_display = ("title", "description", )
    list_filter = ("title", )
    search_fields = ("title", )


@admin.register(PlanetariumDome)
class PlanetariumDome(admin.ModelAdmin):
    list_display = ("name", "rows", "seats_in_row", "total_seats", )
    list_filter = ("name", )
    search_fields = ("name", )


@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_display = ("created_at", "user", )
    list_filter = ("created_at", )
    search_fields = ("user", )


@admin.register(Ticket)
class Ticker(admin.ModelAdmin):
    list_display = ("row", "seat", "show_session", "reservation", )
    search_fields = ("show_session", )
