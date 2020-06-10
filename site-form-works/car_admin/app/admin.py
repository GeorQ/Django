from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review', 'id')
    list_display_links = ('brand',)
    ordering = ['id']
    search_fields = ('brand', 'model',)

    def review(self, obj):
        return obj.review_count()


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'title', 'text', 'id')
    list_display_links = ('car',)
    ordering = ['id']
    search_fields = ('car', 'title',)
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
