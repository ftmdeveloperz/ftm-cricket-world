document.addEventListener("DOMContentLoaded", function () {
    // Set a gradient background
    document.body.style.background = "linear-gradient(to right, #00c6ff, #0072ff)";

    // Add dynamic functionality to refresh scores
    const refreshButton = document.createElement('button');
    refreshButton.innerText = 'Refresh Scores';
    refreshButton.style.padding = '10px 20px';
    refreshButton.style.border = 'none';
    refreshButton.style.borderRadius = '5px';
    refreshButton.style.backgroundColor = '#35424a';
    refreshButton.style.color = '#ffffff';
    refreshButton.style.cursor = 'pointer';
    refreshButton.style.position = 'fixed';
    refreshButton.style.top = '20px';
    refreshButton.style.right = '20px';

    refreshButton.onclick = function() {
        location.reload(); // Reload the page to refresh scores
    };

    document.body.appendChild(refreshButton);
});
