import uuid as uuid_lib #pip install uuid
# import google.protobuf
import io
import tensorflow.compat.v1 as tf

from PIL import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django.db.models import F
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from ia.disaggregate import split_sample
from ia.label_image_tensor import prediction_grain

from utils.comparelists import list_counter
from utils.percent import percent_all

@python_2_unicode_compatible # For Python 3.5+ and 2.7
class Grain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid_lib.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    class Meta:
        #abstract = True
        ordering = ['name',]
        verbose_name_plural = 'Grains'

@python_2_unicode_compatible # For Python 3.5+ and 2.7
class CategoryGrain(models.Model):
    # uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    id = models.UUIDField(
        primary_key=True, default=uuid_lib.uuid4, editable=False
    )
    name = models.CharField(max_length=255)
    min_measure = models.FloatField(default=0)
    max_measure = models.FloatField(default=0)
    
    
    def __str__(self):
        return str(self.name)

    #def get_absolute_url(self):
        #return reverse('name_url', kwargs={'pk': self.pk})

    class Meta:
        #abstract = True
        ordering = ['name',]
        verbose_name = 'Category Grain'
        verbose_name_plural = 'Categories Grains'

@python_2_unicode_compatible # For Python 3.5+ and 2.7
class TypeGrain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid_lib.uuid4, editable=False)
    name_type = models.CharField(max_length=255)
    grain = models.ForeignKey(Grain, on_delete=models.CASCADE, related_name='grain_type')
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name_type)

    class Meta:
        #abstract = True
        ordering = ['name_type',]
        verbose_name_plural = 'Types Grains'

def sample_path(instance, filename):
    slugify_name = slugify(instance.name_sample)
    return 'sample-{0}/{1}'.format(slugify_name, filename)

@python_2_unicode_compatible # For Python 3.5+ and 2.7
class SampleGrain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid_lib.uuid4, editable=False)
    name_sample = models.CharField(max_length=255)
    image = models.ImageField(upload_to=sample_path)
    image_recognized_grains = models.ImageField(
        upload_to=sample_path, blank=True
    )
    grain = models.ForeignKey(
        Grain, on_delete=models.CASCADE, related_name='grain_sample'
    )
    total_grains = models.IntegerField(default=0)
    
    __original_image = None

    def __init__(self, *args, **kwargs):
        super(SampleGrain, self).__init__(*args, **kwargs)
        self.__original_image = self.image
    
    def __str__(self):
        return (str(self.grain.name) + ' | ' + str(self.name_sample))

    def image_from_array(self, array_image):
        image_temp = Image.fromarray(array_image)
        image_blob = io.BytesIO()
        image_temp.save(image_blob, 'JPEG')
        return ContentFile(image_blob.getvalue())
        # return image_create

    def save(self, *args, **kwargs):
        super(SampleGrain, self).save(*args, **kwargs)
        if self.image != self.__original_image:
            print("New Sample")
            result_grains = split_sample(self.image.url)
            self.total_grains = int(result_grains['total_grains'])
            super(SampleGrain, self).save(*args, **kwargs)
        else:
            print("Update Sample")
            result_grains = split_sample(self.image.url)
            grains = result_grains['grains_result']
            
            # image_out = Image.new('RGB', (640, 480))
            # grain_out = result_grains['image_border']
            # image_out.save(grain_out, format='JPEG')
            # outlines = ContentFile(grain_out.getvalue())
            # self.image_recognized_grains.save('outlines.jpg', outlines)
            # sdg.image_result.save(name_g + '.jpg', isf)
            # self.save()


            categories = CategoryGrain.objects.all()
            # categories_grains = {}
            # for cg in range(len(categories)):
            #     types_found.append(detail_grains[sdg].type_grain_detail.id)
            for g in range(1, len(grains) + 1):
                name_g = str(g)
                area_g = grains[g]['area']
                width_g = grains[g]['width']
                height_g = grains[g]['height']
                image_g = grains[g]['image']
                diameter_level = (width_g + height_g)/2

                sdg = SampleDetailGrain()
                sdg.name_seed = name_g
                sdg.sample = self
                sdg.area = area_g
                sdg.width_grain = width_g
                sdg.heigth_grain = height_g
                sdg.diameter_grain = diameter_level 
                
                # sdg.category_grain_detail = 
                
                ima = Image.fromarray(image_g)
                blob = io.BytesIO()
                ima.save(blob, 'JPEG')
                isf = ContentFile(blob.getvalue())
                sdg.image_result.save(name_g + '.jpg', isf)

                sdg.save()
                # print(path_image)
                # print(path_image_url)
                # print(os.path.basename(path_image))

                # image_f = cv2.imwrite(name_g + '.jpg', image_g)
                # image_d = Image.open(io.BytesIO(image_g))


                # SampleDetailGrain.objects.get_or_create(
                #     name_seed=name_g, width_grain=width_g, 
                #     heigth_grain=height_g, 
                #     image_result=cv2.imwrite(name_g + '.jpg', image_g).save(),
                # )

        # print(self._state.adding)
        # types = TypeGrain.objects.filter(status=True, grain=self.grain.id)
        # for type in range(len(types)):
        #     name_type_grain = str(types[type].name_type)
        #     name_type_grain = name_type_grain.replace(' ', '_').lower()

        #     id_type = types[type].id
        #     # AnalysisGrain.objects.get_or_create(
        #     #     sample=self, type_grain=types[type], point_percent=1
        #     # )
        #     print(id_type, name_type_grain)

        #     analysis = AnalysisGrain()
        # print(self.grain.id)
        # print(self.id)

    class Meta:
        #abstract = True
        ordering = ['name_sample',]
        verbose_name = 'Sample Grain'
        verbose_name_plural = 'Samples Grains'

def sample_detail_path(instance, filename):
    slugify_name_sample = slugify(instance.sample.name_sample)
    return 'sample-{0}/{1}'.format(slugify_name_sample, filename)

@python_2_unicode_compatible # For Python 3.5+ and 2.7
class SampleDetailGrain(models.Model):
    # uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    id = models.UUIDField(
        primary_key=True, default=uuid_lib.uuid4, editable=False
    )
    name_seed = models.CharField(max_length=25)
    area = models.FloatField(default=0)
    width_grain = models.FloatField(default=0)
    heigth_grain = models.FloatField(default=0)
    diameter_grain = models.FloatField(default=0)
    # category_grain_detail = models.ForeignKey(
    #     CategoryGrain, on_delete=models.CASCADE, 
    #     related_name='detail_category'
    # )
    type_grain_detail = models.ForeignKey(
        TypeGrain, on_delete=models.CASCADE, related_name='detail_type',
        blank=True, null=True
    )
    sample = models.ForeignKey(
        SampleGrain, on_delete=models.CASCADE, related_name='detail_sample'
    )
    point_percent = models.FloatField(default=0)
    image_result = models.ImageField(upload_to=sample_detail_path, blank=True)

    
    def __str__(self):
        return (str(self.name_seed) + ' | ' + str(self.sample.name_sample))

    def save(self, *args, **kwargs):


        # print(self._state.adding)
        if self._state.adding:
            # pass
        # else: 
            grain_url = self.image_result.url
            g_result = prediction_grain(grain_url)
            sorted_result = sorted(
                g_result.items(), key=lambda x: x[1], reverse=True
            )
            r_key, r_value = sorted_result[0][0], sorted_result[0][1]
            name_type_grain = (r_key.lower()).capitalize()
            # print(name_type_grain, r_value)
            types = TypeGrain.objects.get(
                status=True, grain=self.sample.grain.id,
                name_type=name_type_grain
            )
            self.point_percent = r_value
            self.type_grain_detail = types
        super(SampleDetailGrain, self).save(*args, **kwargs)

    class Meta:
        #abstract = True
        ordering = ['name_seed',]
        verbose_name = 'Sample Detail Grain'
        verbose_name_plural = 'Samples Details Grains'

@python_2_unicode_compatible # For Python 3.5+ and 2.7
class AnalysisGrain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid_lib.uuid4, editable=False)
    sample = models.ForeignKey(
        SampleGrain, on_delete=models.CASCADE, related_name='analysis_sample'
    )


    def __str__(self):
        return (
            str(self.sample.grain.name) + ' | '
        )

    def save(self, *args, **kwargs):
        
        detail_grains = SampleDetailGrain.objects.filter(
            sample__id=self.sample.id
        )
        types = TypeGrain.objects.filter(
            status=True, grain=self.sample.grain.id
        )
        types_found = []
        for sdg in range(len(detail_grains)):
            types_found.append(detail_grains[sdg].type_grain_detail.id)
        
        percent_hundred = percent_all(
            self.sample.total_grains, list_counter(types_found)
        )

        for k in percent_hundred.keys():
            find_type = TypeGrain.objects.get(id=k)

            per_type = PercentageTypeGrain()
            per_type.analysis_percent_grain = self
            per_type.percent_type_grain = find_type
            per_type.percentage = percent_hundred.get(k)
            per_type.save()

        super(AnalysisGrain, self).save(*args, **kwargs)

    class Meta:
        #abstract = True
        ordering = ['sample__name_sample']
        verbose_name_plural = 'Analysis Grains'

@python_2_unicode_compatible # For Python 3.5+ and 2.7
class PercentageTypeGrain(models.Model):
    # uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    id = models.UUIDField(
        primary_key=True, default=uuid_lib.uuid4, editable=False
    )
    analysis_percent_grain = models.ForeignKey(
        AnalysisGrain, on_delete=models.CASCADE, related_name='percent_analysis'
    )
    percent_type_grain = models.ForeignKey(
        TypeGrain, on_delete=models.CASCADE, related_name='percent_type'
    )
    percentage = models.FloatField(default=0)
    
    
    def __str__(self):
        return str(self.percent_type_grain.name_type)

    #def get_absolute_url(self):
        #return reverse('name_url', kwargs={'pk': self.pk})

    class Meta:
        #abstract = True
        # ordering = ['name',]
        verbose_name = 'Percentage Type Grain'
        verbose_name_plural = 'Percentage Types Grain'
