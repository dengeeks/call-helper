from django.contrib import admin
from breaks.models import organizations, groups, replacements, breaks


#########################################
# INLINES
#########################################
class ReplacementEmployeeInline(admin.TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status')


#########################################
# MODELS
#########################################
@admin.register(organizations.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director')


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active')


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date', 'breaks_start', 'breaks_end', 'breaks_max_duration')
    inlines = (ReplacementEmployeeInline,)


@admin.register(replacements.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active')


@admin.register(breaks.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active')


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = ('id', 'replacement', 'break_start', 'break_end',)
