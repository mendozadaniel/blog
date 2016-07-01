from django.contrib import admin

# Register your models here.
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "created", "last_updated", "id"]
	list_display_links = ["last_updated"]
	list_editable = ["title"]
	list_filter = ["created", "last_updated"]

	search_fields = ["title", "content"]

	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)
