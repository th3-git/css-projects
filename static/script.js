(async () => {
    const flaskForm = document.getElementById('flask-data-form')
    flaskForm.addEventListener('submit', async (event) => {
        const formData = new FormData(flaskForm)
        const { username, password } = [formData.get('username'), formData.get('password')]
        const response = await fetch('/authenticate', {
            method: 'POST', 
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                'username': username,
                'password': password
            })
        })
        
    })
})()