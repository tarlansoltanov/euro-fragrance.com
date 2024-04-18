from django.db import models


class BaseSetting(models.Model):
    """Model definition for BaseSetting."""

    company_name = models.CharField(verbose_name="Company Name", max_length=255)
    advert = models.CharField(verbose_name="Advertisement", max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=255)
    phone = models.CharField(verbose_name="Phone", max_length=255)
    facebook = models.CharField(verbose_name="Facebook", max_length=255)
    instagram = models.CharField(verbose_name="Instagram", max_length=255)
    address = models.CharField(verbose_name="Address", max_length=255)
    address_url = models.CharField(verbose_name="Address URL", max_length=255)

    class Meta:
        """Meta definition for BaseSetting."""

        verbose_name = "BaseSetting"
        verbose_name_plural = "BaseSettings"

    def __str__(self):
        """Unicode representation of BaseSetting."""
        return self.company_name
