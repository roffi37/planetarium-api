from django.contrib.auth import get_user_model
from django.db import models


class ShowTheme(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self) -> str:
        return self.name


class AstronomyShow(models.Model):
    title = models.CharField(max_length=63, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ("title", )


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def total_seats(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("name", )


class ShowSession(models.Model):
    astronomy_show = models.ForeignKey(AstronomyShow, on_delete=models.CASCADE)
    planetarium_dome = models.ForeignKey(PlanetariumDome, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.astronomy_show.title} at {self.show_time}"

    class Meta:
        ordering = ("-show_time", )


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = get_user_model()

    def __str__(self) -> str:
        return str(self.created_at)

    class Meta:
        ordering = ("created_at", )


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    show_session = models.ForeignKey(ShowSession, on_delete=models.CASCADE, related_name="tickets")
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="tickets")

    def __str__(self) -> str:
        return f"{self.show_session} {self.row} {self.seat}"

    class Meta:
        ordering = ("row", "seat", )
