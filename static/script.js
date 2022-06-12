function calculate(f):

function eval() {
	let input = document.getElementById("eval").value
  fetch(`eval/${input}`)
	.then(response => response.text())
	.then(answer => {
		let ansBox = document.getElementById("ansbx")
		ansBox.innerHTML = answer
	})
}

function sin() {
	let input = document.getElementById("sin").value
  fetch(`sin/${input}`)
	.then(response => response.text())
	.then(answer => {
		let ansBox = document.getElementById("ansbx")
		ansBox.innerHTML = answer
	})
}

