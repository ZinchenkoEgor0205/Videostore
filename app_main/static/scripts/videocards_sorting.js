let nameInput = document.querySelector('.form-input')
let videocards = document.querySelectorAll('.popular-content-positions-item')
let videocardsBlock = document.getElementsByClassName('content-items')[0]

nameInput.addEventListener('input', () => {
    let timeout = setTimeout(() => {
        let inputText = nameInput.value
        videocards.forEach((videocard) => {
            let videocardName = videocard.querySelector('.popular-content-positions-item-footer-info').textContent
            if (videocardName.includes(inputText)) {
                videocard.remove()
                videocardsBlock.append(videocard)
            } else videocard.remove()
        })
    }, 1000)
    clearTimeout(timeout - 1)
})