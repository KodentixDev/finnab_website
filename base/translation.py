from modeltranslation.translator import register, TranslationOptions
from .models import (
    HeroSection, AboutSection, AboutFeature,
    WhyChooseUs, WhyChooseItem, WhoWeHelp,
    WhoWeHelpItem, Service, FAQ, StatCounter
)


@register(HeroSection)
class HeroSectionTranslation(TranslationOptions):
    fields = ('title', 'description', 'primary_btn_text', 'secondary_btn_text')


@register(AboutSection)
class AboutSectionTranslation(TranslationOptions):
    fields = ('subtitle', 'title', 'description')


@register(AboutFeature)
class AboutFeatureTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(WhyChooseUs)
class WhyChooseUsTranslation(TranslationOptions):
    fields = ('subtitle', 'title', 'description')


@register(WhyChooseItem)
class WhyChooseItemTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(WhoWeHelp)
class WhoWeHelpTranslation(TranslationOptions):
    fields = ('subtitle', 'title', 'description')


@register(WhoWeHelpItem)
class WhoWeHelpItemTranslation(TranslationOptions):
    fields = ('title',)


@register(Service)
class ServiceTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(FAQ)
class FAQTranslation(TranslationOptions):
    fields = ('question', 'answer')


@register(StatCounter)
class StatCounterTranslation(TranslationOptions):
    fields = ('label',)
