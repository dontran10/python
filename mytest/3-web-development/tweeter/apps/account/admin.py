from django.contrib import admin, messages
from django.utils.translation import ngettext
from apps.account.models import Post

@admin.action(description='Mark selected posts as UNAPPROVED')
def make_unapproved(modelaadmin, request, queryset):
    updates = queryset.update(is_active=False)
    modelaadmin.message_user(request, ngettext(
            '%d post was successfully marked as UNAPPROVED.',
            '%d posts were successfully marked as UNAPPROVED.',
            updates,
        ) % updates, messages.SUCCESS)

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['content', 'is_active']
    fields = ['content', 'is_active']
    actions = [make_unapproved, 'make_approved']

    @admin.action(description='Mark selected posts as APPROVED')
    def make_approved(self, request, queryset):
        updates = queryset.update(is_active=True)
        self.message_user(request, ngettext(
                '%d post was successfully marked as APPROVED.',
                '%d posts were successfully marked as APPROVED.',
                updates,
            ) % updates, messages.SUCCESS)

admin.site.register(Post, PostAdmin)
