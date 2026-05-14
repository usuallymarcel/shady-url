const API_URL = window.ENV.API_URL

const input = document.getElementById('url-input')
const output = document.getElementById('url-response')
const button = document.getElementById('url-button')

document.addEventListener("DOMContentLoaded", async () => {
    input.addEventListener('keydown', async (e) => {
        if (e.key === 'Enter') {
            e.preventDefault()
            await generateUrl()
        }
    })

    button.addEventListener('click', generateUrl)
})

const generateUrl = async () => {
    const url = input.value

    const res = await fetch(API_URL + '/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })

    const urlRes = await res.json()

    output.textContent = window.location.href + urlRes.url
}