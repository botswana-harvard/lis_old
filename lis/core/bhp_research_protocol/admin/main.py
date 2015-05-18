from django.contrib import admin
from ..models import Protocol, PrincipalInvestigator, SiteLeader, FundingSource, Site, Location


class PrincipalInvestigatorAdmin(admin.ModelAdmin):
    pass
admin.site.register(PrincipalInvestigator, PrincipalInvestigatorAdmin)


class  SiteLeaderAdmin(admin.ModelAdmin):
    pass
admin.site.register(SiteLeader, SiteLeaderAdmin)


class  ProtocolAdmin(admin.ModelAdmin):
    list_display = ('protocol_identifier', 'research_title')
admin.site.register(Protocol, ProtocolAdmin)


class  FundingSourceAdmin(admin.ModelAdmin):
    pass
admin.site.register(FundingSource, FundingSourceAdmin)


class  SiteAdmin(admin.ModelAdmin):
    list_display = ('site_identifier', 'location',)
admin.site.register(Site, SiteAdmin)


class  LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)
