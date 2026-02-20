from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    
    # Aquí es donde configuras qué se ve en la lista
    list_display = ["question_text", "pub_date", "was_published_recently"]
    
    # El filtro lateral que ya agregaste
    list_filter = ["pub_date"]
    
    # LA NUEVA LÍNEA: Agrega la barra de búsqueda arriba
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)