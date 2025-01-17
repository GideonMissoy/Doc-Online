from events.models import Event
from events.utils import request_wrapper, ThirdPartyAPIConnectionError
import os
from dotenv import load_dotenv

load_dotenv()


NOCODEAPI_GOOGLE_CALENDAR_BASE_URL = "https://v1.nocodeapi.com/shokudaikiri/calendar/QlwzhfmTCwyoyitT" 

def nocodeapi_google_calendar_create_event(event: Event, user_email: str):
    """Create an event on google calendar using nocodeapi."""
    response_data = None
    # payload to be sent to nocodeapi to create an event
    request_data = {
        "summary": event['title'],
        "location": event['location'],
        "description": event['description'],
        "start": {"dateTime": event['start_at']},
        "end": {"dateTime": event['end_at']},
        "locked": True,
        "sendNotifications": True,
        "attendees": [{"email": user_email}],
        "guestsCanInviteOthers": False,
        "guestsCanModify": False,
        "guestsCanSeeOtherGuests": False,
    }

    try:
        response = request_wrapper(
            method='post',
            params={'sendUpdates': 'all'},
            post_data=request_data,
            url=f'{NOCODEAPI_GOOGLE_CALENDAR_BASE_URL}/event',
            headers={'Content-Type': 'application/json', 'Authorization': f'Bearer'},
        )
        # check if the response is not None, and the status_code is 200'
        if response is not None and response.status_code == 200:
            return response.response_data['id']

    except ThirdPartyAPIConnectionError as error:
        pass
        # you can log to an error handler like sentry
    return response_data


def nocodeapi_google_calendar_edit_event(event: Event, user_email: str):
    """Edit an event."""
    response_data = None
    # payload to be sent to nocodeapi google_calendar to edit an event.
    request_data = {
        "summary": event['title'],
        "location": event['location'],
        "description": event['description'],
        "start": {"dateTime": str(event['start_at'].isoformat())},
        "end": {
            "dateTime": str(event['end_at'].isoformat()),
        },
        "sendNotifications": True,
        "guestsCanInviteOthers": False,
        "guestsCanModify": False,
        "guestsCanSeeOtherGuests": False,
        "locked": True,
        "attendees": [{"email": user_email}],

    }
    try:
        response = request_wrapper(
            method='put',
            params={"eventId": event['google_calendar_event_id'], "sendUpdates": "all"},
            post_data=request_data,
            url=f'{NOCODEAPI_GOOGLE_CALENDAR_BASE_URL}/event',
            headers={'Content-Type': 'application/json'},
        )
        # check if the response is not None, and the status_code is 200
        if response is not None and response.status_code == 200:
            response_data = {'nocodeapi_google_calendar_api': response.response_data}
            return response.response_data['id']
    except ThirdPartyAPIConnectionError as error:
        pass
        # you can log to an error handler like sentry
    return response_data


def nocodeapi_google_calendar_delete_event(event: str):
    """Delete an event on nocodeapi google calendar."""
    try:
        request_wrapper(
            method='delete',
            params={"eventId": event['google_calendar_event_id'], "sendUpdates": "all"},
            url=f'{NOCODEAPI_GOOGLE_CALENDAR_BASE_URL}/event',
            headers={'Content-Type': 'application/json'},
        )
    except ThirdPartyAPIConnectionError as error:
        pass
        # you can log to an error handler like sentry
    return True
