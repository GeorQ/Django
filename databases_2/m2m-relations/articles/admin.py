from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Article, Tag



class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            print(form.cleaned_data)


class MembershipInline(admin.TabularInline):
    model = Tag.articles.through
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ("articles",)