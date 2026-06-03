from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class HeroSection(models.Model):
    google_rating = models.FloatField(default=5.0)
    review_count = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()
    primary_btn_text = models.CharField(max_length=100, default='bizimlə əməkdaşlıq et')
    secondary_btn_text = models.CharField(max_length=100, default='xidmətlərə bax')
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Hero Bölməsi'
        verbose_name_plural = 'Hero Bölməsi'

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    subtitle = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    satisfied_client_count = models.PositiveIntegerField(default=0)
    image1 = models.ImageField(upload_to='about/', blank=True, null=True)
    image2 = models.ImageField(upload_to='about/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Haqqımızda Bölməsi'
        verbose_name_plural = 'Haqqımızda Bölməsi'

    def __str__(self):
        return self.title


class AboutFeature(models.Model):
    about = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='features')
    icon = models.ImageField(upload_to='about/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Haqqımızda Xüsusiyyəti'
        verbose_name_plural = 'Haqqımızda Xüsusiyyətləri'
        ordering = ['order']

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    subtitle = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Niyə Bizi Seçməlisiniz'
        verbose_name_plural = 'Niyə Bizi Seçməlisiniz'

    def __str__(self):
        return self.title


class WhyChooseItem(models.Model):
    section = models.ForeignKey(WhyChooseUs, on_delete=models.CASCADE, related_name='items')
    icon = models.ImageField(upload_to='why_choose/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Niyə Bizi Seçməlisiniz - Maddə'
        verbose_name_plural = 'Niyə Bizi Seçməlisiniz - Maddələr'
        ordering = ['order']

    def __str__(self):
        return self.title


class StatCounter(models.Model):
    label = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='counters/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Statistika Sayğacı'
        verbose_name_plural = 'Statistika Sayğacları'
        ordering = ['order']

    def __str__(self):
        return self.label


class WhoWeHelp(models.Model):
    subtitle = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Kimə Kömək Edirik'
        verbose_name_plural = 'Kimə Kömək Edirik'

    def __str__(self):
        return self.title


class WhoWeHelpItem(models.Model):
    section = models.ForeignKey(WhoWeHelp, on_delete=models.CASCADE, related_name='items')
    icon = models.ImageField(upload_to='who_we_help/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Kimə Kömək Edirik - Maddə'
        verbose_name_plural = 'Kimə Kömək Edirik - Maddələr'
        ordering = ['order']

    def __str__(self):
        return self.title


class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Xidmət'
        verbose_name_plural = 'Xidmətlər'
        ordering = ['order']

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Sual-Cavab'
        verbose_name_plural = 'Sual-Cavablar'
        ordering = ['order']

    def __str__(self):
        return self.question


class ContactInfo(models.Model):
    address = models.CharField(max_length=300)
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True)
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50, blank=True)
    map_embed_url = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Əlaqə Məlumatları'
        verbose_name_plural = 'Əlaqə Məlumatları'

    def __str__(self):
        return self.address


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Əlaqə Mesajı'
        verbose_name_plural = 'Əlaqə Mesajları'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Abunəçi'
        verbose_name_plural = 'Abunəçilər'

    def __str__(self):
        return self.email


class SEOSettings(models.Model):
    # Hansı modelə aid olduğunu göstərir
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    # Saytın ümumi SEO-su üçün (heç bir modelə bağlı olmayan)
    page_identifier = models.CharField(
        max_length=50, blank=True,
        help_text='Ümumi sayt SEO-su üçün: "global" yazın'
    )

    # Meta məlumatlar (3 dildə — modeltranslation ilə)
    meta_title = models.CharField(max_length=70, blank=True, help_text='Maksimum 70 simvol')
    meta_description = models.TextField(max_length=160, blank=True, help_text='Maksimum 160 simvol')
    meta_keywords = models.CharField(max_length=255, blank=True, help_text='Vergüllə ayrılmış açar sözlər')

    # Open Graph
    og_title = models.CharField(max_length=70, blank=True)
    og_description = models.TextField(max_length=200, blank=True)
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True, help_text='1200x630 px tövsiyə olunur')

    # Twitter Card
    twitter_title = models.CharField(max_length=70, blank=True)
    twitter_description = models.TextField(max_length=200, blank=True)
    twitter_card = models.CharField(max_length=20, default='summary_large_image')

    # Texniki
    canonical_url = models.URLField(blank=True)
    robots = models.CharField(max_length=50, default='index, follow')

    # Schema.org
    schema_organization_name = models.CharField(max_length=100, blank=True)
    schema_phone = models.CharField(max_length=50, blank=True)
    schema_email = models.EmailField(blank=True)
    schema_address = models.CharField(max_length=300, blank=True)

    is_active = models.BooleanField(default=True)
    auto_generated = models.BooleanField(default=False, help_text='Signal tərəfindən avtomatik yaradılıb')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'SEO Ayarı'
        verbose_name_plural = 'SEO Ayarları'

    def __str__(self):
        if self.page_identifier:
            return f'SEO: {self.page_identifier}'
        if self.content_type and self.object_id:
            return f'SEO: {self.content_type.model} #{self.object_id}'
        return 'SEO Ayarı'

    @classmethod
    def get_for_object(cls, obj):
        ct = ContentType.objects.get_for_model(obj)
        return cls.objects.filter(content_type=ct, object_id=obj.pk, is_active=True).first()

    @classmethod
    def get_global(cls):
        return cls.objects.filter(page_identifier='global', is_active=True).first()
