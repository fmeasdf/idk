const fileInput = document.getElementById('file-input');
const predictButton = document.getElementById('predict-button');
const resultDiv = document.getElementById('result');

predictButton.addEventListener('click', async () => {
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    try {
        const response = await fetch('http://your-server-url/classify', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        resultDiv.innerText = `Predicted Animal: ${data.label}`;
    } catch (error) {
        console.error('Error:', error);
    }
});
