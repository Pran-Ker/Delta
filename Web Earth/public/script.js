document.addEventListener('DOMContentLoaded', function() {
    const prompt = 'Tell me about this location';
    const endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions';
    
    fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
                        'Authorization': 'sk-proj-EhFXjrhbsBEgHD8YJ0OdT3BlbkFJyqG2e2FGDMysbsfAZFj0' // Ensure proper use of your API key
                    },
        body: JSON.stringify({
            'prompt': prompt,
            'max_tokens': 5
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        // Add DOM manipulation here if needed
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });
});