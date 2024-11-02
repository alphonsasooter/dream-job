document.getElementById('selectJobButton').addEventListener('click', function() {
    fetch('/get_job')
        .then(response => response.json())
        .then(data => {
            document.getElementById('jobResult').innerText = `Your dream job is: ${data.job}`;
        })
        .catch(error => {
            console.error('Error fetching job:', error);
        });
});
