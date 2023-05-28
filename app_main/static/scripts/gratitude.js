
const body = document.querySelector('body')
const gratitudeSection = document.createElement('section')
const gratitudeContainer = document.createElement('div')
const gratitudeText = document.createElement('h1')


console.log('start')

gratitudeSection.classList.add('gratitude')
gratitudeContainer.classList.add('container', 'gratitude-container')
gratitudeText.classList.add('gratitude-text')


let gratitudeMessage = document.querySelector('.hidden').textContent
gratitudeText.textContent = gratitudeMessage

gratitudeContainer.append(gratitudeText)
gratitudeSection.append(gratitudeContainer)

body.append(gratitudeSection)

let opacity = 1

setTimeout(
    () => {
        setInterval(() => {
            opacity = opacity - 0.05
            gratitudeSection.style = `opacity: ${opacity}`
            if (opacity <= 0) gratitudeSection.remove()
        }, 50)
    }, 1000
)