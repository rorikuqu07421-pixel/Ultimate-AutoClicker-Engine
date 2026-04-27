import json

class AutoClickerDataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_by_threshold(self, threshold):
        return [entry for entry in self.data if entry['clicks'] >= threshold]

    def calculate_average_clicks(self):
        total_clicks = sum(entry['clicks'] for entry in self.data)
        return total_clicks / len(self.data) if self.data else 0

    def convert_to_json(self):
        return json.dumps(self.data)

    def from_json(self, json_data):
        self.data = json.loads(json_data)

    def get_click_data_summary(self):
        filtered_data = self.filter_by_threshold(100)
        average = self.calculate_average_clicks()
        return {
            'filtered_entries': len(filtered_data),
            'average_clicks': average
        }

# Example usage:
# data = [{'time': '2023-01-01', 'clicks': 150}, {'time': '2023-01-02', 'clicks': 90}]
# processor = AutoClickerDataProcessor(data)
# print(processor.get_click_data_summary())
