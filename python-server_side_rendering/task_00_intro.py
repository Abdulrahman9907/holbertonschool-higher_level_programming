def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Attendees must be a list of dictionaries")
            return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        processed_template = template

        name = attendee.get('name', 'N/A')
        if name is None:
            name = 'N/A'

        event_title = attendee.get('event_title', 'N/A')
        if event_title is None:
            event_title = 'N/A'

        event_date = attendee.get('event_date', 'N/A')
        if event_date is None:
            event_date = 'N/A'

        event_location = attendee.get('event_location', 'N/A')
        if event_location is None:
            event_location = 'N/A'

        processed_template = processed_template.replace('{name}', str(name))
        processed_template = processed_template.replace('{event_title}', str(event_title))
        processed_template = processed_template.replace('{event_date}', str(event_date))
        processed_template = processed_template.replace('{event_location}', str(event_location))

        filename = f"output_{index}.txt"

        try:
            with open(filename, 'w') as file:
                file.write(processed_template)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")