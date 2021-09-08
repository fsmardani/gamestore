from django.contrib import admin

from cart_ordering.models import Cart, Ordering

admin.site.register(Cart)
admin.site.register(Ordering)


# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'date')
#     list_editable = ('name', 'due_at', )
#     list_display_links = None
#     fieldsets = (
#         ('identification', {'fields': ('id', 'name')}),
#         ('time_section', {'fields': ('created_at', 'due_at')}),
#         ('category_section', {'fields': ('cat',)})
#     )
#     # fields = (('id', 'created_at'), 'description')
#     # exclude = ('description',)
#     list_display = ('name', 'due_at' )
#     list_filter = ('cat__name', 'due_at')
#     date_hierarchy = 'due_at'
#     actions_on_top = True
#     actions_selection_counter = True
#
#     actions = ['update_due_at']