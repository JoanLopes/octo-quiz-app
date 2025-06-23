from rest_framework_simplejwt.tokens import RefreshToken

def user_token(request):
    token = None
    if request.user.is_authenticated:
        refresh = RefreshToken.for_user(request.user)
        token = str(refresh.access_token)
    return {'token': token}
