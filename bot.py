import requests

def getDefinitions(word_id):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word_id.lower()
    r = requests.get(url)
    response = r.json()
    definitions_list = []

    if isinstance(response, list):
        for entry in response:
            meanings = entry.get('meanings', [])
            for meaning in meanings:
                definitions = meaning.get('definitions', [])
                for index, definition in enumerate(definitions, start=1):
                    definitions_list.append(f"👉 Definition {index}: {definition['definition']}")

            lexicalEntries = entry.get('lexicalEntries', [])
            for lexicalEntry in lexicalEntries:
                entries = lexicalEntry.get('entries', [])
                for entry in entries:
                    pronunciations = entry.get('pronunciations', [])
                    for pronunciation in pronunciations:
                        audio_url = pronunciation.get('audioFile', '')
                        if audio_url:
                            definitions_list.append(f"🔊 Pronunciation: {audio_url}")
    else:
        definitions_list.append("Error: Word not found")

    return definitions_list
