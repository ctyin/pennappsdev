from django.forms import ModelForm
from main.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields = ['title', 'content', 'pub_date', 'poster']
        exclude = ['pub_date', 'poster']
