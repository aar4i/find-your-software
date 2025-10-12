const form = document.getElementById('searchForm');
const loading = document.getElementById('loading');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const query = document.getElementById('query').value.trim();
    
    if (!query) {
        alert('Please enter your requirements');
        return;
    }
    
    // Show loading, hide result
    loading.classList.remove('hidden');
    resultDiv.classList.add('hidden');
    
    try {
        const response = await fetch('/recommend', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ query })
        });
        
        const data = await response.json();
        
        // Hide loading
        loading.classList.add('hidden');
        
        // Show result
        if (data.success) {
            showResult(data);
        } else {
            showError(data.message);
        }
        
    } catch (error) {
        loading.classList.add('hidden');
        showError('An error occurred. Please try again.');
    }
});

function showResult(data) {
    const s = data.software;
    const matchPercent = Math.round(data.score * 100);
    
    resultDiv.innerHTML = `
        <div class="flex items-start justify-between mb-4">
            <div>
                <h3 class="text-2xl font-bold text-gray-900">${s.name}</h3>
                <span class="inline-block mt-1 px-3 py-1 text-xs font-medium text-gray-600 bg-gray-100 rounded-full">
                    ${s.category}
                </span>
            </div>
            <span class="px-3 py-1 text-sm font-semibold text-green-700 bg-green-100 rounded-full">
                ${matchPercent}% match
            </span>
        </div>
        
        <p class="text-gray-700 mb-4">${s.description}</p>
        
        <div class="border-t border-gray-200 pt-4">
            <h4 class="text-sm font-semibold text-gray-900 mb-2">Key Features:</h4>
            <p class="text-sm text-gray-600 leading-relaxed">${s.features}</p>
        </div>
    `;
    
    resultDiv.classList.remove('hidden');
}

function showError(message) {
    resultDiv.innerHTML = `
        <div class="text-center py-8">
            <svg class="mx-auto h-12 w-12 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <p class="mt-4 text-red-600 font-medium">${message}</p>
        </div>
    `;
    resultDiv.classList.remove('hidden');
}