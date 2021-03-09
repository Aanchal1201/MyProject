from .models import UserProfile

def profile(request):
    if not request.user.is_authenticated:
        return { 
            'profile': 'Anonymous'
        }
    else:
        return{
        'profile': UserProfile.objects.filter(UserUsername=request.user).first()
        }