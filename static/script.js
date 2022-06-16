function navigate(page) {
  fetch(page)
  .then(response => response.text())
  .then(data => {
    let content = document.getElementById("dynHTML")
    content.innerHTML = data
  })
}

function calculate(f, event) {
  if (event == undefined || event.keyCode == 13) {
    let input = document.getElementById(f).value
    if (!input) input = "undefined"
    fetch(`${f}/${input}`)
    .then(response => {
      if (response.ok) {
        return response.text()
      } else {
        return "Error!"
      }
    })
    .then(answer => {
      let answerBox = document.getElementById("answerBox")
		  answerBox.innerHTML = answer;
    })
  }
}