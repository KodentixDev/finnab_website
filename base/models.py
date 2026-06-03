from django.db import models


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
