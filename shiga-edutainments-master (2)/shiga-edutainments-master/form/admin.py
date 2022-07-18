from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'date', 'happy','good','average','bad',)
    list_filter = ('date',)
    search_fields = ('details',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
