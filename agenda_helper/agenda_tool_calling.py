import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from langchain_core.tools import tool

from agenda_helper.utils.agenda_authentication import authenticate_google_calendar

load_dotenv(".env")

api_key = os.environ["OPENAI_KEY"]


@tool(parse_docstring=True)
def check_availability(date: str) -> str:
    """
    Use this tool to check the availibility in the agenda of the user for a given day

    Args:
        date:the day for which we want to check the availibility
    """
    service = authenticate_google_calendar()

    start_time = datetime.strptime(date, "%Y-%m-%d").isoformat() + "Z"
    end_time = (
        datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)
    ).isoformat() + "Z"

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start_time,
            timeMax=end_time,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])

    if not events:
        return f"No events found on {date}. You are available."
    else:
        event_list = "\n".join(
            [
                f"- {event['summary']} at {event['start'].get('dateTime', event['start'].get('date'))}"
                for event in events
            ]
        )
        return f"You have the following events on {date}:\n{event_list}"


@tool(parse_docstring=True)
def create_event(summary: str, start_datetime: str, end_datetime: str) -> str:
    """
    Use this tool to book an appointment in the agenda of the user

    Args:
        summary: The title of the event
        start_datetime: the start of the event
        end_datetime: the end of the event
    """
    service = authenticate_google_calendar()

    event = {
        "summary": summary,
        "start": {"dateTime": start_datetime, "timeZone": "UTC"},
        "end": {"dateTime": end_datetime, "timeZone": "UTC"},
    }

    created_event = service.events().insert(calendarId="primary", body=event).execute()
    return (
        f"Event '{summary}' created successfully! Link: {created_event.get('htmlLink')}"
    )
