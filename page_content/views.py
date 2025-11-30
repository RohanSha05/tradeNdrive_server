from rest_framework.decorators import api_view
from isamauto.utils import success_response, error_response
from .models import HeroBanner, ScrollBar, AboutContent


@api_view(['GET'])
def get_hero_banners(request):
    try:
        banners = HeroBanner.objects.all().order_by('-created_at')
        data = [
            {
                'id': banner.id,
                'title': banner.title,
                'short_description': banner.short_description,
                'hero_image': request.build_absolute_uri(banner.hero_image.url) if banner.hero_image else None,
            }
            for banner in banners
        ]
        return success_response(data=data, status=200)
    except Exception as e:
        return error_response(code=500, message=str(e))


@api_view(['GET'])
def get_scroll_bars(request):
    try:
        bars = ScrollBar.objects.all().order_by('-id')
        data = [
            {
                'id': bar.id,
                'title': bar.title,
            }
            for bar in bars
        ]
        return success_response(data=data, status=200)
    except Exception as e:
        return error_response(code=500, message=str(e))


@api_view(['GET'])
def get_about_content(request):
    try:
        content = AboutContent.objects.first()
        if not content:
            return error_response(code=404, message="About content not found")

        data = {
            'title': content.title,
            'description': content.description,

            'feature_1_title': content.feature_1_title,
            'feature_2_title': content.feature_2_title,
            'feature_3_title': content.feature_3_title,

            'content_title_1': content.content_title_1,
            'content_description_1': content.content_description_1,
            'content_icon_1': request.build_absolute_uri(content.content_icon_1.url) if content.content_icon_1 else None,

            'content_title_2': content.content_title_2,
            'content_description_2': content.content_description_2,
            'content_icon_2': request.build_absolute_uri(content.content_icon_2.url) if content.content_icon_2 else None,

            'content_title_3': content.content_title_3,
            'content_description_3': content.content_description_3,
            'content_icon_3': request.build_absolute_uri(content.content_icon_3.url) if content.content_icon_3 else None,

            'content_image1': request.build_absolute_uri(content.content_image1.url) if content.content_image1 else None,
            'content_image2': request.build_absolute_uri(content.content_image2.url) if content.content_image2 else None,
        }

        return success_response(data=data, status=200)
    except Exception as e:
        return error_response(code=500, message=str(e))