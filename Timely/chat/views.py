from multiprocessing.connection import answer_challenge

from django.shortcuts import render
from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse, HttpResponse

from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import datetime
import pytz

from chat.models import ChatMessage

# Create your views here.

client = OpenAI(api_key=settings.OPEN_AI_API_KEY, organization=settings.OPENAI_ORG_ID)
def index(request):
    return render(request, 'index.html')

def response(request):
    if request.method == 'POST':
        message = request.POST.get("message", "")
        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        answer = completion.choices[0].message.content
        chat_message = ChatMessage(message=message, response=answer)
        chat_message.save()
        return JsonResponse({'response': answer}, status=200)

    return JsonResponse({'response', 'Invalid Request'}, status=400)

# Define Google OAuth scopes
# These scopes determine the level of access the application has to the user's Google account.
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid',
]

def google_login(request):
    """
    Initiate the Google OAuth login process.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects the user to Google's OAuth consent screen.
    """
    # Create a Flow object for managing the OAuth process
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    # Generate the authorization URL
    auth_url, _ = flow.authorization_url(
        prompt='consent',
        access_type='offline',
        include_granted_scopes=False
    )

    return redirect(auth_url)


def oauth2callback(request):
    """
    Handle the OAuth2 callback after the user authorizes the application.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects the user to the home page after successful login.
    """
    # Exchange the authorization code for credentials
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials

    # Retrieve user information from Google
    user_service = build('oauth2', 'v2', credentials=credentials)
    user_info = user_service.userinfo().get().execute()
    email = user_info.get('email')
    first_name = user_info.get('given_name')
    last_name = user_info.get('family_name')

    if not email:
        return HttpResponse("Unable to retrieve user email.", status=400)

    # Create or retrieve the user in the Django database
    user, _ = User.objects.get_or_create(
        username=email,
        first_name=first_name,
        last_name=last_name,
        defaults={'email': email}
    )
    # Log the user in
    login(request, user)

    # Save credentials in the session (for prototype purposes; use a database for production)
    request.session['google_token'] = credentials_to_dict(credentials)
    return redirect('/')



def logout_view(request):
    """
    Log the user out and redirect to the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the home page.
    """
    logout(request)
    return redirect('/')


def credentials_to_dict(credentials):
    """
    Convert Google OAuth credentials to a dictionary for storage.

    Args:
        credentials: The Google OAuth credentials object.

    Returns:
        dict: A dictionary representation of the credentials.
    """
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': list(credentials.scopes),
    }
