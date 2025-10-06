document.addEventListener('DOMContentLoaded', function () {
    const fileInput = document.getElementById('dog-image');
    const previewImage = document.getElementById('preview-image');
    const cameraBtn = document.getElementById('camera-btn');
    const form = document.getElementById('upload-form');

    fileInput.addEventListener('change', function (e) {
        if (e.target.files && e.target.files[0]) {
            const file = e.target.files[0];

            const reader = new FileReader();
            reader.onload = function (event) {
                previewImage.src = event.target.result;
                previewImage.classList.remove('hidden');
            }
            reader.readAsDataURL(file);
            form.submit()
        } else {
            console.log('No file selected or selection canceled');
        }
    });

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch('/', {
            method: 'POST',
            body: formData
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok: ' + response.statusText);
                }
                return response.text();
            })
            .then(data => {
                console.log('Success:', data);
                alert('Upload successful!');
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('Upload failed: ' + error);
            });
    });

    cameraBtn.addEventListener('click', function () {
        alert('Camera functionality coming soon!');
    });
});