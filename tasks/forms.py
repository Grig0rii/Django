from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    new_category = forms.CharField(
        required=False,
        label='Новая категория',
        help_text='Введите название новой категории, если нужной категории нет в списке'
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'category', 'priority', 'due_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
            'completed': 'Выполнено',
            'category': 'Категория',
            'priority': 'Приоритет',
            'due_date': 'Срок выполнения',
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        new_category_name = self.cleaned_data.get('new_category')
        if new_category_name:
            category, created = Category.objects.get_or_create(name=new_category_name)
            instance.category = category
        if commit:
            instance.save()
        return instance 