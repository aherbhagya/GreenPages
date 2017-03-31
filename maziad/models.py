
from django.db import models

# Create your models here.

class ServiceProvider(models.Model):
    # user = models.ForeignKey(unique=True)
    company_name = models.CharField(max_length=65)
    owner_name = models.CharField(max_length=65)
    image = models.ImageField(upload_to='service_providers', blank=True, help_text="image size 230 x 150 (wxh)")
    address = models.TextField(blank=True)
    description = models.TextField()
    emaill = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    mobile = models.CharField(max_length=15)
    mobile2 = models.CharField(max_length=15, blank=True)
    website = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(db_index=True)

    def __str__(self):
        return str(self.company_name)


class Category(models.Model):

    category_name = models.CharField(max_length=50)
    slug = models.SlugField(db_index=True, unique=True)
    sequence = models.IntegerField()

    class Meta:
        ordering = ['sequence']

    def __str__(self):
        return str(self.category_name)

        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.category_name)


class SubCategory(models.Model):
    category_id = models.ForeignKey(Category)
    subcategory_name = models.CharField(max_length=50)
    slug = models.SlugField(db_index=True, unique=True)

    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return str(self.subcategory_name)

    def __unicode__(self):
        return unicode(self.subcategory_name)

    def provider_count(self):
        return ServiceProvider.objects.filter(subcategory=self).count()



# class Ad(models.Model):
#     category = models.ForeignKey(Category)
#     user = models.ForeignKey(ServiceProvider)
# 	title = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.FileField(upload_to='adImages', null=True, blank=True)
# 	location = models.CharField(max_length=50, null=False)
#     created_on = models.DateTimeField(auto_now_add=True)
#     expires_on = models.DateTimeField()



# class ZipCode(models.Model):
#     zipcode = models.IntegerField(primary_key=True)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     city = models.CharField(max_length=30)
#     state = models.CharField(max_length=2)

#     def nearby(self, radius):
#         radius = float(radius)
#         rangeFactor = 0.014457
#         # bounding box
#         objs = self.get_queryset().filter(latitude__gte=self.latitude - (radius * rangeFactor),
#                                           latitude__lte=self.latitude + (radius * rangeFactor),
#                                           longitude__gte=self.longitude - (radius * rangeFactor),
#                                           longitude__lte=self.longitude + (radius * rangeFactor))

#         # if there are any results left, use GetDistance stored function to finish
#         if objs.count() > 0:
#             objs = objs.extra(where=['GetDistance(%s,%s,latitude,longitude) <= %s'],
#                               params=[self.latitude, self.longitude, radius])

#         return objs

#     def __unicode__(self):
#         return _(u'Zip: %s, City: %s, State: %s') % (unicode(self.zipcode),
#                                                      self.city, self.state,)
