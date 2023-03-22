import json

# Load SQuAD format JSON data from a file
with open('train-v2.0.json') as f:
    squad_data = json.load(f)

# Convert SQuAD format JSON data to intent format
intents = []
for paragraph in squad_data['data'][0]['paragraphs']:
    for qa in paragraph['qas']:
        # Create new intent with tag and context_set
        intent = {
            'tag': qa['id'],
            'context_set': ''
        }

        # Get question as the pattern for this intent
        intent['patterns'] = [qa['question']]

        # Get answer as the response for this intent
        intent['responses'] = [qa['answers'][0]['text']]

        intents.append(intent)

# Save intents as JSON file
with open('intents.json', 'w') as f:
    json.dump({'intents': intents}, f, indent=2)