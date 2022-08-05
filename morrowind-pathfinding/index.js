/// DOCUMENT ELEMENTS

// Selection Fields
const sSources = document.querySelector('#s_sources');
const sDestinations = document.querySelector('#s_destinations');

// Buttons
const bCalculate = document.querySelector('#b_calculate');

// Text Fields
const tMaxTime = document.querySelector('#t_max_time');
const tMaxCost = document.querySelector('#t_max_cost');

// Checkboxes
const cMaxTime = document.querySelector('#c_max_time');
const cMaxCost = document.querySelector('#c_max_cost');
const cAllowRoad = document.querySelector('#c_allow_road');
const cAllowBoat = document.querySelector('#c_allow_boat');
const cAllowStrider = document.querySelector('#c_allow_strider');
const cAllowGuild = document.querySelector('#c_allow_guild');
const cAllowPropylon = document.querySelector('#c_allow_propylon');
const cAllowMasterPropylon = document.querySelector('#c_allow_master_propylon');
const cAllowDLC = document.querySelector('#c_allow_dlc');


/// GLOBALS

const DATA_DIR = "./data/";


/// LOAD DATA

lockUI();
loadData();
unlockUI();


/// EVENT LISTENERS

// Buttons
bCalculate.onclick = (e) => {
	lockUI();
	calculatePath(sSources.value, sDestinations.value);
	unlockUI();
};

cAllowDLC.onchange = (e) => {
	lockUI();
	if (e.target.checked) {
		for (let locName in DLC_LOCATIONS) {
			addLocationOption(locName);
		}
	} else {
		for (let i=sSources.length-1; i >= 0; i--) {
			if (sSources.options[i].value in DLC_LOCATIONS) {
				sSources.remove(i);
				sDestinations.remove(i);
			}
		}
	}
	unlockUI();
};

cMaxTime.onchange = (e) => {
	if (e.target.checked) {
		tMaxTime.disabled = false;
	} else {
		tMaxTime.disabled = true;
	}
};

cMaxCost.onchange = (e) => {
	if (e.target.checked) {
		tMaxCost.disabled = false;
	} else {
		tMaxCost.disabled = true;
	}
};


/// HELPER FUNCTIONS

function calculatePath(source, destination, goal) {
	console.log("Calculating Path.");
	
	if (source == '' || destination == '') {
		alert("Invalid selection.");
		return;
	}
	
	console.log(calculatePathHelper(source, destination, goal, {"cost": 0, "time":0, "path": []}))
	
	console.log("Path Calculated.")
	return;
}

function calculatePathHelper(source, destination, goal, data) {
	if (source == destination) {
		return data;
	}
	
	let bestResult = {goal: Number.MAX_SAFE_INTEGER};
	for (method in ROUTES) {
		for (nextStop in ROUTES[method][source]) {
			let newData = Object.assign({}, data);
			newData["time"] += ROUTES[method][source][nextStop]["travel_time"];
			newData["cost"] += ROUTES[method][source][nextStop]["gold_cost"];
			let currentResult = calculatePathHelper(nextStop, destination, goal, newData)
			console.log(currentResult);
			if (currentResult[goal] < bestResult[goal]) {
				bestResult = currentResult
			}
		}
	}
	return bestResult;
}

function loadData() {
	console.log("Loading Data.");
	
	for (let locName in LOCATIONS) {
		addLocationOption(locName);
	}
	
	console.log("Data Loaded.");
	return;
}

function addLocationOption(name) {
		let newOption1 = document.createElement("option");
		newOption1.value = name;
		newOption1.text = name;
		sSources.add(newOption1);
		
		let newOption2 = document.createElement("option");
		newOption2.value = name;
		newOption2.text = name;
		sDestinations.add(newOption2);
}

function lockUI() {
	sSources.disabled = true;
	sDestinations.disabled = true;
	bCalculate.disabled = true;
	tMaxTime.disabled = true;
	tMaxCost.disabled = true;
	cMaxTime.checked = false;
	cMaxCost.checked = false;
	cMaxTime.disabled = true;
	cMaxCost.disabled = true;
	cAllowRoad.disabled = true;
	cAllowBoat.disabled = true;
	cAllowStrider.disabled = true;
	cAllowGuild.disabled = true;
	cAllowPropylon.disabled = true;
	cAllowMasterPropylon.disabled = true;
	cAllowDLC.disabled = true;
	console.log("UI Locked");
	return;
}

function unlockUI() {
	sSources.disabled = false;
	sDestinations.disabled = false;
	bCalculate.disabled = false;
	cMaxTime.disabled = false;
	cMaxCost.disabled = false;
	cAllowRoad.disabled = false;
	cAllowBoat.disabled = false;
	cAllowStrider.disabled = false;
	cAllowGuild.disabled = false;
	cAllowPropylon.disabled = false;
	cAllowMasterPropylon.disabled = false;
	cAllowDLC.disabled = false;
	console.log("UI Unlocked");
	return;
}
