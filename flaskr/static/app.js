document.getElementById('searchForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const query = document.getElementById('query').value;
    
    const response = await fetch('/recommend', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ query })
    });
    
    const data = await response.json();
    
    if (data.success) {
        alert(`Recommended: ${data.software.name}\n\nDescription: ${data.software.description}\n\nMatch: ${Math.round(data.score * 100)}%`);
    } else {
        alert('Error: ' + data.message);
    }
});