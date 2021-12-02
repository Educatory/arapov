from django.contrib import admin

from app.account.models import Account

#
# class AccountAdmin(admin.ModelAdmin):
#     # search_fields = ['role']


admin.site.register(Account)