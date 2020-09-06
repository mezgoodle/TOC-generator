const copy = () => {
	/* Get the text field */
	const copyText = document.getElementById('textarea2');

	/* Check if value is not empty */
	if (copyText.value) {
		/* Select the text field */
		copyText.select();
		copyText.setSelectionRange(0, 99999); /*For mobile devices*/

		/* Copy the text inside the text field */
		document.execCommand("copy");

		/* Alert the copied text */
		alert("Text has been copied");	
	} else {
		alert('Result is empty');
	}
	console.log(copyText.value);
}
