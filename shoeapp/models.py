from django.db import models

# Create your models here.


class Manufacturer (models.Model):
    name = models.CharField(max_length=40)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Shoetype (models.Model):
    SHOE_CHOICES = (
        ('SNEAKER', 'SNEAKER'),
        ('BOOT', 'BOOT'),
        ('SANDAL', 'SANDAL'),
        ('DRESS', 'DRESS'),
        ('OTHER', 'OTHER')
    )

    style = models.CharField(max_length=10, choices=SHOE_CHOICES)

    def __str__(self):
        return self.style


class ShoeColor (models.Model):
    COLOR_CHOICES = (
        ('R', 'RED'),
        ('O', 'ORANGE'),
        ('Y', 'YELLOW'),
        ('G', 'GREEN'),
        ('B', 'BLUE'),
        ('I', 'INDIGO'),
        ('V', 'VIOLET'),
        ('W', 'WHITE'),
        ('BL', 'BLACK')
    )

    color_name = models.CharField(max_length=10, choices=COLOR_CHOICES)

    def __str__(self):
        return self.color_name

# Joe made friends with hyenas Shenzi, Banzai & Ed in the African Savanna


class Shoe (models.Model):
    size = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=20)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(Shoetype, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.color}-{self.brand_name}-{self.shoe_type}'
