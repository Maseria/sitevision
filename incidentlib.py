class IncidentHelper:
    def __init__(self, incident):
        self.incident = incident

    def is_valid(self):
        required_fields = ['incidentid', 'title', 'date', 'location', 'description']
        return all(field in self.incident and self.incident[field] for field in required_fields)

    def normalize(self):
        self.incident['severity'] = self.incident.get('severity', 'Low')
        return self.incident

    def summary(self):
        return {
            'incidentid': self.incident['incidentid'],
            'title': self.incident['title'],
            'wordCount': len(self.incident.get('description', '').split())
        }