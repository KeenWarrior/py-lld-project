from django.db import models


class User(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    default_shipping_address = models.ForeignKey(
        "ShippingAddress",
        on_delete=models.DO_NOTHING,
        null=True,
        related_query_name="user_info"
    )

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        abstract = True


class ShippingAddress(Address):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shipping_addresses"
    )



