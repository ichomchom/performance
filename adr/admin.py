from django.contrib import admin
from adr.models import Neutral, Inquiry

# Register your models here.
# admin.site.register(Neutral)
# admin.site.register(Inquiry)

# Format inline Inquiry for Neutral section
class InquiryInline(admin.TabularInline):
    model = Inquiry
    
@admin.register(Neutral)
class NeutralAdmin(admin.ModelAdmin):
    inlines = [InquiryInline]

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_filter = ('date_inquiry', 'neutral')

    fieldsets = (
        (None, {
            'fields' :('neutral', 'inquirer','note')
        }),
        ('Date', {
            'fields' :('date_inquiry', 'confirmed', 'notice_sent')
        }),
        ('Follow up',{
            'fields' :('follow1', 'follow2', 'closed')
        }),
        
        )