from rest_framework import authentication, exceptions
from django.contrib.auth.models import AnonymousUser
from django.conf import settings
import jwt

class SupabaseUser(AnonymousUser):
    @property
    def is_authenticated(self):
        return True

class SupabaseAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            prefix, token = auth_header.split()
            print("TOKEN RECBIDO ===>", token)
            if prefix.lower() != 'bearer':
                raise exceptions.AuthenticationFailed('Invalid token prefix.')
        except ValueError:
            raise exceptions.AuthenticationFailed('Invalid Authorization header format.')

        try:
            payload = jwt.decode(
                token,
                settings.SUPABASE_JWT_SECRET,
                algorithms=["HS256"],
                options={"verify_aud": False}  # Desactiva la verificación de aud para pruebas
            )
            print("PAYLOAD DECODIFICADO ===>", payload)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired.')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token.')

        # Aquí podrías devolver un User real, si sincronizas con auth_user
        # por ahora devolvemos None para pruebas
        return (SupabaseUser(), None)
