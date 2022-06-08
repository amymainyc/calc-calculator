function eval() {
	let evalInput = document.getElementById("eval1").value
  fetch(`eval/${evalInput}`)
	.then(response => response.text())
	.then(answer => {
		let ansBox = document.getElementById("ansbx")
		ansBox.value = answer
	})
};

