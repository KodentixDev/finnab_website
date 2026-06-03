from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import (
    HeroSection, AboutSection, Service, FAQ,
    WhoWeHelp, WhyChooseUs, ContactInfo, SEOSettings
)


def _get_text(obj, field):
    """Mövcud dil variantlarından birini qaytarır: _az → _en → _ru → field"""
    for lang in ('az', 'en', 'ru'):
        val = getattr(obj, f'{field}_{lang}', None)
        if val:
            return val
    return getattr(obj, field, '') or ''


def _truncate(text, length):
    text = str(text).strip()
    return text[:length - 3] + '...' if len(text) > length else text


def _create_or_update_seo(obj, title_az='', title_en='', title_ru='',
                           desc_az='', desc_en='', desc_ru='',
                           keywords_az='', keywords_en='', keywords_ru='',
                           og_image=None):
    ct = ContentType.objects.get_for_model(obj)
    seo, created = SEOSettings.objects.get_or_create(
        content_type=ct,
        object_id=obj.pk,
        defaults={'auto_generated': True}
    )

    # Yalnız avtomatik yaradılmışdırsa yenilə (istifadəçi əl ilə dəyişibsə toxunma)
    if not seo.auto_generated and not created:
        return

    seo.auto_generated = True

    # AZ
    seo.meta_title_az = _truncate(title_az, 70) if title_az else ''
    seo.meta_description_az = _truncate(desc_az, 160) if desc_az else ''
    seo.meta_keywords_az = keywords_az
    seo.og_title_az = _truncate(title_az, 70) if title_az else ''
    seo.og_description_az = _truncate(desc_az, 200) if desc_az else ''
    seo.twitter_title_az = _truncate(title_az, 70) if title_az else ''
    seo.twitter_description_az = _truncate(desc_az, 200) if desc_az else ''

    # EN
    seo.meta_title_en = _truncate(title_en, 70) if title_en else ''
    seo.meta_description_en = _truncate(desc_en, 160) if desc_en else ''
    seo.meta_keywords_en = keywords_en
    seo.og_title_en = _truncate(title_en, 70) if title_en else ''
    seo.og_description_en = _truncate(desc_en, 200) if desc_en else ''
    seo.twitter_title_en = _truncate(title_en, 70) if title_en else ''
    seo.twitter_description_en = _truncate(desc_en, 200) if desc_en else ''

    # RU
    seo.meta_title_ru = _truncate(title_ru, 70) if title_ru else ''
    seo.meta_description_ru = _truncate(desc_ru, 160) if desc_ru else ''
    seo.meta_keywords_ru = keywords_ru
    seo.og_title_ru = _truncate(title_ru, 70) if title_ru else ''
    seo.og_description_ru = _truncate(desc_ru, 200) if desc_ru else ''
    seo.twitter_title_ru = _truncate(title_ru, 70) if title_ru else ''
    seo.twitter_description_ru = _truncate(desc_ru, 200) if desc_ru else ''

    if og_image:
        seo.og_image = og_image

    seo.robots = 'index, follow'
    seo.is_active = True
    seo.save()


@receiver(post_save, sender=HeroSection)
def seo_for_hero(sender, instance, **kwargs):
    _create_or_update_seo(
        instance,
        title_az=instance.title_az or instance.title,
        title_en=instance.title_en or instance.title,
        title_ru=instance.title_ru or instance.title,
        desc_az=instance.description_az or instance.description,
        desc_en=instance.description_en or instance.description,
        desc_ru=instance.description_ru or instance.description,
        keywords_az='mühasibat, maliyyə, vergi, Finnab',
        keywords_en='accounting, finance, tax, Finnab',
        keywords_ru='бухгалтерия, финансы, налоги, Finnab',
        og_image=instance.hero_image if instance.hero_image else None,
    )


@receiver(post_save, sender=AboutSection)
def seo_for_about(sender, instance, **kwargs):
    _create_or_update_seo(
        instance,
        title_az=f"Haqqımızda | {instance.title_az or instance.title}",
        title_en=f"About Us | {instance.title_en or instance.title}",
        title_ru=f"О нас | {instance.title_ru or instance.title}",
        desc_az=instance.description_az or instance.description,
        desc_en=instance.description_en or instance.description,
        desc_ru=instance.description_ru or instance.description,
        keywords_az='haqqımızda, mühasibat şirkəti, Finnab',
        keywords_en='about us, accounting company, Finnab',
        keywords_ru='о нас, бухгалтерская компания, Finnab',
        og_image=instance.image1 if instance.image1 else None,
    )


@receiver(post_save, sender=Service)
def seo_for_service(sender, instance, **kwargs):
    _create_or_update_seo(
        instance,
        title_az=f"{instance.title_az or instance.title} | Finnab",
        title_en=f"{instance.title_en or instance.title} | Finnab",
        title_ru=f"{instance.title_ru or instance.title} | Finnab",
        desc_az=instance.description_az or instance.description,
        desc_en=instance.description_en or instance.description,
        desc_ru=instance.description_ru or instance.description,
        keywords_az=f"{instance.title_az or instance.title}, mühasibat xidməti, Finnab",
        keywords_en=f"{instance.title_en or instance.title}, accounting service, Finnab",
        keywords_ru=f"{instance.title_ru or instance.title}, бухгалтерская услуга, Finnab",
        og_image=instance.image if instance.image else None,
    )


@receiver(post_save, sender=FAQ)
def seo_for_faq(sender, instance, **kwargs):
    _create_or_update_seo(
        instance,
        title_az=f"FAQ: {instance.question_az or instance.question}",
        title_en=f"FAQ: {instance.question_en or instance.question}",
        title_ru=f"FAQ: {instance.question_ru or instance.question}",
        desc_az=instance.answer_az or instance.answer,
        desc_en=instance.answer_en or instance.answer,
        desc_ru=instance.answer_ru or instance.answer,
        keywords_az='sual cavab, mühasibat, Finnab',
        keywords_en='faq, accounting, Finnab',
        keywords_ru='вопросы ответы, бухгалтерия, Finnab',
    )


@receiver(post_save, sender=ContactInfo)
def seo_for_contact(sender, instance, **kwargs):
    _create_or_update_seo(
        instance,
        title_az='Əlaqə | Finnab',
        title_en='Contact | Finnab',
        title_ru='Контакты | Finnab',
        desc_az=f'Bizimlə əlaqə saxlayın. Ünvan: {instance.address}. Tel: {instance.phone1}',
        desc_en=f'Get in touch with us. Address: {instance.address}. Phone: {instance.phone1}',
        desc_ru=f'Свяжитесь с нами. Адрес: {instance.address}. Тел: {instance.phone1}',
        keywords_az='əlaqə, ünvan, telefon, Finnab',
        keywords_en='contact, address, phone, Finnab',
        keywords_ru='контакты, адрес, телефон, Finnab',
    )
