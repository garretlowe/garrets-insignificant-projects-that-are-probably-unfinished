
function toHexColour(hex) {
	return '#' + hex.toString(16)
}

function main() {
	
	const boxContainer = document.querySelector('#box-container');
	const box = document.querySelector('#box');
	const boxText = document.querySelector('#box-text');
	
	// GUI
	var values = {
		'Font Size': 12,
		'Progress Bar': true,
		'Artwork': true,
		'Liked': true
	};
	
	var specialValues = {
		'Chroma Key': 0xff00ff,
		'Background': 0x181818,
		'Primary Foreground': 0xffffff,
		'Secondary Foreground': 0xb3b3b3,
		'Highlight': 0x1db954,
		'Height': 10,
		'Width': 30
	};
	
	document.body.style.background = toHexColour(specialValues['Chroma Key']);
	box.style.background = toHexColour(specialValues['Background']);
	boxText.style.color = toHexColour(specialValues['Primary Foreground']);
	
	var gui = new dat.GUI();
	var colourOptions = gui.addFolder('Colour Options');
	
	colourOptions.addColor(specialValues, 'Chroma Key').onChange(function () {
		document.body.style.background = toHexColour(specialValues['Chroma Key']);
	});
	colourOptions.addColor(specialValues, 'Background').onChange(function () {
		box.style.background = toHexColour(specialValues['Background']);
	});
	colourOptions.addColor(specialValues, 'Primary Foreground').onChange(function () {
		boxText.style.color = toHexColour(specialValues['Primary Foreground']);
	});
	colourOptions.addColor(specialValues, 'Secondary Foreground').onChange(function () {
		boxText.style.color = toHexColour(specialValues['Secondary Foreground']);
	});
	colourOptions.addColor(specialValues, 'Highlight').onChange(function () {
		boxText.style.color = toHexColour(specialValues['Highlight']);
	});
	
	gui.add(specialValues, 'Height', 1, 95, 1).onChange(function () {
		//boxContainer.style.height = specialValues['Height'].toString() + '%';
		box.style.height = specialValues['Height'].toString() + '%';
	});
	gui.add(specialValues, 'Width', 30, 75, 1).onChange(function () {
		//boxContainer.style.width = specialValues['Width'].toString() + '%';
		box.style.width = specialValues['Width'].toString() + '%';
	});

	
	for (const [key, value] of Object.entries(values)) {
		gui.add(values, key).listen();
	}
	
}

main();