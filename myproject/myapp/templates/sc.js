const app = document.getElementById('cont')

// const logo = document.createElement('img')
// logo.src = 'logo.png'

// const container = document.createElement('div')
// container.setAttribute('class', 'container')

// app.appendChild(logo)
// app.appendChild(container)

var request = new XMLHttpRequest()
request.open('GET', 'https://ghibliapi.herokuapp.com/films', true)
// request.withCredentials = true;
// request.setRequestHeader("Authorization", 'Basic ' + btoa('kunat:kunat'));
request.onload = function() {
  console.log(request.responseText);
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)
  if (request.status >= 200 && request.status < 400) {
    data.forEach(movie => {
      const card = document.createElement('div')
      card.setAttribute('class', 'card')

      const h1 = document.createElement('h1')
      h1.textContent = movie.title

      const p = document.createElement('p')
      movie.description = movie.description.substring(0, 300)
      p.textContent = `${movie.description}...`

      app.appendChild(card)
      card.appendChild(h1)
      card.appendChild(p)
    })
  } else {
    const errorMessage = document.createElement('marquee')
    errorMessage.textContent = `Gah, it's not working!`
    app.appendChild(errorMessage)
  }
}

request.send()