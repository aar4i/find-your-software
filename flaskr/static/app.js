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
    let html = '<div class="mb-6"><h3 class="text-2xl font-bold text-gray-900">Top 3 Matches</h3></div>';
    
    data.recommendations.forEach((software, index) => {
        const matchPercent = Math.round(software.score * 100);
        const isFirst = index === 0;
        
        html += `
            <div class="mb-4 p-5 rounded-xl border ${isFirst ? 'border-green-300 bg-green-50 shadow-md' : 'border-gray-200 bg-white shadow-sm'}">
                
                <!-- Header -->
                <div class="flex items-center justify-between mb-3">
                    <div class="flex items-center gap-3">
                        ${isFirst ? `
                            <span class="flex items-center justify-center w-7 h-7 rounded-full bg-green-500 text-white text-sm font-bold">
                                1
                            </span>
                        ` : ''}
                        <h4 class="text-xl font-bold text-gray-900">${software.name}</h4>
                    </div>
                    <span class="px-3 py-1 text-sm font-semibold text-green-700 bg-green-100 rounded-full">
                        ${matchPercent}% match
                    </span>
                </div>
                
                <!-- Category Badge -->
                <div class="mb-2 ${isFirst ? 'ml-10' : ''}">
                    <span class="inline-block px-2.5 py-0.5 text-xs font-medium text-gray-600 bg-gray-200 rounded-full">
                        ${software.category}
                    </span>
                </div>
                
                <!-- Description -->
                <p class="text-gray-700 text-base mb-3 ${isFirst ? 'ml-10' : ''} leading-relaxed">${software.description}</p>
                
                <!-- Features -->
                <div class="border-t border-gray-300 pt-3 ${isFirst ? 'ml-10' : ''}">
                    <h5 class="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1.5">Key Features</h5>
                    <p class="text-sm text-gray-600 leading-relaxed">${software.features}</p>
                </div>
                
            </div>
        `;
    });
    
    resultDiv.innerHTML = html;
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