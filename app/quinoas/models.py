import uuid as uuid_lib #pip install uuid
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible # For Python 3.5+ and 2.7
class Quinua(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')
    datetimer = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name',]
        verbose_name_plural = 'Quinuas'

@python_2_unicode_compatible # For Python 3.5+ and 2.7
class Sample(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    quinua = models.ForeignKey(Quinua, on_delete=models.CASCADE, \
                               related_name='Quinua')
    image = models.ImageField(upload_to='samples/')
    broken_grain = models.FloatField(default=0.00)
    damaged_grain = models.FloatField(default=0.00)
    immature_grain = models.FloatField(default=0.00)
    coated_grain = models.FloatField(default=0.00)
    germinated_grain = models.FloatField(default=0.00)
    whole_grain = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00)
    
    def __str__(self):
        return str(self.uuid)

    def save(self, *args, **kwargs):
        self.total = self.broken_grain + self.damaged_grain
        # url = self.image.url
        # print(str(url))
        # re = prediction_grain(str(url))
        # print(re)
        super(Sample, self).save(*args, **kwargs)
        if self.image:
            # from ia.label_image_tensor import prediction_grain
            # url = self.image.url
            # result = prediction_grain(url)
            # who = result['bueno']
            # self.whole_grain = round(who, 2)
            super(Sample, self).save(*args, **kwargs)

    class Meta:
        ordering = ['uuid',]
        verbose_name_plural = 'Sample'
