from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.utils import translation
from django.conf import settings
import logging

logger = logging.getLogger(__name__)
from .models import (
    HeroSection, AboutSection, WhyChooseUs,
    StatCounter, WhoWeHelp, Service, FAQ,
    ContactInfo, ContactMessage, NewsletterSubscriber
)


def index(request):
    # LocaleMiddleware tərəfindən request.LANGUAGE_CODE set edilir
    current_lang = getattr(request, 'LANGUAGE_CODE', None) or translation.get_language() or 'az'
    translation.activate(current_lang)

    hero = HeroSection.objects.filter(is_active=True).first()
    about = AboutSection.objects.filter(is_active=True).prefetch_related('features').first()
    why_choose = WhyChooseUs.objects.filter(is_active=True).prefetch_related('items').first()
    stat_counters = StatCounter.objects.all()
    who_we_help = WhoWeHelp.objects.filter(is_active=True).prefetch_related('items').first()
    services = Service.objects.filter(is_active=True)
    faqs = FAQ.objects.filter(is_active=True)
    contact_info = ContactInfo.objects.filter(is_active=True).first()

    context = {
        'hero': hero,
        'about': about,
        'why_choose': why_choose,
        'stat_counters': stat_counters,
        'who_we_help': who_we_help,
        'services': services,
        'faqs': faqs,
        'contact_info': contact_info,
        'LANGUAGE_CODE': current_lang,
    }
    return render(request, 'index.html', context)


def contact_submit(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            first_name=request.POST.get('fname', ''),
            last_name=request.POST.get('lname', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            message=request.POST.get('msg', ''),
        )
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'ok'})
        messages.success(request, 'Mesajınız göndərildi. Tezliklə sizinlə əlaqə saxlayacağıq.')
        return redirect('home')
    return redirect('home')


def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'ok'})
        return redirect('home')
    return redirect('home')


def change_language(request):
    if request.method == 'POST':
        lang = request.POST.get('language', 'az')
        valid_langs = [code for code, _ in settings.LANGUAGES]
        if lang in valid_langs:
            translation.activate(lang)
            next_url = '/' if lang == 'az' else f'/{lang}/'
            response = redirect(next_url)
            response.set_cookie(
                key=settings.LANGUAGE_COOKIE_NAME,
                value=lang,
                max_age=365 * 24 * 60 * 60,
                path='/',
                samesite='Lax',
            )
            return response
    return redirect('/')
