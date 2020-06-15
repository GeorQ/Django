from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    counter += 1
                    if counter > 1:
                        raise ValidationError('Выберите только один главный Tag')
        return super().clean()
        #     print("\n\n\n")
        #     print(form.cleaned_data)
        #     print("\n\n\n")


class MembershipInline(admin.TabularInline):
    model = Tag.articles.through
    formset = RelationshipInlineFormset
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
