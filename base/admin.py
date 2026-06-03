from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
from .models import (
    HeroSection, AboutSection, AboutFeature,
    WhyChooseUs, WhyChooseItem, StatCounter,
    WhoWeHelp, WhoWeHelpItem, Service, FAQ,
    ContactInfo, ContactMessage, NewsletterSubscriber,
    SEOSettings
)


class AboutFeatureInline(TranslationTabularInline):
    model = AboutFeature
    extra = 1


class WhyChooseItemInline(TranslationTabularInline):
    model = WhyChooseItem
    extra = 1


class WhoWeHelpItemInline(TranslationTabularInline):
    model = WhoWeHelpItem
    extra = 1


@admin.register(HeroSection)
class HeroSectionAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'google_rating', 'review_count', 'is_active')
    list_editable = ('is_active',)


@admin.register(AboutSection)
class AboutSectionAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'satisfied_client_count', 'is_active')
    list_editable = ('is_active',)
    inlines = [AboutFeatureInline]


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    inlines = [WhyChooseItemInline]


@admin.register(StatCounter)
class StatCounterAdmin(TabbedTranslationAdmin):
    list_display = ('label', 'value', 'order')
    list_editable = ('order',)


@admin.register(WhoWeHelp)
class WhoWeHelpAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    inlines = [WhoWeHelpItemInline]


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(FAQ)
class FAQAdmin(TabbedTranslationAdmin):
    list_display = ('question', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'email1', 'phone1', 'is_active')
    list_editable = ('is_active',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at', 'is_read')
    list_editable = ('is_read',)
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('first_name', 'last_name', 'email', 'phone', 'message', 'created_at')


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    readonly_fields = ('subscribed_at',)


@admin.register(SEOSettings)
class SEOSettingsAdmin(TabbedTranslationAdmin):
    list_display = ('__str__', 'auto_generated', 'robots', 'is_active', 'updated_at')
    list_editable = ('is_active',)
    list_filter = ('auto_generated', 'is_active', 'content_type')
    readonly_fields = ('content_type', 'object_id', 'auto_generated', 'updated_at')
    fieldsets = (
        ('Hansı Obyektə Aid', {
            'fields': ('content_type', 'object_id', 'page_identifier', 'auto_generated')
        }),
        ('Meta Məlumatlar', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_description', 'og_image')
        }),
        ('Twitter Card', {
            'fields': ('twitter_card', 'twitter_title', 'twitter_description')
        }),
        ('Texniki', {
            'fields': ('canonical_url', 'robots')
        }),
        ('Schema.org', {
            'fields': ('schema_organization_name', 'schema_phone', 'schema_email', 'schema_address')
        }),
        ('Status', {
            'fields': ('is_active', 'updated_at')
        }),
    )
