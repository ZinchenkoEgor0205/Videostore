let nameInput = document.querySelector('.form-input')
let videocards = document.querySelectorAll('.popular-content-positions-item')
let videocardsBlock = document.getElementsByClassName('content-items')[0]

nameInput.addEventListener('input', () => {
    let timeout = setTimeout(() => {
        let inputText = nameInput.value.toLowerCase()
        videocards.forEach((videocard) => {
            let videocardName = videocard.querySelector('.popular-content-positions-item-footer-info').textContent.toLowerCase()
            if (videocardName.includes(inputText)) {
                videocard.remove()
                videocardsBlock.append(videocard)
            } else videocard.remove()
        })
    }, 500)
    clearTimeout(timeout - 1)
})

let select = document.querySelector('#id_parameter')

select.addEventListener('change', () => {
    let selectValue = select.value
    let videocardsPriceList = []
    for (const videocard of videocards) {
        let videocardPrice = Number(videocard.querySelector('.popular-content-positions-item-footer-link-price').textContent.split(' ')[0])
        videocardsPriceList.push(videocardPrice)
        videocard.remove()
    }
    if (selectValue === '1') {
        videocardsPriceList.sort((a, b) => {
            if (a < b) return -1
            if (a === b) return 0
            if (a > b) return 1
        })
    } else videocardsPriceList.sort((a, b) => {
            if (a < b) return 1
            if (a === b) return 0
            if (a > b) return -1
        })
    for (const price of videocardsPriceList) {
        for (const videocard of videocards) {
            if (Number(videocard.querySelector('.popular-content-positions-item-footer-link-price').textContent.split(' ')[0]) === price) {
                videocardsBlock.append(videocard)
                continue
            }
        }
    }
})